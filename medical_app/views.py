from django.http.response import HttpResponse
from django.shortcuts import render
from medical_project.settings import *
from medical_app.models import *
from django.core.mail import EmailMultiAlternatives, EmailMessage, message
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from medical_project.settings import EMAIL_HOST_USER
from blog_app.models import SosialŞəbəkəLinkləri, PostPaylaşılma

def homepage(request):
    footer_bloq = Footer_Bloq.objects.all()
    haqqimda = SosialŞəbəkəLinkləri.objects.all()
    tezverilenfoto = Tez_Tez_VerilənSualların_Foto.objects.all()
    tezverilensuallar = Tez_Tez_VerilənSuallar.objects.all()
    reyler = PasiyentlərinRəyi_Slayder.objects.all()
    # tecilielektron = TəciliElektron_Əlaqe.objects.all()
    # teciliinfo = TəciliInfo.objects.all()
    bloqanaseyfefoto = Bloq_AnaSəhifə_SolArxaFoto.objects.all()
    muksektor = MükafatSektoru.objects.all()
    melumatsek = MəlumatSektoru.objects.all()
    posts = PostPaylaşılma.objects.all()
    haqqimizdasekil = HaqqımızdaŞəkillər.objects.all()
    logosekil = LogoŞəkilAnaSəhifə.objects.all()
    servismelumat = Servis_Məlümat_AnaSəhifə.objects.all()
    serviceustyazi = Servis_Üst_Yazılar.objects.all()
    komandayazi = Komanda_Haqqında_yazılar.objects.all()
    haqqimizdamuellif = Haqqımızdamüəllif.objects.all()
    haqqimizdayazi = HaqqımızdaYazılar.objects.all()
    slidersekil = GirişŞəkil.objects.all()
    numberemail = BaşlıqNömrəEpoct.objects.all()
    photobashlig = SaytınBaşlığıFoto.objects.all()
    bashlig = SaytınBaşlığı.objects.all()
    slayderyazi = GirişŞəkilYazılar.objects.all()
    return render(request, "homepage.html", {
        'tezverilenfoto' : tezverilenfoto,
        'tezverilensuallar' : tezverilensuallar,
        'baslig': bashlig,
        'numberemail': numberemail,
        'slayderyazi': slayderyazi,
        'slidersekil': slidersekil,
        'haqqimizdayazi':haqqimizdayazi,
        'haqqimizdamuellif': haqqimizdamuellif,
        'komandayazi': komandayazi,
        'serviceustyazi': serviceustyazi,
        'servismelumat' : servismelumat,
        'photobashlig': photobashlig,
        'logosekil' : logosekil,
        'haqqimizdasekil' : haqqimizdasekil,
        'melumatsek': melumatsek,
        'posts' : posts,
        'muksektor' : muksektor,
        'bloqanaseyfefoto': bloqanaseyfefoto,
        # 'teciliinfo' : teciliinfo,
        # 'tecilielektron': tecilielektron,
        'reyler' : reyler,
        'haqqimda' : haqqimda,
        'footer_bloq' : footer_bloq,
    })












