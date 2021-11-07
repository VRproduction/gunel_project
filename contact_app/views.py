from django.shortcuts import render
from medical_app.views import *
from .models import *
from qebul_app.views import *

# Create your views here.

def contact(request):
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
    return render(request, "contact.html", {
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
        'footer_bloq' : footer_bloq
    })