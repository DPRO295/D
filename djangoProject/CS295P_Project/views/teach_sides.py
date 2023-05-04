from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from CS295P_Project.models import *
from django.shortcuts import render, HttpResponse, redirect
from datetime import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def teach_side(request):
    if request.method == "GET":
        if request.user.is_staff:
        # send login info
            user_obj = request.user.is_authenticated
            email = request.user.email
            name_list  = User.objects.filter(is_staff=False).values_list('id', 'username', 'email')
            return_chart = []
            for each_student in name_list:
                countquestion = PostReward.objects.filter(user_id=each_student[0]).count()
                countquestion += PostThread.objects.filter(user_id=each_student[0]).count()
                answerquestion = AnswerReward.objects.filter(answer_user=each_student[0]).count()
                answerquestion += CommentThread.objects.filter(comment_user_id=each_student[0]).count()
                liked = 0
                records = PostThread.objects.filter(user_id=each_student[0])
                for record in records:
                    liked += int(record.likes)
                Tips = CoinsLog.objects.filter(user_id=each_student[0]).count()
                Penalities = 0
                dict_form = {"name": each_student[1],
                             "CountQ" : countquestion,
                             "CountA" : answerquestion,
                             "Tips" : Tips,
                             "liked" : liked,
                             "Pen" : Penalities}
                return_chart.append(dict_form)
            dict_form = {"name": "student5",
                         "CountQ": 4,
                         "CountA": 5,
                         "Tips": 50,
                         "liked": 62,
                         "Pen": 2}
            return_chart.append(dict_form)
            return render(request, "teach_side.html",
                          {"check_login": user_obj, "user_email": email,
                           "username": request.user.username,
                           "datas_chart": return_chart})
        else:
            return redirect("/main_page/")
