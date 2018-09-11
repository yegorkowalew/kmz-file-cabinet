# Generated by Django 2.1.1 on 2018-09-11 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_detail_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
            ],
        ),
        migrations.RemoveField(
            model_name='detail',
            name='shop',
        ),
        migrations.AddField(
            model_name='membershop',
            name='from_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_detail_to_shop', to='catalog.Detail', verbose_name='Родитель'),
        ),
        migrations.AddField(
            model_name='membershop',
            name='to_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_shop', to='catalog.Shop', verbose_name='Цех'),
        ),
        migrations.AddField(
            model_name='detail',
            name='shop',
            field=models.ManyToManyField(related_name='related_to', through='catalog.MemberShop', to='catalog.Shop'),
        ),
    ]
