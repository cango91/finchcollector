from django.urls import path
from . import views
app_name = "finches"
urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about, name="about"),
    path('finches/',views.index, name="index"),
    path('finches/<int:id>/',views.detail,name="detail"),
    path('finches/create/', views.CreateFinch.as_view(), name="create"),
    path('finches/<int:pk>/edit/',views.UpdateFinch.as_view(),name="update"),
    path('finches/<int:pk>/delete/',views.DeleteFinch.as_view(),name="delete"),
    path('finches/<int:pk>/add_feeding/',views.add_feeding,name="add_feeding"),
    path('toys/',views.ListToys.as_view(),name="toys"),
    path('toys/create/',views.CreateToy.as_view(),name="create_toy"),
    path('toys/<int:pk>/edit/',views.UpdateToy.as_view(),name="update_toy"),
    path('toys/<int:pk>/delete',views.DeleteToy.as_view(),name="delete_toy"),
    path('toys/<int:pk>/',views.DetailToy.as_view(),name="toy_details"),
    path('finches/<int:finch_id>/give_toy/<int:toy_id>/',views.associate_toy,name="associate_toy"),
    path('finches/<int:finch_id>/take_toy/<int:toy_id>/',views.disassociate_toy,name="disassociate_toy"),
    path('finches/<int:finch_id>/add_photo/',views.add_photo,name="add_photo"),
    
]

