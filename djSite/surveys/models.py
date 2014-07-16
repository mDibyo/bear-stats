from django.db import models


COLLEGES = (("Chem", "College of Chemistry"),
            ("CoE", "College of Engineering"),
            ("CED", "College of Environmental Design"),
            ("LS", "College of Letters and Sciences"),
            ("CNR", "College of Natural Resources"),
            ("Haas", "Haas School of Business"))

MAJORS = (("CHEM", "Chemistry"),
          ("C"))


class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    questions_file = models.CharField(max_length=100)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    create_date = models.DateField('date created')
    reply_type = models.CharField(max_length=10)