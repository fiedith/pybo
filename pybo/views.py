from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    page = request.GET.get('page', '1')  # 페이지. # GET방식으로 호출된 url에서 page값을 가져올 때 사용됨
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}   # question_list는 페이징 객체(page_obj)
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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 현재 로그인된 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':    # "저장하기" 버튼 -> POST요청으로 작성된 질문을 저장함
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # commit=False -> db에 아직 저장은 안함. 임시 저장만 함.
            question.author = request.user      # author 속성에 현재 로그인된 계정 저장
            question.create_date = timezone.now()   # date 생성
            question.save()                     # 실제로 저장
            return redirect('pybo:index')
    else:   # else이므로 GET: "질문 등록하기" 버튼 -> 질문을 등록하기 위한 페이지를 띄워야 하므로
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)