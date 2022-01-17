import email
from operator import mod
from django.db import models

# Create your models here.
class Category(models.Model):
    month = models.CharField(max_length=2000,default="")

    def __str__(self) -> str:
        return self.month

COLOR_CHOICES = (
    ('#FFFADE','Light Cream'),
    ('#E3F5FF', 'Sky Blue'),
    ('#FFEAEA','Pink'),
    ('#EBEAFC','Light Purple'),
    ('#FFF3E2','Dark Cream'),
)

class New(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    heading = models.CharField(max_length=2000)
    website = models.CharField(max_length=2000)
    url = models.CharField(max_length=2000)
    date = models.DateField()
    color = models.CharField(max_length=10,choices=COLOR_CHOICES,default="#FFFADE")

    def __str__(self) -> str:
        return self.category.month + '-' + self.heading

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name + '-' + str(self.date)

class Career(models.Model):
    code = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    email = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title + ' - ' + self.code


class JobApply(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    file = models.FileField()
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name + '-' + str(self.date)