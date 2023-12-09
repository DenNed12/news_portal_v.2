from django.urls import path
from .views import NewsList,NewsDetail,NewsSearch, NewsCreate, NewstUpdate,NewsDelete
urlpatterns = [
   path('',NewsList.as_view()),
   path('<int:pk>', NewsDetail.as_view(), name= 'news_detail'),
   path('search/',NewsSearch.as_view(),name = 'news_list'),
   path('create/', NewsCreate.as_view(), name = 'news_create'),
   path('<int:pk>/update/', NewstUpdate.as_view(), name ='news_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name ='news_delete')

]