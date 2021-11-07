from django.db import models

class Users(models.Model):
    nickname = models.CharField(max_length=12, unique=True, null=False, blank=False, verbose_name="Логин пользователя")
    email = models.EmailField(unique=True, verbose_name="Почта пользователя")
    password = models.CharField(max_length=12, null=False, blank=False, verbose_name="Пароль пользователя")

    def __str__(self):
        return self.nickname


class CollectionsMemes(models.Model):
    description = models.CharField(max_length=250, null=True, blank=True, verbose_name="Описание мема")
    photo = models.ImageField(upload_to=f'users/%Y/%m/%d/')
    user = models.ForeignKey(Users, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Автор мема", related_name='users')
