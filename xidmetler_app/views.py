from django.shortcuts import render
from medical_app.views import *
from seo.models import ServiceSeo
from .models import *
from django.urls import reverse
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def bizim_xidmetler(request):
    xidmetlerimiz = Xidmətlər_Postları.objects.all()
    acilish_vaxt = Footer_Açılış_Vaxtları.objects.all()
    footer_yazi = Footer_Yazısı.objects.all()
    melumat_sektoru = Məlumat_Sektoru.objects.all()
    footer_bloq = Footer_Bloq.objects.all()
    haqqimda = SosialŞəbəkəLinkləri.objects.all()
    # baner = Sagbaner.objects.all()
    # digerservis = DigərServislər.objects.all()
    esasfotos = ƏsasFoto.objects.all()
    esasfotoyazilar = ƏsasFoto_ÜstYazılar.objects.all()
    haqqimizdamel = Xidmətlərimiz_Haqqında.objects.all()

    number_items = 6
    page = request.GET.get('page')
    paginator = Paginator(haqqimizdamel, number_items)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    
    index = items.number - 4
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    bashlig = SaytınBaşlığı.objects.all()
    numberemail = BaşlıqNömrəEpoct.objects.all()
    logosekil = LogoŞəkilAnaSəhifə.objects.all()
    photobashlig = SaytınBaşlığıFoto.objects.all()
    bashlig = SaytınBaşlığı.objects.all()
    # servismelumat = ServisMəlumat.objects.all()
    # teciliinfo = TəciliInfo.objects.all()
    # tecilielektron = TəciliElektron_Əlaqe.objects.all()
    numberemail = BaşlıqNömrəEpoct.objects.all()
    logosekil = LogoŞəkilAnaSəhifə.objects.all()
    photobashlig = SaytınBaşlığıFoto.objects.all()
    seo = ServiceSeo.objects.last()
    about = HaqqımızdaŞəkillər.objects.last()
    
    return render(request, 'xidmet.html',{
        'bashlig' : bashlig,
        'photobashlig' : photobashlig,
        'numberemail' : numberemail,
        'logosekil' : logosekil,
        'esasfotos' : esasfotos,
        'esasfotoyazilar' : esasfotoyazilar,
        'haqqimizdamel' : haqqimizdamel,
        # 'servismelumat' : servismelumat,
        # 'digerservis' : digerservis,
        # 'baner' : baner,
        # 'teciliinfo' : teciliinfo,
        # 'tecilielektron' : tecilielektron,
        'haqqimda' : haqqimda,
        'melumat_sektoru' : melumat_sektoru,
        'footer_bloq' : footer_bloq,
        'footer_yazi' : footer_yazi,
        'acilish_vaxt' : acilish_vaxt,
        'xidmetlerimiz' : xidmetlerimiz,
        'page_range' : page_range,
        'items' : items,
        'seo': seo,
        'about': about,
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
        context['diger_bloq'] = PostPaylaşılma.objects.all().order_by('-vaxt')[:6]
        context['acilish_vaxt'] = Footer_Açılış_Vaxtları.objects.all()
        context['footer_yazi'] = Footer_Yazısı.objects.all()
        context['footer_bloq'] = Footer_Bloq.objects.all()
        context['logosekil'] = LogoŞəkilAnaSəhifə.objects.all()
        return context

    

def detail(request):
    haqqimizdamel = Xidmətlərimiz_Haqqında.objects.all()
    return render(request, 'xidmet_detail.html', {
        'haqqimizdamel' : haqqimizdamel,
    })
