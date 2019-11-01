from django.db import models

class Field(models.Model):
    number = models.IntegerField(verbose_name='Порядковый номер')
    name = models.CharField(max_length=20, verbose_name='Имя')
    width = models.IntegerField(verbose_name='Ширина')

    def __str__(self):
        return self.name


class FilePath(models.Model):
    path = models.FilePathField(verbose_name='Путь к csv')

    @staticmethod
    def get_path():
        return FilePath.objects.first().path

    @staticmethod
    def set_path():
        return FilePath.objects.update_or_create(pk=1, path='phones.csv')

    def __str__(self):
        return f'{self.path}'