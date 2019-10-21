from django.contrib import admin
from .models import Field, FilePath


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'width',)


@admin.register(FilePath)
class FilePathAdmin(admin.ModelAdmin):
    list_display = ('path',)