# Generated by Django 2.2 on 2021-07-29 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default='dojo antiguo', max_length=255),
            preserve_default=False,
        ),
    ]
