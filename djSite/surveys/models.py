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
    """
    Each Survey is stored in a separate JSON file with all the questions and 
    possible answers specified. Example survey JSON file:
    {
        "title": "Example Survey",
        "date": "07/16/2014",
        "context": "This is the reason for creating this survey. This is entered 
            purely for the sake of documentation. ",
        "questions": [{
            "question_id": "This is the primary key of the question in the database",
            "question_text": "What is question number 1?",
            "reply_type": "How is question number 1 supposed to be answered?",
            "additional_info": {
                # These are all the additional attributes that are required as
                # specified by reply_type. Reply_type specifies a set of instructions
                # on how to parse additional_info as a colon separated list
                "image_file": "/url/to/image/resource",
                "options": [{
                    "option_text": "Option 1#",
                    "is_selected": true
                }, {
                    "option_text": "Option #2",
                    "is_selected": false
                }]
            }
        }, {
            "question_id": "This is the primary key of the question in the database",
            "question_text": "What is question number 2?",
            "reply_type": "How is question number 2 supposed to be answered?",
            "additional_info": {
                "default_answer": "This is the default answer for question 2"
            }
        }]
    }

    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    questions_file = models.CharField(max_length=100)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    create_date = models.DateField('date created')
    reply_type = models.CharField(max_length=10)