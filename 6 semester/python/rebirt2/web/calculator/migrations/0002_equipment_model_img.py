# Generated by Django 4.1.7 on 2023-04-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='model_img',
            field=models.ImageField(default='', upload_to='img/'),
        ),
    ]
