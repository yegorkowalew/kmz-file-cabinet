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
    name = models.CharField(max_length=50)
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
        verbose_name_plural = "Узлы"

class Membership(models.Model):
    from_u = models.ForeignKey(Unit, related_name='from_unit', on_delete=models.CASCADE)
    to_u = models.ForeignKey(Unit, related_name='to_unit', on_delete=models.CASCADE)
    
    invite_reason = models.CharField(max_length=64)
    class Meta:
        unique_together = ('from_u', 'to_u')