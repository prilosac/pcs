# Generated by Django 4.1.1 on 2022-09-28 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_controller_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controller',
            name='mods',
            field=models.ManyToManyField(blank=True, to='core.mod'),
        ),
    ]
