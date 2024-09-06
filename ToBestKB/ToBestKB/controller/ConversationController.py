from ToBestKB.services import ConversationServices
from DataBase.models import Dialog, User,KnowledgeBase
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def conversation_create(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_id = request.user.id
            data = json.loads(request.body)
            title = data.get('title')
            kdb_id = data.get('kdbid')
            kb = KnowledgeBase.objects.get(id=kdb_id)
            user = User.objects.get(id=user_id)

            dialog = Dialog.objects.create(title = title, owner = user, attach_knowledgebase = kb)

            return JsonResponse({'conversationid': dialog.id}, status=201)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
    elif request.method == 'GET':
        conversation_id = request.GET.get('conversationid')
        query = request.GET.get('query')

        content, matched_text = query, str(conversation_id)
        return JsonResponse({"match_text:": matched_text, "answer": content})

    else:
        return JsonResponse({'error': 'conversation_create Invalid request method'}, status=405)

@csrf_exempt
def conversation_delete(request):
    if request.method == 'DELETE':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            dialog_id = data["conversationid"]
            dialog = Dialog.objects.get(id=dialog_id)
            if dialog.owner == request.user:
                dialog.delete()
                return JsonResponse({'message': 'Conversation deleted successfully'}, status=200)
            else:
                return JsonResponse({'error': 'User is not authorized to delete this conversation'}, status=403)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
    else:
        return JsonResponse({'error': 'conversation_delete Invalid request method'}, status=405)



@csrf_exempt
def conversation_list(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            dialogs = Dialog.objects.filter(owner=user)
            # dialogs = ConversationServices.get_conversations()
            dialogs_L = []
            for dialog in dialogs:
                dialogs_L.append({"title":dialog.title,"id":dialog.id})
            return JsonResponse({'data': dialogs_L}, safe=False)
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
    else:
        return JsonResponse({'error': 'conversation_list Invalid request method'}, status=405)

@csrf_exempt
def conversation_content(request):
    if request.method == 'GET':
        conversation_id = request.GET.get('conversation_id')
        query  = request.GET.get('query')

        content ,matched_text = "LLM中封装好的函数（参数为query，和可选向量库，可选历史内容）"
        """
        此处为大模型中的函数，接受一个必需项query，两个可选项向量库地址，历史内容
        返回回答内容
        """
        history = Dialog.objects.filter(id=conversation_id)
        history.append({""})


        return JsonResponse({"match_text:" : matched_text, "answer": content})
    else:
        return JsonResponse({'error': 'conversation_content Invalid request method'}, status=405)
