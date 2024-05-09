from django.db import models

# Create your models here.
class Todo(models.Model) :

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    created = models.DateTimeField()
    complete = models.BooleanField()
    important = models.BooleanField()

    def __str__(self) :
        return self.title