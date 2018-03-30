from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse


class TalkList(models.Model):
    user = models.ForeignKey(User, related_name='lists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(primary_key=True, max_length=255, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug, ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(TalkList, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('user', 'name')


class Talk(models.Model):
    ROOM_CHOICES = (
        ('517D', '517D'),
        ('517C', '517C'),
        ('517AB', '517AB'),
        ('520', '520'),
        ('710A', '710A')
    )

    talk_list = models.ForeignKey(TalkList, related_name='talks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(primary_key=True, max_length=255, blank=True)
    when = models.DateTimeField()
    room = models.CharField(max_length=10, choices=ROOM_CHOICES)
    host = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Talk, self).save(*args, **kwargs)

    class Meta:
        ordering = ('when', 'room')
        unique_together = ('talk_list', 'name')
