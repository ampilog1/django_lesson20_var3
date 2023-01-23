from django.db import models
from userapp.models import BlogUser



# Create your models here.
# Создаем модель нашей базы данных
class Region(models.Model):
    name = models.CharField(max_length=32, unique=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=32, unique=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=32, unique=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def has_image(self):
        return bool(self.image)

    def some_method(self):
        return 'hello from method'

    def __str__(self):
        return f'{self.name}, user: {self.user.username}'


class NumberOffer(models.Model):
    name = models.CharField(max_length=32, unique=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FullOffer(models.Model):
    numberOffer = models.ForeignKey(NumberOffer, on_delete=models.CASCADE)
    VACANCY = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    REGION = models.ForeignKey(Region, on_delete=models.CASCADE)
    SKILLS = models.ForeignKey(Skills, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.numberOffer, self.VACANCY, self.REGION, self.SKILLS)
