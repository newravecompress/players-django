from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify
from django.utils.translation import gettext_lazy as _

from spheres.models import Interest


class Article(models.Model):
    AWAIT = 'AW'
    REJECTED = 'RJ'
    VERIFIED = 'VF'
    STATUS_CHOICES = [
        (AWAIT, 'Await'),
        (REJECTED, 'Rejected'),
        (VERIFIED, 'Verified')
    ]

    title = models.CharField(max_length=250, unique=True, help_text=_('Заголовок'), verbose_name=_('Заголовок'))
    text = models.TextField(help_text=_('Текст'), verbose_name=_('Текст'))
    code = models.CharField(max_length=250, editable=False, help_text=_('Символьный код'),
                            verbose_name=_('Символьный код'))
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=AWAIT, help_text=_('Статус'),
                              verbose_name=_('Статус'))
    date_create = models.DateTimeField(auto_now_add=True, help_text=_('Дата создания'), verbose_name=_('Дата создания'))
    date_update = models.DateTimeField(auto_now=True, help_text=_('Дата изменения'), verbose_name=_('Дата изменения'))
    picture = models.ImageField(blank=True, upload_to='upload/images/%Y/%m/%d/', help_text=_('Картинка'),
                                verbose_name=_('Картинка'))
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, help_text=_('Автор'),
                               verbose_name=_('Автор'))
    theme = models.ManyToManyField(Interest, blank=True, verbose_name=_('Тема'), help_text=_('Тема'))

    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')

    def __str__(self):
        return self.title

    def verified(self):
        return self.status == self.VERIFIED

    def save(self, *args, **kwargs):
        self.code = slugify(self.title, separator='_')
        super().save(*args, **kwargs)
