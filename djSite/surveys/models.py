from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
