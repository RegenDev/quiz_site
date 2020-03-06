from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class QuizTip(models.Model):
    tip_title = models.CharField(max_length=200)
    tip_text = models.CharField(max_length=400)
    def __str__(self):
        return self.tip_title
