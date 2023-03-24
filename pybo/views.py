from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer

# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    # render: python data를 template에 적용하여 HTMl로 반환해주는 함수

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # Question모델의 pk에 해당하는 값이 존재하지 않으면 404
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
    # urls.py 에서 명시됐듯 localhost:8000/pybo/2 와 같이 요청되면
    # 매개변수 question_id에 2가 세팅되어 detail 함수가 실행되는 것임.

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date = timezone.now())
    answer.save()
    # request.POST.get('content') 은 POST로 전송된 form 데이터 항목 중 content 값을 의미함

    return redirect('pybo:detail', question_id=question.id)
