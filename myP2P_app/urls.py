from myP2P_app import views

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout
from django.conf.urls import include, url

APPEND_SLASH = True

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^borrowing/$', views.borrowing, name='borrowing'),
    url(r'^investing/$', views.investing, name='investing'),
    url(r'^register_user/$', views.register_user, name='register_user'),
    url(r'^faq/$', views.faq, name='faq'),
    url('^register_details/$', views.register_details, name='register_details'),
    url('^register_details_lenders/$', views.register_details_lenders, name='register_details_lenders'),
    url('^register_details_borrowers/$', views.register_details_borrowers, name='register_details_borrowers'),
]

# url(r'^oauth/',include('social_django.urls',namespace='social'))


