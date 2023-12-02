from django_filters import FilterSet,ModelChoiceFilter,DateTimeFilter
from django.forms import DateTimeInput
from .models import Post,Category


class NewsFilter(FilterSet):
    category = ModelChoiceFilter(field_name='postCategory',
        queryset= Category.objects.all(),
        label='Category',
        empty_label='Select a category')
    added_after = DateTimeFilter(
        field_name='added_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
        model = Post
        fields = {
            'title': ['icontains']
        }