from django.db import models


class Document(models.Model):
    model_img = models.ImageField(upload_to='img/', default="")
    title = models.CharField('Название', max_length=50)
    ad = models.CharField('Анонс', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
