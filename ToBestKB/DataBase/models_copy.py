from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20,verbose_name="用户名")
    account = models.CharField(max_length=20,verbose_name="账号")
    password = models.CharField(max_length=20,verbose_name="密码")
    is_admin = models.CharField(max_length=1,verbose_name="是否为管理员",default='0')
    phone = models.CharField(max_length=11,verbose_name="电话")
    create_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间",auto_now=True)
class Document(models.Model):
    name = models.CharField(max_length=50,verbose_name="文档名称")
    type = models.CharField(max_length=10,verbose_name="文档类型")
    # modify_permission = models.CharField(max_length=1,verbose_name="文档修改权限")
    create_time = models.DateTimeField(verbose_name="文档创建时间",auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="文档更新时间",auto_now=True)
    path = models.CharField(max_length=50,verbose_name="文档路径")
    attach_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True, verbose_name="文档创建者")

class Admin(models.Model):
    admin_mobile_phone = models.CharField(max_length=11,verbose_name="管理员电话")
    admin_account = models.CharField(max_length=20,verbose_name="管理员账号")
    admin_password = models.CharField(max_length=20,verbose_name="管理员密码")

class KnowledgeBase(models.Model):
    kb_name = models.CharField(max_length=50, blank=False, null=False)
    kb_description = models.CharField(max_length=100, blank=False, null=False,default="为您的知识库创建描述")
    kb_content = models.CharField(max_length=100, blank=False, null=False)
    create_Time = models.DateTimeField(auto_now_add=True)
    update_Time = models.DateTimeField(null=True,auto_now=True)
    attach_document  = models.ManyToManyField(Document, blank=True,verbose_name="知识库文档")
class Dialog(models.Model):
    title = models.CharField(max_length=50, blank=False, null=True,verbose_name="对话标题")
    state = models.CharField(max_length=1, blank=False, null=False,verbose_name="对话状态",default="0")
    content = models.JSONField(verbose_name="对话内容",null=True)
    create_time = models.DateTimeField(blank=False, null=False,verbose_name="对话创建时间",auto_now_add=True)
    update_time = models.DateTimeField(blank=False, null=False,verbose_name="对话更新时间",auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True ,null=True ,verbose_name="对话创建者")
    attach_knowledgebase = models.OneToOneField(KnowledgeBase,on_delete=models.CASCADE,verbose_name="关联知识库")





