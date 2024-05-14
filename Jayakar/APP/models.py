from django.db import models

# Create your models here.

class SkillsModel(models.Model):
    logo = models.ImageField(upload_to='skilllogos')
    skill1 = models.CharField(max_length=10)

class Projects(models.Model):
    ProjectName = models.CharField(max_length=20)
    Tools = models.ManyToManyField(SkillsModel)
    Description = models.TextField(max_length=2000)
    link = models.URLField(max_length=200, default='https://example.com', null=True)

    
class UserRequest(models.Model):
    username = models.CharField(max_length=20)
    useremail = models.EmailField()
    message = models.CharField(max_length=2000)
    


