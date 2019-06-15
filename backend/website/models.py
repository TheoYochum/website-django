from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    published = models.BooleanField(default=False)

    def _str_(self):
        return self.title