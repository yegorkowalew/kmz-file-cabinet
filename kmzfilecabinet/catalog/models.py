from django.db import models

# Create your models here.
class PreName(models.Model):
    name = models.CharField("Название", 
                            max_length=30,
                            help_text="Название типа узла"
                            )
    def __str__(self):
            return self.name
    class Meta:
        ordering = ["name"]
        verbose_name = "тип узла"
        verbose_name_plural = "типы узлов"

class Unit(models.Model):
    # Инвентарный номер на титульной странице, дата? "Экз №" - оригинален?
    # "действителен на"
    name = models.CharField(max_length=50,
                            unique = True,
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

    def __unicode__(self):
        return self.name % self.id
    def __str__(self):
            return self.name+' ('+self.prename.name+')'
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
            return self.from_u.name+' -> '+self.from_u.name+' ('+str(self.amount)+'шт.)'


class Metaltype(models.Model):
    name = models.CharField(max_length=50,
                            unique = True,
                            )
    class Meta:
        ordering = ["name"]
        verbose_name = "тип металла"
        verbose_name_plural = "типы металлов"

class Сoatingclass(models.Model):
    name = models.CharField(max_length=50,
                            unique = True,
                            )
    class Meta:
        ordering = ["name"]
        verbose_name = "класс покрытия"
        verbose_name_plural = "классы покрытия"

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


class Operation(models.Model):
    text_name = models.CharField(max_length=50,
                            unique = True,
                            )
    class Meta:
        ordering = ["text_name"]
        verbose_name = "операция"
        verbose_name_plural = "операции"

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
    part_weight = models.PositiveIntegerField(verbose_name="Теоретический вес детали", 
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
    detail_date = models.DateField(
                            verbose_name="Дата редактирования детали", 
                            # auto_now=True,
                            )
    