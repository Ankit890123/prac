from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('auth/send-otp/', views.send_otp, name='send_otp'),
    path('auth/login/', views.login, name='login'),
    
    # User Profile
    path('user/profile/', views.user_profile, name='user_profile'),
    
    # Services
    path('services/', views.services_list, name='services_list'),
    
    # Cart
    path('cart/', views.cart_items, name='cart_items'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    
    # Orders
    path('orders/', views.user_orders, name='user_orders'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/<uuid:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<uuid:order_id>/tracking/', views.order_tracking, name='order_tracking'),
    
    # Contact
    path('contact/', views.contact_form, name='contact_form'),
    
    # Admin
    path('admin/stats/', views.admin_stats, name='admin_stats'),
    path('admin/recent-orders/', views.admin_recent_orders, name='admin_recent_orders'),
    path('admin/orders/', views.admin_orders, name='admin_orders'),
    path('admin/orders/<uuid:order_id>/status/', views.update_order_status, name='update_order_status'),
]