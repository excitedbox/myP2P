from myP2P_app import views

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout

APPEND_SLASH = True

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^login/$', auth_views.login, name='login'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^borrowing/$', views.borrowing, name='borrowing'),
    url(r'^investing/$', views.investing, name='investing'),
    url(r'^register/$', views.register, name='register'),
    url(r'^faq/$', views.faq, name='faq')
]



# urlpatterns = [
#     url(r'^login/$', django.contrib.auth.views.login, name="login"),
#     url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': '/'}),
#     # url(r'^borrowing/$', views.borrowing, name='borrowing'),
#     # url(r'^investing/$', views.investing, name='investing'),
#     # url(r'^register/$', views.register, name='register')
# ]
