from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from .models import User, OTP, Service, CartItem, Order, OrderItem, Contact, OrderTracking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'phone', 'role', 'is_verified', 'created_at']
        read_only_fields = ['id', 'created_at']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'phone', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['email', 'otp_code']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'service_id', 'service_name', 'service_option_id', 'service_option_name', 'price', 'quantity', 'created_at']
        read_only_fields = ['id', 'created_at']


class AddToCartSerializer(serializers.Serializer):
    service_id = serializers.IntegerField()
    service_option_id = serializers.CharField()
    quantity = serializers.IntegerField(default=1, min_value=1)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['service_id', 'service_name', 'service_option_id', 'service_option_name', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_amount', 'status', 'payment_status', 'pickup_address', 
                 'delivery_address', 'pickup_date', 'delivery_date', 'notes', 'created_at', 'updated_at', 'order_items']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']


class CreateOrderSerializer(serializers.Serializer):
    pickup_address = serializers.CharField()
    delivery_address = serializers.CharField()
    pickup_date = serializers.DateTimeField()
    notes = serializers.CharField(required=False, allow_blank=True)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']


class OrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTracking
        fields = ['status', 'description', 'location', 'created_at']
        read_only_fields = ['created_at']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)


class SendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()


class AdminStatsSerializer(serializers.Serializer):
    total_orders = serializers.IntegerField()
    pending_orders = serializers.IntegerField()
    total_users = serializers.IntegerField()
    completed_orders = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=10, decimal_places=2)