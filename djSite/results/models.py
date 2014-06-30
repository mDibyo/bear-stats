from django.db import models


class User(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=20)

class SurveyResult(models.Model):
    user = models.ForeignKey('User')
    question = models.ForeignKey('surveys.Question')
    answer = models.CharField(max_length=100)
