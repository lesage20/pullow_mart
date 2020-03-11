from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('confirm', views.confirm, name='confirm'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('login', views.login, name='login'),
    path('main', views.main, name='main'),
    path('product', views.product, name='product'),
    path('single', views.single, name='single'),
    path('single_product', views.single_product, name='single_product'),

]
