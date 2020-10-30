from django.db import models
from users.models import NewUser
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):     
    title       = models.CharField(max_length=500)
    author      = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    category    = models.ForeignKey(Category,default='uncategorized', null=True, max_length=255, on_delete=models.PROTECT)
    date_created= models.DateTimeField(auto_now_add=True)
    image       = models.ImageField(null=True, blank=True)
    lead        = models.CharField(max_length=1000,null=True,blank=True)
    post_body   = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home')