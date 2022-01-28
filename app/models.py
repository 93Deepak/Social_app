from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

__all__ = ['User', 'Status']


class User(AbstractUser):
    username    = models.CharField(max_length=50, unique=True)
    first_name  = models.CharField(max_length=50, blank=True, null=True)
    last_name   = models.CharField(max_length=50, blank=True, null=True)
    email       = models.EmailField(unique=True)
    birth_date  = models.DateField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile/', blank=True, null=True)
    following   = models.ManyToManyField('app.User', related_name='follows')
    followed_by = models.ManyToManyField('app.User', related_name='followers')

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __Str__(self):
        return self.username
    
    
    
class Status(models.Model):
    status      = models.CharField(max_length=300,)
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    created_date_time = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.created_by.username + self.status
    
    
