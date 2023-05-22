from .views import index,conn_db,select,db_aggre
from django.urls import path

urlpatterns = [
    path('', index,name='index'),
    path('button-click/',conn_db),
    path('select/',select,name='select'),
    path('aggre/',db_aggre,name='aggre'),
    path('index/',conn_db,name='home')

]