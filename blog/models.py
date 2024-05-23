from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    auther = models.ForeignKey(User,null=True, blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='images/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog'
