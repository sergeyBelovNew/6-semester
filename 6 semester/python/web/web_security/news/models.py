from django.db import models


class Document(models.Model):
    title = models.CharField('Название', max_length=50, default=None)
    anons = models.CharField('Анонс', max_length=50, default=None)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
