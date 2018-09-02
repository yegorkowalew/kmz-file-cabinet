# Generated by Django 2.1.1 on 2018-08-31 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180831_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название типа узла', max_length=30, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Используйте формат: <em>XXX.XXX.XXX.XXX</em>.', max_length=30, verbose_name='Название узла')),
                ('prename', models.ForeignKey(help_text='Используйте формат: <em>XXX.XXX.XXX.XXX</em>.', max_length=30, on_delete='Название узла', to='catalog.PreName')),
                ('stuff', models.ManyToManyField(blank=True, to='catalog.Unit')),
            ],
            options={
                'verbose_name_plural': 'Узлы',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='stuff',
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
