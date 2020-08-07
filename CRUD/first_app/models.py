from django.db import models

# Create your models here.

class Student(models.Model):
	first_name  = models.CharField(max_length=50)
	last_name	= models.CharField(max_length=50)
	email 		= models.EmailField()
	phone		= models.IntegerField()

	def __str__(self):
		return self.first_name+" "+self.last_name
	
	class Meta:		
		verbose_name       ='Student'    
		verbose_name_plural='Students'    

    




