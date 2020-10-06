from django.db import models

# Create your models here.
class Data(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    employeeId = models.IntegerField(unique=True)
    city = models.CharField(max_length=50)

    def __str__(self):

        return str(self.employeeId)

    class Meta:
        verbose_name_plural = "Data"