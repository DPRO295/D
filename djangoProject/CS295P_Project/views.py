from django.shortcuts import render, HttpResponse
from pymongo import MongoClient
import certifi

ca=certifi.where()
database_path = 'mongodb+srv://Dpropro:Dpropro@dpro.qls8nuc.mongodb.net/?retryWrites=true&w=majority'
# Create your views here.
def home(request):
    return render(request, "home.html")


def signin(request):
    if(request.method == "GET"):
        return render(request, "signin.html")
    else:
        email = request.POST.get("email")
        password = request.POST.get("pwd")

        client = MongoClient(database_path,tlsCAFile=ca)
        user = client["try"]["user"]
        doc = list(user.find({"email":email}))
        client.close()
        if(doc == []):
            return render(request, "signin.html", {"error_msg": "This email haven't been registered."})
        elif(doc[0]["pwd"] != password):
            return render(request, "signin.html", {"error_msg": "Wrong password!"})
        else:
            return HttpResponse("Sign in successfully!")            # login success

def register(request):
    if(request.method == "GET"):
        return render(request, "register.html")
    else:
        email = request.POST.get("email")
        password = request.POST.get("pwd")

        client = MongoClient(database_path,tlsCAFile=ca)
        user = client["try"]["user"]
        doc = list(user.find({"email":email}))
        if(doc != []):
            client.close()
            return render(request, "register.html", {"error_msg": "This email have been used."})
        else:
            user.insert_one({"email":email,"pwd":password})
            client.close()
            return HttpResponse("Register successfully!")
