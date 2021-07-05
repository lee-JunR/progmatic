from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') #profile 과 User 객체 하나씩 연결, on_delete: user가 삭제될시 어떻게 될지 -> cascade 둘다 삭제되게 related_name = 'profile'은 연결된 필드 바로 불러올 수 있게 만드려고

    image = models.ImageField(upload_to='profile/', null= True) # media 파일 밑에 profile 이라는 폴더 경로 안에 저장/ null = True 프로필 사진 없어도 됨
    DEPT_CHOICES = {
        ('mju', 'MJU'),
        ('uplex', 'UPLEX'),
        ('not-specified', 'Not Specified')
    }
    dept = models.CharField(max_length=100, choices=DEPT_CHOICES, null=True) # 소속
    email = models.EmailField(max_length=50) # 이메일
    nickname = models.CharField(max_length=20, unique=True, null=True) # 유일한 닉네임을 가지도록
    message = models.CharField(max_length=100, null=True)
    zonecode = models.CharField(max_length=100)