from rest_framework import generics
from todos.models import Todo
from .serializers import TodoSerializer

class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    def get_queryset(self):
        return Todo.objects.order_by('-id')

class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer        