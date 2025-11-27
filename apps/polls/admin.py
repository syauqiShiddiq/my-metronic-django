from django.contrib import admin
from .models import Question, Choice

# Opsi 1: Cara Sederhana
# admin.site.register(Question)
# admin.site.register(Choice)

# Opsi 2: Cara Lebih Rapi (Recommended untuk Metronic)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)