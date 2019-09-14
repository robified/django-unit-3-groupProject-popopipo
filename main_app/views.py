from django.shortcuts import render, redirect
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .models import Comment

# This is our Create Post view. We create new posts passing in the fields from the model.
class PostCreate(CreateView):
  model = Post
  fields = ['title', 'categories', 'company', 'company_office_city', 'body']
  success_url = '/post'

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'categories', 'company', 'company_office_city', 'body']

class PostDelete(DeleteView):
    model = Post
    success_url = '/'

class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

def home(request):
  return render(request, 'home.html')

def post_index(request):
  post = Post.objects.all().order_by('-created_on')
  return render(request, 'blog/index.html', {'post': post})

def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  # Post views counter not working properly
  post.views += 1

  form = CommentForm()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = Comment(
        body=form.cleaned_data["body"],
        post=post
      )
      comment.save()

  comments = Comment.objects.filter(post=post).order_by('-created_on')
  context = {
    "post": post,
    "comments": comments,
    "form": form,
  }
  return render(request, 'blog/detail.html', { 'post': post , 'form': form, 'comments': comments})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      # This is the route that will redirect after a succesful sign up.
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)  