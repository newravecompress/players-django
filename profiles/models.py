from django.core.exceptions import ObjectDoesNotExist
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

    # boolean
    investor_quest = models.BooleanField(default=False, help_text=_('Готов выступить инвестором'),
                                         verbose_name=_('Готов выступить инвестором'))
    investor_search = models.BooleanField(default=False, help_text=_('В поисках инвестиций'),
                                          verbose_name=_('В поисках инвестиций'))
    business_quest = models.BooleanField(default=False, help_text=_('В поисках бизнес-партнера'),
                                         verbose_name=_('В поисках бизнес-партнера'))
    project_quest = models.BooleanField(default=False, help_text=_('Готов работать в проектах'),
                                        verbose_name=_('Готов работать в проектах'))

    class Meta:
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
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


class Subscribe(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, help_text=_('Пользователь'),
                                verbose_name=_('Пользователь'))
    recommend_email = models.BooleanField(default=False, help_text=_('Рассылка рекомендаций Email'),
                                          verbose_name=_('Рассылка рекомендаций Email'))
    recommend_sms = models.BooleanField(default=False, help_text=_('Рассылка рекомендаций Sms'),
                                        verbose_name=_('Рассылка рекомендаций Sms'))
    system_email = models.BooleanField(default=False, help_text=_('Сервисные сообщения Email'),
                                       verbose_name=_('Сервисные сообщения Email'))
    system_sms = models.BooleanField(default=False, help_text=_('Сервисные сообщения Sms'),
                                     verbose_name=_('Сервисные сообщения Sms'))
    user_email = models.BooleanField(default=False, help_text=_('Сообщения пользователей Email'),
                                     verbose_name=_('Сообщения пользователей Email'))
    user_sms = models.BooleanField(default=False, help_text=_('Сообщения пользователей Sms'),
                                   verbose_name=_('Сообщения пользователей Sms'))
    news_email = models.BooleanField(default=False, help_text=_('Дайджест новостей Email'),
                                     verbose_name=_('Дайджест новостей Email'))
