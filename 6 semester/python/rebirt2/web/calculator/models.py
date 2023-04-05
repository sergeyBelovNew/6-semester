from django.db import models


class Equipment(models.Model):
    model_img = models.ImageField(upload_to='img/', default="")
    title = models.CharField('Название', max_length=50)
    type = models.CharField('Вид оборудования', max_length=50)
    description = models.TextField('Описание')
    cost = models.CharField('Цена', max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/calculator/{self.id}'

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'
