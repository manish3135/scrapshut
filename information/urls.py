from django.conf.urls import url
from .import views

app_name = 'information'

urlpatterns = [
    url(r'^$',views.information_list, name="list"),
    url(r'^add_detail$',views.add_detail, name="add_detail"),
]