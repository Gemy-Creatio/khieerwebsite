# Generated by Django 3.0 on 2022-04-13 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenCircle', '0025_documentdownload_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinishCircle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('help_accepted', models.BooleanField(blank=True, choices=[(True, 'نعم'), (False, 'لا')], null=True)),
                ('notes', models.TextField(blank=True, max_length=255, null=True)),
                ('is_entertainment', models.BooleanField(blank=True, choices=[(True, 'نعم'), (False, 'لا')], null=True)),
                ('is_loved', models.BooleanField(blank=True, choices=[(True, 'نعم'), (False, 'لا')], null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='documentdownload',
            name='name',
        ),
        migrations.AddField(
            model_name='documentdownload',
            name='firstName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='documentdownload',
            name='lastName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='documentdownload',
            name='category',
            field=models.CharField(blank=True, choices=[('مسار الوعى', 'مسار الوعى'), ('مسار الأرشاد', 'مسار الأرشاد'), ('مسار الولاء ', 'مسار الولاء '), (' لا ارغب  ', ' لا ارغب ')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='greensurvey',
            name='choices',
            field=models.CharField(choices=[('الاطفال المحتضنين ', 'الاطفال المحتضنين '), ('دعم حرفة الخيوط ', 'دعم حرفة الخيوط ')], max_length=255),
        ),
    ]
