from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .models import Student, Course
from .views import CourseViewSet, StudentViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('student', StudentViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]