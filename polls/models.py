from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question = models.CharField(verbose_name="question", max_length=200)
    publication_date = models.DateTimeField(
        verbose_name="publication date",
        null=True,
        auto_created=True,
    )

    def was_published_recently(self):
        return self.publication_date >= timezone.now() - datetime.date(days=1)

    def __str__(self) -> str:
        return self.question + " - " + str(self.publication_date)


class Choice(models.Model):
    question = models.ForeignKey(
        verbose_name="Question", to=Question, on_delete=models.CASCADE
    )
    choice_text = models.CharField(verbose_name="Choice text", max_length=200)
    votes = models.IntegerField(verbose_name="Choice Votes", default=0)

    def __str__(self) -> str:
        return self.choice_text + " - votes:" + str(self.votes)
