from django.views.generic import View
from django.shortcuts import render


class MyView(View):
    def get(self, request):
        # 处理GET请求
        return render(request, "signin.html")

    def post(self, request):
        # 处理POST请求
        return render(request, "signin.html")


