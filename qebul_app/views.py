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
from .models import *
from blog_app.models import SosialŞəbəkəLinkləri


# Create your views here.
def appoinment(request):
    footer_bloq = Footer_Bloq.objects.all()
    xerite_url = QəbulXəritə.objects.all()
    # tecilielektron = TəciliElektron_Əlaqe.objects.all()
    haqqimizdayazi = HaqqımızdaYazılar.objects.all()
    # bloqsolmetn = BloqSolMətn.objects.all()
    # bloqxeber = Bloq_YeniXəbərlər_AnaSehifə.objects.all()
    bloqanaseyfefoto = Bloq_AnaSəhifə_SolArxaFoto.objects.all()
    arxasekilform = Qəbul_Form_Arxa_Foto.objects.all()
    haqqimizda = SosialŞəbəkəLinkləri.objects.all()
    foto = Qəbul_Haqqımızda_foto.objects.all()
    esasyazilar = Əsas_Şəkilin_Yazıları.objects.all()
    sekil = Əsas_Şəkil.objects.all()
    photobashlig = SaytınBaşlığıFoto.objects.all()
    bashlig = SaytınBaşlığı.objects.all()
    numberemail = BaşlıqNömrəEpoct.objects.all()
    # haqqimda = HaqqımdaMəlumat.objects.all()
    logosekil = LogoŞəkilAnaSəhifə.objects.all()

    if request.method == 'POST':
        adtext = request.POST.get('adtext')
        soyadtext = request.POST.get('soyadtext')
        telefon = request.POST.get('number')
        mal = request.POST.get('mal')

        data = {
            'adtext': adtext,
            'soyadtext': soyadtext,
            'telefon': telefon,
            'mal': mal,

        }
        adtext = '''
           Ad: {}
           Soyad: {}
           telefon: {}
           Email: {}
       '''.format(data['adtext'], data['soyadtext'], data['telefon'], data['mal'])
        # sehf yazmisan bax buna
        send_mail(
            "Müştəri tərəfindən sizə mesaj gəlib",            
            adtext,
            settings.EMAIL_HOST_USER,  # birde yoxala
            ['emka6451@gmail.com'],
            fail_silently=False
        )



    return render(request, 'appoinment.html', {
        'photobashlig': photobashlig,
        'bashlig': bashlig,
        'numberemail': numberemail,
        'logosekil': logosekil,
        'esassekil': sekil,
        'esasyazilar': esasyazilar,
        'foto': foto,
        'haqqimizda': haqqimizda,
        'arxasekilform': arxasekilform,
        'bloqanaseyfefoto': bloqanaseyfefoto,
        # 'bloqxeber' : bloqxeber,
        # 'bloqsolmetn' : bloqsolmetn,
        'haqqimizdayazi': haqqimizdayazi,
        # 'tecilielektron' : tecilielektron,
        'xerite_url': xerite_url,
        # 'haqqimda' : haqqimda,
        'footer_bloq': footer_bloq,

    })
