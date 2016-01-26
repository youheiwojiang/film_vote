from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length = 20)
	user_password = models.CharField(max_length = 20)
	log_time = models.DateTimeField('log time')


class Film(models.Model):
	pub_time = models.DateTimeField('show time')
	film_name = models.CharField(max_length = 50)
	publish_year = models.IntegerField(default = 2016)
	category  = models.CharField(max_length = 20)
	def __str__(self):
		return self.film_name


class Score(models.Model):
	film = models.ForeignKey(Film, on_delete = models.CASCADE)
	num_people = models.IntegerField(default = 0)
	total_score = models.IntegerField(default = 0)
	update_time = models.DateTimeField('score time')	
	def __str__(self):
		return self.total_score