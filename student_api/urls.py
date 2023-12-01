from django.urls import path
from .views import home, butun_ograncileri_getir, yeni_ogrenci_create_et, tek_ogrenciyi_goruntuleme_islemi, ogrenciyi_guncelle, ogrenci_sil
urlpatterns = [
    path('homesayfasinigetir/', home),
    path("ogrencilerinhepsinigetir/", butun_ograncileri_getir),
    path("yeniogrenciolustur/", yeni_ogrenci_create_et),
    path("tekogrenci/<int:pk>/", tek_ogrenciyi_goruntuleme_islemi),
    path("ogrenciyiguncele/<int:pk>/", ogrenciyi_guncelle),
    path("ogrencisil/<int:pk>/", ogrenci_sil)

]
