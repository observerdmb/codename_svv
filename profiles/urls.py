from django.conf.urls import url, include
from . import views
from django.views.generic import RedirectView
from django.contrib.auth.views import logout


urlpatterns = [
    url('^main/', views.my_page, name='main_page'),
    url('^not_exists/', views.empty_view, name='empty_page'),
    url('login/', views.login_user, name='log-in'),
    url('^logout/', logout, {'template_name': 'empty.html', 'next_page': '/'}, name='logout'),
    url('', RedirectView.as_view(url='main/')),
]
