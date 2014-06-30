from django.db import models


class User(models.Model):
    # Common options for different questions
    SEMESTERS = (('FA09', 'Fall 2009'),
                 ('SP10', 'Spring 2010'),
                 ('FA10', 'Fall 2010'),
                 ('SP11', 'Spring 2011'),
                 ('FA11', 'Fall 2011'),
                 ('SP12', 'Spring 2012'),
                 ('FA12', 'Fall 2012'),
                 ('SP13', 'Spring 2013'),
                 ('FA13', 'Fall 2013'),
                 ('SP14', 'Spring 2014'),
                 ('FA14', 'Fall 2014'),
                 ('SP15', 'Spring 2015'),
                 ('FA15', 'Fall 2015'),
                 ('SP16', 'Spring 2016'),
                 ('FA16', 'Fall 2016'),
                 ('SP17', 'Spring 2017'),
                 ('FA17', 'Fall 2017'),
                 ('SP18', 'Spring 2018'),
                 ('FA18', 'Fall 2018'),
                 ('SP19', 'Spring 2019'),
                 ('FA19', 'Fall 2019'),
                 ('SP20', 'Spring 2020') )
    
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=20)
    
    # Keep track of when users are entering and graduating to keep data current
    entry_semester = models.CharField(max_length=1, choices=SEMESTERS[:11])
    grad_semester = models.CharField(max_length=1, choices=SEMESTERS[11:])


class SurveyResult(models.Model):
    # Perform joins with different tables to get different results
    user = models.ForeignKey('User')
    question = models.ForeignKey('surveys.Question')
    
    answer = models.CharField(max_length=100)
