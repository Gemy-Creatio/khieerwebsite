# Generated by Django 3.0 on 2022-03-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220126_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicGreen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('filed', models.CharField(blank=True, max_length=200, null=True)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('number_target', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('effect', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
