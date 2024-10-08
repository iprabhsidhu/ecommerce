from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('forgetpassword/', views.forgetPassword, name='forgetPassword'),
    path('resetpassword_validate/<str:uidb64>/<str:token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword', views.resetPassword, name='resetPassword'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('order_detail/<int:order_id>', views.order_detail, name="order_detail"),
    path('order_admin_view/', views.admin_orders_view, name='order_admin_view'),
]
