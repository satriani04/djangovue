from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ('task', 'desc', 'completed')
    list_filter = ('completed', 'created')
admin.site.register(Todo, TodoAdmin)
