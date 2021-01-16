from django.db import models

# Create your models here.
class CareerHighlight(models.Model):

    image = models.ImageField(default='default.jpg', upload_to='pics')
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name
