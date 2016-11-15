from django.conf.urls import url
from .views import (
        TodoListView,
        TodoCreateView
    )

urlpatterns = [
    url(r'^$', TodoListView.as_view(), name='todo-list'),
    url(r'^create/$', TodoCreateView.as_view(), name='todo-list'),
]