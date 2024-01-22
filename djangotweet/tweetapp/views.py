from django.shortcuts import render, redirect
from . import models
from django.urls import reverse,reverse_lazy
from tweetapp.forms import AddTweetForm,AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.
def listTweet(request):
    all_tweets=models.Tweet.objects.all()
    tweet_dict={"tweets":all_tweets}
    return render(request,'tweetapp/listTweet.html',context=tweet_dict)

@login_required(login_url="/login")
def addTweet(request):
    if request.method=='POST':
        message=request.POST["message"]
        models.Tweet.objects.create(username=request.user, message=message)
        return redirect(reverse('tweetapp:listTweet'))
    else:
        return render(request,'tweetapp/addTweet.html')
    
def addtweetbyform(request):
    if request.method=='POST':
        form= AddTweetForm(request.POST)
        if form.is_valid():
            nickname=form.cleaned_data["nickname_input"]
            message=form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            return redirect(reverse('tweetapp:listTweet'))
        else:
            print("error in form")
            return render(request,'tweetapp/addtweetbyform.html',context={"form":form})

    else:
        form = AddTweetForm()
        return render(request,'tweetapp/addtweetbyform.html',context={"form":form})
     

def addtweetbymodelform(request):
    if request.method=='POST':
        form= AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname=form.cleaned_data["nickname"]
            message=form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            print(form.cleaned_data)
            return redirect(reverse('tweetapp:listTweet'))
        else:
            print("error in form")
            return render(request,'tweetapp/addtweetbymodelform.html',context={"form":form})

    else:
        form = AddTweetModelForm()
        return render(request,'tweetapp/addtweetbymodelform.html',context={"form":form})
    
@login_required    
def deletetweet(request,id):
    tweet= models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        tweet.delete()
    return redirect(reverse('tweetapp:listTweet'))

class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')    
    template_name="registration/signup.html"


