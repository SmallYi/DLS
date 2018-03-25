# -*- coding: utf-8 -*-
import os
import cx_Oracle
import time
from datetime import datetime, timedelta
from django.db import connection, transaction
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import appone.db


def thresold(request):
    appone.db.connect()
    agent = ['Z4YAZWRB', '537TT03OT', '5VM42727', '5VM452F4', '5VMTSDK5' ]
    max = appone.db.executeSQL("SELECT MAX(PREDICTION) FROM LSTM_ALL")
    min = appone.db.executeSQL("SELECT MIN(PREDICTION) FROM LSTM_ALL")
    center = appone.db.executeSQL(
        "SELECT CENTERS FROM MODEL_PARAMETER WHERE MODEL_NAME='LSTM_all' ")
    a = center[0][0].split(",")
    max_thresold = a[3]
    min_thresold = a[0]
    count_oo = appone.db.executeSQL("SELECT COUNT(*) FROM OO_RELATIONAPP")
    relation_oo = appone.db.executeSQL("SELECT COUNT(*) FROM OO_RELATIONAPP WHERE FPITEMS_COUNT > 0")
    e = count_oo[0][0]
    f = relation_oo[0][0]
    g = f/e
    count_pp = appone.db.executeSQL("SELECT COUNT(*) FROM PP_RELATIONPEOPLE")
    relation_pp = appone.db.executeSQL("SELECT COUNT(*) FROM PP_RELATIONPEOPLE WHERE FPITEMS_COUNT > 0")
    h = count_pp[0][0]
    i = relation_pp[0][0]
    j =i/h

    ret_list = []
    ret_list.append(max_thresold)
    ret_list.append(min_thresold)
    ret_list.append(j)
    ret_list.append(g)
    for k in range(5):
        count = appone.db.executeSQL("SELECT DISTINCT COUNT(*) FROM %s WHERE FPITEMS_COUNT >= 10*(SELECT MINSUPPORT FROM FPGROWTH_PARAMETER WHERE FPMODELNAME = '%s')" %('PO_'+agent[k]+'_RELATIONAPP','PO_'+agent[k]+'_20180314'))
        relation_app = appone.db.executeSQL("SELECT DISTINCT COUNT(*) FROM %s WHERE FPITEMS_COUNT >= 0" %('PO_'+agent[k]+'_RELATIONAPP'))
        b = count[0][0]
        c = relation_app[0][0]
        d = b/c
        print(d)
        ret_list.append(d)
    return JsonResponse(ret_list, safe=False)

def prediction(request):
    # history_time = []
    # now = datetime.now()
    # history_time.append(now)
    # for x in range(1,11):
    #     history_time.append((now - timedelta(days = x)).strftime('%Y-%m-%d'))

    history_time = ['2018-03-20',
        '2017-02-16', '2017-02-15', '2017-02-14', '2017-02-13', '2017-02-12',
        '2017-02-11', '2017-02-10', '2017-02-09', '2017-02-08', '2017-02-07'
    ]
    agent = [
        '5VM45975', 'S2A58BGQ', 'WDWCASZ0627345', 'Z1D3XB0A', 'Z4YAZWRB',
        '537TT03OT', 'Z4YAZTH6', 'P02703102649', 'Z4YAZTKF', 'Z4YAZVXM'
    ]
    ret_list1 = []
    ret_list2 = []
    length = 0
    maxtomin = 0
    min_prediction = 0
    appone.db.connect()
    for y in range(10):
        normalization = []
        a = []
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        length = appone.db.executeSQL("SELECT COUNT(*) FROM %s" %
                                      ('LSTM_' + agent[y] + '_SINGLE'))
        normalization = appone.db.executeSQL("SELECT PREDICTION FROM %s" %
                                             ('LSTM_' + agent[y] + '_SINGLE'))
        maxtomin = appone.db.executeSQL(
            "SELECT MAX(PREDICTION)-MIN(PREDICTION) FROM %s" %
            ('LSTM_' + agent[y] + '_SINGLE'))
        min_prediction = appone.db.executeSQL(
            "SELECT MIN(PREDICTION) FROM %s" %
            ('LSTM_' + agent[y] + '_SINGLE'))
        for i in range(length[0][0]):
            a.append(
                (normalization[i][0] - min_prediction[0][0]) / maxtomin[0][0])
        for j in range(length[0][0]):
             if (int(a[j]*10)<10):
                 b[int(a[j]*10)] += 1

        for j in range(10):
            b[j] /= length[0][0]
            ret_list2.append(b[j])

        for x in range(10):
            ret_list1.append(
                appone.db.executeSQL('''SELECT COUNT(*) from %s
                                            WHERE ACT_TIME BETWEEN
                                            to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')
                                            AND ABNORMAL=0
                                         ''' %
                                     ('LSTM_' + agent[y] + '_SINGLE',
                                      history_time[x + 1], history_time[x])))
            ret_list1.append(
                appone.db.executeSQL('''SELECT COUNT(*) FROM %s
                                            WHERE ACT_TIME BETWEEN
                                            to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')
                                          ''' %
                                     ('LSTM_' + agent[y] + '_SINGLE',
                                      history_time[x + 1], history_time[x])))

    ret_dict = {'abnormalratio': ret_list1, 'lstm': ret_list2}
    # for y in range(1):
    #     normalization = []
    #     normalization = appone.db.executeSQL("select prediction from %s"%('LSTM_'+agent[y]+'_SINGLE'))
    #     for x in range(10):
    #         ret_list2.append(appone.db.executeSQL('''SELECT count(*) from %s
    #                                         WHERE ACT_TIME BETWEEN
    #                                         to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')
    #                                         AND PREDICTION BETWEEN %f AND %f
    #                                      '''% ('LSTM_'+agent[y]+'_SINGLE', history_time[0], history_time[10], x, x+0.1)))
    return JsonResponse(ret_dict)

def recordnumber(request):
    # history_time = []
    # now = datetime.now()
    # history_time.append(now)
    # for x in range(1,11):
    #     history_time.append((now - timedelta(days = x)).strftime('%Y-%m-%d'))

    history_time = [
        '20170122', '20170123', '20170124', '20170206', '20170207', '20170208',
        '20170209', '20170210', '20170211', '20170212'
    ]
    agent = [
        'WD-WCASZ0627345', 'S2A58BGQ', '5VM45975', 'Z1D3XB0A', 'Z4YAZWRB',
        'Z4YAZVXM', 'Z4YAZW4W', 'Z4YAZVV4', '537TT03OT', '6VY152TL',
        'Z4YAZTEF', 'Z4YAZTKF'
    ]
    ret_list = []
    appone.db.connect()
    for x in range(12):
        for y in range(10):
            ret_list.append(
                appone.db.executeSQL(
                    "SELECT COUNT(*) FROM %s WHERE AGENT_ID = '%s' " %
                    ('DL_TMSAPP_C0A80006_' + history_time[y], agent[x])))
    return JsonResponse(ret_list, safe=False)


def addconfiguretodatabase(request):
    if request.method == "POST":
        base_line = request.POST["base"]
        #base_linevalue = request.POST["line"]
        base_lineunit = request.POST["baseunit"]
        model_name = request.POST["model"]
        check_box_list = request.POST.getlist('check_box_list')

    if len(check_box_list) == 2:
        fields_study = check_box_list[0] + ',' + check_box_list[1]
    else:
        fields_study = ''

    if base_lineunit == 'single':
        base_linevalue = request.POST["line"]
        table_name = 'agentid' + '_' + base_lineunit + '_' + base_linevalue + '_' + model_name
    else:
        base_linevalue = 'all'
        table_name = 'agentid' + '_' + base_lineunit + '_' + model_name
    table_name = table_name.replace('-', '')
    appone.db.connect()

    if len(appone.db.executeSQL('''
                        SELECT * FROM MODEL_PARAMETER WHERE MODEL_NAME = '%s'
                        ''' % (table_name))) == 1:
        #return JsonResponse('Model exists!', safe=False)
        return HttpResponseRedirect('/addfail/')

    print('''
                            CREATE TABLE %s 
                            (	
                                DATA VARCHAR2(1024 BYTE) PRIMARY KEY, 
	                            PREDICTION NUMBER(10,5), 
	                            ABNORMAL NUMBER(1,0), 
	                            INSERT_TIME DATE, 
                                ACT_TIME DATE
                            )
                        ''' % table_name)
    try:
        appone.db.executeSQL2('''
                            CREATE TABLE %s 
                            (	
                                DATA VARCHAR2(1024 BYTE) PRIMARY KEY, 
	                            PREDICTION NUMBER(10,5), 
	                            ABNORMAL NUMBER(1,0), 
	                            INSERT_TIME DATE, 
                                ACT_TIME DATE
                            )
                            ''' % table_name)
    except cx_Oracle.DatabaseError as e:
        print('Database except: ', e)

    print('''
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
                            ) VALUES
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
                        ''' % (table_name, fields_study, base_line,
                               base_linevalue, base_lineunit, table_name))
    try:
        appone.db.executeSQL2('''
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
                            ) VALUES
                            (
                                '%s',
                                '%s',
                                '%s',
                                '%s',
                                '%s',
                                '%s',
                                to_DATE('2017-03-03', 'YYYY-MM-DD'),
                                0
                            )
                            ''' % (table_name, fields_study, base_line,
                                    base_linevalue, base_lineunit, table_name))
    except cx_Oracle.DatabaseError as e:
        print('Database except: ', e)

    return HttpResponseRedirect('/addok/')


def addconfiguretodatabaseRelation(request):
    if request.method == "POST":
        operation_type = request.POST["relation_type"]
        #user_name = request.POST["user_name"]
        min_support = request.POST["min_support"]
        min_confidence = request.POST["min_confidence"]
        model_name = request.POST["model2"]

    if operation_type == 'PeopleOperation':
        user_name = request.POST["user_name"]
        model_type = 'PO'
        agent_id = user_name
        table_name = 'PO' + '_' + user_name + '_' + model_name
    elif operation_type == 'OperationOperation':
        model_type = 'OO'
        agent_id = ''
        table_name = 'OO' + '_' + model_name
    else:
        model_type = 'PP'
        agent_id = ''
        table_name = 'PP' + '_' + model_name
    table_name=table_name.replace('-', '')
    appone.db.connect()

    print('''
                            SELECT * FROM FPGROWTH_PARAMETER WHERE FPMODELNAME = '%s'
                            ''' % (table_name))
    if len(appone.db.executeSQL('''
                            SELECT * FROM FPGROWTH_PARAMETER WHERE FPMODELNAME = '%s'
                            ''' % (table_name))) == 1:
        #return JsonResponse('Model exists!', safe=False)
        return HttpResponseRedirect('/addfail/')

    print('''
                            CREATE TABLE %s 
                            (	
                                ITEMS VARCHAR2(1024 BYTE) PRIMARY KEY, 
	                            VALUE NUMBER(10,2), 
	                            TYPE NUMBER(1,0), 
	                            INSERT_TIME DATE
                            )
                        ''' % table_name)
    appone.db.executeSQL2('''
                            CREATE TABLE %s 
                            (	
                                ITEMS VARCHAR2(1024 BYTE) PRIMARY KEY, 
	                            VALUE NUMBER(10,2), 
	                            TYPE NUMBER(1,0), 
	                            INSERT_TIME DATE
                            )
                        ''' % table_name)

    print('''
                            INSERT INTO FPGROWTH_PARAMETER 
                            (	
                                FPMODELNAME, 
	                            MINSUPPORT, 
	                            MINCONFIDENCE, 
	                            INPUTFILE, 
                                OUTPUTTABLE,
                                INSERT_TIME,
                                MODEL_TYPE,
                                AGENT_ID
                            ) VALUES
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
                        ''' % (table_name, float(min_support),
                               float(min_confidence), table_name, table_name,
                               model_type, agent_id))
    appone.db.executeSQL2('''
                            INSERT INTO FPGROWTH_PARAMETER 
                            (	
                                FPMODELNAME, 
	                            MINSUPPORT, 
	                            MINCONFIDENCE, 
	                            INPUTFILE, 
                                OUTPUTTABLE,
                                INSERT_TIME,
                                MODEL_TYPE,
                                AGENT_ID
                            ) VALUES
                            (
                                '%s',
                                %f,
                                %f,
                                'fpgrowth/%s.csv',
                                '%s',
                                to_DATE('2017-03-03', 'YYYY-MM-DD'),
                                '%s',
                                '%s'
                            )
                        ''' % (table_name, float(min_support),
                               float(min_confidence), table_name, table_name,
                               model_type, agent_id))

    return HttpResponseRedirect('/addok2/')

def addok(request):
    return render(request, 'addok.html')

def addok2(request):
    return render(request, 'addok2.html')

def addfail(request):
    return render(request, 'addfail.html')

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
    ret_dict['total'] = appone.db.executeSQL(
        "SELECT COUNT(*) FROM %s WHERE %s = '%s'" % (model_type, unit,
                                                     baseline))
    ret_dict['head'] = appone.db.executeSQL(
        "SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'" %
        model_type)
    ret_dict['body'] = appone.db.executeSQL('''
                                            SELECT * FROM
                                            (
                                                SELECT A.*, ROWNUM RN
                                                FROM (SELECT * FROM %s WHERE %s = '%s') A
                                                WHERE ROWNUM <= %d
                                            )   WHERE RN >= %d
                                        ''' % (model_type, unit, baseline,
                                               page * size, page * size - 14))

    return JsonResponse(ret_dict)

def load_agent(request):
    ret_dict = {}
    appone.db.connect()
    ret_dict['agent'] = appone.db.executeSQL('''
                                            SELECT TERM_AGENT_ID FROM CP_TERMINAL_INFO
                                            ''')
    return JsonResponse(ret_dict)

def search(request):
    ret_dict = {}
    model = request.GET['model']
    start_date = request.GET['start_date']
    end_date = request.GET['end_date']
    page = int(request.GET['page'])
    size = int(request.GET['size'])

    if model == None:
        ret_dict['total'] = -1
        return JsonResponse(ret_dict)
    ret_dict['head'] = appone.db.executeSQL(
        "SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'" %
        model.upper())
    ret_dict['body'] = appone.db.executeSQL('''
                                            SELECT * FROM
                                            (
                                                SELECT A.*, ROWNUM RN
                                                FROM (SELECT * FROM %s WHERE INSERT_TIME BETWEEN to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')) A
                                                WHERE ROWNUM <= %d
                                            )   WHERE RN >= %d
                                        ''' % (model, start_date, end_date,
                                               page * size, page * size - 14))
    ret_dict['total'] = appone.db.executeSQL(
        '''SELECT COUNT(*) FROM %s WHERE INSERT_TIME BETWEEN 
                                           to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD') 
                                        ''' % (model, start_date, end_date))
    return JsonResponse(ret_dict)

def analyse_lstm(request):
    model = request.GET['model']
    chart = request.GET['chart']

    if chart == '-1':
        return render(request, 'analyse_lstm.html', {'model': model})

    ret_dict = {}
    ab = request.GET['ab']
    page = int(request.GET['page'])
    size = int(request.GET['size'])
    if ab == 'all':
        ab_select = ''
    else:
        ab_select = 'WHERE ABNORMAL = %s' % ab
    appone.db.connect()

    model = 'LSTM_' + model + '_SINGLE'

    ret_dict['total'] = -1
    ret_dict['head'] = appone.db.executeSQL(
        "SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'" %
        model.upper())
    ret_dict['body'] = appone.db.executeSQL('''
                                            SELECT * FROM
                                            (
                                                SELECT A.*, ROWNUM RN
                                                FROM (SELECT * FROM %s %s) A
                                                WHERE ROWNUM <= %d
                                            )   WHERE RN >= %d
                                            ''' %
                                            (model, ab_select, page * size,
                                             page * size - 14))
    ret_dict['total'] = appone.db.executeSQL('''SELECT COUNT(*) FROM %s %s
                                            ''' % (model, ab_select))
    if chart == '0':
        return JsonResponse(ret_dict)

    bar_list = []
    for x in range(20):
        bar_tmp = appone.db.executeSQL('''
                                            SELECT COUNT(*) FROM %s
                                                WHERE PREDICTION BETWEEN %f AND %f
                                            ''' % (model, 0.05 * x,
                                                   0.05 * x + 0.05))
        bar_list.append(bar_tmp[0][0])
    ret_dict['bar'] = bar_list

    code_list = appone.db.executeSQL('''
                                    SELECT KEY, CODE FROM SIGNALFIELD_CODE
                                        WHERE FIELD_NAME = 'APP_NAME'
                                    ''')
    code_dict = {}
    for e in code_list:
        code_dict[e[0]] = e[1]
    ret_sql = appone.db.executeSQL('''
                                    SELECT ACT_TIME, DATA FROM %s
                                ''' % (model))

    scatter_list = []
    for record in ret_sql:
        x = record[0].hour * 60 + record[0].minute
        y = code_dict.get(record[1].split(' ')[2], -1)
        # change the 2
        if y != -1:
            scatter_list.append((x, y))
    ret_dict['scatter'] = scatter_list

    return JsonResponse(ret_dict)

def analyse_fp(request):
    model = request.GET['model']
    chart = request.GET['chart']

    if chart == '-1':
        return render(request, 'analyse_fp.html', {'model': model})

    ret_dict = {}
    page = int(request.GET['page'])
    size = int(request.GET['size'])
    appone.db.connect()

    data_tbname = 'PO_' + model + '_20180314'
    ret_dict['total'] = -1
    ret_dict['head'] = appone.db.executeSQL(
        "SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'" %
        data_tbname.upper())
    ret_dict['body'] = appone.db.executeSQL('''
                                            SELECT * FROM
                                            (
                                                SELECT A.*, ROWNUM RN
                                                FROM (SELECT * FROM %s) A
                                                WHERE ROWNUM <= %d
                                            )   WHERE RN >= %d
                                            ''' % (data_tbname, page * size,
                                                   page * size - 14))
    ret_dict['total'] = appone.db.executeSQL('''SELECT COUNT(*) FROM %s 
                                            ''' % (data_tbname))
    if chart == '0':
        return JsonResponse(ret_dict)

    # bar_list = []
    # for x in range(1, 11):
    #     bar_tmp = appone.db.executeSQL('''
    #                                         SELECT COUNT(*) FROM %s
    #                                             WHERE VALUE = %d AND TYPE = 1
    #                                         ''' % (data_tbname, x))
    #     bar_list.append(bar_tmp[0][0])
    # ret_dict['bar'] = bar_list

    bar1_xdata = []
    bar1_ydata = []
    bar1_tbname = 'PO_' + model + '_RELATIONAPP'
    ret_sql = appone.db.executeSQL('''
                                    SELECT MAX(FPITEMS_COUNT), MIN(FPITEMS_COUNT) FROM %s
                                    ''' % (bar1_tbname))
    max_count = ret_sql[0][0]
    min_count = ret_sql[0][1]
    step_count = (max_count - min_count) / 10
    for i in range(0,11):
        bar1_xdata.append(min_count + step_count * i)
        bar1_xdata[i] = round(bar1_xdata[i])
    for i in range(10):
        ret_sql = appone.db.executeSQL('''
                                        SELECT COUNT(*) FROM %s 
                                            WHERE FPITEMS_COUNT BETWEEN %d AND %d
                                        ''' % (bar1_tbname, bar1_xdata[i], bar1_xdata[i+1]))
        bar1_ydata.append(ret_sql[0][0])    
    ret_dict['bar1_xdata'] = bar1_xdata
    ret_dict['bar1_ydata'] = bar1_ydata

    bar2_xdata = []
    bar2_ydata = []
    date_list = []
    bar2_tbname = 'PO_' + model + '_RELATIONAPP'
    ret_sql = appone.db.executeSQL('''
                                        SELECT DISTINCT ACT_DATE FROM %s
                                        ''' % (bar2_tbname))
    for x in ret_sql: 
        date_list.append(x[0])
    date_list.sort()
    for d in date_list:
        r_num = appone.db.executeSQL('''
                                        SELECT COUNT(*) FROM %s 
                                            WHERE ACT_DATE = to_DATE('%s', 'YYYY-MM-DD')
                                                AND FPITEMS_COUNT <> 0
                                        ''' % (bar2_tbname, d.strftime('%Y-%m-%d')))
        a_num = appone.db.executeSQL('''
                                        SELECT COUNT(*) FROM %s 
                                            WHERE ACT_DATE = to_DATE('%s', 'YYYY-MM-DD')
                                        ''' % (bar2_tbname, d.strftime('%Y-%m-%d')))
        bar2_xdata.append(d.strftime('%Y-%m-%d'))
        bar2_ydata.append(r_num[0][0]/a_num[0][0])
    ret_dict['bar2_xdata'] = bar2_xdata
    ret_dict['bar2_ydata'] = bar2_ydata

    return JsonResponse(ret_dict)

    # pie_list = []
    # date_list = []
    # pie_tbname = 'PO_' + model + '_RELATIONAPP'
    # ret_sql = appone.db.executeSQL('''
    #                                     SELECT DISTINCT ACT_DATE FROM %s
    #                                     ''' % (pie_tbname))
    # for x in ret_sql: 
    #     date_list.append(x[0])
    # date_list.sort()
    # for d in date_list:
    #     r_num = appone.db.executeSQL('''
    #                                     SELECT COUNT(*) FROM %s 
    #                                         WHERE ACT_DATE = to_DATE('%s', 'YYYY-MM-DD')
    #                                             AND FPITEMS_COUNT <> 0
    #                                     ''' % (pie_tbname, d.strftime('%Y-%m-%d')))
    #     a_num = appone.db.executeSQL('''
    #                                     SELECT COUNT(*) FROM %s 
    #                                         WHERE ACT_DATE = to_DATE('%s', 'YYYY-MM-DD')
    #                                     ''' % (pie_tbname, d.strftime('%Y-%m-%d')))
    #     pie_list.append({'value': r_num[0][0]/a_num[0][0], 'name': d.strftime('%Y-%m-%d')})
    # ret_dict['pie'] = pie_list
