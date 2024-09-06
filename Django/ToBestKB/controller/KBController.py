from ToBestKB.services import KBServices
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from DataBase.models import KnowledgeBase,User,Dialog,Document


@csrf_exempt
def KB_show(request):
    if request.method  == 'GET':
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            KB_L = KnowledgeBase.objects.filter(owner=user)
            Data = []
            for kb in KB_L:
                Data.append({'kb_id': kb.id, 'name': kb.name})
            return JsonResponse({'data':Data},status=200)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
    return JsonResponse({'error': 'KB_show Invalid request method'}, status=400)

@csrf_exempt
def KB_file_show(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            kdb_id = request.GET.get('id')
            kb = KnowledgeBase.objects.get(id=kdb_id)
            doc_L = Document.objects.filter(attach_knowledge=kb)
            Data = []
            for doc in doc_L:
                Data.append({'filename': doc.name, 'fileid':doc.id})
            return JsonResponse({'data':Data,"code":-1,"msg":"success"},status=200)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
    return JsonResponse({'error': 'KB_file Invalid request method'}, status=400)


@csrf_exempt
def KB_del(request):
    if request.method == 'DELETE':
        try:
            # KBServices.delete_kb(kdb_id)
            kbid = request.GET.get('id')
            kb = KnowledgeBase.objects.get(id=kbid)

            """
            此处需要一个函数
            参数为向量库地址
            效果是删除向量库
            
            """

            kb.delete()
            return JsonResponse({'id':kbid, 'msg': 'success'},status=200)
        except Exception as e:
            return JsonResponse({'error': e}, status=401)
    return JsonResponse({'error': 'KB_del Invalid request method'}, status=400)

@csrf_exempt
def KB_create(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            name = data['kdbtitle']
            kb = KnowledgeBase(name=name ,owner = request.user)
            kb.save()
            return JsonResponse({'kdbid': kb.id},status=200)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
        # Check if the user is authenticated

    return JsonResponse({'error': 'KB_create Invalid request method'}, status=400)

