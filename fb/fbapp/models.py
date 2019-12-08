from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length = 30)
	email = models.CharField(max_length = 50)
	password = models.CharField(max_length = 20)
	image = models.TextField(blank = True)

class Friend(models.Model):
	user_id = models.TextField(blank = True)
	pending_frd = models.TextField(blank = True)
	frd = models.TextField(blank = True)
	requested_frd = models.TextField(blank = True)