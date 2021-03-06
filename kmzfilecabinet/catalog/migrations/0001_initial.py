# Generated by Django 2.1.1 on 2018-11-02 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColorCoating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=50, unique=True, verbose_name='Цвет по каталогу RAL')),
                ('color_type', models.CharField(max_length=20, verbose_name='Грунт или емаль')),
            ],
            options={
                'verbose_name': 'цвет покрытия',
                'verbose_name_plural': 'цвета покрытия',
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_num', models.CharField(max_length=50, verbose_name="Наименование 'Крышка'")),
                ('designation', models.CharField(max_length=50, verbose_name="Обозначение 'ТСЦ-400.000.000'")),
                ('file_pdf', models.FileField(blank=True, upload_to='', verbose_name='pdf файл')),
                ('file_jpg', models.FileField(blank=True, upload_to='', verbose_name='jpg файл')),
                ('file_cdw', models.FileField(blank=True, upload_to='', verbose_name='cdw файл')),
                ('part_weight', models.FloatField(blank=True, null=True, verbose_name='Теоретический вес детали')),
                ('test_width', models.PositiveIntegerField(blank=True, help_text='Длинна черновой детали', null=True, unique=True, verbose_name='Длинна')),
                ('test_height', models.PositiveIntegerField(blank=True, help_text='Ширина черновой детали', null=True, unique=True, verbose_name='Ширина')),
                ('diameter', models.PositiveIntegerField(blank=True, help_text='Диаметр, если это труба или цилиндр', null=True, unique=True, verbose_name='Диаметр')),
                ('shelf_height', models.PositiveIntegerField(blank=True, help_text='Высота полки, если это уголок', null=True, unique=True, verbose_name='Высота полки')),
                ('thickness', models.PositiveIntegerField(blank=True, help_text='Толщина детали', null=True, unique=True, verbose_name='Толщина')),
                ('array_height', models.PositiveIntegerField(blank=True, help_text='Длинна заготовки для массива', null=True, unique=True, verbose_name='Длинна')),
                ('array_width', models.PositiveIntegerField(blank=True, help_text='Ширина заготовки для массива', null=True, unique=True, verbose_name='Ширина')),
                ('array_amount', models.PositiveIntegerField(blank=True, help_text='Количество деталей из массива', null=True, unique=True, verbose_name='Количество')),
                ('edit_date', models.DateField(auto_now=True, verbose_name='Последнее изменение')),
                ('detail_date', models.DateField(auto_now=True, verbose_name='Дата редактирования детали')),
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
                'verbose_name': 'деталь',
                'verbose_name_plural': 'детали',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'сборочная единица',
                'verbose_name_plural': 'сборочные единицы',
            },
        ),
        migrations.CreateModel(
            name='MemberShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='очередь')),
                ('from_u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_detail_to_shop', to='catalog.Detail', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'цех',
                'verbose_name_plural': 'цехи',
            },
        ),
        migrations.CreateModel(
            name='Memberstandartdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'стандартное изделие',
                'verbose_name_plural': 'стандартные изделия',
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
                ('text_name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'операция',
                'verbose_name_plural': 'операции',
                'ordering': ['text_name'],
            },
        ),
        migrations.CreateModel(
            name='PreName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например: "Роликоопора", "Опора цепи"', max_length=30, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'тип узла',
                'verbose_name_plural': 'типы узлов',
                'ordering': ['name'],
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
            name='StandartDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_num', models.CharField(max_length=50, unique=True, verbose_name='Обозначение')),
                ('edit_date', models.DateField(auto_now=True, verbose_name='Последнее изменение')),
            ],
            options={
                'verbose_name': 'стандартное изделие',
                'verbose_name_plural': 'стандартные изделия',
            },
        ),
        migrations.CreateModel(
            name='StandartDetailCreator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('edit_date', models.DateField(auto_now=True, verbose_name='Последнее изменение')),
            ],
            options={
                'verbose_name': 'Родитель стандартной детали',
                'verbose_name_plural': 'Родители стандартной детали',
            },
        ),
        migrations.CreateModel(
            name='StubName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например: "Уголок", "Двутавр"', max_length=30, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'тип заготовки',
                'verbose_name_plural': 'типы заготовок',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('papnum', models.PositiveIntegerField(blank=True, help_text='Оригинальный номер папки', null=True, unique=True, verbose_name='Номер папки')),
                ('name', models.CharField(help_text='Используйте формат: <em>XXX.XXX.XXX.XXX</em>.', max_length=30, unique=True, verbose_name='Обозначение')),
                ('edit_date', models.DateField(auto_now=True, verbose_name='Последнее изменение')),
                ('titul_image', models.ImageField(blank=True, upload_to='photos', verbose_name='Фото титульной страницы')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('detail', models.ManyToManyField(blank=True, related_name='related_to', through='catalog.Memberdetail', to='catalog.Detail')),
                ('members', models.ManyToManyField(blank=True, related_name='related_to', through='catalog.Membership', to='catalog.Unit')),
                ('prename', models.ForeignKey(help_text='Например: "Роликоопора", "Опора цепи"', max_length=30, on_delete=django.db.models.deletion.CASCADE, to='catalog.PreName', verbose_name='Наименование')),
                ('standartdetail', models.ManyToManyField(blank=True, related_name='related_to', through='catalog.Memberstandartdetail', to='catalog.StandartDetail')),
            ],
            options={
                'verbose_name': 'сборочная единица',
                'verbose_name_plural': 'сборочные единицы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UnitContentPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unitimage', to='catalog.Unit')),
            ],
            options={
                'verbose_name': 'скан спецификации',
                'verbose_name_plural': 'сканы спецификации',
            },
        ),
        migrations.CreateModel(
            name='Сoatingclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='Название')),
                ('type', models.CharField(max_length=20, verbose_name='Холодный или горячий')),
            ],
            options={
                'verbose_name': 'тип цинкования',
                'verbose_name_plural': 'типы цинкования',
                'ordering': ['type'],
            },
        ),
        migrations.AddField(
            model_name='standartdetail',
            name='standart_detail_creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.StandartDetailCreator', verbose_name='Родитель стандартной детали'),
        ),
        migrations.AddField(
            model_name='memberstandartdetail',
            name='from_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_unit_to_standart_detail', to='catalog.Unit', verbose_name='Родитель'),
        ),
        migrations.AddField(
            model_name='memberstandartdetail',
            name='to_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_standart_detail', to='catalog.StandartDetail', verbose_name='Стандартное изделие'),
        ),
        migrations.AddField(
            model_name='membershop',
            name='to_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_shop', to='catalog.Shop', verbose_name='Цех'),
        ),
        migrations.AddField(
            model_name='membership',
            name='from_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_unit', to='catalog.Unit', verbose_name='Родитель'),
        ),
        migrations.AddField(
            model_name='membership',
            name='to_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_unit', to='catalog.Unit', verbose_name='Сборочная единица'),
        ),
        migrations.AddField(
            model_name='memberdetail',
            name='from_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_unit_to_detail', to='catalog.Unit', verbose_name='Родитель'),
        ),
        migrations.AddField(
            model_name='memberdetail',
            name='to_u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_detail', to='catalog.Detail', verbose_name='деталь'),
        ),
        migrations.AddField(
            model_name='detail',
            name='coatingclass',
            field=models.ForeignKey(blank=True, help_text='Тип цинка, если деталь на цинковании', max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Сoatingclass', verbose_name='Тип цинка'),
        ),
        migrations.AddField(
            model_name='detail',
            name='color_coating',
            field=models.ForeignKey(blank=True, help_text='Цвет покрытия, если деталь красят', max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.ColorCoating', verbose_name='Цвет покрытия'),
        ),
        migrations.AddField(
            model_name='detail',
            name='metaltype',
            field=models.ForeignKey(blank=True, help_text='Обязательное поле', max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Metaltype', verbose_name='Тип стали'),
        ),
        migrations.AddField(
            model_name='detail',
            name='shop',
            field=models.ManyToManyField(related_name='related_to_shop', through='catalog.MemberShop', to='catalog.Shop'),
        ),
        migrations.AddField(
            model_name='detail',
            name='stub_name',
            field=models.ForeignKey(blank=True, help_text='Например: "Уголок", "Двутавр"', max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.StubName', verbose_name='Заготовка'),
        ),
        migrations.AlterUniqueTogether(
            name='memberstandartdetail',
            unique_together={('from_u', 'to_u')},
        ),
        migrations.AlterUniqueTogether(
            name='membershop',
            unique_together={('from_u', 'to_u')},
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together={('from_u', 'to_u')},
        ),
        migrations.AlterUniqueTogether(
            name='memberdetail',
            unique_together={('from_u', 'to_u')},
        ),
    ]
