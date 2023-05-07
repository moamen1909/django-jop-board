from django.db import models


# Create your models here.

JOP_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Jop(models.Model):
    title=models.CharField(max_length=100)
    jop_type=models.CharField( max_length=50,choices=JOP_TYPE)
    descriptions=models.TextField(max_length=1000)
    Published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experiense=models.IntegerField(default=1)
    category=models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name