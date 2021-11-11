from django.urls import path
from .views import StudentDataView

urlpatterns = [
    path('student/',StudentDataView,name= 'student'),
]