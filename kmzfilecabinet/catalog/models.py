from django.db import models
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize, ResizeToFit, Adjust
import re

def clear_string(str):
    """ Очистить строку от лишних символов. Первая буква заглавной """
    for char in '?.!/;:,':
        str = str.replace(char,'') 
    return re.sub(r'\s+', ' ', str.strip().lower().capitalize())

class Unit(models.Model):
    # Инвентарный номер на титульной странице, дата? "Экз №" - оригинален?
    # "действителен на"
    papnum = models.PositiveIntegerField(
                                        verbose_name="Номер папки",
                                        null = True,
                                        blank = True,
                                        unique=True,
                                        help_text="Оригинальный номер папки"
                                        )
    prename = models.ForeignKey(
                            'PreName',
                            verbose_name="Наименование",
                            max_length=30,
                            on_delete=models.CASCADE,
                            help_text='Например: "Роликоопора", "Опора цепи"',
                            )
    name = models.CharField(
                            verbose_name="Обозначение", 
                            unique = True,
                            max_length=30,
                            help_text="Используйте формат: <em>XXX.XXX.XXX.XXX</em>."
                            )
    edit_date = models.DateField(
                            verbose_name="Последнее изменение", 
                            auto_now=True,
                            )
    titul_image = models.ImageField(
                            upload_to='photos',
                            verbose_name="Фото титульной страницы", 
                            blank = True, 
                            )
    comment = models.TextField(
                            verbose_name="Комментарий", 
                            blank = True, 
                            )
    members = models.ManyToManyField(
        'self',
        blank = True,
        through='Membership',
        symmetrical=False,
        related_name='related_to'
        )
    detail = models.ManyToManyField(
        'Detail',
        blank = True,
        through='Memberdetail',
        symmetrical=False,
        related_name='related_to'
        )
    standartdetail = models.ManyToManyField(
        'StandartDetail',
        blank = True,
        through='Memberstandartdetail',
        symmetrical=False,
        related_name='related_to'
        )
    crop200 = ImageSpecField([
        Adjust(contrast=1.2, sharpness=1.1),
        SmartResize(170, 170),
    ],
        source='titul_image',
        options={
            'quality': 90,
            'progressive': True,
        }
    )
    def __unicode__(self):
        return self.name % self.id
    def __str__(self):
            return '%s %s %s' % (self.name, self.prename.name)
    def get_absolute_url(self):
        return "/units/%i/" % self.id
    class Meta:
        ordering = ["name"]
        verbose_name = "сборочная единица"
        verbose_name_plural = "сборочные единицы"

class Detail(models.Model):
    nom_num = models.CharField(max_length=50, #1
                            verbose_name="Наименование 'Крышка'", 
                            )
    designation = models.CharField(max_length=50, #2
                            verbose_name="Обозначение 'ТСЦ-400.000.000'", 
                            )
    file_pdf = models.FileField( #3
                            verbose_name="pdf файл", 
                            blank = True, 
                            )
    file_jpg = models.FileField( #4
                            verbose_name="jpg файл", 
                            blank = True, 
                            )
    file_cdw = models.FileField( #5
                            verbose_name="cdw файл", 
                            blank = True, 
                            )
    stub_name = models.ForeignKey( #6
                            'StubName',
                            verbose_name="Заготовка",
                            max_length=30,
                            on_delete=models.CASCADE,
                            help_text='Например: "Уголок", "Двутавр"',
                            blank = True,
                            null = True,
                            )
    part_weight = models.FloatField( #7
                            verbose_name="Теоретический вес детали", 
                            blank = True,
                            null = True,
                                                )
    metaltype = models.ForeignKey( #8
                            'Metaltype',
                            verbose_name="Тип стали", 
                            max_length=30,
                            help_text="Обязательное поле",
                            on_delete=models.CASCADE,
                            blank = True,
                            null = True,
                            )
    test_width = models.PositiveIntegerField( #10
                            verbose_name="Длинна",
                            null = True,
                            blank = True,
                            unique=True,
                            help_text="Длинна черновой детали"
                            )
    test_height = models.PositiveIntegerField( #11
                            verbose_name="Ширина",
                            null = True,
                            blank = True,
                            unique=True,
                            help_text="Ширина черновой детали"
                            )
    diameter = models.PositiveIntegerField( #12
                            verbose_name="Диаметр",
                            null = True,
                            blank = True,
                            unique=True,
                            help_text="Диаметр, если это труба или цилиндр"
                            )
    shelf_height = models.PositiveIntegerField( #13
                            verbose_name="Высота полки",
                            null = True,
                            blank = True,
                            unique=True,
                            help_text="Высота полки, если это уголок"
                            )
    thickness = models.PositiveIntegerField( #9
                            verbose_name="Толщина",
                            null = True,
                            blank = True,
                            unique=True,
                            help_text="Толщина детали"
                            )

    array_height = models.PositiveIntegerField( #14
                            verbose_name="Длинна",
                            null = True,
                            blank = True,
                            unique=True,
                            help_text="Длинна заготовки для массива"
                            )
    array_width = models.PositiveIntegerField( #15
                            verbose_name="Ширина",
                            null = True,
                            blank = True,
                            unique=True,
                            help_text="Ширина заготовки для массива"
                            )
    array_amount = models.PositiveIntegerField( #16
                            verbose_name="Количество",
                            null = True,
                            blank = True,
                            unique=True,
                            help_text="Количество деталей из массива"
                            )
    color_coating = models.ForeignKey( #18
                            'ColorCoating',
                            verbose_name="Цвет покрытия", 
                            max_length=30,
                            help_text='Цвет покрытия, если деталь красят',
                            on_delete=models.CASCADE,
                            blank = True,
                            null = True,
                            )
    coatingclass = models.ForeignKey(
                            'Сoatingclass',
                            verbose_name="Тип цинка", 
                            max_length=30,
                            help_text="Тип цинка, если деталь на цинковании",
                            on_delete=models.CASCADE,
                            blank = True,
                            null = True,
                            )
    edit_date = models.DateField(
                            verbose_name="Последнее изменение", 
                            auto_now=True,
                            )
    shop = models.ManyToManyField(
        'Shop',
        through='MemberShop',
        symmetrical=False,
        related_name='related_to_shop'
        )
    detail_date = models.DateField(
                            verbose_name="Дата редактирования детали", 
                            auto_now=True,
                            )
    class Meta:
        ordering = ["nom_num"]
        verbose_name = "деталь"
        verbose_name_plural = "детали"
    def __str__(self):
            return self.nom_num
    def get_absolute_url(self):
        return "/details/%i/" % self.id

class StandartDetailCreator(models.Model):
    name = models.CharField(max_length=50,
                            unique = True,
                            verbose_name="Название", 
                            )
    edit_date = models.DateField(
                            verbose_name="Последнее изменение", 
                            auto_now=True,
                            )
    class Meta:
        verbose_name = ("Родитель стандартной детали")
        verbose_name_plural = ("Родители стандартной детали")
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
        # return reverse("standartdetailcreator_detail", kwargs={"pk": self.pk})

class StandartDetail(models.Model):
    nom_num = models.CharField(max_length=50,
                            unique = True,
                            verbose_name="Обозначение", 
                            )
    standart_detail_creator = models.ForeignKey(
        "StandartDetailCreator", 
        verbose_name=("Родитель стандартной детали"), 
        on_delete=models.CASCADE,
        blank = True)
    edit_date = models.DateField(
                            verbose_name="Последнее изменение", 
                            auto_now=True,
                            )
    class Meta:
        verbose_name = "стандартное изделие"
        verbose_name_plural = "стандартные изделия"

    def __unicode__(self):
        return self.standart_detail_creator.name % self.nom_num
    def __str__(self):
        return '%s %s' % (self.standart_detail_creator.name, self.nom_num)

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

class UnitContentPhoto(models.Model):
    image = models.ImageField(
                            upload_to='photos',
                            )
    unit = models.ForeignKey(
                            Unit, 
                            related_name='unitimage', 
                            on_delete=models.CASCADE,
                            )
    crop200 = ImageSpecField([
        Adjust(contrast=1.2, sharpness=1.1),
        SmartResize(200, 200),
    ],
        source='image',
        options={
            'quality': 90,
            'progressive': True,
        }
    )
    class Meta:
        verbose_name = "скан спецификации"
        verbose_name_plural = "сканы спецификации"

class PreName(models.Model):
    name = models.CharField("Название", 
                            max_length=30,
                            help_text='Например: "Роликоопора", "Опора цепи"',
                            unique = True,
                            )
    def __str__(self):
            return self.name
    class Meta:
        ordering = ["name"]
        verbose_name = "тип узла"
        verbose_name_plural = "типы узлов"
    def save(self):
        self.name = clear_string(self.name)
        super(PreName, self).save()

class StubName(models.Model):
    name = models.CharField("Название", 
                            max_length=30,
                            help_text='Например: "Уголок", "Двутавр"',
                            unique = True,
                            )
    def __str__(self):
            return self.name
    class Meta:
        ordering = ["name"]
        verbose_name = "тип заготовки"
        verbose_name_plural = "типы заготовок"
    def save(self):
        self.name = clear_string(self.name)
        super(PreName, self).save()

class Membership(models.Model):
    from_u = models.ForeignKey(Unit, 
                                related_name='from_unit', 
                                on_delete=models.CASCADE,
                                verbose_name="Родитель", 
                                )
    to_u = models.ForeignKey(Unit, 
                                related_name='to_unit', 
                                on_delete=models.CASCADE,
                                verbose_name="Сборочная единица", 
                                )
    amount = models.PositiveIntegerField(verbose_name="Количество", 
                                        )
    class Meta:
        unique_together = ('from_u', 'to_u')
        verbose_name = "сборочная единица"
        verbose_name_plural = "сборочные единицы"
    def __str__(self):
            return '%s -> %s (%s)' % (self.from_u.name, self.from_u.name, str(self.amount))

class Metaltype(models.Model):
    name = models.CharField(max_length=50,
                            unique = True,
                            )
    class Meta:
        ordering = ["name"]
        verbose_name = "тип металла"
        verbose_name_plural = "типы металлов"
    def __str__(self):
            return self.name

class Сoatingclass(models.Model):
    name = models.CharField(max_length=10,
                            unique = True,
                            verbose_name="Название",
                            )
    type = models.CharField(max_length=20,
                            verbose_name="Холодный или горячий",
                            )
    class Meta:
        ordering = ["type"]
        verbose_name = "тип цинкования"
        verbose_name_plural = "типы цинкования"
    def __str__(self):
            return '%s: %s' % (self.type, self.name)

class ColorCoating(models.Model):
    color_name = models.CharField(max_length=50,
                            unique = True,
                            verbose_name="Цвет по каталогу RAL",
                            )
    color_type = models.CharField(max_length=20,
                            verbose_name="Грунт или емаль",
                            )
    class Meta:
        verbose_name = "цвет покрытия"
        verbose_name_plural = "цвета покрытия"
    def __str__(self):
            return '%s: %s' % (self.color_type, self.color_name)

class Shop(models.Model):
    text_name = models.CharField(max_length=50,
                            unique = True,
                            )
    num_name = models.CharField(max_length=50,
                            unique = True,
                            )
    class Meta:
        ordering = ["num_name"]
        verbose_name = "цех"
        verbose_name_plural = "цехи"
    def __str__(self):
            return '%s (%s)' % (self.num_name, self.text_name)
    def save(self):
        self.text_name = clear_string(self.text_name)
        super(Shop, self).save()

class Operation(models.Model):
    text_name = models.CharField(max_length=50,
                            unique = True,
                            verbose_name = "Название"
                            )
    class Meta:
        ordering = ["text_name"]
        verbose_name = "операция"
        verbose_name_plural = "операции"
    def __str__(self):
            return self.text_name
    def save(self):
        self.text_name = clear_string(self.text_name)
        super(Operation, self).save()

class MemberShop(models.Model):
    from_u = models.ForeignKey('Detail', 
                                related_name='from_detail_to_shop', 
                                on_delete=models.CASCADE,
                                verbose_name="Родитель", 
                                )
    to_u = models.ForeignKey(Shop, 
                                related_name='to_shop', 
                                on_delete=models.CASCADE,
                                verbose_name="Цех", 
                                )
    amount = models.PositiveIntegerField(verbose_name="очередь",)
    class Meta:
        unique_together = ('from_u', 'to_u')
        verbose_name = "цех"
        verbose_name_plural = "цехи"
    def __str__(self):
            return '%s -> %s (%s)' % (self.from_u.nom_num, self.to_u.text_name, str(self.amount))

class Memberdetail(models.Model):
    from_u = models.ForeignKey('Unit', 
                                related_name='from_unit_to_detail', 
                                on_delete=models.CASCADE,
                                verbose_name="Родитель", 
                                )
    to_u = models.ForeignKey('Detail', 
                                related_name='to_detail', 
                                on_delete=models.CASCADE,
                                verbose_name="деталь", 
                                )
    amount = models.PositiveIntegerField(verbose_name="Количество", 
                                        )
    class Meta:
        unique_together = ('from_u', 'to_u')
        verbose_name = "деталь"
        verbose_name_plural = "детали"
    def __str__(self):
            return '%s -> %s (%s)' % (self.from_u.name, self.to_u.nom_num, str(self.amount))

class Memberstandartdetail(models.Model):
    from_u = models.ForeignKey('Unit', 
                                related_name='from_unit_to_standart_detail', 
                                on_delete=models.CASCADE,
                                verbose_name="Родитель", 
                                )
    to_u = models.ForeignKey('StandartDetail', 
                                related_name='to_standart_detail', 
                                on_delete=models.CASCADE,
                                verbose_name="Стандартное изделие", 
                                )
    amount = models.PositiveIntegerField(verbose_name="Количество", 
                                        )
    class Meta:
        unique_together = ('from_u', 'to_u')
        verbose_name = "стандартное изделие"
        verbose_name_plural = "стандартные изделия"
    def __str__(self):
            return '%s -> %s (%s)' % (self.from_u.name, self.to_u.nom_num, str(self.amount))