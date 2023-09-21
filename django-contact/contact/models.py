from django.db import models

class contact(models.Model):
    name = models.CharField(default='A', max_length=20)
    family = models.CharField(default='B', max_length=20)
    number = models.CharField(default='0', max_length=15)


    @property
    def toJson(self):
        return {"name": self.name, "family": self.family, "number": self.number}

    def __unicode__(self):
        return self.name + " " + self.family