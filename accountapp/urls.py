from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView


app_name = "accountapp"
# "127.0.0.1/account/hello_world/" 이렇게 칠 것을 나중에 불러오기 편하게 "account:hello_world" 로 표시하기 위해 name 과 app_name 표시하는 것

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name = 'create'),
    # as_view()를 함수형 뷰와는 다르게꼭 붙여야함
    path('detail/<int:pk>', AccountDetailView.as_view(), name = 'detail'),
    # 계정의 pk가 필요함 <int:pk>
    path('update/<int:pk>', AccountUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name = 'delete'),
]
