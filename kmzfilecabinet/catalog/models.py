from django.db import models

# Create your models here.

class MyModel(models.Model):
    name = models.CharField("Название узла", max_length=30)
    stuff = models.ManyToManyField('self', related_name = name, blank = True, symmetrical=False)

    def __unicode__(self):
        return self.name % self.id

    def __str__(self):
            return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Узлы"