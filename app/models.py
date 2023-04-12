from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    subject = models.TextField()
    
    def __str__(self):
        return self.name