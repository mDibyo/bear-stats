from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    create_date = models.DateField('date created')
    
