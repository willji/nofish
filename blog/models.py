from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=100, default='')   

    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    github = models.CharField(max_length=100, default='')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_time']

    def __unicode__(self):
        return self.name

class Aboutme(models.Model):
    tag = models.CharField(max_length=200)
    skill = models.TextField()
    github = models.CharField(max_length=100)
    blog = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    goal = models.TextField()
    motto = models.TextField()

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    categorie = models.ForeignKey(Categorie)
    
    class Meta:
        ordering = ['-created_time']

    def __unicode__(self):
        return self.title
