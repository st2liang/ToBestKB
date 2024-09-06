"""
URL configuration for ToBestKB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ToBestKB.controller import UsersController as UserController
from ToBestKB.controller import KBController as KBController
from ToBestKB.controller import ConversationController

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("login/", UserController.user_login),
    path("sign_up/", UserController.sign_up),
    path("person/", UserController.person_show),
    path("person/change/", UserController.person_update),

    path("kdb/list/", KBController.KB_show),
    path("kdb/", KBController.KB_file),
    path("kdb/delete/", KBController.KB_del),
    path("kdb/create/", KBController.KB_create),

    path("conversation/list/",ConversationController.conversation_list),
    path("conversation/create/",ConversationController.conversation_create),
    path("conversation/delete/",ConversationController.conversation_delete),

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
