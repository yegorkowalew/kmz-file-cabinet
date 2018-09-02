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
        verbose_name_plural = "Тип узла"

class Unit(models.Model):
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
    stuff = models.ManyToManyField(
                            'self', 
                            verbose_name="Вложенные узлы", 
                            blank = True, 
                            symmetrical=False
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

    def __unicode__(self):
        return self.name % self.id

    def __str__(self):
            return self.name+' ('+self.prename.name+')'

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Узлы"
