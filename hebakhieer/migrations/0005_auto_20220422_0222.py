# Generated by Django 3.0 on 2022-04-22 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hebakhieer', '0004_auto_20220422_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='joiners_cv/'),
        ),
    ]
