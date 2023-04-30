from django.db import models
import datetime
from ckeditor.fields import RichTextField

class New(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='News/')
    text = RichTextField()
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name