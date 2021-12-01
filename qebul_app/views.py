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
from medical_project.settings import *
from .models import *
from blog_app.models import SosialŞəbəkəLinkləri
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from blog_app.models import *


# Create your views here.


def appoinment(request):
    sekil = Əsas_Şəkil.objects.all()
    acilish_vaxt = Footer_Açılış_Vaxtları.objects.all()
    footer_yazi = Footer_Yazısı.objects.all()
    footer_bloq = Footer_Bloq.objects.all()
    xerite_url = QəbulXəritə.objects.all()
    haqqimda = SosialŞəbəkəLinkləri.objects.all()
    # tecilielektron = TəciliElektron_Əlaqe.objects.all()
    haqqimizdayazi = HaqqımızdaYazılar.objects.all()
    # bloqsolmetn = BloqSolMətn.objects.all()
    # bloqxeber = Bloq_YeniXəbərlər_AnaSehifə.objects.all()
    haqqimizda = SosialŞəbəkəLinkləri.objects.all()
    foto = Qəbul_Haqqımızda_foto.objects.all()
    esasyazilar = Əsas_Şəkilin_Yazıları.objects.all()
    photobashlig = SaytınBaşlığıFoto.objects.all()
    bashlig = SaytınBaşlığı.objects.all()
    numberemail = BaşlıqNömrəEpoct.objects.all()
    # haqqimda = HaqqımdaMəlumat.objects.all()
    logosekil = LogoŞəkilAnaSəhifə.objects.all()

    if request.method == 'POST':
        adtext = request.POST.get('adtext')
        soyadtext = request.POST.get('soyadtext')
        telefon = request.POST.get('telefon')
        mal = request.POST.get('mal')
        subject = request.POST.get('subject')

        data = {
            'adtext': adtext,
            'soyadtext' : soyadtext,
            'telefon': telefon,
            'mal': mal,
            'subject': subject,

        }
    #     adtext = '''
    #        Ad və Soyad: {}
    #        telefon: {}
    #        Email: {}
    #        Mesaj: {}
    #    '''.format(data['adtext'], data['telefon'], data['mal'], data['subject'])
        message = render_to_string('mail.html', data)
        send_mail(
            "Müştəri tərəfindən sizə mesaj gəlib",
            message,
            settings.EMAIL_HOST_USER,
            ['info@sudvezixercengi.az'],
            fail_silently=False, html_message=message
        )



    return render(request, 'qebul.html', {
        'photobashlig': photobashlig,
        'bashlig': bashlig,
        'numberemail': numberemail,
        'logosekil': logosekil,
        'esasyazilar': esasyazilar,
        'foto': foto,
        'haqqimizda': haqqimizda,
        # 'bloqxeber' : bloqxeber,
        # 'bloqsolmetn' : bloqsolmetn,
        'haqqimizdayazi': haqqimizdayazi,
        # 'tecilielektron' : tecilielektron,
        'xerite_url': xerite_url,
        'haqqimda' : haqqimda,
        'footer_bloq' : footer_bloq,
        'footer_yazi' : footer_yazi,
        'acilish_vaxt' : acilish_vaxt,
        'sekil' : sekil,

    })


