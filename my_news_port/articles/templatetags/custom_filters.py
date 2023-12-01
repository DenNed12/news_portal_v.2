from django import template
from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from ..models import Post

register = template.Library()

@register.filter()
def censor(text):
    l = text.split()
    restricted_words = ['ipsum']
    res = []
    for w in l:
        m = w.lower()
        if m in restricted_words:
            s = w[0] + '*' * (len(w) - 1)
            res.append(s)
        else:
            res.append(w)
    return ' '.join(res)



# class NewsFilter(FilterSet):
#     added_after = DateTimeFilter(
#         field_name='added_at',
#         lookup_expr='gt',
#         widget=DateTimeInput(
#             format='%Y-%m-%dT%H:%M',
#             attrs={'type': 'datetime-local'},
#         ),
#     )
#     class Meta:
#         model = Post
#         fields = {
#             'name': ['icontains'],
#         }