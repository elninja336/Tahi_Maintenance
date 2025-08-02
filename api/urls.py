from django.urls import path
from myapp import views
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('students/', views.manage_student),
    path('students/<int:id>',views.manage_student),

    path('admins/', views.manage_admin),
    path('admins/<int:id>',views.manage_admin),

    path('maintenances/', views.manage_maintenance),
    path('maintenances/<int:id>',views.manage_maintenance),

    path('suggestions/', views.manage_suggestion),
    path('suggestions/<int:id>',views.manage_suggestion),
    
    path('student/login', views.StudentLoginView.as_view(), name='student_login'),
    path('admin/login', views.AdminLoginView.as_view(), name='admin_login'),

]
