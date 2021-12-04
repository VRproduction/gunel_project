from django.contrib import admin
from .models import *

fields = ['image_tag']
readonly_fields = ['image_tag']
#HomePage
admin.site.register(SaytınBaşlığı)
admin.site.register(SaytınBaşlığıFoto)
admin.site.register(BaşlıqNömrəEpoct)
admin.site.register(GirişŞəkilYazılar)
admin.site.register(GirişŞəkil)
admin.site.register(HaqqımızdaYazılar)
admin.site.register(Haqqımızdamüəllif)
admin.site.register(Servis_Üst_Yazılar)
admin.site.register(Servis_Məlümat_AnaSəhifə)
admin.site.register(LogoŞəkilAnaSəhifə)
admin.site.register(HaqqımızdaŞəkillər)
admin.site.register(MəlumatSektoru)
admin.site.register(MükafatSektoru)
# admin.site.register(TəciliInfo)
# admin.site.register(TəciliElektron_Əlaqe)
admin.site.register(PasiyentlərinRəyi_Slayder)
admin.site.register(Tez_Tez_VerilənSualların_Foto)
admin.site.register(Tez_Tez_VerilənSuallar)
admin.site.register(Footer_Bloq)
admin.site.register(Youtube_Link_Əsas)
admin.site.register(MobileFoto)