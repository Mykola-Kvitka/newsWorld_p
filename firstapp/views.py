from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import News, Comment,Topic
from .forms import CommentForm,NewUserForm
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages #import messages

def index(request):
    allNews = News.objects.all().order_by('date').reverse
    allTopics = Topic.objects.all()
    return render(request, "index.html", {"news": allNews,"topics":allTopics})

def getCertainNews(request,id):
    if request.method == "POST":
        form_obj = CommentForm(request.POST)
        if form_obj.is_valid():
            newComment = Comment(authorName=form_obj.cleaned_data['authorName'], commentBody=form_obj.cleaned_data['commentBody'], dateTime=timezone.now(),newsId=id)
            newComment.save()
            new_form_obj = CommentForm()
    

    new_form_obj = CommentForm()
    certainNews=News.objects.get(id=id)
    comments=Comment.objects.filter(newsId=id).order_by('dateTime').reverse


    return render(request, "newsPage.html", {"certainNews": certainNews, 'form':new_form_obj, 'comments':comments})

def getCertainTopic(request,id):
    certainTopicNews=News.objects.filter(topicId=id).order_by('date').reverse
    topic=Topic.objects.get(id=id)
    return render(request, "topicPage.html", {"certainTopicNews": certainTopicNews, 'topic':topic})


def register_request(request):
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful." )
                
            messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm
        return render (request=request, template_name="register.html", context={"register_form":form})


