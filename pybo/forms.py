from django import forms
from pybo.models import Question, Answer


# Question모델과 연결된 폼으로, 속성으로 Question모델의 subject와 content를 사용함
class QuestionForm(forms.ModelForm):    # extends forms.ModelForm
    class Meta:         # ModelForm은 Meta 이너클래스가 반드시 필요함
        model = Question
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변 내용',
        }
