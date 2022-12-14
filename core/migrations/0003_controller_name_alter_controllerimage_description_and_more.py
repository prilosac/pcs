# Generated by Django 4.1.1 on 2022-09-26 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_controllerimage_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='controller',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='controllerimage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mod',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modimage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
