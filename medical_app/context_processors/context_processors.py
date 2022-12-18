from medical_app.models import SaytınBaşlığıFoto


def header_and_footer(request):
    context = {
        'context_icons': SaytınBaşlığıFoto.objects.last(),
    }
    return context
