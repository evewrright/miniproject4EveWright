from django.urls import path
from .views import IndexView
from . import views
from .views import IndexView, DetailView


app_name = 'todo'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create", views.Create.as_view(), name="create"),
    path("update/<int:pk>/", views.Update.as_view(), name="update"),
]