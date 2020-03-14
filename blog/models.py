from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


class Article(models.Model):
    AWAIT = 'AW'
    REJECTED = 'RJ'
    VERIFIED = 'VF'
    STATUS_CHOICES = [
        (AWAIT, 'Await'),
        (REJECTED, 'Rejected'),
        (VERIFIED, 'Verified')
    ]

    title = models.CharField(max_length=250)
    text = models.TextField()
    code = models.CharField(max_length=250, editable=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=AWAIT)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    picture = models.ImageField()
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)

    def verified(self):
        return self.status == self.VERIFIED

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = slugify(self.title, separator='-')
        super().save(*args, **kwargs)
