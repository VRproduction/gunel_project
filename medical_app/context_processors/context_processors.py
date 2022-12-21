from medical_app.models import SaytınBaşlığıFoto
from seo.models import HeadSeoContent, BodySeoContent


def header_and_footer(request):
    context = {
        'context_icons': SaytınBaşlığıFoto.objects.last(),
        'head_seo_content': HeadSeoContent.objects.all(),
        'body_seo_content': BodySeoContent.objects.all(),
    }
    return context
