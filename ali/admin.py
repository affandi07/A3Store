from django.contrib import admin
from .models import Kategori, Produk, Slide, Kontak,Profil,Statis,ChatID

class DataKategoriAdmin(admin.ModelAdmin):
    list_display = ("nama", "aktif", "banner_satu", "banner_dua",)
    prepopulated_fields = {"slug": ("nama",)}
class DataKontakAdmin(admin.ModelAdmin):
    list_display = ("nama","no_whatsup","email","subject", )
class DataProfilAdmin(admin.ModelAdmin):
    list_display = ("nama","keterangan","gambar","tanggal_upload", )
class DataStatisAdmin(admin.ModelAdmin):
    list_display = ("alamat_kami","telpon","email",)    
class DataProdukAdmin(admin.ModelAdmin):
    list_display = ("nama_produk","kategori", "aktif", "gambar","harga","no_whatsup",)
    prepopulated_fields = {"slug": ("nama_produk",)}

admin.site.register(Produk,DataProdukAdmin)

admin.site.register(Kategori,DataKategoriAdmin)

admin.site.register(Slide)
admin.site.register(Kontak, DataKontakAdmin)
admin.site.register(Profil, DataProfilAdmin)
admin.site.register(Statis,DataStatisAdmin)
admin.site.register(ChatID)
