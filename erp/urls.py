from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("erp.urls")),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("erp.urls")),
    # path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    # path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    
]
urlpatterns = [
    path('home/', views.index, name='index'),  # This will render index.html at http://127.0.0.1:8000/home/
]

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),  # URL to view the employee list
    path('add-employee/', views.add_employee, name='add_employee'),  # URL to add a new employee
    path('home/', views.index, name='Home'),
]
