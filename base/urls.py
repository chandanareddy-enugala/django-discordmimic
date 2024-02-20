from django.urls import path
from .views import home, room, createRoom,updateRoom,deleteRoom,loginPage,logoutUser,registerUser


urlpatterns = [
    path('login/',loginPage, name="login"),
    path('register/',registerUser, name="register"),
    path('logout/',logoutUser, name="logout"),
    path("home/", home, name="home"),
    path("room/<int:pk>", room, name="room"),
    path('create-room/',createRoom, name ='create-room'),
    path('update-room/<int:pk>',updateRoom,name='update-room'),
    path('deleteroom/<int:pk>',deleteRoom,name='delete-room'),
    
]
