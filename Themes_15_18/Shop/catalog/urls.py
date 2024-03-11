from django.urls import path
from .import views
from .views import CustomLoginView, RegisterPage
from .views import logout_view


urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    # Маршруты 
    path('', views.index, name='index'), # общий маршрут

    path('manufacturer_list/', views.manufacturer_list, name='manufacturer_list'),
    path('display_manufacturers/', views.display_manufacturers, name='display_manufacturers'),
    path('add_manufacturer/', views.add_manufacturer, name='add_manufacturer'),  

    path('product_list/', views.product_list, name='product_list'),
    path('display_products/', views.display_products, name='display_products'),
    path('add_product/', views.add_product, name='add_product'),   
]
