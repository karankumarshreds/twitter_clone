from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)	

	def __str__(self):
		return self.title

# The User model and the Post model are going to have a relationship (obviously).
# We will use one(user) to many(posts) relationship.To do this, we will use a foreign key.
# 'on_delete': tells what to do with Post if affiliated user is deleted.
# models.CASCADE: tells delete the posts. 