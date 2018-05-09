from django.conf.urls import url
from . import views

urlpatterns = [
    url('^main/', views.my_page, name='main_page'),
    url('^not_exists/', views.empty_view, name='empty_page'),
]
