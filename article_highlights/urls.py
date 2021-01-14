from django.urls import path
from .views import ArticleHighlightList, ArticleHighlightDetail

urlpatterns = [
    path('<int:pk>/', ArticleHighlightDetail.as_view()),
    path('', ArticleHighlightList.as_view()),
]
