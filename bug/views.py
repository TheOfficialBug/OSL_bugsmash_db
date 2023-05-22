from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import person
import pymysql
from .forms import db_form,db_aggreagtion

data = person.objects.all()

def index(request):

    return render(request, 'index.html')


def conn_db(request):
    connection = pymysql.connect(
    host='db-mysql-blr1-69476-do-user-14046288-0.b.db.ondigitalocean.com',
    user='doadmin',
    password='AVNS_YijafuhF4slggX8rKO7',
    database='bugsmash',
    port=25060
)
    table_data = list(data.values())
    context = {
        'model_data': table_data,
        'db_response':'The db is not connected'
    }
    if connection:
        return render(request,"index.html",context)

def select(request):
    if request.method == "POST":
        form = db_form(request.POST)
        if form.is_valid():
            column_name = form.cleaned_data['column_name']
            print(column_name)
            try:
                field_values = person.objects.values(column_name).all()
                print(field_values.values())
            except Exception as e:
                return render(request,"db_form.html",{"error":str(e)})
            return render(request, 'db_form.html', {'field_values': field_values,'col':column_name})

      
    else:
        form = db_form()
    return render(request, "db_form.html", {'form': form})


def db_aggre(request):
    if request.method == "POST":
        db_agg = db_aggreagtion(request.POST)
        if db_agg.is_valid():
            column_name = db_agg.cleaned_data['column_name']
            fun_name = db_agg.cleaned_data['fun_name']
            field_values = person.objects.values(column_name)
            return HttpResponse([column_name,fun_name])
          

    db_agg = db_aggreagtion()
    return render(request,"aggre.html",{'form':db_agg})