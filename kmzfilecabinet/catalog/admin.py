from django.contrib import admin
from django.db import models

from .models import Unit, PreName, Membership, Metaltype, Сoatingclass, Shop, Operation, Detail, MemberShop

class TermInlineAdmin(admin.TabularInline):
    model = Unit.members.through
    fk_name = 'from_u'

class DetailInlineAdmin(admin.TabularInline):
    model = Unit.detail.through
    fk_name = 'from_u'

class UnitAdmin(admin.ModelAdmin):
    fields = (('prename', 'name'), ('titul_file'), 'comment')
    list_display = ('name', 'prename', 'edit_date')
    search_fields = ['name']
    inlines = (TermInlineAdmin, DetailInlineAdmin,)
    # inlines = ()

class MembershipAdmin(admin.ModelAdmin):
    fields = ('amount', 'from_u', 'to_u')

class MemberShopAdmin(admin.ModelAdmin):
    fields = ('amount', 'from_u', 'to_u')

admin.site.register(Unit, UnitAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(MemberShop, MemberShopAdmin)
admin.site.register(PreName)
admin.site.register(Metaltype)
admin.site.register(Сoatingclass)
admin.site.register(Shop)
admin.site.register(Operation)
admin.site.register(Detail)