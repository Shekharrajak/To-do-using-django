from django.db import models

# Create your models here.
class todo(models.MODEL):

	work=models.CharField(max_length=100,unique=true)
	created=models.DateTimeField()

	def __unicode__(self):
		return self.name
