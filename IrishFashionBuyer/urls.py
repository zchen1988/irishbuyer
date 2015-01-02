from django.conf.urls import patterns, url
from IrishFashionBuyer import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<order_number>\d+)/$', views.details, name='details'),
    url(r'^(?P<order_number>\d+)/add/$', views.add, name='add'),
    url(r'^agentlogin/$', views.agentlogin, name='agentlogin'),
    url(r'^auth_login/$', views.auth_login, name='auth_login'),
    url(r'^agent_order/$', views.agent_order, name='agent_order'),
    url(r'^admin_order/$', views.admin_order, name='admin_order'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'^add_new_order/$', views.add_new_order, name='add_new_order'),


)