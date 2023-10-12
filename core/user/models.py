from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL

class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/',null=True, blank=True)
    
    def get_image(self):
        if self.image:
            return f'{MEDIA_URL}{self.image}'
        return f'{STATIC_URL}media/img/empty.png'
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
        item['username']=self.username
        item["image"]=self.get_image()
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['groups']=[group.name for group in self.groups.all()]
        return item