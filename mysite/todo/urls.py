from django.urls import path
from .views import MyLoginView
from django.contrib.auth.views import LogoutView
from . import views
from .views import IndexView, DetailView


app_name = 'todo'
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create", views.Create.as_view(), name="create"),
    path("update/<int:pk>/", views.Update.as_view(), name="update"),
]
