from django.urls import path
from . import views
app_name = "finches"
urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about, name="about"),
    path('finches/',views.index, name="index"),
    path('finches/<int:id>/',views.detail,name="detail"),
    path('finches/create', views.CreateFinch.as_view(), name="create"),
    path('finches/<int:pk>/edit',views.UpdateFinch.as_view(),name="update"),
    path('finches/<int:pk>/delete',views.DeleteFinch.as_view(),name="delete"),
    path('finches/<int:pk>/add_feeding',views.add_feeding,name="add_feeding"),
]

