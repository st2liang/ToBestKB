from DataBase.models import Dialog, User, KnowledgeBase
def create_dialog(userid,kbid,title):
    kb = KnowledgeBase.objects.get(id=kbid)
    user = User.objects.get(id=userid)
    dialog_temp=Dialog()
    dialog_temp['title'] = title
    dialog_temp['owner'] = user
    dialog_temp['attach_knowledgebase'] = kb
    dialog_temp.save()
    return dialog_temp.id



def add_dialog_content(dialog,content:list):
    dialog.content.append(content)
    dialog.save()

def get_conversation(userid):
    user = User.objects.get(id=userid)
    Dialog_L = Dialog.objects.filter(owner = user)
    return Dialog_L
