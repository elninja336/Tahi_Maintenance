from django.urls import path
from myapp import views


urlpatterns = [
    path('students/', views.manage_student),
    path('students/<int:id>',views.manage_student),

    path('admins/', views.manage_admin),
    path('admins/<int:id>',views.manage_admin),

    path('maintenances/', views.manage_maintenance),
    path('maintenances/<int:id>',views.manage_maintenance),

    path('suggestions/', views.manage_suggestion),
    path('suggestions/<int:id>',views.manage_suggestion),
]
