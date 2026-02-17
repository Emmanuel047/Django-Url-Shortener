from django.db import models

# Create your models here.
class Links(models.Model):
    url = models.URLField(max_length= 200, blank=False)
    short_code = models.CharField(max_length= 8, unique=True, )
    on_click = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)