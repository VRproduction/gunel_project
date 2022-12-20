from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *

# Register your models here.
admin.site.register(ƏsasFoto)
admin.site.register(ƏsasFoto_ÜstMətn)
admin.site.register(SosialŞəbəkəLinkləri)
admin.site.register(Haqqımda_Məlumat)
admin.site.register(Digər_Bloqlar)
admin.site.register(İnstagram_Postları)
admin.site.register(Footer_Yazısı)
admin.site.register(Footer_Açılış_Vaxtları)


class BloqAdminForm(forms.ModelForm):
    metn = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = PostPaylaşılma
        fields = '__all__'

class BloqAdmin(admin.ModelAdmin):
    form = BloqAdminForm
    list_display = ("metinin_bashligi", "vaxt",)
    prepopulated_fields = {"slug": ("metinin_bashligi",)}

admin.site.register(PostPaylaşılma, BloqAdmin)
