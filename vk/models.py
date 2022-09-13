from django.db import models


class VkUser(models.Model):
    vk_id = models.IntegerField(verbose_name='Идентификатор в ВК', null=False, unique=True)
    photo = models.CharField(verbose_name='Изображение пользователя', null=False, max_length=255)
    last_name = models.CharField(verbose_name='Фамилия пользователя', null=False, max_length=255)
    first_name = models.CharField(verbose_name='Имя пользователя', null=False, max_length=255)

    @property
    def url(self):
        return f'https://vk.com/id{self.vk_id}'

    class Meta:
        verbose_name = 'Пользователь ВКонтакте'
        verbose_name_plural = 'Пользователи ВКонтакте'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
