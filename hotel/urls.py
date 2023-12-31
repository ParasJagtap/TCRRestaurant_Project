from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('menu/', views.menu, name='menu'),
    path('myorders/', views.my_orders, name='my_orders'),
    
    path('dashboard/admin/users/', views.users_admin, name='users_admin'),
    path('dashboard/admin/orders/', views.orders_admin, name='orders_admin'),
    path('dashboard/admin/foods/', views.foods_admin, name='foods_admin'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/admin/sales/', views.sales_admin, name='sales_admin'),
    
    path('dashboard/admin/users/add_user/', views.add_user, name='add_user'),
    path('dashboard/admin/foods/add_food/', views.add_food, name='add_food'),
    path('dashboard/admin/sales/add_sales/', views.add_sales, name='add_sales'),
    path('dashboard/admin/foods/editFood/(?P<foodID>\d+)/', views.edit_food, name='edit_food'),
    path('dashboard/admin/foods/foodDetails/(?P<foodID>\d+)/', views.food_details, name='food_details'),
    path('dashboard/admin/sales/editSale/(?P<saleID>\d+)/', views.edit_sales, name='edit_sales'),
    
    path('dashboard/admin/orders/confirm_order/(?P<orderID>\d+)/', views.confirm_order, name='confirm_order'),
    path('dashboard/admin/orders/confirm_delivery/(?P<orderID>\d+)/', views.confirm_delivery, name='confirm_delivery'),
    
    path('delete_item/(?P<ID>\d+)/', views.delete_item, name='delete_item'),
    path('add_deliveryBoy/(?P<orderID>\d+)/', views.add_deliveryBoy, name='add_deliveryBoy'),
    path('placeOrder/', views.placeOrder, name='placeOrder'),
    path('addTocart/(?P<foodID>\d+)/(?P<userID>\d+)/', views.addTocart, name='addTocart'),

    path('dashboard/delivery_boy/', views.delivery_boy, name='delivery_boy'),
]
