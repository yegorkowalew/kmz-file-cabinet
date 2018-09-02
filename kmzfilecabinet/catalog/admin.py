from django.contrib import admin
from django.db import models
# Register your models here.

from catalog.models import Unit, PreName
# admin.site.register()
class UnitAdmin(admin.ModelAdmin):
    # pass
    fields = (('prename', 'name'), ('stuff', 'titul_file'), 'comment')
    list_display = ('name', 'prename', 'edit_date')
    search_fields = ['name']

admin.site.register(Unit, UnitAdmin)

admin.site.register(PreName)