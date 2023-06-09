from django.urls import path

from .views import base_views, question_views, answer_views

app_name = 'pybo'   # 향후 다른 app들이 동일한 url 별칭을 사용하는 경우가 생기므로 중복 방지를 위해 app_name을 명시한다

urlpatterns = [
    # name : URL 별칭. refactoring을 위해 붙여줌.

    # base_views.py
    path('', base_views.index, name='index'),  # localhost:8000/pybo/
    path('<int:question_id>/', base_views.detail, name='detail'),    # localhost:8000/pybo/2 페이지 요청시 question_id = 2 가 저장되고 views.detail 호출

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),  # 질문 수정
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),  # 질문 삭제
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),    # localhost:8000/pybo/answer/create/2 와 같은 페이지 요청시 views.answer_create 호출
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),  # 답변 수정
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),  # 답변 삭제
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
]
