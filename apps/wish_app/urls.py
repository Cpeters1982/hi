from . import views
from django.conf.urls import url
def test(request):
	print 'in wish'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addform$', views.addForm),
    url(r'^addwish$', views.addWish),
    # url(r'^like/(?P<id>\d+)$', views.likeCat),



]
