from django.db import models
from uuid import UUID

# Create your models here.
class Customer(models.Model):
    id: int = models.IntegerField(primary_key=True)
    first_name: str = models.CharField(max_length=50)
    last_name: str = models.CharField(max_length=50)
    username: str = models.CharField(max_length=50)
    language_code: str = models.CharField(max_length=5)
    
    def __repr__(self):
        return f'<{self.__class__.__name__} {self.username}>'

    def __str__(self):
        return str(self.username)