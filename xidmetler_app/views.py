from django.shortcuts import render
from medical_app.views import *
from .models import *

# Create your views here.
def bizim_xidmetler(request):
    footer_bloq = Footer_Bloq.objects.all()
    haqqimda = SosialŞəbəkəLinkləri.objects.all()
    # baner = Sagbaner.objects.all()
    # digerservis = DigərServislər.objects.all()
    esasfoto = ƏsasFoto.objects.all()
    esasfotoyazilar = ƏsasFoto_ÜstYazılar.objects.all()
    haqqimizdamel = Xidmətlərimiz_Haqqında.objects.all()
    bashlig = SaytınBaşlığı.objects.all()
    # servismelumat = ServisMəlumat.objects.all()
    # teciliinfo = TəciliInfo.objects.all()
    # tecilielektron = TəciliElektron_Əlaqe.objects.all()
    numberemail = BaşlıqNömrəEpoct.objects.all()
    logosekil = LogoŞəkilAnaSəhifə.objects.all()
    photobashlig = SaytınBaşlığıFoto.objects.all()
    
    return render(request, 'xidmetler.html',{
        'bashlig' : bashlig,
        'photobashlig' : photobashlig,
        'numberemail' : numberemail,
        'logosekil' : logosekil,
        'esasfoto' : esasfoto,
        'esasfotoyazilar' : esasfotoyazilar,
        'haqqimizdamel' : haqqimizdamel,
        # 'servismelumat' : servismelumat,
        # 'digerservis' : digerservis,
        # 'baner' : baner,
        # 'teciliinfo' : teciliinfo,
        # 'tecilielektron' : tecilielektron,
        'haqqimda' : haqqimda,
        'footer_bloq' : footer_bloq,
    })

