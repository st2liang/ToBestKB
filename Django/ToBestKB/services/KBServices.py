from DataBase.models import KnowledgeBase,User,Document,Dialog
def create_KB(data:dict):
    """
    好像只要传递姓名和描述
    content以某种形式连接到chroma
    
    """
    kb = KnowledgeBase(name=data['name'])
    kb.save()
    return kb.id

def add_doc_to_kb(kb_id:int,doc_id:int):
    kb = KnowledgeBase.objects.get(id=kb_id)
    doc = Document.objects.get(id=doc_id)
    kb.attach_document.add(doc)

def list_kb(user_id):
    user = User.objects.get(id=user_id)
    Dialog_L = Dialog.objects.filter(owner=user)
    KB_L= []
    for dialog in Dialog_L:
        KB_L.attend(dialog.attach_knowledgebase)
    return KB_L

def list_kb_attach_doc(kb_id):
    kb = KnowledgeBase.objects.get(id=kb_id)
    return kb.attach_document.all()

def delete_kb(kb_id:int):
    kb = KnowledgeBase.objects.get(id=kb_id)
    kb.delete()

def delete_doc_from_kb(kb_id:int,doc_id:int):
    kb = KnowledgeBase.objects.get(id=kb_id)
    doc = Document.objects.get(id=doc_id)
    if doc in kb.attach_document.objects.all():
        kb.attach_document.remove(doc)
    else:
        raise Exception("Document is not in the knowledge base")