from django.db import models

class Post(models.Model):
    '''данные о записи'''
    title = models.CharField('Заголовок записи', max_length=150)
    descriptions = models.TextField('Текст записи')
    autor = models.CharField('Автор', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')


    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return f'{self.title}, {self.autor}'



class Coments(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя:', max_length=50)
    text_comment = models.TextField('Текст коментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


class Likes(models.Model):
    '''лайки'''
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)