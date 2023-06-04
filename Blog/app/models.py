from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
    
class Post(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Publish')
    )
    SECTION = (
        ('Popular', 'Draft'),
        ('Recent', 'Publish'),
        ('Editor_Pick', 'Publish'),
        ('Trending', 'Publish'),
        ('Inspiration', 'Publish'),
        ('Latest_Post', 'Publish'),
    )
    fetured_field = models.ImageField(upload_to='Images')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = RichTextField()
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)
    status = models.CharField(choices=STATUS, max_length=100)
    section = models.CharField(choices=SECTION, max_length=200)
    
    
    def __str__(self) -> str:
        return self.title
    
    
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    if exists := qs.exists():
        new_slug = f'{slug}-{qs.first().id}'
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        
    pre_save.connect(pre_save_post_reciver, Post)
    
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
