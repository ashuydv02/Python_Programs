from django.contrib import admin
from .models import UserProfile, Course, Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_courses')

    def get_courses(self, obj):
        return ", ".join([course.title for course in obj.courses.all()])
    get_courses.short_description = 'Courses'




admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Student, StudentAdmin)
