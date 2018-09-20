from django.contrib import admin
from django.db import models

from .models import Unit, PreName, Membership, Metaltype, Сoatingclass, Shop, Operation, Detail, MemberShop, AbbrName, UnitContentPhoto

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
    fields = (('papnum', 'abbrname'), ('prename', 'name'), ('titul_file'), 'comment')
    list_display = ('name', 'prename', 'edit_date')
    search_fields = ['name']
    inlines = (TermInlineAdmin, DetailInlineAdmin, StandartDetailInlineAdmin, UnitContentPhotoInlineAdmin)


class DetailAdmin(admin.ModelAdmin):
    fields = ('nom_num', ('file_pdf', 'file_jpg', 'file_cdw'), ('part_weight'), ('metaltype', 'сoatingclass'), ('detail_date'),)
    # list_display = ('name', 'prename', 'edit_date')
    search_fields = ['nom_num']
    inlines = (MemberShopInlineAdmin,)
    # inlines = ()

class MembershipAdmin(admin.ModelAdmin):
    fields = ('amount', 'from_u', 'to_u')

admin.site.register(Unit, UnitAdmin)
# admin.site.register(Membership, MembershipAdmin)
# admin.site.register(MemberShop)
admin.site.register(PreName)
admin.site.register(Metaltype)
admin.site.register(Сoatingclass)
admin.site.register(Shop)
admin.site.register(Operation)
admin.site.register(AbbrName)
admin.site.register(Detail, DetailAdmin)