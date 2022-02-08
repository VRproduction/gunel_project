from django.shortcuts import render
from .models import *
from medical_app.models import *
from blog_app.models import *

def med(request):
    acilish_vaxt = Footer_Açılış_Vaxtları.objects.all()
    footer_yazi = Footer_Yazısı.objects.all()
    footer_bloq = Footer_Bloq.objects.all()
    mediayoutube = MediaYouTube.objects.all()
    mediatv = MediaTvProqramları.objects.all()
    musahibe = Müsahibe.objects.all()
    bashlig = SaytınBaşlığı.objects.all()
    numberemail = BaşlıqNömrəEpoct.objects.all()
    photobashlig = SaytınBaşlığıFoto.objects.all()
    logosekil = LogoŞəkilAnaSəhifə.objects.all()
    foto = MediaƏsasŞəkil.objects.all()
    fotometn = ƏsasŞəkilin_ÜstMətini.objects.all()
    haqqimda = SosialŞəbəkəLinkləri.objects.all()
    return render(request, 'media.html', {
        'foto' : foto,
        'fotometn' : fotometn,
        'bashlig' : bashlig ,
        'numberemail' : numberemail ,
        'haqqimda' : haqqimda,
        'photobashlig' : photobashlig ,
        'logosekil' :  logosekil ,
        'musahibe' : musahibe,
        'mediatv' : mediatv,
        'mediayoutube' : mediayoutube,
        'haqqimda' : haqqimda,
        'footer_bloq' : footer_bloq,
        'footer_yazi' : footer_yazi,
        'acilish_vaxt' : acilish_vaxt,
    })

def sitemap(request):
    return render(request,"sitemap.xml")
