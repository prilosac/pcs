from core.models import Mod

def nav_mods(request):
    return {'nav_mods': Mod.objects.all()}
