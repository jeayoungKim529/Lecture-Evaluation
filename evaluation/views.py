from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required # 데코레이터 사용

from .forms import EvalForm
from accounts.models import User
from lectures.models import Lectures
from .models import Evals

# 글 작성하기
@login_required(login_url= '/accounts/login')
def create(request, num):
    if request.method == "POST":
        form = EvalForm(request.POST)
        if form.is_valid():
            eval = form.save(commit=False) # 일단 DB에 저장하지 않고
            eval.lect_id = get_object_or_404(Lectures, pk=num) # 강의 정보를 가져와 넣어주고
            eval.author = User.objects.get(userId=request.user.get_username()) # 글 작성을 요청한 사용자 넣어주고
            eval.date = timezone.datetime.now() # 현재 시간 넣어주고
            eval.hw_level = request.POST['hw_level'] # 과제 난이도 넣어주고
            eval.test_level = request.POST['test_level'] # 시험 난이도 넣어주고
            eval.lect_power = request.POST['lect_power'] # 강의력까지 넣어주고
            eval.save() # db에 저장
            return redirect('/') # 저장되면 강의 자세히 보기 페이지 보여줄 수 있도록 url 수정하기
    else:
        form = EvalForm()
        return render(request, 'create.html', {'form': form})

# 글 삭제하기
@login_required(login_url= '/accounts/login')
def delete(request, eval_id):
    eval = get_object_or_404(Evals, pk=eval_id) # 삭제하려는 글이 없으면 404 오류를 내고, 있으면 가져오기
    eval.delete()
    return redirect('/')

# 강의평 보여주기
def show_eval(request, lect_id):
    evaluations = Evals.objects.filter(lect_id=lect_id) # 사용자가 요청한 강의와 강의 번호가 일치하는 강의평만 가져오기 
    return render(request, 'show_eval.html', {'evaluations':evaluations})