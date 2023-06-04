
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

options = {
    ('draft','Draft'),
    ('publish','Publish'),
}

class StargEntertainment(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    publish = models.DateTimeField(default=timezone.now, unique=True)
    slug = models.SlugField(max_length=200)
    event = models.CharField(max_length=200)
    options = models.CharField(max_length=200, choices=options, default='draft')
    
    def __str__(self):
        return self.title
    
    
class Section (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self) :
        return self.title