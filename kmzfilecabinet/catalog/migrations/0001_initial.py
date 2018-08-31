# Generated by Django 2.1.1 on 2018-08-31 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название узла')),
                ('stuff', models.ManyToManyField(related_name='_mymodel_stuff_+', to='catalog.MyModel')),
            ],
        ),
    ]
