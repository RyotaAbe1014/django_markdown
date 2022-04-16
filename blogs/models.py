from django.db import models
from mdeditor.fields import MDTextField


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = MDTextField()
    technology = models.ForeignKey('Technologies', on_delete=models.CASCADE)

    class Meta:
        db_table = 'article'


class Technologies(models.Model):
    name = models.CharField(verbose_name='言語', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'technologies'
