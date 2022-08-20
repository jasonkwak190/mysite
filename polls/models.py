from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 질문내용, 길이
    pub_date = models.DateTimeField('date published') # 발행일

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 위의 Question을 참고할거임
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text