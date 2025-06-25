from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import (LimitOffsetPagination,
                                       PageNumberPagination)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .filters import CourseFilter, CreditsFilterBackend, StudentFilter, EnrollmentFilter
from .models import Course, Enrollment, Student
from .serializers import (CourseSerializer, EnrollmentSerializer,
                          StudentSerializer)
from rest_framework.decorators import action


# @api_view(['GET'])
# def student_list(request):
#     students = Student.objects.all()
#     serializer = StudentSerializer(students, many=True)
#     return Response(serializer.data)
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.order_by('full_name')
    serializer_class = StudentSerializer
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = StudentFilter
    search_fields = ['full_name', 'email']
    ordering_fields = ['full_name', 'email']
    pagination_class = PageNumberPagination
    pagination_class.page_size = 2
    pagination_class.page_query_param = 'pagenum'
    pagination_class.page_size_query_param = 'size'
    pagination_class.max_page_size = 4


    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

# @api_view(['GET'])
# def course_list(request):
#     courses = Course.objects.all()
#     serializer = CourseSerializer(courses, many=True)
#     return Response(serializer.data)
class CourseListAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
        CreditsFilterBackend
    ]
    filterset_class = CourseFilter
    search_fields = ['credits', 'instructor']
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

# @api_view(['GET'])
# def course_details(request, pk):
#     course = Course.objects.get(pk=pk)
#     serializer = CourseSerializer(course)
#     return Response(serializer.data)

class CourseDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == ['POST', 'PUT', 'PATCH']:
            self.permission_classes = [AdminUser]
        return super().get_permissions()

# @api_view(['GET'])
# def enrollment_list(request):
#     enrollment = Enrollment.objects.all()
#     serializer = EnrollmentSerializer(enrollment, many=True)
#     return Response(serializer.data)
# class EnrollmentListAPIView(generics.ListAPIView):
#     queryset = Enrollment.objects.all()
#     serializer_class = EnrollmentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    filter_backends = [
        DjangoFilterBackend,
        # filters.SearchFilter,
        # filters.OrderingFilter,
        # CreditsFilterBackend
    ]
    filterset_class = EnrollmentFilter

    @action(detail=False, methods=['get'], url_path='enrollment-list', permission_classes = [IsAuthenticated])
    def enrollmentList(self, request):
        enrollments = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(Enrollment, many=True)
        return Response(serializer.data)
        

# @api_view(['GET'])
# def enrollment_details(request, pk):
#     enrollment = get_object_or_404(Enrollment, pk=pk)
#     serializer = EnrollmentSerializer(enrollment)
#     return Response(serializer.data)
# class EnrollmentDetailsAPIView(generics.RetrieveAPIView):
#     queryset = Enrollment.objects.all()
#     serializer_class = EnrollmentSerializer