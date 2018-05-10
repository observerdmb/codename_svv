from django.conf.urls import url
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    url('^main/', views.my_page, name='main_page'),
    url('^not_exists/', views.empty_view, name='empty_page'),
    url('^register', views.registration, name='register'),
    url('', RedirectView.as_view(url='main/'))
]
