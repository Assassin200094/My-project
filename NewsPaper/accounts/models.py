from django.db import models

class Staff(models.Model):
    full_name = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255)
    labor_contract = models.IntegerField()

class Author(models.Model):
    full_name = models.CharField()
    name = models.CharField(null=True)

    def some_method(self):
        self.name = self.full_name.split()[0]
        self.save()

Author.some_method()