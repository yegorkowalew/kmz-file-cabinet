from django.contrib import admin
from django.db import models

from .models import Unit, PreName, Membership, Metaltype, Сoatingclass, Shop, Operation, Detail, MemberShop, UnitContentPhoto, StandartDetail, StandartDetailCreator, StubName

class MemberShopInlineAdmin(admin.TabularInline):
    model = Detail.shop.through
    fk_name = 'from_u'

class TermInlineAdmin(admin.TabularInline):
    model = Unit.members.through
    fk_name = 'from_u'

class DetailInlineAdmin(admin.TabularInline):
    model = Unit.detail.through
    fk_name = 'from_u'

class StandartDetailInlineAdmin(admin.TabularInline):
    model = Unit.standartdetail.through
    fk_name = 'from_u'

class UnitContentPhotoInlineAdmin(admin.TabularInline):
    model = UnitContentPhoto

class UnitAdmin(admin.ModelAdmin):
    fields = (('papnum'), ('name', 'prename'), ('titul_image'), 'comment')
    list_display = ('name', 'prename', 'edit_date')
    search_fields = ['name']
    inlines = (TermInlineAdmin, DetailInlineAdmin, StandartDetailInlineAdmin, UnitContentPhotoInlineAdmin)


class DetailAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основное', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('nom_num', 'designation'), ('stub_name', 'part_weight')),
        }),
        ('Размеры', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('metaltype', 'thickness'), ('test_width', 'test_height')),
        }),
        ('Файлы', {
            'classes': ('collapse',),
            'fields': ('file_pdf', 'file_jpg', 'file_cdw'),
        }),
        ('Труба', {
            'classes': ('collapse',),
            'fields': ('diameter',),
        }),
        ('Уголок или Двутавр', {
            'classes': ('collapse',),
            'fields':  ('shelf_height',),
        }),
        ('Массив', {
            'classes': ('collapse',),
            'fields':  ('array_height', 'array_width', 'array_amount',),
        }),
        ('Цинкование', {
            'classes': ('collapse',),
            'fields':  ('coatingclass',),
        }),
        ('Покраска', {
            'classes': ('collapse',),
            'fields':  ('color_coating',),
        })
    )
    search_fields = ['nom_num']
    inlines = (MemberShopInlineAdmin,)
    # inlines = ()

class MembershipAdmin(admin.ModelAdmin):
    fields = ('amount', 'from_u', 'to_u')

class StandartDetailAdmin(admin.ModelAdmin):
    fields = ('nom_num', 'standart_detail_creator')

# class StandartDetailCreatorAdmin(admin.ModelAdmin):
    # fields = ('name')

admin.site.register(Unit, UnitAdmin)
# admin.site.register(Membership, MembershipAdmin)
# admin.site.register(MemberShop)
admin.site.register(PreName)
admin.site.register(Metaltype)
admin.site.register(Сoatingclass)
admin.site.register(Shop)
admin.site.register(Operation)
admin.site.register(StubName)
# admin.site.register(AbbrName)
admin.site.register(StandartDetail, StandartDetailAdmin)
admin.site.register(StandartDetailCreator)
admin.site.register(Detail, DetailAdmin)