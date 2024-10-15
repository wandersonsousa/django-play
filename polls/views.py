from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from polls.models import Question
from django.views.generic import ListView

import json


class QuestionListView(ListView):
    model = Question

    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        return render(
            request=request,
            template_name="polls/index.html",
            context={"questions": questions},
        )

    def post(self, request, *args, **kwargs):
        body = request.POST
        question = Question(question=body["question"])
        question.save()
        return redirect("/polls")
    
class QuestionDetailView(ListView):
    def delete(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs.get('question_id'))
        question.delete()
        return HttpResponse(status=200)