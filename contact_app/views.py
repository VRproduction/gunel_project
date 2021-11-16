from django.shortcuts import render
from medical_app.views import *
from .models import *
from qebul_app.views import *
from blog_app.models import *

# Create your views here.

def contact(request):
    acilish_vaxt = Footer_Açılış_Vaxtları.objects.all()
    footer_yazi = Footer_Yazısı.objects.all()
    footer_bloq = Footer_Bloq.objects.all()
    xerite_url = QəbulXəritə.objects.all()
    esasfoto = ƏsasFoto.objects.all()
    gmail = Gmail.objects.all()
    esasfotometn = ƏsasFotoMətnlər.objects.all()
    # tecilielektron = TəciliElektron_Əlaqe.objects.all()
    mekan = Məkan.objects.all()
    # teciliinfo = TəciliInfo.objects.all()
    bizezeng = BizəZəng.objects.all()
    bashlig = SaytınBaşlığı.objects.all()
    numberemail = BaşlıqNömrəEpoct.objects.all()
    logosekil = LogoŞəkilAnaSəhifə.objects.all()
    haqqimda = SosialŞəbəkəLinkləri.objects.all()
    photobashlig = SaytınBaşlığıFoto.objects.all()
    return render(request, "elaqe.html", {
        'bashlig' : bashlig,
        'photobashlig' : photobashlig,
        'numberemail' : numberemail,
        'logosekil' : logosekil,
        'gmail' : gmail,
        'mekan' : mekan,
        'bizezeng' : bizezeng,
        'esasfotometn' : esasfotometn,
        'esasfoto' : esasfoto,
        'xerite_url' : xerite_url,
        # 'tecilielektron' : tecilielektron,
        # 'teciliinfo' : teciliinfo,
        'haqqimda' : haqqimda,
        'footer_bloq' : footer_bloq,
        'footer_yazi' : footer_yazi,
        'acilish_vaxt' : acilish_vaxt,
    })