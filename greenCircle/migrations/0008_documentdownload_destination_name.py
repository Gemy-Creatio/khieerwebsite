# Generated by Django 3.0 on 2022-01-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenCircle', '0007_documentdownload_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentdownload',
            name='destination_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
