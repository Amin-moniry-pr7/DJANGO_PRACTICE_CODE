from .views import PMRESPONDE
from django.urls import path


urlpatterns = [
    path('', PMRESPONDE.as_view(), name='PM_A'),
]