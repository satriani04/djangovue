from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    groups = models.ManyToManyField('Group', through='Groupmember')
    alamat = models.TextField(blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length=200)
    desciption = models.TextField(blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class Groupmember(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    type = models.CharField(max_length=100)
    
    def __str__(self):
        return "%s is in group %s (as %s)" % (self.person, self.group, self.type)