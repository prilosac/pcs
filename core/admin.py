from django.contrib import admin
from .models import *

class ModAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# Register your models here.
admin.site.register(Controller)
admin.site.register(Mod, ModAdmin)
admin.site.register(ControllerImage)
admin.site.register(ModImage)
admin.site.register(GalleryImage)
