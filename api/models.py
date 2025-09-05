from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid


class User(AbstractUser):
    """Custom User model with additional fields"""
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email


class OTP(models.Model):
    """OTP model for authentication"""
    email = models.EmailField()
    otp_code = models.CharField(max_length=6)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    def is_expired(self):
        return timezone.now() > self.expires_at
    
    def __str__(self):
        return f"OTP for {self.email}"


class Service(models.Model):
    """Service model matching frontend servicesData.js"""
    id = models.IntegerField(primary_key=True)  # Match frontend service IDs
    emoji = models.CharField(max_length=10)
    name_en = models.CharField(max_length=100)
    name_hi = models.CharField(max_length=100)
    name_mr = models.CharField(max_length=100)
    tagline_en = models.TextField()
    tagline_hi = models.TextField()
    tagline_mr = models.TextField()
    before_en = models.CharField(max_length=200)
    before_hi = models.CharField(max_length=200)
    before_mr = models.CharField(max_length=200)
    after_en = models.CharField(max_length=200)
    after_hi = models.CharField(max_length=200)
    after_mr = models.CharField(max_length=200)
    steps_en = models.JSONField(default=list)
    steps_hi = models.JSONField(default=list)
    steps_mr = models.JSONField(default=list)
    perks_en = models.JSONField(default=list)
    perks_hi = models.JSONField(default=list)
    perks_mr = models.JSONField(default=list)
    options = models.JSONField(default=list)  # Service options with prices
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.emoji} {self.name_en}"


class CartItem(models.Model):
    """Cart item model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    service_id = models.IntegerField()
    service_name = models.CharField(max_length=200)
    service_option_id = models.CharField(max_length=100)
    service_option_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['user', 'service_option_id']
    
    def __str__(self):
        return f"{self.user.email} - {self.service_option_name} x{self.quantity}"


class Order(models.Model):
    """Order model"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('picked_up', 'Picked Up'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    items = models.JSONField()  # Store order items as JSON
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    pickup_address = models.TextField()
    delivery_address = models.TextField()
    pickup_date = models.DateTimeField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.id} - {self.user.email}"


class OrderItem(models.Model):
    """Individual order items"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    service_id = models.IntegerField()
    service_name = models.CharField(max_length=200)
    service_option_id = models.CharField(max_length=100)
    service_option_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.order.id} - {self.service_option_name} x{self.quantity}"


class Contact(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Contact from {self.name} - {self.subject}"


class OrderTracking(models.Model):
    """Order tracking updates"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='tracking_updates')
    status = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.order.id} - {self.status}"