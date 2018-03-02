# -*- coding: utf-8 -*-
import os
import cx_Oracle
import time
from datetime import datetime, timedelta
from django.db import connection,transaction
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from appone.models import configure_lstm
from appone.models import configure_relation
import appone.db
	
def prediction(request):
    now = datetime.now()
    one_month_before = now - timedelta(days = 500)
    ret_list=[]
    appone.db.connect()
    for x in range(10):
        ret_list.append(appone.db.executeSQL('''
                                                SELECT COUNT(*) from LSTM_5VM45975_SINGLE 
                                                WHERE INSERT_TIME BETWEEN 
                                                to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')
                                                AND PREDICTION BETWEEN %f AND %f
                                            ''' % (one_month_before.strftime('%Y-%m-%d'), now.strftime('%Y-%m-%d'), 0.1*x, 0.1*(x+1))))
    for x in range(10):
        ret_list.append(appone.db.executeSQL('''
                                                SELECT COUNT(*) from LSTM_S2A58BGQ_SINGLE 
                                                WHERE INSERT_TIME BETWEEN 
                                                to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')
                                                AND PREDICTION BETWEEN %f AND %f
                                            ''' % (one_month_before.strftime('%Y-%m-%d'), now.strftime('%Y-%m-%d'), 0.1*x, 0.1*(x+1))))

    for x in range(10):
        ret_list.append(appone.db.executeSQL('''
                                                SELECT COUNT(*) from LSTM_WDWCASZ0627345_SINGLE 
                                                WHERE INSERT_TIME BETWEEN 
                                                to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')
                                                AND PREDICTION BETWEEN %f AND %f
                                            ''' % (one_month_before.strftime('%Y-%m-%d'), now.strftime('%Y-%m-%d'), 0.1*x, 0.1*(x+1))))

    for x in range(10):
        ret_list.append(appone.db.executeSQL('''
                                                SELECT COUNT(*) from LSTM_Z1D3XB0A_SINGLE 
                                                WHERE INSERT_TIME BETWEEN 
                                                to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')
                                                AND PREDICTION BETWEEN %f AND %f
                                            ''' % (one_month_before.strftime('%Y-%m-%d'), now.strftime('%Y-%m-%d'), 0.1*x, 0.1*(x+1)))) 

    for x in range(10):
        ret_list.append(appone.db.executeSQL('''
                                                SELECT COUNT(*) from LSTM_Z4YAZWRB_SINGLE 
                                                WHERE INSERT_TIME BETWEEN 
                                                to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')
                                                AND PREDICTION BETWEEN %f AND %f
                                            ''' % (one_month_before.strftime('%Y-%m-%d'), now.strftime('%Y-%m-%d'), 0.1*x, 0.1*(x+1))))                                                                                       
    return JsonResponse(ret_list, safe=False)

def addconfiguretodatabase(request):
    if request.method == "POST":
        base_line = request.POST["base"]
        base_linevalue = request.POST["line"]
        base_lineunit = request.POST["baseunit"]
        model_name = request.POST["model"]
        check_box_list = request.POST.getlist('check_box_list') 

    lstm = configure_lstm()
    lstm.modelname = model_name
    lstm.baseline = base_line
    lstm.baselinevalue = base_linevalue
    lstm.baselineunit = base_lineunit
    lstm.train = check_box_list
    lstm.flag = "0"
    lstm.save()
    
    table_name = model_name + '_' + base_linevalue + '_' + base_lineunit
    table_name.replace('-', '_')
    appone.db.connect()
    appone.db.executeSQL('''
                            CREATE TABLE %s_RESULT 
                            (	
                                DATA VARCHAR2(1024 BYTE) PRIMARY KEY, 
	                            PREDICTION NUMBER(20,0), 
	                            ABNORMAL NUMBER(1,0), 
	                            INSERT_TIME DATE, 
                            )
                        ''' % table_name)

    return HttpResponseRedirect('/addok/')

def addconfiguretodatabaseRelation(request):
    if request.method == "POST":
        operation_type = request.POST["relation_type"]
        user_name = request.POST["user_name"]
        min_support = request.POST["min_support"]
        min_confidence = request.POST["min_confidence"]
        model_name =request.POST["model2"]

    re = configure_relation()
    re.modelname = model_name
    re.operationtype = operation_type
    re.username = user_name
    re.minsupport = min_support
    re.minconfidence = min_confidence
    re.flag = '0'
    re.save()

    if(operation_type == 'PeopleOperation'):
        table_name = operation_type + '_' + user_name + '_' + model_name
    else:
        table_name = operation_type + '_' + model_name
    table_name.replace('-', '_')
    appone.db.connect()
    appone.db.executeSQL('''
                            CREATE TABLE %s_RESULT 
                            (	
                                ITEMS VARCHAR2(1024 BYTE) PRIMARY KEY, 
	                            VALUE NUMBER(10,2), 
	                            TYPE NUMBER(1,0), 
	                            INSERT_TIME DATE, 
                            )
                        ''' % table_name)

    return HttpResponseRedirect('/addok2/')

# 返回页面addok
def addok(request):
    return render(request, 'addok.html')

def addok2(request):
    return render(request, 'addok2.html')    

def addconfigure(request):
    return render(request, 'configureadd.html')

def index(request):
    return render(request, 'first_interface.html')

def main(request):
    return render(request, 'index_real.html')

def simulate(request):
    return render(request, 'realtimecommunicate.html')

def single(request):
	return render(request, 'single_mesh.html')

def relation(request):
	return render(request, 'relation2.html')

def history(request):
    return render(request, 'history.html')

def taiyangxi(request):
	return render(request, 'taiyangxi_small.html')

def load_model(request):
    ret_list = []
    appone.db.connect()
    model_type = request.GET['model_type']
    baseline = request.GET['baseline']
    page = int(request.GET['page'])
    size = int(request.GET['size'])
    if model_type == None or baseline == None:
        return JsonResponse(ret_list, safe = False)
    
    if model_type == 'MODEL_PARAMETER':
        unit = 'BASELINE_UNIT'
        baseline = "'" + baseline + "'"
    elif model_type == 'FPGROWTH_PARAMETER':
        unit = 'MODEL_TYPE'
    ret_list.append(appone.db.executeSQL("SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'" % model_type))
    ret_list.append(appone.db.executeSQL('''
                                            SELECT * FROM
                                            (
                                                SELECT A.*
                                                FROM (SELECT * FROM %s WHERE %s = %s) A
                                                WHERE ROWNUM <= %d
                                            )   WHERE ROWNUM >= %d
                                        ''' % (model_type, unit, baseline, page*size, page*size-14)))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) FROM %s WHERE %s = %s" % (model_type, unit, baseline)))
    return JsonResponse(ret_list, safe = False)

def search(request):
    model = request.GET['model']
    start_date = request.GET['start_date']
    end_date = request.GET['end_date']
    page = int(request.GET['page'])
    size = int(request.GET['size'])
    ret_list = []
    ret_list.append(appone.db.executeSQL("SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'" % model.upper()))
    ret_list.append(appone.db.executeSQL('''
                                            SELECT * FROM
                                            (
                                                SELECT *
                                                FROM (SELECT * FROM %s WHERE INSERT_TIME BETWEEN to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD'))
                                                WHERE ROWNUM <= %d
                                            )   
                                                WHERE ROWNUM >= %d
                                        ''' % (model, start_date, end_date, page*size, page*size-14)))
    ret_list.append(appone.db.executeSQL('''SELECT COUNT(*) FROM %s WHERE INSERT_TIME BETWEEN 
                                           to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD') 
                                        ''' % (model, start_date, end_date)))                              
    return JsonResponse(ret_list, safe = False)

