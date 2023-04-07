from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')       # login required when creating questions
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


@login_required(login_url='common:login')  # 질문 수정
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:         # 현재 login된 사용자와 질문의 글쓴이가 다를 경우
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)    # POST
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # modify date 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        # instance를 기준으로 QuestionForm을 생성하지만 request.POST의 값으로 overwrite함
        form = QuestionForm(instance=question)  # GET
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')   # 질문 삭제
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:     # 현재 login된 사용자와 질문의 글쓴이가 다를 경우
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')