from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ('choice_text', 'votes',)

    fk_name = "question"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text","pub_date", "author")

    list_filter = ("pub_date",)

    search_fields = ("question_text",)
    inlines = [ChoiceInline]