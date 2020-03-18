from django.db import models
from django.utils.translation import gettext_lazy as _


class Activity(models.Model):
    name = models.CharField(max_length=250, help_text=_('Название'), verbose_name=_('Название'))

    class Meta:
        verbose_name = _('Сфера деятельности')
        verbose_name_plural = _('Сферы деятельности')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=250, help_text=_('Название'), verbose_name=_('Название'))
    is_active = models.BooleanField(default=True, help_text=_('Активность'), verbose_name=_('Активность'))

    class Meta:
        verbose_name = _('Группа интересов')
        verbose_name_plural = _('Группы интересов')

    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=250, help_text=_('Название'), verbose_name=_('Название'))
    is_active = models.BooleanField(default=True, help_text=_('Активность'), verbose_name=_('Активность'))
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL,
                              help_text=_('Группа интересов'), verbose_name=_('Группа интересов'))
    picture = models.ImageField(blank=True, upload_to=f'upload/images/interest/', help_text=_('Картинка'),
                                verbose_name=_('Картинка'))

    class Meta:
        verbose_name = _('Область интересов')
        verbose_name_plural = _('Области интересов')

    def __str__(self):
        return self.name
