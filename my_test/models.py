from django.db import models

# Create your models here.

# 1. Run python manage.py makemigrations to create migration files for your new model.
# 2. Then run python manage.py migrate to apply the migration and 
    #create the corresponding table in the database.

#everything must inheret a model.model
class TestInt(models.Model):
    my_integer = models.IntegerField(default = 0)

class MyStrings(models.Model):
    my_string = models.TextField()

class Users(models.Model):
    username = models.TextField
    name = models.TextField
    user_id = models.IntegerField(default = 0)

#videos cant be stored in same database, we will have to use file store to save videos
    #ex: AWS S3