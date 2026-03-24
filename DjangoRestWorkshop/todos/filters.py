import django_filters
from todos.models import Todo


class TodoFilter(django_filters.FilterSet):
    is_done = django_filters.BooleanFilter(field_name='state')

    class Meta:
        model = Todo
        fields = ['category', 'is_done']
