from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    diagnosis = models.TextField()
    date_admitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
