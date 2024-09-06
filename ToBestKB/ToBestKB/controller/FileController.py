from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from DataBase.models import User,KnowledgeBase,Document
from ToBestKB.services import UsersServices
from django.contrib.auth import authenticate, login
from DataBase.form import DocumentForm

@csrf_exempt
def file_upload(request):
    if request.method == 'POST':
        if request.user.is_authenticated:

            data = json.loads(request.body)
            kbid = data.get('kdbid')
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save()
            file = Document.objects.get(id=instance.id)
            kb = KnowledgeBase.objects.get(id=kbid)
            user = User.objects.get(id=request.user.id)
            file.attach_knowledge = kb
            file.attach_user = user
            file.save()

            """
            此处为大模型的函数（file，path）
            path为none，表示要创建向量库，返回向量库地址
            path不为none，表示要查询向量库，返回查询结果
            
            """


            return JsonResponse({'fileid': instance.id},status=200)
        else:
            return JsonResponse({'msg': 'Do not login'},status=401)

    else:
        return JsonResponse({'msg': 'File_upload Invalid request method'},status=405)


def file_delete(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        fileid = data.get('fileid')
        Document.objects.filter(file_id=fileid).delete()
        return JsonResponse({'msg': 'File deleted successfully'},status=200)
    else:
        return JsonResponse({'msg': 'File_delete Invalid request method'},status=405)



