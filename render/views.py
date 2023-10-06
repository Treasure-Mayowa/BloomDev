from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import *


# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})

@login_required
def journal(request):
    journal_entries = Journal.objects.filter(author=request.user).order_by('-created_at')
    return render(request, "render/journal.html", {
        "journals": journal_entries
    })

def blog(request):
    return render(request, "render/blog.html")


@login_required
def add_journal(request):
    prompt = request.GET.get('prompt', '')
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        new_journal = Journal(author=request.user, title=title, content=content)
        new_journal.save()
        return HttpResponseRedirect(reverse("journal"))
    else:
        return render(request, "render/add_journal.html", {
            "prompt": prompt
        })


@login_required
def edit_journal(request, journal_id):
    try:
        journal_entry = Journal.objects.get(pk=journal_id)
    except Journal.DoesNotExist:
        return HttpResponse("You do not have the permission to edit this journal")
    if request.user != journal_entry.author:
        return HttpResponse("You do not have the permission to edit this journal")
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        journal_entry.title = title
        journal_entry.content = content
        journal_entry.save()
        return HttpResponseRedirect(reverse("journal"))
    return render(request, "render/edit_journal.html", {
        "journal": journal_entry
    })


@login_required
def privacy_policy(request):
    return render(request, "render/privacy-policy.html")

@login_required
def bloombot(request):
    return render(request, "render/bloombot.html")


@login_required
def todos(request):
    todos = Todo.objects.filter(user=request.user, day_added=datetime.date.today())
    return render(request, "render/todos.html", {
        "todos": todos
    })


@login_required
def add_todo(request):
    if request.method == "POST":
        todo_item = request.POST["todo"]
        details = request.POST["details"]
        new_todo = Todo(user=request.user, name=todo_item, details=details, day_added=datetime.date.today())
        new_todo.save()
        return HttpResponseRedirect(reverse("todos"))


@login_required
def delete_todo(request, id):
    todo = Todo.objects.get(pk=id)
    if todo.user == request.user:
        todo.delete()
        return HttpResponseRedirect(reverse("todos"))
    else:
        return HttpResponseRedirect(reverse('todos'))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "render/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "render/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "render/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "render/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "render/register.html")