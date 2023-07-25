from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question
    min_num = 1
    extra = 0

class ChoiceInline(admin.StackedInline):
    model = Choice
    min_num = 1
    extra = 0

class LessonInline(admin.StackedInline):
    model = Lesson
    min_num = 1
    extra = 0

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']

# <HINT> Register Question and Choice models here
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Submission)