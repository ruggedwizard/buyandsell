from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index, name="landing-page"), 
    path('product/<str:pk>',views.Detail, name="single-item"),
    path('addproduct/',views.Addproduct, name="add-item"),
    path('login/', views.Login ,name="login-page"), 
    path('logout/', views.Logout, name="logout-user"),
    path('register/', views.Register, name="register-user"),
    path('profile-page/<str:pk>', views.Profilepage,name="profile-page")
]