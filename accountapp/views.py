from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.models import HelloWorld

from accountapp.forms import AccountUpdateForm

from accountapp.decorators import account_ownership_required

has_ownership = [account_ownership_required, login_required]
# @method_decorator(has_ownership , 'get')
# @method_decorator(has_ownership , 'post')
# @account_ownership_required(account_ownership_required,'get')
# @account_ownership_required(account_ownership_required,'post') 을 두줄로 줄여줌
@login_required # if request.user.is_authenticated:~~~ else:   return HttpResponseRedirect(reverse("accountapp:login")) 부분까지 장고에서 지원해줌 위에

def hello_world(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse("accountapp:hello_world"))
        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html', context={'hello_world_list' : hello_world_list})
    else:
        return HttpResponseRedirect(reverse("accountapp:login"))

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    # reverse_lazy는 클래스형 뷰에서 reverse 는 함수형 뷰에서
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership , 'get')
@method_decorator(has_ownership , 'post')
#자기인지 확인하는 과정
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    # reverse_lazy는 클래스형 뷰에서 reverse 는 함수형 뷰에서
    template_name = 'accountapp/update.html'
 # 로그인 해야 수정 가능하게 & 다른유저가 접근 못하게
 #    self = AccountUpdateView, self.get_object()는 기존 data table의 pk값, request.user는 현재 요청을 보내는 유저의 pk 값

# @method_decorator(login_required, 'get')
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()

@method_decorator(has_ownership , 'get')
@method_decorator(has_ownership , 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

