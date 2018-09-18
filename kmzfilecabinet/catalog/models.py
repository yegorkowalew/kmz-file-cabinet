from django.db import models

import re

def clear_string(str):
    """ Очистить строку от лишних символов. Первая буква заглавной """
    for char in '?.!/;:,':
        str = str.replace(char,'') 
    return re.sub(r'\s+', ' ', str.strip().lower().capitalize())

class AbbrName(models.Model):
    name = models.CharField("Аббревиатура узла", 
                            max_length=30,
                            help_text="Аббревиатура узла",
                            unique = True,
                            )
    def __str__(self):
            return self.name
    class Meta:
        ordering = ["name"]
        verbose_name = "аббревиатура"
        verbose_name_plural = "аббревиатуры"
    def save(self):
        self.name = clear_string(self.name)
        super(AbbrName, self).save()

class PreName(models.Model):
    name = models.CharField("Название", 
                            max_length=30,
                            help_text="Название типа узла",
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

class Unit(models.Model):
    # Инвентарный номер на титульной странице, дата? "Экз №" - оригинален?
    # "действителен на"
    # ТСЦ - аббревиатура изделия
    abbrname = models.ForeignKey(
                            'AbbrName',
                            verbose_name="Аббревиатура узла",
                            max_length=30,
                            help_text="Не обязательное поле",
                            on_delete=models.CASCADE,
                            blank = True,
                            null=True,
                            )
    prename = models.ForeignKey(
                            'PreName',
                            verbose_name="Тип узла",
                            max_length=30,
                            help_text="Обязательное поле",
                            on_delete=models.CASCADE,
                            )
    name = models.CharField(
                            verbose_name="Название узла", 
                            unique = True,
                            max_length=30,
                            help_text="Используйте формат: <em>XXX.XXX.XXX.XXX</em>."
                            )
    edit_date = models.DateField(
                            verbose_name="Последнее изменение", 
                            auto_now=True,
                            )
    titul_file = models.FileField(
                            verbose_name="Фото титульной страницы", 
                            blank = True, 
                            )
    comment = models.TextField(
                            verbose_name="Комментарий", 
                            blank = True, 
                            )
    members = models.ManyToManyField(
        'self',
        through='Membership',
        symmetrical=False,
        related_name='related_to'
        )
    detail = models.ManyToManyField(
        'Detail',
        through='Memberdetail',
        symmetrical=False,
        related_name='related_to'
        )

    def __unicode__(self):
        return self.name % self.id

    def __str__(self):
            return '%s -> %s' % (self.name, self.prename.name)
    
    def get_absolute_url(self):
        return "/units/%i/" % self.id

    class Meta:
        ordering = ["name"]
        verbose_name = "узел"
        verbose_name_plural = "Узлы"

class Membership(models.Model):
    from_u = models.ForeignKey(Unit, 
                                related_name='from_unit', 
                                on_delete=models.CASCADE,
                                verbose_name="Родитель", 
                                )
    to_u = models.ForeignKey(Unit, 
                                related_name='to_unit', 
                                on_delete=models.CASCADE,
                                verbose_name="Вложенный узел", 
                                )
    
    amount = models.PositiveIntegerField(verbose_name="Количество", 
                                        )
    class Meta:
        unique_together = ('from_u', 'to_u')
        verbose_name = "вложенный узел"
        verbose_name_plural = "вложенные узлы"
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
    name = models.CharField(max_length=50,
                            unique = True,
                            )
    class Meta:
        ordering = ["name"]
        verbose_name = "класс покрытия"
        verbose_name_plural = "классы покрытия"
    def __str__(self):
            return self.name

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
        verbose_name = "вложенный цех"
        verbose_name_plural = "вложенные цехи"
    def __str__(self):
            return '%s -> %s (%s)' % (self.from_u.nom_num, self.to_u.text_name, str(self.amount))

class Detail(models.Model):
    nom_num = models.CharField(max_length=50,
                            unique = True,
                            verbose_name="Номенкулатурный номер", 
                            )
    file_pdf = models.FileField(
                            verbose_name="pdf файл", 
                            blank = True, 
                            )
    file_jpg = models.FileField(
                            verbose_name="jpg файл", 
                            blank = True, 
                            )
    file_cdw = models.FileField(
                            verbose_name="cdw файл", 
                            blank = True, 
                            )
    part_weight = models.FloatField(verbose_name="Теоретический вес детали", 
                                                )
    metaltype = models.ForeignKey(
                            'Metaltype',
                            verbose_name="Тип металла", 
                            max_length=30,
                            help_text="Обязательное поле",
                            on_delete=models.CASCADE,
                            )
    сoatingclass = models.ForeignKey(
                            'Сoatingclass',
                            verbose_name="Класс покрытия", 
                            max_length=30,
                            help_text="Обязательное поле",
                            on_delete=models.CASCADE,
                            )
    edit_date = models.DateField(
                            verbose_name="Последнее изменение", 
                            auto_now=True,
                            )
    # росцеховка
    # shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    shop = models.ManyToManyField(
        'Shop',
        through='MemberShop',
        symmetrical=False,
        related_name='related_to_shop'
        )

    detail_date = models.DateField(
                            verbose_name="Дата редактирования детали", 
                            # auto_now=True,
                            )

    class Meta:
        ordering = ["nom_num"]
        verbose_name = "деталь"
        verbose_name_plural = "детали"
    def __str__(self):
            return self.nom_num
    def get_absolute_url(self):
        return "/details/%i/" % self.id

class Memberdetail(models.Model):
    from_u = models.ForeignKey(Unit, 
                                related_name='from_unit_to_detail', 
                                on_delete=models.CASCADE,
                                verbose_name="Родитель", 
                                )
    to_u = models.ForeignKey(Detail, 
                                related_name='to_detail', 
                                on_delete=models.CASCADE,
                                verbose_name="Вложенная деталь", 
                                )
    
    amount = models.PositiveIntegerField(verbose_name="Количество", 
                                        )
    class Meta:
        unique_together = ('from_u', 'to_u')
        verbose_name = "вложенная деталь"
        verbose_name_plural = "вложенные детали"
    def __str__(self):
            return '%s -> %s (%s)' % (self.from_u.name, self.to_u.nom_num, str(self.amount))