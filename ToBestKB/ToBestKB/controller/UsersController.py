from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from DataBase.models import User
from ToBestKB.services import UsersServices
from django.contrib.auth import authenticate, login

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            print("Enter POST")
            # Parse JSON data from request body
            # from ToBestKB.system.tools.PasswordUtils import md5SaltEncode
            data = json.loads(request.body)
            account = data["account"]
            password = data["password"]
            user = authenticate(request, username=account, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"return_id": user.id})
            else :
                return JsonResponse({"error": "user_login account or password error"}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"error":"user_login JSONDecodeError"}, status=400)
    return JsonResponse({"error": "user_login request methed is not POST"}, status=405)

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        # print("Enter POST")
        try:
            # from ToBestKB.system.tools.PasswordUtils import md5SaltEncode
            # Parse JSON data from request body
            data = json.loads(request.body)
            account = data["account"]
            password = data["password"]
            # password = md5SaltEncode(password)
            user = User.objects.create_user(name="random", account=account,password=password)
            return JsonResponse({ 'returnid': user.id})
        except json.JSONDecodeError:
            return JsonResponse({"error": "sign_up JSONDecodeError"}, status=400)
    return JsonResponse({"error": "sign_up request methed is not POST"}, status=405)

@csrf_exempt
def person_show(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            temp_user = request.user
            return JsonResponse({ 'name': temp_user.name, 'account': temp_user.account, 'phone': temp_user.phone})
        else :
            return JsonResponse({ "error" :"You do not login"}, status=400)
    return JsonResponse({"error": "person_show request methed is not POST"}, status=405)

@csrf_exempt
def person_update(request):
    if request.method == 'PUT':
        if request.user.is_authenticated:
            try:
                # Parse JSON data from request body
                data = json.loads(request.body)
                # name = data["name"]
                # account = data["account"]
                # password = data["password"]
                # phone = data["phone"]
                # user_id = UsersServices.update_user_info(request.user.id, {"name":name, "password":password, "phone":phone})
                user = User.objects.get(id=request.user.id)
                if 'name' in data:
                    user.name = data['name']
                if 'password' in data:
                    user.set_password(data['password'])
                if 'phone' in data:
                    user.phone = data['phone']
                user.save()

                return JsonResponse({ 'msg': "success"})
            except json.JSONDecodeError:
                return JsonResponse({"msg":"JSONDecodeError"}, status=400)
        else :
            return JsonResponse({ "error" :"You do not login"}, status=400)
    return JsonResponse({"error": "person_update request methed is not PUT"}, status=405)