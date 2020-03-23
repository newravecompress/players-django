from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    # user
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text=_('Пользователь'),
                                verbose_name=_('Пользователь'))
    # social links
    ok_link = models.CharField(max_length=100, blank=True, help_text=_('Ссылка на Одноклассники'),
                               verbose_name=_('Ссылка на Одноклассники'))
    vk_link = models.CharField(max_length=100, blank=True, help_text=_('Ссылка на Вконтакте'),
                               verbose_name=_('Ссылка на Вконтакте'))
    fb_link = models.CharField(max_length=100, blank=True, help_text=_('Ссылка на Facebook'),
                               verbose_name=_('Ссылка на Facebook'))
    tw_link = models.CharField(max_length=100, blank=True, help_text=_('Ссылка на Twitter'),
                               verbose_name=_('Ссылка на Twitter'))
    ig_link = models.CharField(max_length=100, blank=True, help_text=_('Ссылка на Instagram'),
                               verbose_name=_('Ссылка на Instagram'))
    yt_link = models.CharField(max_length=100, blank=True, help_text=_('Ссылка на Youtube'),
                               verbose_name=_('Ссылка на Youtube'))
    gp_link = models.CharField(max_length=100, blank=True, help_text=_('Ссылка на Google'),
                               verbose_name=_('Ссылка на Google'))

    # text
    about = models.TextField(blank=True, help_text=_('О себе кратко'), verbose_name=_('О себе кратко'))
    details = models.TextField(blank=True, help_text=_('О себе подробно'), verbose_name=_('О себе подробно'))
    faith = models.TextField(blank=True, help_text=_('Во что я верю'), verbose_name=_('Во что я верю'))
    practice = models.TextField(blank=True, help_text=_('Как я это реализую'), verbose_name=_('Как я это реализую'))
    hobby = models.TextField(blank=True, help_text=_('Хобби'), verbose_name=_('Хобби'))

    class Meta:
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Visibility(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, help_text=_('Профиль'),
                                   verbose_name=_('Профиль'))
    about = models.BooleanField(default=True, help_text=_('О себе кратко'), verbose_name=_('О себе кратко'))
    details = models.BooleanField(default=True, help_text=_('О себе подробно'), verbose_name=_('О себе подробно'))
    faith = models.BooleanField(default=True, help_text=_('Во что я верю'), verbose_name=_('Во что я верю'))
    practice = models.BooleanField(default=True, help_text=_('Как я это реализую'),
                                   verbose_name=_('Как я это реализую'))
    hobby = models.BooleanField(default=True, help_text=_('Хобби'), verbose_name=_('Хобби'))

    class Meta:
        verbose_name = _('Видимость полей')
        verbose_name_plural = _('Видимость полей')
