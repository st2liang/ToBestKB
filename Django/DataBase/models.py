from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, account, password=None, **extra_fields):
        if not account:
            raise ValueError(_('The Account field must be set'))
        user = self.model(account=account, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name= models.CharField(max_length=150, null=True,blank=True,verbose_name="姓名")
    account = models.CharField(max_length=150, unique=True, null=True,blank=True,verbose_name="账号")
    password = models.CharField(max_length=128)  # Storing hashed password
    phone = models.CharField(max_length=11, verbose_name="手机号",default="")

    create_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间",auto_now=True)
    # Add other fields as needed

    objects = CustomUserManager()

    USERNAME_FIELD = 'account'

class Admin(models.Model):
    admin_mobile_phone = models.CharField(max_length=11,verbose_name="管理员电话")
    admin_account = models.CharField(max_length=20,verbose_name="管理员账号")
    admin_password = models.CharField(max_length=20,verbose_name="管理员密码")

class KnowledgeBase(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100, blank=True, null=True,default="为您的知识库创建描述")
    content = models.CharField(max_length=100, blank=True, null=True)

    create_Time = models.DateTimeField(auto_now_add=True)
    update_Time = models.DateTimeField(null=True,auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,verbose_name="知识库创建者")
class Document(models.Model):
    name = models.CharField(max_length=50,verbose_name="文档名称")
    type = models.CharField(max_length=10,verbose_name="文档类型")
    # modify_permission = models.CharField(max_length=1,verbose_name="文档修改权限")
    file = models.FileField(upload_to='upload/',blank=True,null = True ,verbose_name="文档路径")

    create_time = models.DateTimeField(verbose_name="文档创建时间",auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="文档更新时间",auto_now=True)

    attach_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True, verbose_name="文档创建者")
    attach_knowledge = models.ForeignKey(KnowledgeBase,on_delete=models.CASCADE,null=True, blank=True, verbose_name="文档所属知识库")


class Dialog(models.Model):
    title = models.CharField(max_length=50, blank=False, null=True,verbose_name="对话标题")
    state = models.CharField(max_length=1, blank=True, null=True,verbose_name="对话状态",default="0")
    content = models.JSONField(verbose_name="对话内容",null=True,blank=True)

    create_time = models.DateTimeField(blank=False, null=False,verbose_name="对话创建时间",auto_now_add=True)
    update_time = models.DateTimeField(blank=False, null=False,verbose_name="对话更新时间",auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True ,null=True ,verbose_name="对话创建者")
    attach_knowledgebase = models.ForeignKey(KnowledgeBase, on_delete=models.CASCADE, verbose_name="关联知识库")

