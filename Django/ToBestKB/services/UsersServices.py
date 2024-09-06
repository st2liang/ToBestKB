from DataBase.models import User
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def get_user_id(account, password):
    try:
        user = User.objects.get(account=account, password=password)
        return user.id  # 返回用户的 ID
    except ObjectDoesNotExist:
        return None  # 没有找到匹配的用户
    except MultipleObjectsReturned:
        # 处理找到多个匹配用户的情况
        # 例如，记录日志或采取其他适当的行动
        return None  # 或者处理这种异常的其他方式

def update_user_info(User_id, new_info):
    """
    new_info需要包括什么
    建议包括：姓名，密码暗文，手机号，修改时间

    """
    user = User.objects.get(id=User_id)
    user.name = new_info['name']
    user.account = new_info['account']
    user.password = new_info['password']
    user.phone = new_info['phone']
    user.save()

    return user

def delete_user(User_id):
    """
    根据用户id删除用户
    """
    user = User.objects.get(id=User_id)
    user.delete()

def create_user(new_user):
    """
    new_user需要包括什么
    建议包括：手机号，密码暗文，创建时间
    以字典的形式传递
    """

    new_user['name'] = "random1"
    user = User.objects.create_user(name=new_user['name'], account = new_user["account"], password=new_user['password'])
    return user.id

def now_user(uesr_info):
    """
    获取当前用户
    """
    user = User.objects.get(id=1)

    return user["id"]

