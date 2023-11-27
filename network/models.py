from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "sender")
    information = models.CharField(max_length= 165)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"Post{self.id} posted by {self.user} on {self.date.strftime('%d %b %Y %H %S')}"
    
