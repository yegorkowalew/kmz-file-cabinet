from django.contrib import admin
from django.db import models
# Register your models here.

from .models import Unit, PreName, Membership

class TermInlineAdmin(admin.TabularInline):
    model = Unit.members.through
    fk_name = 'from_u'

class UnitAdmin(admin.ModelAdmin):
    fields = (('prename', 'name'), ('titul_file'), 'comment')
    list_display = ('name', 'prename', 'edit_date')
    search_fields = ['name']
    inlines = (TermInlineAdmin,)


# class GroupAdmin(admin.ModelAdmin):
#     fields = ('name',)
#     inlines = (TermInlineAdmin,)
    # list_display = ('name', 'prename', 'edit_date')
    # search_fields = ['name']
    # inlines = (TermInlineAdmin,)

class MembershipAdmin(admin.ModelAdmin):
    fields = ('invite_reason', 'from_u', 'to_u')
    
    # list_display = ('name', 'prename', 'edit_date')
    # search_fields = ['name']


admin.site.register(Unit, UnitAdmin)
# admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)

admin.site.register(PreName)