from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("journal", views.journal, name="journal"),
    path("journal/add", views.add_journal, name="add_journal"),
    path("journal/edit/<int:journal_id>", views.edit_journal, name="edit_journal"),
    path("bloombot", views.bloombot, name="bloombot"),
    path("todos", views.todos, name="todos"),
    path("add_todo", views.add_todo, name="add_todo"),
    path("delete_todo/<int:id>", views.delete_todo, name="delete_todo"),
    path("privacy-policy", views.privacy_policy, name="privacy-policy"),
    path("blog", views.blog, name="blog"),
]