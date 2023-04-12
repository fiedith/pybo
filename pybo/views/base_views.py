from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from ..models import Question

def index(request):
    3/0     # logtest
    
    page = request.GET.get('page', '1')  # 페이지. # GET방식으로 호출된 url에서 page값을 가져올 때 사용됨
    kw = request.GET.get('kw','')   # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)
    # render: python data를 template에 적용하여 HTMl로 반환해주는 함수

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # Question모델의 pk에 해당하는 값이 존재하지 않으면 404
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
    # urls.py 에서 명시됐듯 localhost:8000/pybo/2 와 같이 요청되면
    # 매개변수 question_id에 2가 세팅되어 detail 함수가 실행되는 것임.