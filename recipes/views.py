from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import authenticate
from .form import RecipeForm, MyUserCreationForm
from .models import Recipe


def home(request):
    return render(request, 'recipes/home.html')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'recipes/loginuser.html', {'form': MyUserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('currentrecipes')
        else:
            return render(request, 'recipes/loginuser.html', {'form':  MyUserCreationForm(), 'error': 'Password do not match'})

def signinuser(request):
    if request.method == 'GET':
        return render(request, 'recipes/signinuser.html', {'form': AuthenticationForm()})
    else:
        try:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            user.save()
            login(request, user)
            return redirect('currentrecipes')
        except AttributeError:
            return render(request, 'recipes/signinuser.html', {'form': AuthenticationForm(), 'error': 'Passoword is not corrected'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def currentrecipes(request):
    recipes = Recipe.objects.filter(user = request.user )
    return render(request, 'recipes/currentrecipes.html', {'recipes': recipes})

def createrecipes(request):
    if request.method == 'GET':
        return render(request, 'recipes/createrecipes.html', {'form': RecipeForm()})
    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('currentrecipes')

def viewsrecipes(request, rec_pk):
    recipes = get_object_or_404(Recipe, pk=rec_pk, user=request.user)
    if request.method == 'GET':
        form = RecipeForm(instance=recipes)
        return render(request, 'recipes/viewsrecipes.html', {'recipes': recipes, 'form': form})
    else:
        form = RecipeForm(request.POST, request.FILES, instance=recipes)
        form.save()
        return redirect('currentrecipes')

def deleterecipes(request, rec_pk):
    recipes = get_object_or_404(Recipe, pk=rec_pk, user=request.user)
    if request.method == 'POST':
        recipes.delete()
        return redirect('currentrecipes')