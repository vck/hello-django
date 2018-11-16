"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from master.views import index_view, view_page_id, delete_page_id, downvote_post_id, upvote_post_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('hello/', index_view),
    path('yowasup/', index_view),
    path('post/<int:post_id>', view_page_id),
    path('kirim/', index_view),
    path('delete/<int:post_id>', delete_page_id),
    path('downvote/<int:post_id>', downvote_post_id),
    path('upvote/<int:post_id>', upvote_post_id)
]
