# Generated by Django 2.1.1 on 2018-10-11 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20181011_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standartdetail',
            name='standart_detail_creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.StandartDetailCreator', verbose_name='Родитель стандартной детали'),
        ),
    ]
