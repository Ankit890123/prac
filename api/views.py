from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from django.utils import timezone
from django.db.models import Q, Count, Sum
from datetime import timedelta
import random
import string
from .models import User, OTP, Service, CartItem, Order, OrderItem, Contact, OrderTracking
from .serializers import (
    UserSerializer, UserRegistrationSerializer, OTPSerializer, ServiceSerializer,
    CartItemSerializer, AddToCartSerializer, OrderSerializer, CreateOrderSerializer,
    ContactSerializer, OrderTrackingSerializer, LoginSerializer, SendOTPSerializer,
    AdminStatsSerializer
)


def generate_otp():
    """Generate a 6-digit OTP"""
    return ''.join(random.choices(string.digits, k=6))


@api_view(['POST'])
@permission_classes([AllowAny])
def send_otp(request):
    """Send OTP to user's email/phone"""
    serializer = SendOTPSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        
        # Generate OTP
        otp_code = generate_otp()
        
        # Create or update OTP record
        otp_obj, created = OTP.objects.get_or_create(
            email=email,
            defaults={
                'otp_code': otp_code,
                'expires_at': timezone.now() + timedelta(minutes=10)
            }
        )
        
        if not created:
            otp_obj.otp_code = otp_code
            otp_obj.is_used = False
            otp_obj.expires_at = timezone.now() + timedelta(minutes=10)
            otp_obj.save()
        
        # In production, send OTP via SMS/Email
        print(f"OTP for {email}: {otp_code}")
        
        return Response({
            'message': 'OTP sent successfully',
            'otp': otp_code  # Remove this in production
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """Login with OTP"""
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        otp_code = serializer.validated_data['otp']
        
        # Verify OTP
        try:
            otp_obj = OTP.objects.get(
                email=email,
                otp_code=otp_code,
                is_used=False
            )
            
            if otp_obj.is_expired():
                return Response({
                    'message': 'OTP has expired'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Mark OTP as used
            otp_obj.is_used = True
            otp_obj.save()
            
            # Get or create user
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # Create new user
                username = email.split('@')[0]
                # Ensure username is unique
                counter = 1
                original_username = username
                while User.objects.filter(username=username).exists():
                    username = f"{original_username}{counter}"
                    counter += 1
                
                user = User.objects.create_user(
                    email=email,
                    username=username,
                    is_verified=True
                )
            
            # Create or get token
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                'message': 'Login successful',
                'token': token.key,
                'user': UserSerializer(user).data
            }, status=status.HTTP_200_OK)
            
        except OTP.DoesNotExist:
            return Response({
                'message': 'Invalid OTP'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """Get current user profile"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def services_list(request):
    """Get all services"""
    services = Service.objects.filter(is_active=True)
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_items(request):
    """Get user's cart items"""
    cart_items = CartItem.objects.filter(user=request.user)
    serializer = CartItemSerializer(cart_items, many=True)
    
    total = sum(item.price * item.quantity for item in cart_items)
    
    return Response({
        'items': serializer.data,
        'total': total,
        'totalQty': sum(item.quantity for item in cart_items)
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    """Add item to cart"""
    serializer = AddToCartSerializer(data=request.data)
    if serializer.is_valid():
        service_id = serializer.validated_data['service_id']
        service_option_id = serializer.validated_data['service_option_id']
        quantity = serializer.validated_data['quantity']
        
        # Get service data (in production, fetch from Service model)
        from .services_data import SERVICES
        service_data = SERVICES.get(service_id)
        
        if not service_data:
            return Response({
                'message': 'Service not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Find the specific option
        option = None
        for opt in service_data['options']:
            if opt['id'] == service_option_id:
                option = opt
                break
        
        if not option:
            return Response({
                'message': 'Service option not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Add to cart
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            service_option_id=service_option_id,
            defaults={
                'service_id': service_id,
                'service_name': service_data['name']['en'],
                'service_option_name': option['label']['en'],
                'price': option['price'],
                'quantity': quantity
            }
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        return Response({
            'message': 'Item added to cart successfully'
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_cart_item(request, item_id):
    """Update cart item quantity"""
    try:
        cart_item = CartItem.objects.get(id=item_id, user=request.user)
        quantity = request.data.get('quantity', 1)
        
        if quantity <= 0:
            cart_item.delete()
            return Response({
                'message': 'Item removed from cart'
            })
        
        cart_item.quantity = quantity
        cart_item.save()
        
        return Response({
            'message': 'Cart updated successfully'
        })
        
    except CartItem.DoesNotExist:
        return Response({
            'message': 'Cart item not found'
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, item_id):
    """Remove item from cart"""
    try:
        cart_item = CartItem.objects.get(id=item_id, user=request.user)
        cart_item.delete()
        
        return Response({
            'message': 'Item removed from cart'
        })
        
    except CartItem.DoesNotExist:
        return Response({
            'message': 'Cart item not found'
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def clear_cart(request):
    """Clear user's cart"""
    CartItem.objects.filter(user=request.user).delete()
    
    return Response({
        'message': 'Cart cleared successfully'
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    """Create order from cart"""
    serializer = CreateOrderSerializer(data=request.data)
    if serializer.is_valid():
        # Get cart items
        cart_items = CartItem.objects.filter(user=request.user)
        
        if not cart_items.exists():
            return Response({
                'message': 'Cart is empty'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Calculate total
        total_amount = sum(item.price * item.quantity for item in cart_items)
        
        # Create order
        order = Order.objects.create(
            user=request.user,
            items=[{
                'service_id': item.service_id,
                'service_name': item.service_name,
                'service_option_id': item.service_option_id,
                'service_option_name': item.service_option_name,
                'price': float(item.price),
                'quantity': item.quantity
            } for item in cart_items],
            total_amount=total_amount,
            pickup_address=serializer.validated_data['pickup_address'],
            delivery_address=serializer.validated_data['delivery_address'],
            pickup_date=serializer.validated_data['pickup_date'],
            notes=serializer.validated_data.get('notes', '')
        )
        
        # Create order items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                service_id=item.service_id,
                service_name=item.service_name,
                service_option_id=item.service_option_id,
                service_option_name=item.service_option_name,
                price=item.price,
                quantity=item.quantity
            )
        
        # Clear cart
        cart_items.delete()
        
        # Create initial tracking update
        OrderTracking.objects.create(
            order=order,
            status='Order Placed',
            description='Your order has been placed successfully'
        )
        
        return Response({
            'message': 'Order created successfully',
            'order_id': str(order.id)
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_orders(request):
    """Get user's orders"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_detail(request, order_id):
    """Get order details"""
    try:
        order = Order.objects.get(id=order_id, user=request.user)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response({
            'message': 'Order not found'
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_tracking(request, order_id):
    """Get order tracking updates"""
    try:
        order = Order.objects.get(id=order_id, user=request.user)
        tracking_updates = OrderTracking.objects.filter(order=order)
        serializer = OrderTrackingSerializer(tracking_updates, many=True)
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response({
            'message': 'Order not found'
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([AllowAny])
def contact_form(request):
    """Handle contact form submission"""
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Contact form submitted successfully'
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Admin Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_stats(request):
    """Get admin dashboard stats"""
    if request.user.role != 'admin':
        return Response({
            'message': 'Access denied'
        }, status=status.HTTP_403_FORBIDDEN)
    
    total_orders = Order.objects.count()
    pending_orders = Order.objects.filter(status__in=['pending', 'confirmed']).count()
    completed_orders = Order.objects.filter(status='completed').count()
    total_users = User.objects.filter(role='user').count()
    total_revenue = Order.objects.filter(payment_status='paid').aggregate(
        total=Sum('total_amount')
    )['total'] or 0
    
    serializer = AdminStatsSerializer({
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
        'total_users': total_users,
        'total_revenue': total_revenue
    })
    
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_recent_orders(request):
    """Get recent orders for admin"""
    if request.user.role != 'admin':
        return Response({
            'message': 'Access denied'
        }, status=status.HTTP_403_FORBIDDEN)
    
    recent_orders = Order.objects.select_related('user').order_by('-created_at')[:10]
    
    orders_data = []
    for order in recent_orders:
        orders_data.append({
            'id': str(order.id),
            'user': order.user.email,
            'status': order.status,
            'total': float(order.total_amount),
            'created_at': order.created_at
        })
    
    return Response(orders_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_orders(request):
    """Get all orders for admin"""
    if request.user.role != 'admin':
        return Response({
            'message': 'Access denied'
        }, status=status.HTTP_403_FORBIDDEN)
    
    orders = Order.objects.select_related('user').order_by('-created_at')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_order_status(request, order_id):
    """Update order status"""
    if request.user.role != 'admin':
        return Response({
            'message': 'Access denied'
        }, status=status.HTTP_403_FORBIDDEN)
    
    try:
        order = Order.objects.get(id=order_id)
        new_status = request.data.get('status')
        
        if new_status not in [choice[0] for choice in Order.STATUS_CHOICES]:
            return Response({
                'message': 'Invalid status'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        order.status = new_status
        order.save()
        
        # Create tracking update
        OrderTracking.objects.create(
            order=order,
            status=new_status.title(),
            description=f'Order status updated to {new_status}'
        )
        
        return Response({
            'message': 'Order status updated successfully'
        })
        
    except Order.DoesNotExist:
        return Response({
            'message': 'Order not found'
        }, status=status.HTTP_404_NOT_FOUND)