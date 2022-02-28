from django.http.request import HttpRequest
from django.shortcuts import render
from medical_app.views import *
from .models import *
from qebul_app.views import *
from blog_app.models import *

# Create your views here.

def contact(request):
    seoelaqe = SEO_Əlaqə.objects.all()
    mobilefoto = MobileƏsasFoto.objects.all()
    acilish_vaxt = Footer_Açılış_Vaxtları.objects.all()
    footer_yazi = Footer_Yazısı.objects.all()
    footer_bloq = Footer_Bloq.objects.all()
    xerite_url = QəbulXəritə.objects.all()
    sekil = Üst_Şəkil.objects.all()
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
        message = render_to_string('mail-murciyyetelaqe.html', data)
        send_mail(
            "Sizə sudvezixercengi.az saytından müraciət gəlib",
            message,
            settings.EMAIL_HOST_USER,
            ['info@sudvezixercengi.az'],
            fail_silently=False, html_message=message
        )

    return render(request, "elaqe.html", {
        'bashlig' : bashlig,
        'photobashlig' : photobashlig,
        'numberemail' : numberemail,
        'logosekil' : logosekil,
        'gmail' : gmail,
        'mekan' : mekan,
        'bizezeng' : bizezeng,
        'esasfotometn' : esasfotometn,
        'sekil' : sekil,
        'xerite_url' : xerite_url,
        # 'tecilielektron' : tecilielektron,
        # 'teciliinfo' : teciliinfo,
        'haqqimda' : haqqimda,
        'footer_bloq' : footer_bloq,
        'footer_yazi' : footer_yazi,
        'acilish_vaxt' : acilish_vaxt,
        'mobilefoto' : mobilefoto,
        'seoelaqe' : seoelaqe,
        
    })


def konfras(request):
    seoelaqe = SEO_Əlaqə.objects.all()
    mobilefoto = MobileƏsasFoto.objects.all()
    acilish_vaxt = Footer_Açılış_Vaxtları.objects.all()
    footer_yazi = Footer_Yazısı.objects.all()
    footer_bloq = Footer_Bloq.objects.all()
    xerite_url = QəbulXəritə.objects.all()
    sekil = Üst_Şəkil.objects.all()
    gmail = Gmail.objects.all()
    esasfotometn = ƏsasFotoMətnlər.objects.all()
    mekan = Məkan.objects.all()
    bizezeng = BizəZəng.objects.all()
    bashlig = SaytınBaşlığı.objects.all()
    numberemail = BaşlıqNömrəEpoct.objects.all()
    logosekil = LogoŞəkilAnaSəhifə.objects.all()
    haqqimda = SosialŞəbəkəLinkləri.objects.all()
    photobashlig = SaytınBaşlığıFoto.objects.all()

    if request.method == 'POST':
        adtext = request.POST.get('adtext')
        num = request.POST.get('num')
        seriya = request.POST.get('seriya')
        ixtisas = request.POST.get('ixtisas')
        mal = request.POST.get('mal')
        muessise = request.POST.get('muessise')

        data = {
            'adtext': adtext,
            'num' : num,
            'seriya': seriya,
            'mal': mal,
            'muessise': muessise,
            'ixtisas': ixtisas,

        }
        message = render_to_string('konfransmail.html', data)
        send_mail(
            "Konfrans Qeydiyyat bölməsinən mesaj",
            message,
            settings.EMAIL_HOST_USER,
            ['info@sudvezixercengi.az'],
            fail_silently=False, html_message=message
        )

    return render(request, "konfras.html", {
        'bashlig' : bashlig,
        'photobashlig' : photobashlig,
        'numberemail' : numberemail,
        'logosekil' : logosekil,
        'gmail' : gmail,
        'mekan' : mekan,
        'bizezeng' : bizezeng,
        'esasfotometn' : esasfotometn,
        'sekil' : sekil,
        'xerite_url' : xerite_url,
        # 'tecilielektron' : tecilielektron,
        # 'teciliinfo' : teciliinfo,
        'haqqimda' : haqqimda,
        'footer_bloq' : footer_bloq,
        'footer_yazi' : footer_yazi,
        'acilish_vaxt' : acilish_vaxt,
        'mobilefoto' : mobilefoto,
        'seoelaqe' : seoelaqe,
        
    })
