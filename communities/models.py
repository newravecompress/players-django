from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify
from django.utils.translation import gettext_lazy as _


class Community(models.Model):
    AWAIT = 'AW'
    REJECTED = 'RJ'
    VERIFIED = 'VF'
    STATUS_CHOICES = [
        (AWAIT, 'Await'),
        (REJECTED, 'Rejected'),
        (VERIFIED, 'Verified')
    ]

    FREE = 'FR'
    PAID = 'PD'
    TYPE_CHOICES = [
        (FREE, 'Free'),
        (PAID, 'Paid')
    ]

    name = models.CharField(max_length=250, help_text=_('Название'), verbose_name=_('Название'))
    code = models.CharField(max_length=250, editable=False, help_text=_('Символьный код'),
                            verbose_name=_('Символьный код'))
    is_active = models.BooleanField(default=True, help_text=_('Активность'), verbose_name=_('Активность'))
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=AWAIT, help_text=_('Статус'),
                              verbose_name=_('Статус'))
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=FREE, help_text=_('Тип'), verbose_name=_('Тип'))

    picture = models.ImageField(blank=True, upload_to=f'upload/images/community/', help_text=_('Картинка'),
                                verbose_name=_('Картинка'))
    video = models.CharField(blank=True, max_length=250, help_text=_('Видео'), verbose_name=_('Видео'))

    info = models.TextField(help_text=_('Информация'), verbose_name=_('Информация'), blank=True)
    rules = models.TextField(help_text=_('Правила'), verbose_name=_('Правила'), blank=True)
    faith = models.TextField(help_text=_('Во что мы верим'), verbose_name=_('Во что мы верим'), blank=True)
    realization = models.TextField(help_text=_('Как мы это реализуем'), verbose_name=_('Как мы это реализуем'),
                                   blank=True)

    date_create = models.DateTimeField(auto_now_add=True, help_text=_('Дата создания'), verbose_name=_('Дата создания'))
    date_update = models.DateTimeField(auto_now=True, help_text=_('Дата изменения'), verbose_name=_('Дата изменения'))

    class Meta:
        verbose_name = _('Сообщество')
        verbose_name_plural = _('Сообщества')

    def __str__(self):
        return self.name

    def verified(self):
        return self.status == self.VERIFIED

    def save(self, *args, **kwargs):
        self.code = slugify(self.name, separator='_')
        super().save(*args, **kwargs)


class Member(models.Model):
    AWAIT = 'AW'
    REJECTED = 'RJ'
    VERIFIED = 'VF'
    STATUS_CHOICES = [
        (AWAIT, 'Await'),
        (REJECTED, 'Rejected'),
        (VERIFIED, 'Verified')
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, help_text=_('Пользователь'),
                             verbose_name=_('Пользователь'))
    community = models.ForeignKey(Community, on_delete=models.CASCADE, help_text=_('Сообщество'),
                                  verbose_name=_('Сообщество'))
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=AWAIT, help_text=_('Статус'),
                              verbose_name=_('Статус'))

    date_create = models.DateTimeField(auto_now_add=True, help_text=_('Дата создания'), verbose_name=_('Дата создания'))
    date_update = models.DateTimeField(auto_now=True, help_text=_('Дата изменения'), verbose_name=_('Дата изменения'))

    class Meta:
        verbose_name = _('Участник')
        verbose_name_plural = _('Участники')

    def __str__(self):
        return self.user.username
