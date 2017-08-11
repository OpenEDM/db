from django.contrib import admin

# Register your models here.
from core.models import DataLoad
from core.models import OOP, Student, Activity, Quiz, SubjectUP, StudentCourseSubject, Result, \
    CurrentProgress


@admin.register(DataLoad)
class DataLoadAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(OOP)
class OOPAdmin(admin.ModelAdmin):
    list_display = ('import_id',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('import_id',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('import_id',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('import_id',)


@admin.register(SubjectUP)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('import_id',)


@admin.register(StudentCourseSubject)
class StudentCourseSubjectAdmin(admin.ModelAdmin):
    list_display = ('import_id',)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('import_id',)


@admin.register(CurrentProgress)
class CurrentProgressAdmin(admin.ModelAdmin):
    list_display = ('import_id',)
