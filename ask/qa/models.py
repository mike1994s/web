from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField()
	author = models.ForeignKey(User, db_constraint=False)
	likes  = models.ManyToManyField(User, related_name='likes_set')
	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ['-added_at']

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	question =  models.ForeignKey(Question,related_name='question')
	author = models.ForeignKey(User, db_constraint=False)
	def __unicode__(self):
		return self.text
	class Meta:
		ordering = ['-added_at']
