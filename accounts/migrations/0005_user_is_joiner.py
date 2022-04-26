# Generated by Django 3.0 on 2022-04-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220401_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_joiner',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as an Joiner Circle. ', verbose_name='Joiner Circle '),
        ),
    ]
