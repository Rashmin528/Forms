from django.db import models

class Post(models.Model):
		post = models.CharField(max_length=1000)
		created = models.DateTimeField(auto_now_add=True)


