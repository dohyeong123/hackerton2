from django.shortcuts import render
from .models import Thumbnail
# Create your views here.
def home(request):
    return render(request, 'testapp/home.html')
def login(request):
    return render(request,'testapp/login.html')
def logout(request):
    return render(request,'testapp/logout.html')
def signup(request):
    return render(request,'testapp/signup.html')
def cate_trend(request):
    thumbnails = Thumbnail.objects
    checkname = 1
    category = 'trend'
    cate_real_name = request.GET.get('sport_category')
    
    if cate_real_name == 'trend':
        checkname = 1
        category = '#트렌드운동'
    
    elif cate_real_name == 'difficulty':
        checkname = 2
        category = '#난이도별'
    elif cate_real_name == 'genre':
        checkname = 3
        category = '#장르'
    elif cate_real_name == 'guideline':
        checkname = 4
        category = '#헬스기구사용법'
    elif cate_real_name == 'sub1':
        checkname = 5
        category = '#저쩌구별'
    elif cate_real_name == 'sub2':
        checkname = 6
        category = '#쟈쩌구별'
    category_filter = thumbnails.objects.filter(cate_number=checkname)
    return render(request, 'testapp/cate_trend.html', 
{'thumbnails':thumbnails, 'category':category, 'category_filter':category_filter })