from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    text= models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.text

class Comment(models.Model):
    text= models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.text
    
class Soport(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

class Like(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Payment(models.Model):
    user= models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    bank = models.CharField(max_length=20)
    account_number = models.IntegerField()
    page = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

