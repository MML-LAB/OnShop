from django import forms
from django.forms import ModelChoiceField
from django.contrib import admin
from .models import *

class NotebookAdmin(admin.ModelAdmin):
    def formfield_for_fk(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Notebooks'))
        return super().formfield_for_fk(db_field, request, **kwargs)

class SmartphoneAdmin(admin.ModelAdmin):
    def formfield_for_fk(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Smartphones'))
        return super().formfield_for_fk(db_field, request, **kwargs)

admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)

