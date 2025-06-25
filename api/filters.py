import django_filters
from .models import Student, Course, Enrollment
from rest_framework import filters

class CreditsFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(credits__gt=1)

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'full_name': ['iexact', 'icontains'], 
            'email': ['iexact', 'icontains'],
        }

class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'title': ['iexact', 'icontains'], 
            'credits': ['exact', 'lt', 'gt', 'range'],
        }

class EnrollmentFilter(django_filters.FilterSet):
    # enrolled = django_filters.DateFilter(field_name='enrolled__date')
    class Meta:
        model = Enrollment
        fields = {
            'grade': ['exact'],
            'enrolled': ['lt', 'gt', 'exact']
        }