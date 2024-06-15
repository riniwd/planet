from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Описание', max_length=250)
    full_text = models.TextField('Новость')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Data(models.Model):
    tel = models.CharField('Номер телефона', max_length=12)
    count = models.CharField('Количество людей', max_length=3)

    def __str__(self):
        return self.tel

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'

# Create your models here.

class TimeTable(models.Model):
    topic = models.CharField('Тема', max_length=50)
    comments = models.CharField('Комментарии', max_length=150, null=True)
    data = models.CharField('Сроки проведения', max_length=70)
    link_article = models.CharField('Ссылка на статью', max_length=150)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class Gallery(models.Model):
    title = models.CharField('Название', max_length=50)
    img = models.ImageField('Изображение', upload_to='img/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

