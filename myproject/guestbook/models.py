from django.db import models
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
	#Comment is the name of table
	#every attribute/column will be created now
	name = models.CharField(max_length=20)
	comment=models.TextField()
	date_added=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Name: {}, ID: {}>'.format(self.name,self.id)