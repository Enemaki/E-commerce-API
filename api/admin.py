from django.contrib import admin

from .models import Student, Course, Enrollment, User

class EnrollmentInline(admin.TabularInline):
    model = Enrollment

class StudentAdmin(admin.ModelAdmin):
    inlines = [
        EnrollmentInline
    ]

admin.site.register(Student, StudentAdmin)
admin.site.register(User)
admin.site.register(Course)