from django.db import models

# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# from mongoengine import Document,fields,connect
# connect('Mongo', host='127.0.0.1', port=27017)

# Create your models here.


# Now, every time a new user is saved in your database, this function will run and 
# a new Token will be created for that user.

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class userdata(models.Model):
	username = models.CharField(max_length=17)
	password = models.CharField(max_length=17)
	email = models.CharField(max_length=27)

	def __str__(self):
		return self.username


# class mongouserdata(Document):
# 	username = fields.StringField(max_length=20)
# 	password = fields.StringField(max_length=20)
# 	email = fields.StringField(max_length=30)

# 	def __str__(self):
# 		return self.username