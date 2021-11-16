from django.shortcuts import render
from medical_app.models import *
from medical_app.views import *
from xidmetler_app.models import *
from .models import *
from django.views.generic import DetailView
# Create your views here.

def blog(request):
    acilish_vaxt = Footer_Açılış_Vaxtları.objects.all()
    footer_yazi = Footer_Yazısı.objects.all()
    instagram_post = İnstagram_Postları.objects.all()
    haqqimda_melumat = Haqqımda_Məlumat.objects.all()
    diger_bloq = Digər_Bloqlar.objects.all()
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
        'hekaye' : hekaye,
        # 'baner' : baner,
        'footer_bloq' : footer_bloq,
        'haqqimda_melumat' : haqqimda_melumat,
        'diger_bloq' : diger_bloq,
        'instagram_post' : instagram_post,
        'footer_yazi' : footer_yazi,
        'acilish_vaxt' : acilish_vaxt,
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