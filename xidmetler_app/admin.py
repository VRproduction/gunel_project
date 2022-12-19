from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ƏsasFoto)
admin.site.register(ƏsasFoto_ÜstYazılar)
# admin.site.register(ServisMəlumat)
# admin.site.register(DigərServislər)
# admin.site.register(Sagbaner)
admin.site.register(Məlumat_Sektoru)
admin.site.register(Xidmətlər_Postları)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("haqqimizda_ust_yazi_1", "created_at",)
    prepopulated_fields = {"slug": ("haqqimizda_ust_yazi_1",)}

admin.site.register(Xidmətlərimiz_Haqqında, ServiceAdmin)
