from django.db import models
import random

# Create your models here.
class Links(models.Model):
    url = models.URLField(max_length= 200, blank=False)
    short_code = models.CharField(max_length= 8, unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.short_code:
            chars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            while True:
                self.short_code = ''.join(random.choices(chars, k=6))
                if not Links.objects.filter(short_code=self.short_code).exists():
                    break
        super().save(*args, **kwargs)
    on_click = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)