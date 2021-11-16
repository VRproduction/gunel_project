from django.shortcuts import render
from medical_app.views import *
from .models import *
from blog_app.models import *
from django.urls import reverse
from django.views.generic import DetailView

# Create your views here.
def bizim_xidmetler(request):
    melumat_sektoru = Məlumat_Sektoru.objects.all()
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
        'melumat_sektoru' : melumat_sektoru,
    })


class NewsDetailView(DetailView):
    model = Xidmətlərimiz_Haqqında
    template_name = 'xidmet_detail.html'
    context_object_name = 'haqqimizdameli'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['numberemail'] = BaşlıqNömrəEpoct.objects.all()
        context['haqqimda'] = SosialŞəbəkəLinkləri.objects.all()
        context['esasfoto'] = ƏsasFoto.objects.all()
        context['haqqimda_melumat'] = Haqqımda_Məlumat.objects.all()
        context['instagram_post'] = İnstagram_Postları.objects.all()
        context['diger_bloq'] = Digər_Bloqlar.objects.all()
        return context

    

def detail(request):
    haqqimizdamel = Xidmətlərimiz_Haqqında.objects.all()
    return render(request, 'xidmet_detail.html', {
        'haqqimizdamel' : haqqimizdamel,
    })
