from django.urls import path
from .import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('profil-kami', views.profil, name='profil'),
    path('<slug:kategori_slug>/<slug:slug>', views.produk, name='produk'),
    path('pemesanan', views.pemesanan, name='pemesanan'),
    path('checkout', views.CheckoutView.as_view(), name='checkout'),
    path('hubungi-kami', views.KontakView.as_view(), name='kontak'), 
    path('<slug:slug>', views.kategori, name='kategori'),
]