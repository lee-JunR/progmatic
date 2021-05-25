# 코드 간소화를 위한 데코레이터 부분입니다 for views.py
from profileapp.models import Profile

from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

#    self = AccountUpdateView, self.get_object()는 기존 data table의 pk값, request.user는 현재 요청을 보내는 유저의 pk 값
def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk = kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
