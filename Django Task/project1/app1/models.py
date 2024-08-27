from django.db import models
from django.utils.text import slugify

# Create your models here.

class TagLine(models.Model):
    caption = models.CharField(max_length=255)

    def __str__(self):
        return f"Caption {self.caption}"
    
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    def __str__(self):
        return f"Author name: {self.first_name} {self.last_name} "



class Posts(models.Model):
    title = models.CharField(max_length=50)
    image_name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="", null=False,editable=False)
    tags = models.ManyToManyField(TagLine, related_name='posts')
    author = models.ForeignKey(Author, on_delete=models.CASCADE,default=1)

    def save(self, *args, **kwargs):  
        self.slug = slugify(f"{self.title}{self.image_name}")
        super(Posts, self).save(*args, **kwargs)
    def __str__(self):
        return f"Title: {self.title}"

class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    text = models.TextField(max_length=50)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return f"Comment: {self.text}"