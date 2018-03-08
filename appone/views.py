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
    one_day_before = now - timedelta(days = 1)
    two_day_before = now - timedelta(days = 2)
    three_day_before = now - timedelta(days = 3)
    four_day_before = now - timedelta(days = 4)
    five_day_before = now - timedelta(days = 5)
    six_day_before = now - timedelta(days = 6)
    seven_day_before = now - timedelta(days = 7)
    eight_day_before = now - timedelta(days = 8)
    nine_day_before = now - timedelta(days = 9)
    ten_day_before = now - timedelta(days = 10)

    now = '2017-02-17'
    one_day_before = '2017-02-16'
    two_day_before = '2017-02-15'
    three_day_before = '2017-02-14'
    four_day_before = '2017-02-13'
    five_day_before = '2017-02-12'
    six_day_before = '2017-02-11'
    seven_day_before = '2017-02-10'
    eight_day_before = '2017-02-09'
    nine_day_before = '2017-02-08'
    ten_day_before = '2017-02-07'
    history_time=[now, one_day_before, two_day_before, three_day_before, four_day_before, five_day_before, six_day_before, seven_day_before, eight_day_before, nine_day_before, ten_day_before]
    low_threshold=0.995
    high_threshold=0.998
    ret_list=[]
    appone.db.connect()
    for x in range(10):
        ret_list.append(appone.db.executeSQL('''SELECT count(*) from LSTM_5VM45975_SINGLE
                                            WHERE ACT_TIME BETWEEN
                                            to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')
                                            AND PREDICTION BETWEEN %f AND %f
                                         '''% (history_time[x+1], history_time[x], low_threshold, high_threshold)))
        ret_list.append(appone.db.executeSQL('''SELECT count(*) from LSTM_5VM45975_SINGLE
                                            WHERE ACT_TIME BETWEEN
                                            to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')
                                          '''% (history_time[x+1], history_time[x])))

    
    
                                                                                       
    return JsonResponse(ret_list, safe=False)

def recordnumber(request):
    now = datetime.now()
    one_day_before = now - timedelta(days = 1)
    print("%s"%(one_day_before))
    two_day_before = now - timedelta(days = 2)
    three_day_before = now - timedelta(days = 3)
    four_day_before = now - timedelta(days = 4)
    five_day_before = now - timedelta(days = 5)
    six_day_before = now - timedelta(days = 6)
    seven_day_before = now - timedelta(days = 7)
    eight_day_before = now - timedelta(days = 8)
    nine_day_before = now - timedelta(days = 9)
    ten_day_before = now - timedelta(days = 10)
    ret_list=[]

    one_day_before = '20170122'
    two_day_before = '20170123'
    three_day_before = '20170124'
    four_day_before = '20170206'
    five_day_before = '20170207'
    six_day_before = '20170208'
    seven_day_before = '20170209'
    eight_day_before = '20170210'
    nine_day_before = '20170211'
    ten_day_before = '20170212'
    history_time=[one_day_before, two_day_before, three_day_before, four_day_before, five_day_before, six_day_before, seven_day_before, eight_day_before, nine_day_before, ten_day_before]
    agent =['WD-WCASZ0627345', 'S2A58BGQ', '5VM45975', 'Z1D3XB0A', 'Z4YAZWRB', 'Z4YAZVXM', 'Z4YAZW4W', 'Z4YAZVV4', '537TT03OT', '6VY152TL', 'Z4YAZTEF', 'Z4YAZTKF']
    appone.db.connect()
    for x in range(12):
        ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from %s WHERE AGENT_ID = '%s' " %('DL_TMSAPP_C0A80006_'+history_time[0], agent[x])))
        ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from %s WHERE AGENT_ID = '%s' " %('DL_TMSAPP_C0A80006_'+history_time[1], agent[x])))
        ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from %s WHERE AGENT_ID = '%s' " %('DL_TMSAPP_C0A80006_'+history_time[2], agent[x])))
        ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from %s WHERE AGENT_ID = '%s' " %('DL_TMSAPP_C0A80006_'+history_time[3], agent[x])))
        ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from %s WHERE AGENT_ID = '%s' " %('DL_TMSAPP_C0A80006_'+history_time[4], agent[x])))
        ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from %s WHERE AGENT_ID = '%s' " %('DL_TMSAPP_C0A80006_'+history_time[5], agent[x])))
        ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from %s WHERE AGENT_ID = '%s' " %('DL_TMSAPP_C0A80006_'+history_time[6], agent[x])))
        ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from %s WHERE AGENT_ID = '%s' " %('DL_TMSAPP_C0A80006_'+history_time[7], agent[x])))
        ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from %s WHERE AGENT_ID = '%s' " %('DL_TMSAPP_C0A80006_'+history_time[8], agent[x])))
        ret_list.append(appone.db.executeSQL("SELECT COUNT(*) from %s WHERE AGENT_ID = '%s' " %('DL_TMSAPP_C0A80006_'+history_time[9], agent[x])))                                                                                    
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

    # lstm = configure_lstm()
    # lstm.modelname = model_name
    # lstm.baseline = base_line
    # lstm.baselinevalue = base_linevalue
    # lstm.baselineunit = base_lineunit
    # lstm.train = check_box_list
    # lstm.flag = "0"
    # lstm.save()

    return HttpResponseRedirect('/addok/')

def addconfiguretodatabaseRelation(request):
    if request.method == "POST":
        operation_type = request.POST["relation_type"]
        user_name = request.POST["user_name"]
        min_support = request.POST["min_support"]
        min_confidence = request.POST["min_confidence"]
        model_name =request.POST["model2"]

    # re = configure_relation()
    # re.modelname = model_name
    # re.operationtype = operation_type
    # re.username = user_name
    # re.minsupport = min_support
    # re.minconfidence = min_confidence
    # re.flag = '0'
    # re.save()

    if operation_type == 'PeopleOperation':
        model_type = 'PO'
        agent_id = user_name
        table_name = 'PO' + '_' + user_name + '_' + min_support + '_' + min_confidence + '_' + model_name
    elif operation_type == 'OperationOperation':
        model_type = 'OO'
        agent_id =''
        table_name = 'OO' + '_' + min_support + '_' + min_confidence + '_' + model_name
    else:
        model_type = 'PP'
        agent_id =''
        table_name = 'PP' + '_' + min_support + '_' + min_confidence + '_' + model_name

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

