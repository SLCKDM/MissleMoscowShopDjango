from django.db import models

# Create your models here.
class Customer(models.Model):
    """Покупатель.
    
    Args:
        id (int): идентификатор;
        first_name (str): имя;
        last_name (str): фамилия;
        username (str): юзернейм;
        language_code (str): код языка;
    """
    id: int = models.IntegerField(primary_key=True)
    first_name: str = models.CharField(max_length=50, verbose_name="Имя")
    last_name: str = models.CharField(
        max_length=50, verbose_name="Фамилия", blank=True
    )
    username: str = models.CharField(max_length=50, verbose_name="Юзернейм")
    language_code: str = models.CharField(max_length=5, verbose_name="Язык (код)")
    
    def __repr__(self):
        return f'<{self.__class__.__name__} {self.username}>'

    def __str__(self):
        return str(self.username)