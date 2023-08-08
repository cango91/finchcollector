from django.urls import path
from . import views
app_name = "finches"
urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about, name="about"),
    path('finches/',views.index, name="index"),
    path('finches/<int:id>/',views.detail,name="detail")
]

