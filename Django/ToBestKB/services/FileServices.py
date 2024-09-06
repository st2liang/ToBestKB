from DataBase.models import Document

def add_doc(filepath,user):
    import re
    filename = re.split('/',filepath)[-1]
    type = re.split('.',filename)[-1]

    doc = Document.object.create(name = filename, type = type ,path=filepath) #create a new document in the database
    doc.add(user) #add the user to the document

def upload_doc(doc):

    return True

def delete_doc(doc,user):
    # doc.delete(user) #delete the user from the document
    doc.delete() #delete the document from the database
    return True

def select_dos(dos_id):
    return Document.object.get(id = dos_id)
