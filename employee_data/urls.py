from django.urls import path
from .views import DataList, DataDetail, DataLoad

urlpatterns = [
    path('', DataList.as_view(), name='list_employee'),
    path('<int:pk>/', DataDetail.as_view()),
    path('spreadsheet/<key>/', DataLoad),
]