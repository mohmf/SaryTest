from django.contrib import admin

from .models import Answer, AnswerComment, Question, QuestionComment, Tag
# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionComment)
admin.site.register(AnswerComment)
admin.site.register(Answer)
admin.site.register(Tag)