from django.conf.urls import url
from App17 import views

# TEMPLATE URLS!

app_name = 'Pro17'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),

]
