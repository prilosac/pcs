import datetime
from time import strftime

from django.db import models
from django.utils import timezone

# Create your models here.
class Controller(models.Model):

    CONTROLLER_TYPE_CHOICES = [
        ('gcc', 'OEM GameCube Controller'),
        ('phobgcc', 'PhobGCC'),
        ('rectangle', 'Rectangle')
    ]

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=CONTROLLER_TYPE_CHOICES)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    discount = models.DecimalField(max_digits=14, decimal_places=2)
    mods = models.ManyToManyField('Mod')
    hidden = models.BooleanField(default=True)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Mod(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    slug = models.SlugField(max_length=50)
    display_nav = models.BooleanField(default=True)

    def __str__(self):
        return self.name

#class ModSet(models.Model):
#    """
#    Set of mods grouped together.
#    Usually for discounting certain groupings
#    """
#
#    mods = models.ManyToManyField('Mod')
#    discount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
#    active_at = models.DateTimeField(default=timezone.now)
#    inactive_at = models.DateTimeField()
#
#    def set_active(self, datetime=datetime.datetime.now):
#        self.active_at = datetime
#        self.save()
#
#    def set_inactive(self, datetime=datetime.datetime.now):
#        self.inactive_at = datetime
#        self.save()

def image_upload_path(instance, filename):
    return '{}/{}/{}'.format(
                type(instance).__name__,
                strftime('%Y/%m/%d'),
                filename
            )

class Image(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=image_upload_path)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title

class ControllerImage(Image):
    controller = models.ForeignKey('Controller', on_delete=models.DO_NOTHING)
    primary = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.controller.name, 'primary' if self.primary else 'secondary')

class ModImage(Image):
    mod = models.ForeignKey('Mod', on_delete=models.DO_NOTHING)
    primary = models.BooleanField(default=False)
    
    def __str__(self):
        return '{} {}'.format(self.mod.name, 'primary' if self.primary else 'secondary')

class GalleryImage(Image):
    pass

