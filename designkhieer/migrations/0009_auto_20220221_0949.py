# Generated by Django 3.0 on 2022-02-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designkhieer', '0008_designerjoinus_is_accept_policy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designerjoinus',
            name='national_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
