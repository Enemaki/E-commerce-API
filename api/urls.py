from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('students/', views.StudentListCreateAPIView.as_view(), name='students'),
    path('courses/', views.CourseListAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', views.CourseDetailsAPIView.as_view()),
    # path('enrollment/', views.EnrollmentListAPIView.as_view()),
    # path('enrollment/<int:pk>/', views.EnrollmentDetailsAPIView.as_view()),
]

router = DefaultRouter()
router.register('enrollment', views.EnrollmentViewSet)
urlpatterns += router.urls