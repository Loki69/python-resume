from django.db import models

# Create your models here.

class Skill(models.Model):
    class Meta:
        db_table = "SKILL"
    skill = models.CharField(max_length=50)
    def __str__(self):
        return self.skill

class Persona(models.Model):
    class Meta:
        db_table = "PERSONA"
    fio = models.CharField(max_length=250)
    years = models.DateTimeField()
    location = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.fio



class Article(models.Model):
    class Meta:
        db_table = "ARTICLE"
    title = models.CharField(max_length=100)
    article = models.TextField()
    shor_article = models.TextField()

    def __str__(self):
        return self.title

# class Photo(models.Model):
#     photo=models

class Project(Article):
    class Meta:
        db_table = "PROJECT"
    skills = models.ManyToManyField(Skill)
    links = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# class About(models.Model):
