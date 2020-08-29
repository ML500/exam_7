from django.db import models


class Poll(models.Model):
    text = models.TextField(max_length=3000, verbose_name='Опрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    text = models.TextField(max_length=3000, verbose_name='Ответ')
    poll = models.ForeignKey('webapp.Poll', related_name='pols',
                             on_delete=models.CASCADE, verbose_name='Опрос')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Вариант ответов'


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='polls',
                             on_delete=models.CASCADE, verbose_name='Опрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    choice = models.ForeignKey('webapp.Choice', related_name='choices',
                               on_delete=models.CASCADE, verbose_name='Ответ')
