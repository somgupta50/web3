from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100] # return first 100 characters of content
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = [self.title.replace(' ', '-').lower()][:50] # replace spaces with hyphens and make it lowercase
        super().save(*args, **kwargs)

class Subscriber(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email