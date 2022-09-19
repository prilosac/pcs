import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Controller(models.Model):

    CONTROLLER_TYPE_CHOICES = [
        ('gcc', 'OEM GameCube Controller'),
        ('phobgcc', 'PhobGCC'),
        ('rectangle', 'Rectangle')
    ]

    type = models.CharField(max_length=20, choices=CONTROLLER_TYPE_CHOICES)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    mods = models.ManyToManyField('Mod')
    image = models.ForeignKey('Image', on_delete=models.DO_NOTHING, null=True)

class Mod(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    image = models.ForeignKey('Image', on_delete=models.DO_NOTHING, null=True)

class ModSet(models.Model):
    """
    Set of mods grouped together.
    Usually for discounting certain groupings
    """

    mods = models.ManyToManyField('Mod')
    discount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    active_at = models.DateTimeField(default=timezone.now)
    inactive_at = models.DateTimeField()

    def set_active(self, datetime=datetime.datetime.now):
        self.active_at = datetime
        self.save()

    def set_inactive(self, datetime=datetime.datetime.now):
        self.inactive_at = datetime
        self.save()

def image_upload_path(instance, filename):
    return '{}/%Y/%m/%d'.format(instance.type)

class Image(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=20)
    image = models.ImageField(upload_to=image_upload_path)
    
