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
# from appone.models import configure_lstm
# from appone.models import configure_relation
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

def recordnumber(request):
    now = datetime.now()
    one_month_before = now - timedelta(days = 500)
    ret_list=[]
    appone.db.connect()
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170122 WHERE AGENT_ID = 'WD-WCASZ0627345' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170123 WHERE AGENT_ID = 'WD-WCASZ0627345' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170124 WHERE AGENT_ID = 'WD-WCASZ0627345' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170206 WHERE AGENT_ID = 'WD-WCASZ0627345' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170207 WHERE AGENT_ID = 'WD-WCASZ0627345' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170208 WHERE AGENT_ID = 'WD-WCASZ0627345' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170209 WHERE AGENT_ID = 'WD-WCASZ0627345' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170210 WHERE AGENT_ID = 'WD-WCASZ0627345' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170211 WHERE AGENT_ID = 'WD-WCASZ0627345' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170212 WHERE AGENT_ID = 'WD-WCASZ0627345' "))

    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170122 WHERE AGENT_ID = 'S2A58BGQ' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170123 WHERE AGENT_ID = 'S2A58BGQ' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170124 WHERE AGENT_ID = 'S2A58BGQ' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170206 WHERE AGENT_ID = 'S2A58BGQ' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170207 WHERE AGENT_ID = 'S2A58BGQ' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170208 WHERE AGENT_ID = 'S2A58BGQ' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170209 WHERE AGENT_ID = 'S2A58BGQ' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170210 WHERE AGENT_ID = 'S2A58BGQ' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170211 WHERE AGENT_ID = 'S2A58BGQ' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170212 WHERE AGENT_ID = 'S2A58BGQ' "))  

    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170122 WHERE AGENT_ID = '5VM45975' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170123 WHERE AGENT_ID = '5VM45975' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170124 WHERE AGENT_ID = '5VM45975' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170206 WHERE AGENT_ID = '5VM45975' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170207 WHERE AGENT_ID = '5VM45975' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170208 WHERE AGENT_ID = '5VM45975' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170209 WHERE AGENT_ID = '5VM45975' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170210 WHERE AGENT_ID = '5VM45975' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170211 WHERE AGENT_ID = '5VM45975' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170212 WHERE AGENT_ID = '5VM45975' "))  

    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170122 WHERE AGENT_ID = 'Z1D3XB0A' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170123 WHERE AGENT_ID = 'Z1D3XB0A' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170124 WHERE AGENT_ID = 'Z1D3XB0A' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170206 WHERE AGENT_ID = 'Z1D3XB0A' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170207 WHERE AGENT_ID = 'Z1D3XB0A' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170208 WHERE AGENT_ID = 'Z1D3XB0A' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170209 WHERE AGENT_ID = 'Z1D3XB0A' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170210 WHERE AGENT_ID = 'Z1D3XB0A' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170211 WHERE AGENT_ID = 'Z1D3XB0A' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170212 WHERE AGENT_ID = 'Z1D3XB0A' "))   

    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170122 WHERE AGENT_ID = 'Z4YAZWRB' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170123 WHERE AGENT_ID = 'Z4YAZWRB' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170124 WHERE AGENT_ID = 'Z4YAZWRB' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170206 WHERE AGENT_ID = 'Z4YAZWRB' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170207 WHERE AGENT_ID = 'Z4YAZWRB' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170208 WHERE AGENT_ID = 'Z4YAZWRB' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170209 WHERE AGENT_ID = 'Z4YAZWRB' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170210 WHERE AGENT_ID = 'Z4YAZWRB' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170211 WHERE AGENT_ID = 'Z4YAZWRB' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170212 WHERE AGENT_ID = 'Z4YAZWRB' "))   

    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170122 WHERE AGENT_ID = 'Z4YAZVXM' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170123 WHERE AGENT_ID = 'Z4YAZVXM' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170124 WHERE AGENT_ID = 'Z4YAZVXM' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170206 WHERE AGENT_ID = 'Z4YAZVXM' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170207 WHERE AGENT_ID = 'Z4YAZVXM' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170208 WHERE AGENT_ID = 'Z4YAZVXM' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170209 WHERE AGENT_ID = 'Z4YAZVXM' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170210 WHERE AGENT_ID = 'Z4YAZVXM' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170211 WHERE AGENT_ID = 'Z4YAZVXM' "))
    ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from DL_TMSAPP_C0A80006_20170212 WHERE AGENT_ID = 'Z4YAZVXM' "))   
                                                                                    
    return JsonResponse(ret_list, safe=False)

def addconfiguretodatabase(request):
    if request.method == "POST":
        base_line = request.POST["base"]
        base_linevalue = request.POST["line"]
        base_lineunit = request.POST["baseunit"]
        model_name = request.POST["model"]
        check_box_list = request.POST.getlist('check_box_list') 
    
    if len(check_box_list) == 2:
        fields_study = check_box_list[0] + ',' + check_box_list[1]
    else:
        fields_study = ''
    
    if base_lineunit == 'single':
        baseline_values = base_linevalue
    else:
        baseline_values = 'all'
    
    table_name = 'agentid' + '_' + base_lineunit + '_' + base_linevalue + '_' + model_name
    table_name.replace('-', '')

    appone.db.connect()
    appone.db.executeSQL('''
                            CREATE TABLE %s_RESULT 
                            (	
                                DATA VARCHAR2(1024 BYTE) PRIMARY KEY, 
	                            PREDICTION NUMBER(10,5), 
	                            ABNORMAL NUMBER(1,0), 
	                            INSERT_TIME DATE, 
                                ACT_TIME DATE, 
                            )
                        ''' % table_name)
    
    appone.db.connect()
    appone.db.executeSQL('''
                            INSERT INTO MODEL_PARAMETER 
                            (	
                                MODEL_NAME, 
	                            FIELDS_STUDY, 
	                            FIELD_BASELINE, 
	                            BASELINE_VALUES, 
                                BASELINE_UNIT,
                                RESULT_TABLENAME,
                                INSERT_TIME,
                                DETECT_FLAG
                            ) VALUSES
                            (
                                '%s',
                                '%s',
                                '%s',
                                '%s',
                                '%s',
                                '%s',
                                sysdate,
                                0
                            )
                        ''' % (table_name, fields_study, base_line, baseline_values, base_lineunit, table_name + '_RESULT'))

    return HttpResponseRedirect('/addok/')

def addconfiguretodatabaseRelation(request):
    if request.method == "POST":
        operation_type = request.POST["relation_type"]
        user_name = request.POST["user_name"]
        min_support = request.POST["min_support"]
        min_confidence = request.POST["min_confidence"]
        model_name =request.POST["model2"]

    if operation_type == 'PeopleOperation':
        model_type = 'PO'
        agent_id = user_name
        table_name = 'PO' + '_' + user_name + '_' + model_name
    elif operation_type == 'OperationOperation':
        model_type = 'OO'
        agent_id =''
        table_name = 'OO' + '_' + model_name
    else:
        model_type = 'PP'
        agent_id =''
        table_name = 'PP' + '_' + model_name

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

    appone.db.connect()
    appone.db.executeSQL('''
                            INSERT INTO MODEL_PARAMETER 
                            (	
                                FPMODELNAME, 
	                            MINSUPPORT, 
	                            MINCONFIDENCE, 
	                            INPUTFILE, 
                                OUTPUTTABLE,
                                INSERT_TIME,
                                MODEL_TYPE,
                                AGENT_ID
                            ) VALUSES
                            (
                                '%s',
                                %f,
                                %f,
                                'fpgrowth/%s.csv',
                                '%s',
                                sysdate,
                                '%s',
                                '%s'
                            )
                        ''' % (table_name, float(min_support), float(min_confidence), table_name, table_name + '_RESULT', model_type, agent_id))

    return HttpResponseRedirect('/addok2/')

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
    ret_dict = {}
    appone.db.connect()
    model_type = request.GET['model_type']
    baseline = request.GET['baseline']
    page = int(request.GET['page'])
    size = int(request.GET['size'])

    if model_type == None or baseline == None:
        ret_dict['total'] = -1
        return JsonResponse(ret_dict)

    if model_type == 'MODEL_PARAMETER':
        unit = 'BASELINE_UNIT'
    elif model_type == 'FPGROWTH_PARAMETER':
        unit = 'MODEL_TYPE'
    ret_dict['total'] = appone.db.executeSQL("SELECT COUNT(*) FROM %s WHERE %s = '%s'" % (model_type, unit, baseline))
    ret_dict['head'] = appone.db.executeSQL("SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'" % model_type)
    ret_dict['body'] = appone.db.executeSQL('''
                                            SELECT * FROM
                                            (
                                                SELECT A.*
                                                FROM (SELECT * FROM %s WHERE %s = '%s') A
                                                WHERE ROWNUM <= %d
                                            )   WHERE ROWNUM >= %d
                                        ''' % (model_type, unit, baseline, page*size, page*size-14))
    
    return JsonResponse(ret_dict)

def search(request):
    ret_dict = {}
    model = request.GET['model']
    start_date = request.GET['start_date']
    end_date = request.GET['end_date']
    page = int(request.GET['page'])
    size = int(request.GET['size'])
    
    ret_dict['total'] = -1
    ret_dict['head'] = appone.db.executeSQL("SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s_RESULT'" % model.upper())
    ret_dict['body'] = appone.db.executeSQL('''
                                            SELECT * FROM
                                            (
                                                SELECT *
                                                FROM (SELECT * FROM %s_RESULT WHERE INSERT_TIME BETWEEN to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD'))
                                                WHERE ROWNUM <= %d
                                            )   WHERE ROWNUM >= %d
                                        ''' % (model, start_date, end_date, page*size, page*size-14))
    ret_dict['total'] = appone.db.executeSQL('''SELECT COUNT(*) FROM %s_RESULT WHERE INSERT_TIME BETWEEN 
                                           to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD') 
                                        ''' % (model, start_date, end_date))                              
    return JsonResponse(ret_dict)

