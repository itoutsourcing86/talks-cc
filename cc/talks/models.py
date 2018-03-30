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