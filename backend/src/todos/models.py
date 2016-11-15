from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=30)
    desc = models.TextField(default='lorem ipsum dolor sir amet')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task