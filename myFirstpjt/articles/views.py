from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request,'articles/index.html') # render 함수는 첫번 째 인자는 무조건 request를 받아야함함