# Generated by Django 2.1.1 on 2018-09-04 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180904_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_num', models.CharField(max_length=50, unique=True, verbose_name='Номенкулатурный номер')),
                ('file_pdf', models.FileField(blank=True, upload_to='', verbose_name='pdf файл')),
                ('file_jpg', models.FileField(blank=True, upload_to='', verbose_name='jpg файл')),
                ('file_cdw', models.FileField(blank=True, upload_to='', verbose_name='cdw файл')),
                ('part_weight', models.PositiveIntegerField(verbose_name='Теоретический вес детали')),
                ('edit_date', models.DateField(auto_now=True, verbose_name='Последнее изменение')),
                ('detail_date', models.DateField(verbose_name='Дата редактирования детали')),
            ],
            options={
                'verbose_name': 'деталь',
                'verbose_name_plural': 'детали',
                'ordering': ['nom_num'],
            },
        ),
        migrations.CreateModel(
            name='Memberdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'вложенная деталь',
                'verbose_name_plural': 'вложенные детали',
            },
        ),
        migrations.CreateModel(
            name='Metaltype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'тип металла',
                'verbose_name_plural': 'типы металлов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'операция',
                'verbose_name_plural': 'операции',
                'ordering': ['text_name'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_name', models.CharField(max_length=50, unique=True)),
                ('num_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'цех',
                'verbose_name_plural': 'цехи',
                'ordering': ['num_name'],
            },
        ),
        migrations.CreateModel(
            name='Сoatingclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'класс покрытия',
                'verbose_name_plural': 'классы покрытия',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='membership',
            options={'verbose_name': 'вложенный узел', 'verbose_name_plural': 'вложенные узлы'},
        ),
        migrations.AlterModelOptions(
            name='prename',
            options={'ordering': ['name'], 'verbose_name': 'тип узла', 'verbose_name_plural': 'типы узлов'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['name'], 'verbose_name': 'узел', 'verbose_name_plural': 'Узлы'},
        ),
        migrations.AddField(
            model_name='memberdetail',
            name='from_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_unit_to_detail', to='catalog.Unit', verbose_name='Родитель'),
        ),
        migrations.AddField(
            model_name='memberdetail',
            name='to_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_detail', to='catalog.Detail', verbose_name='Вложенная деталь'),
        ),
        migrations.AddField(
            model_name='detail',
            name='metaltype',
            field=models.ForeignKey(help_text='Обязательное поле', max_length=30, on_delete=django.db.models.deletion.CASCADE, to='catalog.Metaltype', verbose_name='Тип металла'),
        ),
        migrations.AddField(
            model_name='detail',
            name='сoatingclass',
            field=models.ForeignKey(help_text='Обязательное поле', max_length=30, on_delete=django.db.models.deletion.CASCADE, to='catalog.Сoatingclass', verbose_name='Класс покрытия'),
        ),
        migrations.AddField(
            model_name='unit',
            name='detail',
            field=models.ManyToManyField(related_name='related_to', through='catalog.Memberdetail', to='catalog.Detail'),
        ),
        migrations.AlterUniqueTogether(
            name='memberdetail',
            unique_together={('from_u', 'to_u')},
        ),
    ]