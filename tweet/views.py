from django.shortcuts import render
from .models import Tweet
from .forms import xform, userregistrationform
from django.shortcuts import get_object_or_404,redirect 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweet = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweetlist.html', {'tweet': tweet})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = xform(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = xform()
    return render(request, 'tweetform.html', {'form': form})

@login_required
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == 'POST':
        form = xform(request.POST,request.FILES, instance=tweet)
        if (form.is_valid()):
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = xform(instance=tweet)
    return render(request, 'tweetform.html', {'form': form})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_delete.html', {'tweet': tweet})

def tweet_register(request):
    if request.method == 'POST':
        form = userregistrationform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})