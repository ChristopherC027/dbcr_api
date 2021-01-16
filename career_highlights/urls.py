from django.urls import path
from .views import CareerHighlightList, CareerHighlightDetail

urlpatterns = [
    path('<int:pk>/', CareerHighlightDetail.as_view()),
    path('', CareerHighlightList.as_view()),
]
