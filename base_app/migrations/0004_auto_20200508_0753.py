# Generated by Django 3.0.6 on 2020-05-08 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0003_realestate_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.TypeOffice', verbose_name='Przeznaczenie lokalu'),
        ),
    ]
