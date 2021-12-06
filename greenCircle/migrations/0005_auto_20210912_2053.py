# Generated by Django 3.0 on 2021-09-12 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greenCircle', '0004_auto_20210912_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='greenCircle.Trainer', verbose_name='المدرب'),
        ),
        migrations.AlterField(
            model_name='courserequest',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Requests', to='greenCircle.Course'),
        ),
    ]