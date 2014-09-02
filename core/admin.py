from django.contrib import admin
from django import forms

from redactor.widgets import RedactorEditor

from models import Entry
# Register your models here.

class EntryAdminForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['titulo','slug', 'status','data_publicacao','texto','imagem']
		widgets = {
			'texto' : RedactorEditor(),
		}

class EntryAdmin(admin.ModelAdmin):
	form = EntryAdminForm
	prepopulated_fields = {"slug": ("titulo",)}

admin.site.register(Entry,EntryAdmin)
