from django.shortcuts import render
from medical_app.models import *
from medical_app.views import *
from xidmetler_app.models import *
from .models import *
# Create your views here.

def blog(request):
    footer_bloq = Footer_Bloq.objects.all()
    hekaye = Hekayə.objects.all()
    haqqimda = SosialŞəbəkəLinkləri.objects.all()
    # baner = Sagbaner.objects.all()
    esasfoto_metn = ƏsasFoto_ÜstMətn.objects.all()
    esasfoto = ƏsasFoto.objects.all()
    posts = PostPaylaşılma.objects.all()
    bashlig = SaytınBaşlığı.objects.all()
    numberemail = BaşlıqNömrəEpoct.objects.all()
    logosekil = LogoŞəkilAnaSəhifə.objects.all()
    # tecilielektron = TəciliElektron_Əlaqe.objects.all()
    # teciliinfo = TəciliInfo.objects.all()
    photobashlig = SaytınBaşlığıFoto.objects.all()
    return render(request, 'blog.html', {
        # 'tecilielektron' : tecilielektron,
        # 'teciliinfo' : teciliinfo,
        'bashlig' : bashlig,
        'photobashlig' : photobashlig,
        'numberemail' : numberemail,
        'logosekil' : logosekil,
        'esasfoto_metn' : esasfoto_metn,
        'esasfoto' : esasfoto,
        'posts' : posts,
        'haqqimda' : haqqimda,
        'hekaye' : hekaye,
        # 'baner' : baner,
        'footer_bloq' : footer_bloq,
    })