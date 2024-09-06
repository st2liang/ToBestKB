from ToBestKB.services import KBServices
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from DataBase.models import KnowledgeBase,User,Dialog


@csrf_exempt
def KB_show(request):
    if request.method  == 'GET':
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            KB_L = KnowledgeBase.objects.filter(owner=user)
            Data = []
            for kb in KB_L:
                Data.append({'kb_id': kb.id, 'name': kb.name})
            return JsonResponse({'data':Data})
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
    return JsonResponse({'error': 'KB_show Invalid request method'}, status=400)

@csrf_exempt
def KB_file(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            kdb_id = request.GET.get('id')
            doc_L = KBServices.list_kb_attach_doc(id)
            Dict_doc = []
            for doc in doc_L:
                Dict_doc.append({'filename': doc.name, 'fileid':doc.id})
            return JsonResponse({'data':Dict_doc})
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
    if request.method == 'DElETE':
        kdb_id = request.GET.get('kbid')
        file_id = request.GET.get('fileid')
        try:
            KBServices.delete_kb_from_doc(kdb_id,file_id)
            return JsonResponse({'data': 'success'})
        except Exception as e:
            return JsonResponse({'error': e}, status=401)
    return JsonResponse({'error': 'KB_file Invalid request method'}, status=400)


@csrf_exempt
def KB_del(request):
    if request.method == 'DELETE':
        try:
            # KBServices.delete_kb(kdb_id)
            kb_id = request.GET.get('id')
            kb = KnowledgeBase.objects.get(id=kb_id)
            """
            此处需要一个函数
            参数为向量库地址
            效果是删除向量库
            
            """


            kb.delete()
            return JsonResponse({'id':kb_id, 'msg': 'success'})
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
            return JsonResponse({'kdbid': kb.id})
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
        # Check if the user is authenticated

    return JsonResponse({'error': 'KB_create Invalid request method'}, status=400)

