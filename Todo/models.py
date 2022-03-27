from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 10)
    image = models.CharField(max_length = 200)
    rent = models.CharField(max_length = 10)
     

    def __str___(self):
        return self.title