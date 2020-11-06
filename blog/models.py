from django.db import models
from users.models import NewUser
from django.urls import reverse
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):     
    title       = models.CharField(max_length=500)
    slug        = models.SlugField(max_length=50,null=True, blank=True)
    author      = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    category    = models.ForeignKey(Category,default='uncategorized', null=True, max_length=255, on_delete=models.PROTECT)
    date_created= models.DateTimeField(auto_now_add=True)
    image       = models.ImageField(null=True, blank=True)
    lead        = models.CharField(max_length=1000,null=True,blank=True)
    post_body   = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home')

class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['-published']

    def __str__(self):
        return f"Comment by {self.name}"
    
    def get_absolute_url(self):
        return reverse('blog/post_detail', args=(str(self.id)))

class Subscribe(models.Model):
    name    = models.CharField(max_length=200)
    email   = models.EmailField(max_length=200)

    def __str__(self):
        return self.name
