from django.core import paginator
from django.shortcuts import render
from medical_app.models import *
from medical_app.views import *
from xidmetler_app.models import *
from .models import *
from django.views.generic import DetailView
from xidmetler_app.views import NewsDetailView,detail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def blog(request):
    metatag = SEO_Bloq.objects.all()
    xidmetlerimiz = Xidmətlər_Postları.objects.all()
    footer_yazi = Footer_Yazısı.objects.all()
    acilish_vaxt = Footer_Açılış_Vaxtları.objects.all()
    instagram_post = İnstagram_Postları.objects.all()
    haqqimda_melumat = Haqqımda_Məlumat.objects.all()
    diger_bloq = Digər_Bloqlar.objects.all()
    footer_bloq = Footer_Bloq.objects.all()
    haqqimda = SosialŞəbəkəLinkləri.objects.all()
    # baner = Sagbaner.objects.all()
    esasfoto_metn = ƏsasFoto_ÜstMətn.objects.all()
    esasfoto = ƏsasFoto.objects.all()
    posts = PostPaylaşılma.objects.all()

    number_items = 3
    page = request.GET.get('page')
    paginator = Paginator(posts, number_items)
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
    return render(request, 'blog_main.html', {
        'bashlig' : bashlig,
        'photobashlig' : photobashlig,
        'numberemail' : numberemail,
        'logosekil' : logosekil,
        'esasfoto_metn' : esasfoto_metn,
        'esasfoto' : esasfoto,
        'posts' : posts,
        'haqqimda' : haqqimda,
        # 'baner' : baner,
        'haqqimda_melumat' : haqqimda_melumat,
        'diger_bloq' : diger_bloq,
        'instagram_post' : instagram_post,
        'footer_bloq' : footer_bloq,
        'footer_yazi' : footer_yazi,
        'acilish_vaxt' : acilish_vaxt,
        'xidmetlerimiz' : xidmetlerimiz,
        'page_range' : page_range,
        'items' : items,
        'metatag' : metatag,
    })

class BlogDetailView(DetailView):
    model = PostPaylaşılma
    template_name = 'blog_detail.html'
    context_object_name = 'bloging'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['numberemail'] = BaşlıqNömrəEpoct.objects.all()
        context['haqqimda'] = SosialŞəbəkəLinkləri.objects.all()
        context['esasfoto'] = ƏsasFoto.objects.all()
        context['haqqimda_melumat'] = Haqqımda_Məlumat.objects.all()
        context['instagram_post'] = İnstagram_Postları.objects.all()
        context['diger_bloq'] = Digər_Bloqlar.objects.all()
        context['logosekil'] = LogoŞəkilAnaSəhifə.objects.all()
        context['acilish_vaxt'] = Footer_Açılış_Vaxtları.objects.all()
        context['footer_yazi'] = Footer_Yazısı.objects.all()
        context['footer_bloq'] = Footer_Bloq.objects.all()
        context['xidmetlerimiz'] = Xidmətlər_Postları.objects.all()
        return context

    
def blogin(request):
    haqqimda = SosialŞəbəkəLinkləri.objects.all()
    posts = PostPaylaşılma.objects.all()
    numberemail = BaşlıqNömrəEpoct.objects.all()
    print(numberemail)
    return render(request, 'blog_detail.html', {
        'posts' : posts,
        'numberemail' : numberemail,
        'haqqimda' : haqqimda,
    })