from django.db import models
from users.models import NewUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class Post(models.Model):
    title       = models.CharField(max_length=500)
    author      = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    category    = models.CharField(choices=choice_list,default='uncategorized', null=True, max_length=255)
    date_created= models.DateTimeField(auto_now_add=True)
    image       = models.ImageField(null=True, blank=True)
    lead        = models.CharField(max_length=1000,null=True,blank=True)
    post_body   = models.TextField()

    def __str__(self):
        return self.title