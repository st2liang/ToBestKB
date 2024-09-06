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
            import re
            kbid = request.GET.get('kdbid')
            # print(kbid)

            form = DocumentForm(request.POST, request.FILES)
            if not form.is_valid():
                return JsonResponse({'error': 'Invalid form data'}, status=400)
            instance = form.save()

            doc = Document.objects.get(id=instance.id)
            filename = doc.file.name
            filename = re.split('/',filename)[-1]
            # print(filename)
            type = re.split(r'\.', filename)[-1]

            kb = KnowledgeBase.objects.get(id=kbid)
            user = User.objects.get(id=request.user.id)

            doc.name = filename
            doc.type = type
            doc.attach_knowledge = kb
            doc.attach_user = user
            doc.save()

            """
                此处为大模型的函数（file，path,kbid）
                path为none，表示要创建向量库，返回向量库地址
                path不为none，表示要查询向量库，返回查询结果

            """

            if not kb.content:
                file = doc
                path = None
                kb.content = "上述函数"
            else :
                file = doc
                path = kb.content
                "上述函数"

            return JsonResponse({'fileid': instance.id},status=200)
        else:
            return JsonResponse({'error': 'Do not login'},status=401)

    else:
        return JsonResponse({'error': 'File_upload Invalid request method'},status=405)


@csrf_exempt
def file_delete(request):
    if request.method == 'DELETE':
        fileid = request.GET.get('fileid')
        kdid = request.GET.get('kbid')

        """
        该处维删除函数，接受两个参数filename和kb。content
        
        """
        # fileid = data.get('fileid')
        Document.objects.filter(id=fileid).delete()
        return JsonResponse({'msg': 'File deleted successfully'},status=200)
    else:
        return JsonResponse({'msg': 'File_delete Invalid request method'},status=405)



