from django.db import models

class Field(models.Model):
    number = models.IntegerField(verbose_name='Порядковый номер')
    name = models.CharField(max_length=20, verbose_name='Имя')
    width = models.FloatField(verbose_name='Ширина')

    def __str__(self):
        return self.name


class FilePath(models.Model):
    path = models.FilePathField(verbose_name='Путь к csv')

    def get_path(self):
        return self.path

    def set_path(self, new_path):
        self.pk = 1
        self.path = new_path
        self.save()

    def __str__(self):
        return f'{self.path}'