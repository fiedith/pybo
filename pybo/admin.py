from django.contrib import admin
from .models import Question    # feat: register Question model
# from .models import Answer      # feat: register Answer model

# Register your models here.

# admin.site.register(Question)   # feat: register Question model
# admin.site.register(Answer)     # feat: register Answer model

class QuestionAdmin(admin.ModelAdmin):      # feat: find Question data using subject search field
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)    # feat: find Question data using subject search field
