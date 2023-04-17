from django.db import models


class GeneralDocument(models.Model):
    model_img = models.ImageField(upload_to='img/', default="")
    title = models.CharField('Название', max_length=50)
    ad = models.CharField('Вид', max_length=50)
    full_text = models.TextField('Статья')
    doc_file = models.FileField(upload_to='doсs', blank=True)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/docs/{self.id}'

    class Meta:
        verbose_name = 'GeneralDocument'
        verbose_name_plural = 'GeneralDocuments'
