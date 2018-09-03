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
    def __unicode__(self):
        return self.name % self.id
    def __str__(self):
            return self.name+' ('+self.prename.name+')'
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Узлы"

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        'Group',
        through='Membership',
        # through_fields=('group',),
    )

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # group2 = models.ForeignKey(Group, on_delete=models.CASCADE)
    # unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="membership_group",
    )
    invite_reason = models.CharField(max_length=64)