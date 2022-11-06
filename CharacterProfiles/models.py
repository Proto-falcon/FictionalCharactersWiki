from django.db import models


# Create your models here.
class CharacterProfile(models.Model):
    name = models.CharField(max_length=254)
    date_of_birth = models.DateField("Date of Birth:")
    age = models.IntegerField()
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return self.name
