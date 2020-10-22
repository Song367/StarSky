from common import views
from django.urls import path


urlpatterns=[
    path('index/',views.index),
    path('earth/',views.earth),
    path('planet/',views.planets),
    path('planetdata/',views.planetdata)
]