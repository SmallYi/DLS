# -*- coding: utf-8 -*-
import os
import time
import math
import cx_Oracle
from datetime import datetime, timedelta
from django.db import connection, transaction
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from appone.db import oracle


def thresold(request):
    db = oracle()
    agent = ['Z4YAZWRB', '537TT03OT', '5VM42727', '5VM452F4', '5VMTSDK5']
    center = db.select("SELECT CENTERS FROM MODEL_PARAMETER WHERE MODEL_NAME='LSTM_all' ")
    a = center[0][0].split(",")
    max_thresold = a[3]
    min_thresold = a[0]
    count_oo = db.select('''
        SELECT * FROM (
            SELECT appname, people_count/total as ratio FROM (
                SELECT * FROM OO_20180314_R cross join (
                    SELECT count(people_count) as total,act_date
                        FROM OO_20180314_R group by act_date))
                    order by ratio)
                where rownum<=5''')
    count_pp = db.select('''
        SELECT * FROM (
            SELECT PEOPLENAME,count(*) FROM (
                SELECT PEOPLENAME, APP_COUNT, ACT_DATE, APP_TOTAL FROM PP_20180314_R
                    where app_count < app_total*0.1)  
                group by PEOPLENAME order by count(*) desc)
            where rownum<=5''')

    ret_list = []
    ret_list.append(max_thresold)
    ret_list.append(min_thresold)
    ret_list.append(count_pp)
    ret_list.append(count_oo)
    for k in range(5):
        count = db.select(
            "SELECT DISTINCT COUNT(*) FROM %s WHERE FPITEMS_COUNT >= 10*(SELECT MINSUPPORT FROM FPGROWTH_PARAMETER WHERE FPMODELNAME = '%s')"
            % ('PO_' + agent[k] + '_20180314_R', 'PO_' + agent[k] + '_20180314'))
        relation_app = db.select(
            "SELECT DISTINCT COUNT(*) FROM %s WHERE FPITEMS_COUNT >= 0" 
            % ('PO_' + agent[k] + '_20180314_R'))
        b = count[0][0]
        c = relation_app[0][0]
        d = b / c
        ret_list.append(d)
    return JsonResponse(ret_list, safe=False)


def prediction(request):
    # history_time = []
    # now = datetime.now()
    # history_time.append(now)
    # for x in range(1,11):
    #     history_time.append((now - timedelta(days = x)).strftime('%Y-%m-%d'))
    db = oracle()
    history_time = [
        '2018-03-20', '2017-02-16', '2017-02-15', '2017-02-14', '2017-02-13',
        '2017-02-12', '2017-02-11', '2017-02-10', '2017-02-09', '2017-02-08',
        '2017-02-07'
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
    for y in range(10):
        normalization = []
        a = []
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        length = db.select("SELECT COUNT(*) FROM %s" % ('LSTM_' + agent[y] + '_SINGLE'))
        normalization = db.select("SELECT PREDICTION FROM %s" % ('LSTM_' + agent[y] + '_SINGLE'))
        maxtomin = db.select("SELECT MAX(PREDICTION)-MIN(PREDICTION) FROM %s" % ('LSTM_' + agent[y] + '_SINGLE'))
        min_prediction = db.select("SELECT MIN(PREDICTION) FROM %s" % ('LSTM_' + agent[y] + '_SINGLE'))
        for i in range(length[0][0]):
            a.append((normalization[i][0] - min_prediction[0][0]) / maxtomin[0][0])
        for j in range(length[0][0]):
            if (int(a[j] * 10) < 10):
                b[int(a[j] * 10)] += 1

        for j in range(10):
            b[j] /= length[0][0]
            ret_list2.append(b[j])

        for x in range(10):
            ret_list1.append(
                db.select('''
                    SELECT COUNT(*) from %s
                        WHERE ACT_TIME BETWEEN to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')
                            AND ABNORMAL=0''' %
                                ('LSTM_' + agent[y] + '_SINGLE', history_time[x + 1], history_time[x])))
            ret_list1.append(
                db.select('''
                    SELECT COUNT(*) FROM %s 
                        WHERE ACT_TIME BETWEEN to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')''' %
                            ('LSTM_' + agent[y] + '_SINGLE', history_time[x + 1], history_time[x])))

    ret_dict = {'abnormalratio': ret_list1, 'lstm': ret_list2}
    # for y in range(1):
    #     normalization = []
    #     normalization = db.select("select prediction from %s"%('LSTM_'+agent[y]+'_SINGLE'))
    #     for x in range(10):
    #         ret_list2.append(db.select('''SELECT count(*) from %s
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

    db = oracle()
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
    for x in range(12):
        for y in range(10):
            ret_list.append(
                db.select(
                    "SELECT COUNT(*) FROM %s WHERE AGENT_ID = '%s' " %
                    ('DL_TMSAPP_C0A80006_' + history_time[y], agent[x])))
    return JsonResponse(ret_list, safe=False)

def guard(request):
    # history_time = []
    # now = datetime.now()
    # history_time.append(now)
    # for x in range(1,11):
    #     history_time.append((now - timedelta(days = x)).strftime('%Y-%m-%d'))

    db = oracle()
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
    for x in range(12):
        for y in range(10):
            record = db.select("SELECT COUNT(*) FROM %s WHERE agent_id='%s'" % ('DL_TMSAPP_C0A80006_' + history_time[y], agent[x]))
            total = db.select("SELECT COUNT(*) FROM %s"% ('DL_TMSAPP_C0A80006_' + history_time[y]))
            a=record[0][0]
            b=total[0][0]
            if(b==0):
                c=0
            else:
                c=a/b
            ret_list.append(c)
    return JsonResponse(ret_list, safe=False)


def add_LSTM(request):
    base_line = request.POST.get("base", None)
    base_lineunit = request.POST.get("baseunit", None)
    model_name = request.POST.get("model", None)
    check_box_list = request.POST.getlist('check_box_list')

    if base_line == '' or base_lineunit == '' or model_name == '' or len(check_box_list) == 0:
        return render(request, 'addfail.html', {'reason': '参数缺失'})

    check_box_len = len(check_box_list)
    fields_study = ''
    for i in range(check_box_len):
        if i == 0:
            fields_study += check_box_list[i]
        else:
            fields_study += (',' + check_box_list[i])

    if base_lineunit == 'single':
        base_linevalue = request.POST["line"]
        table_name = 'NN' + '_' + base_linevalue + '_' + model_name + '_S' 
    elif base_lineunit == 'all':
        base_linevalue = 'all'
        table_name = 'NN' + '_' + model_name + '_A'
    
    table_name += '_N'
    table_name = table_name.replace('-', '')
    table_name = table_name.upper()

    db = oracle()
    if len(
            db.select('''
                        SELECT * FROM MODEL_PARAMETER WHERE MODEL_NAME = '%s'
                        ''' % (table_name))) >= 1:
        return render(request, 'addfail.html', {'reason': '模型重复'})
    db.alter('''
                CREATE TABLE %s 
                (	
                    DATA VARCHAR2(1024 BYTE) PRIMARY KEY, 
                    PREDICTION NUMBER(10,5), 
                    ABNORMAL NUMBER(1,0), 
                    INSERT_TIME DATE, 
                    ACT_TIME DATE
                )
                ''' % table_name)

    db.alter('''
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

    return render(request, 'addok.html')


def add_GUARD(request):
    data_format = request.POST.get("foramt", None)
    name = request.POST.get("name", None)
    unit = request.POST.get("unit", None)
    training_fields = request.POST.get("training_fields", None)
    label_fields = request.POST.get("label_field", None)
    date_fields = request.POST.get("date_field", None)
    model_name = request.POST.get("model3", None)

    if data_format == '' or name == '' or unit == '' or training_fields == '' or label_fields == '' or date_fields == '' or model_name == '':
        return render(request, 'addfail.html', {'reason': '参数缺失'})

    table_name = 'NN_' + name + '_' + model_name + '_A_G'
    table_name = table_name.replace('-', '')
    table_name = table_name.upper()

    db = oracle()
    if len(
            db.select('''
                        SELECT * FROM GUARD_PARAMETER WHERE MODEL_NAME = '%s'
                        ''' % (table_name))) >= 1:
        return render(request, 'addfail.html', {'reason': '模型重复'})
    db.alter('''
                CREATE TABLE %s 
                (	
                    DATA VARCHAR2(1024 BYTE) PRIMARY KEY, 
                    PREDICTION NUMBER(10,5), 
                    ABNORMAL NUMBER(1,0), 
                    INSERT_TIME DATE, 
                    ACT_TIME DATE
                )
                ''' % table_name)

    db.alter('''
                INSERT INTO GUARD_PARAMETER 
                (	
                    MODEL_NAME, 
                    DESCRIPTION, 
                    FORMAT, 
                    NAME, 
                    UNIT,
                    TRAINING_FIELDS,
                    LABEL_FIELD,
                    DATE_FIELD
                ) VALUES
                (
                    '%s',
                    '%s',
                    '%s',
                    '%s',
                    '%s',
                    '%s',
                    '%s',
                    '%s'
                )
                ''' % (table_name, model_name, data_format, name, unit, 
                        training_fields, label_fields, date_fields))

    return render(request, 'addok.html')


def add_Ralation(request):
    operation_type = request.POST.get("relation_type", None)
    min_support = request.POST.get("min_support", None)
    min_confidence = request.POST.get("min_confidence", None)
    model_name = request.POST.get("model2", None)

    if operation_type == '' or min_support == '' or min_confidence == '' or model_name == '':
        return render(request, 'addfail.html', {'reason': '参数缺失'})

    if operation_type == 'PeopleOperation':
        user_name = request.POST.get("user_name", None)
        if user_name == '':
            return render(request, 'addfail.html', {'reason': '参数缺失'})
        model_type = 'PO'
        agent_id = user_name
        table_name = 'PO' + '_' + user_name + '_' + model_name
    elif operation_type == 'OperationOperation':
        model_type = 'OO'
        agent_id = 'ALL'
        table_name = 'OO' + '_' + model_name
    elif operation_type == 'PeoplePeople':
        model_type = 'PP'
        agent_id = 'ALL'
        table_name = 'PP' + '_' + model_name
    else:
        return render(request, 'addfail.html', {'reason': '参数错误'})
    table_name = table_name.replace('-', '')
    table_name = table_name.upper()

    db = oracle()
    if len(
            db.select('''
                        SELECT * FROM FPGROWTH_PARAMETER 
                            WHERE FPMODELNAME = '%s' AND MINSUPPORT = %f AND MINCONFIDENCE = %f
                        ''' % (table_name, float(min_support),
                                float(min_confidence)))) >= 1:
        return render(request, 'addfail.html', {'reason': '模型重复'})
    db.alter('''
                CREATE TABLE %s 
                (	
                    ITEMS VARCHAR2(1024 BYTE) PRIMARY KEY, 
                    VALUE NUMBER(10,2), 
                    TYPE NUMBER(1,0), 
                    INSERT_TIME DATE
                )
            ''' % table_name)
    db.alter('''
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

    return render(request, 'addok.html')


def add_model(request):
    return render(request, 'add_model.html')


def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')


def simulate(request):
    return render(request, 'realtimecommunicate.html')


def lstm(request):
    return render(request, 'lstm.html')


def relation(request):
    return render(request, 'relation.html')


def history(request):
    return render(request, 'history.html')


def galaxy(request):
    return render(request, 'galaxy.html')


def lstm_guard(request):
    model = request.GET.get('model', None)
    if model == None:
        return render(request, 'lstm_guard.html', {'model': 'test'})
    else:
        return render(request, 'lstm_guard.html', {'model': model})


def main_guard(request):
    model = request.GET.get('model', None)
    if model == None:
        return render(request, 'main_guard.html', {'model': 'test'})
    else:
        return render(request, 'main_guard.html', {'model': model})


def load_model(request):
    ret_dict = {}
    model_type = request.GET.get('model_type', None)
    baseline = request.GET.get('baseline', None)
    page = request.GET.get('page', None)
    size = request.GET.get('size', None)

    if model_type == None or baseline == None or page == None or size == None:
        return JsonResponse({})

    try:
        page = int(page)
        size = int(size)
    except:
        return JsonResponse({})

    if model_type == 'MODEL_PARAMETER':
        unit = 'BASELINE_UNIT'
    elif model_type == 'FPGROWTH_PARAMETER':
        unit = 'MODEL_TYPE'
    else:
        return JsonResponse({})

    db = oracle() 
    ret_sql = db.select('''
                            SELECT COUNT(*) FROM %s WHERE %s = '%s'
                            ''' % (model_type, unit, baseline))
    ret_dict['total'] = ret_sql[0][0]
    ret_dict['head'] = db.select('''
                                    SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'
                                    ''' % model_type)
    ret_dict['body'] = db.select('''
                                    SELECT * FROM
                                    (
                                        SELECT A.*, ROWNUM RN
                                        FROM (SELECT * FROM %s WHERE %s = '%s') A
                                        WHERE ROWNUM <= %d
                                    )   WHERE RN >= %d
                                    ''' %
                                    (model_type, unit, baseline,
                                        page * size, page * size - size + 1))

    return JsonResponse(ret_dict)


def load_agent(request):
    try:
        db = oracle()
        ret_dict = {}
        ret_dict['agent'] = db.select('''
                                    SELECT TERM_AGENT_ID FROM CP_TERMINAL_INFO
                                    ''')
    except cx_Oracle.DatabaseError as e:
        print(e)
        ret_dict['guard'] = []
    return JsonResponse(ret_dict)


def load_guard(request):
    try:
        db = oracle()
        ret_dict = {}
        ret_dict['guard'] = db.select('''
                                    SELECT MODEL_NAME FROM GUARD_PARAMETER
                                    ''')
    except cx_Oracle.DatabaseError as e:
        print(e)
        ret_dict['guard'] = []
    return JsonResponse(ret_dict)


def search(request):
    ret_dict = {}
    model_type = request.GET.get('model_type', None)
    model = request.GET.get('model', None)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    page = request.GET.get('page', None)
    size = request.GET.get('size', None)

    if model_type == None or model_type == None or model_type == None \
        or model_type == None or model_type == None or model_type == None:
        return JsonResponse({})

    try:
        page = int(page)
        size = int(size)
    except:
        return JsonResponse({})

    if model_type == 'MODEL_PARAMETER':
        mdname = 'MODEL_NAME'
        tbname = 'RESULT_TABLENAME'
    elif model_type == 'FPGROWTH_PARAMETER':
        mdname = 'FPMODELNAME'
        tbname = 'OUTPUTTABLE'
    else:
        return JsonResponse({})

    db = oracle()
    table_name = db.select('''
                            SELECT %s FROM %s WHERE %s = '%s'
                            ''' % (tbname, model_type, mdname,
                                    model))
    if table_name == None:
        return JsonResponse({})
    table_name = table_name[0][0]
    table_name = table_name.upper()
    if model_type == 'FPGROWTH_PARAMETER':
        table_name = table_name + '_R'

    ret_dict['head'] = db.select('''
                                    SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'
                                    ''' % table_name)
    ret_dict['body'] = db.select('''
                                    SELECT * FROM
                                    (
                                        SELECT A.*, ROWNUM RN
                                        FROM (SELECT * FROM %s WHERE INSERT_TIME BETWEEN to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD')) A
                                        WHERE ROWNUM <= %d
                                    )   WHERE RN >= %d
                                    ''' %
                                        (table_name, start_date, end_date,
                                            page * size, page * size - size + 1))
    ret_sql = db.select('''
                            SELECT COUNT(*) FROM %s WHERE INSERT_TIME BETWEEN 
                            to_DATE('%s', 'YYYY-MM-DD') and to_DATE('%s', 'YYYY-MM-DD') 
                            ''' % (table_name, start_date,
                                    end_date))
    ret_dict['total'] = ret_sql[0][0]

    return JsonResponse(ret_dict)


def analyse_lstm(request):
    ret_dict = {}
    model = request.GET.get('model', None)
    chart = request.GET.get('chart', None)
    if model == None or chart == None:
        return JsonResponse({})

    if chart == '-1':
        return render(request, 'analyse_lstm.html', {'model': model})

    ab = request.GET.get('ab', None)
    page = request.GET.get('page', None)
    size = request.GET.get('size', None)
    if ab == None or page == None or size == None:
        return JsonResponse({})

    try:
        page = int(page)
        size = int(size)
    except:
        return JsonResponse({})
    
    if ab == 'all':
        ab_select = ''
    elif ab == '0' or ab == '1':
        ab_select = 'WHERE ABNORMAL = %s' % ab
    else: 
        return JsonResponse({})
    model = 'LSTM_' + model + '_SINGLE'
    model = model.upper()

    db = oracle()
    ret_dict['head'] = db.select('''
                                    SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'
                                    ''' % model)
    ret_dict['body'] = db.select('''
                                    SELECT * FROM
                                    (
                                        SELECT A.*, ROWNUM RN
                                        FROM (SELECT * FROM %s %s) A
                                        WHERE ROWNUM <= %d
                                    )   WHERE RN >= %d
                                    ''' %
                                    (model, ab_select, page * size,
                                        page * size - size + 1))
    ret_sql = db.select('''
                            SELECT COUNT(*) FROM %s %s
                            ''' % (model, ab_select))
    ret_dict['total'] = ret_sql[0][0]
    if chart == '0':
        return JsonResponse(ret_dict)

    bar_list = []
    for x in range(20):
        bar_tmp = db.select('''
                                SELECT COUNT(*) FROM %s
                                    WHERE PREDICTION BETWEEN %f AND %f
                                ''' % (model, 0.05 * x,
                                        0.05 * x + 0.05))
        bar_list.append(bar_tmp[0][0])
    ret_dict['bar'] = bar_list

    code_list = db.select('''
                            SELECT KEY, CODE FROM SIGNALFIELD_CODE
                                WHERE FIELD_NAME = 'APP_NAME'
                            ''')
    code_dict = {}
    for e in code_list:
        code_dict[e[0]] = e[1]
    ret_sql = db.select('''
                            SELECT ACT_TIME, DATA FROM %s
                            ''' % (model))

    scatter_list = []
    for record in ret_sql:
        x = record[0].hour * 60 + record[0].minute
        y = code_dict.get(record[1].split(' ')[2], -1)
        if y != -1:
            scatter_list.append((x, y))
    ret_dict['scatter'] = scatter_list

    if chart == '1':
        return JsonResponse(ret_dict)
    
    return JsonResponse({})


def analyse_lstm_g(request):
    ret_dict = {}
    model = request.GET.get('model', None)
    chart = request.GET.get('chart', None)
    if model == None or chart == None:
        return JsonResponse({})

    if chart == '-1':
        return render(request, 'analyse_lstm_g.html', {'model': model})

    ab = request.GET.get('ab', None)
    page = request.GET.get('page', None)
    size = request.GET.get('size', None)
    if ab == None or page == None or size == None:
        return JsonResponse({})

    try:
        page = int(page)
        size = int(size)
    except:
        return JsonResponse({})
    
    if ab == 'all':
        ab_select = ''
    elif ab == '0' or ab == '1':
        ab_select = 'WHERE ABNORMAL = %s' % ab
    else: 
        return JsonResponse({})
    model = 'NN_' + model + '_A_G'
    model = model.upper()

    db = oracle()
    try:
        ret_dict['head'] = db.select('''
                                    SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'
                                    ''' % model)
        ret_dict['body'] = db.select('''
                                    SELECT * FROM
                                    (
                                        SELECT A.*, ROWNUM RN
                                        FROM (SELECT * FROM %s %s) A
                                        WHERE ROWNUM <= %d
                                    )   WHERE RN >= %d
                                    ''' %
                                    (model, ab_select, page * size,
                                        page * size - size + 1))
        ret_sql = db.select('''
                                    SELECT COUNT(*) FROM %s %s
                                    ''' % (model, ab_select))
        ret_dict['total'] = ret_sql[0][0]
    except cx_Oracle.DatabaseError as e:
        print(e)
        return JsonResponse({})

    if chart == '0':
        return JsonResponse(ret_dict)
    
    return JsonResponse({})


def analyse_fp(request):
    ret_dict = {}
    model = request.GET.get('model', None)
    chart = request.GET.get('chart', None)
    if model == None or chart == None:
        return JsonResponse({})
    
    if chart == '-1':
        return render(request, 'analyse_fp.html', {'model': model})
    
    page = request.GET.get('page', None)
    size = request.GET.get('size', None)
    if page == None or size == None:
        return JsonResponse({})

    try:
        page = int(page)
        size = int(size)
    except:
        return JsonResponse({})

    model = 'PO_' + model + '_20180314'

    db = oracle()
    data_tbname = db.select('''
                                SELECT OUTPUTTABLE FROM FPGROWTH_PARAMETER 
                                    WHERE FPMODELNAME = '%s'
                                ''' % (model))
    data_tbname = data_tbname[0][0] + '_R'
    data_tbname = data_tbname.upper()
    ret_dict['head'] = db.select('''
                                    SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = '%s'
                                    ''' % data_tbname)
    ret_dict['body'] = db.select('''
                                    SELECT * FROM
                                    (
                                        SELECT A.*, ROWNUM RN
                                        FROM (SELECT * FROM %s) A
                                        WHERE ROWNUM <= %d
                                    )   WHERE RN >= %d
                                    ''' % (data_tbname, page * size,
                                            page * size - size + 1))
    ret_sql = db.select('''
                                    SELECT COUNT(*) FROM %s 
                                    ''' % (data_tbname))
    ret_dict['total'] = ret_sql[0][0]
    if chart == '0':
        return JsonResponse(ret_dict)

    bar1_xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bar1_ydata = []
    bar1_tbname = db.select('''
                                SELECT OUTPUTTABLE FROM FPGROWTH_PARAMETER 
                                    WHERE FPMODELNAME = '%s'
                                ''' % (model))
    bar1_tbname = bar1_tbname[0][0] + '_R'
    bar1_tbname = bar1_tbname.upper()
    for x in bar1_xdata:
        ret_sql = db.select('''
                                SELECT DISTINCT COUNT(*) FROM %s
                                    WHERE FPITEMS_COUNT = %d
                                ''' % (bar1_tbname, x))
        bar1_ydata.append(ret_sql[0][0])
    ret_dict['bar1_xdata'] = bar1_xdata
    ret_dict['bar1_ydata'] = bar1_ydata

    bar2_xdata = []
    bar2_ydata = []
    date_list = []
    bar2_tbname = db.select('''
                                SELECT OUTPUTTABLE FROM FPGROWTH_PARAMETER 
                                    WHERE FPMODELNAME = '%s'
                                ''' % (model))
    bar2_tbname = bar2_tbname[0][0] + '_R'
    bar2_tbname = bar2_tbname.upper()
    ret_sql = db.select('''
                            SELECT MINSUPPORT FROM FPGROWTH_PARAMETER
                                WHERE FPMODELNAME LIKE '%%%s%%'
                            ''' % (model))
    min_support = ret_sql[0][0]
    min_support = math.ceil(min_support * 10)
    ret_sql = db.select('''
                            SELECT DISTINCT ACT_DATE FROM %s
                            ''' % (bar2_tbname))
    for x in ret_sql:
        date_list.append(x[0])
    date_list.sort()
    for d in date_list:
        relation_count = db.select('''
                                    SELECT DISTINCT COUNT(*) FROM %s 
                                        WHERE ACT_DATE = to_DATE('%s', 'YYYY-MM-DD')
                                            AND FPITEMS_COUNT >= %d
                                        ''' % (bar2_tbname,
                                                d.strftime('%Y-%m-%d'),
                                                min_support))
        all_count = db.select('''
                                SELECT DISTINCT COUNT(*) FROM %s 
                                    WHERE ACT_DATE = to_DATE('%s', 'YYYY-MM-DD')
                                    ''' % (bar2_tbname,
                                            d.strftime('%Y-%m-%d')))
        bar2_xdata.append(d.strftime('%Y-%m-%d'))
        bar2_ydata.append(relation_count[0][0] / all_count[0][0])
    ret_dict['bar2_xdata'] = bar2_xdata
    ret_dict['bar2_ydata'] = bar2_ydata

    if chart == '1':
        return JsonResponse(ret_dict)

    return JsonResponse({})


def analyse_OO(request):
    model = request.GET.get('model', None)
    chart = request.GET.get('chart', None)

    if model == None or chart == None:
        return JsonResponse({})

    if chart == '-1':
        return render(request, 'analyse_OO.html', {'model': model})

    ret_dict = {}
    page = request.GET.get('page', None)
    size = request.GET.get('size', None)

    if page == None or size == None:
        return JsonResponse({})

    try:
        page = int(page)
        size = int(size)
    except:
        return JsonResponse({})

    db = oracle()
    data_tbname = db.select('''
                                SELECT OUTPUTTABLE FROM FPGROWTH_PARAMETER 
                                    WHERE FPMODELNAME = '%s'
                                ''' % (model))
    data_tbname = data_tbname[0][0] + '_R'
    data_tbname = data_tbname.upper()
    ret_dict['head'] = db.select('''
                                    SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'
                                    ''' % data_tbname)
    ret_dict['body'] = db.select('''
                                    SELECT * FROM
                                    (
                                        SELECT A.*, ROWNUM RN
                                        FROM (SELECT * FROM %s) A
                                        WHERE ROWNUM <= %d
                                    )   WHERE RN >= %d
                                    ''' % (data_tbname, page * size,
                                            page * size - size + 1))
    ret_sql = db.select('''
                                    SELECT COUNT(*) FROM %s 
                                    ''' % (data_tbname))
    ret_dict['total'] = ret_sql[0][0]
    if chart == '0':
        return JsonResponse(ret_dict)

    bar1_xdata = [0]
    bar1_ydata = []
    bar1_tbname = db.select('''
                                SELECT OUTPUTTABLE FROM FPGROWTH_PARAMETER 
                                    WHERE FPMODELNAME = '%s'
                                ''' % (model))
    bar1_tbname = bar1_tbname[0][0] + '_R'
    bar1_tbname = bar1_tbname.upper()

    ret_sql = db.select('''
                            SELECT MIN(PEOPLE_COUNT) FROM %s
                            ''' % (bar1_tbname))
    min_count = ret_sql[0][0]
    ret_sql = db.select('''
                            SELECT MAX(PEOPLE_COUNT) FROM %s
                            ''' % (bar1_tbname))
    max_count = ret_sql[0][0]
    step = (max_count - min_count) / 10
    for x in range(1, 11):
        bar1_xdata.append(min_count + math.ceil(step * x))

    for x in range(1, 11):
        ret_sql = db.select('''
                                SELECT COUNT(*) FROM %s
                                    WHERE PEOPLE_COUNT > %d AND PEOPLE_COUNT <= %d
                                ''' % (bar1_tbname, bar1_xdata[x - 1],
                                        bar1_xdata[x]))
        bar1_ydata.append(ret_sql[0][0])
    bar1_xdata.pop(0)
    ret_dict['bar1_xdata'] = bar1_xdata
    ret_dict['bar1_ydata'] = bar1_ydata

    bar2_xdata = []
    bar2_ydata = []
    date_list = []
    bar2_tbname = db.select('''
                                SELECT OUTPUTTABLE FROM FPGROWTH_PARAMETER 
                                    WHERE FPMODELNAME = '%s'
                                ''' % (model))
    bar2_tbname = bar2_tbname[0][0] + '_R'
    bar2_tbname = bar2_tbname.upper()
    ret_sql = db.select('''
                            SELECT MINSUPPORT FROM FPGROWTH_PARAMETER
                                WHERE FPMODELNAME = '%s'
                            ''' % (model))
    min_support = ret_sql[0][0]
    ret_sql = db.select('''
                            SELECT COUNT(*) FROM CP_TERMINAL_INFO
                            ''')
    people_count = ret_sql[0][0]
    min_support = math.ceil(min_support * people_count)

    ret_sql = db.select('''
                            SELECT DISTINCT ACT_DATE FROM %s
                            ''' % (bar2_tbname))
    for x in ret_sql:
        date_list.append(x[0])
    date_list.sort()
    for d in date_list:
        relation_count = db.select('''
                                        SELECT DISTINCT COUNT(*) FROM %s 
                                            WHERE ACT_DATE = to_DATE('%s', 'YYYY-MM-DD')
                                                AND PEOPLE_COUNT >= %d
                                            ''' % (bar2_tbname,
                                                   d.strftime('%Y-%m-%d'),
                                                   min_support))
        all_count = db.select('''
                                SELECT DISTINCT COUNT(*) FROM %s 
                                    WHERE ACT_DATE = to_DATE('%s', 'YYYY-MM-DD')
                                    ''' % (bar2_tbname,
                                            d.strftime('%Y-%m-%d')))
        bar2_xdata.append(d.strftime('%Y-%m-%d'))
        bar2_ydata.append(relation_count[0][0] / all_count[0][0])
    ret_dict['bar2_xdata'] = bar2_xdata
    ret_dict['bar2_ydata'] = bar2_ydata

    if chart == '1':
        return JsonResponse(ret_dict)

    return JsonResponse({})


def analyse_PP(request):
    model = request.GET.get('model', None)
    chart = request.GET.get('chart', None)

    if model == None or chart == None:
        return JsonResponse({})

    if chart == '-1':
        return render(request, 'analyse_PP.html', {'model': model})

    ret_dict = {}
    page = request.GET.get('page', None)
    size = request.GET.get('size', None)

    if page == None or size == None:
        return JsonResponse({})

    try:
        page = int(page)
        size = int(size)
    except:
        return JsonResponse({})

    db = oracle()

    data_tbname = db.select('''
                                SELECT OUTPUTTABLE FROM FPGROWTH_PARAMETER 
                                    WHERE FPMODELNAME = '%s'
                                ''' % (model))
    data_tbname = data_tbname[0][0] + '_R'
    data_tbname = data_tbname.upper()
    ret_dict['head'] = db.select(
        "SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME='%s'" %
        data_tbname)
    ret_dict['body'] = db.select('''
                                    SELECT * FROM
                                    (
                                        SELECT A.*, ROWNUM RN
                                        FROM (SELECT * FROM %s) A
                                        WHERE ROWNUM <= %d
                                    )   WHERE RN >= %d
                                    ''' % (data_tbname, page * size,
                                            page * size - size + 1))
    ret_sql = db.select('''SELECT COUNT(*) FROM %s 
                                            ''' % (data_tbname))
    ret_dict['total'] = ret_sql[0][0]
    if chart == '0':
        return JsonResponse(ret_dict)

    bar1_xdata = [0]
    bar1_ydata = []
    bar1_tbname = db.select('''
                                SELECT OUTPUTTABLE FROM FPGROWTH_PARAMETER 
                                    WHERE FPMODELNAME = '%s'
                                ''' % (model))
    bar1_tbname = bar1_tbname[0][0] + '_R'
    bar1_tbname = bar1_tbname.upper()

    ret_sql = db.select('''
                            SELECT MIN(APP_COUNT) FROM %s
                            ''' % (bar1_tbname))
    min_count = ret_sql[0][0]
    ret_sql = db.select('''
                            SELECT MAX(APP_COUNT) FROM %s
                            ''' % (bar1_tbname))
    max_count = ret_sql[0][0]
    step = (max_count - min_count) / 10
    for x in range(1, 11):
        bar1_xdata.append(min_count + math.ceil(step * x))

    for x in range(1, 11):
        ret_sql = db.select('''
                                SELECT COUNT(*) FROM %s
                                    WHERE APP_COUNT > %d AND APP_COUNT <= %d
                                ''' % (bar1_tbname, bar1_xdata[x - 1],
                                        bar1_xdata[x]))
        bar1_ydata.append(ret_sql[0][0])
    bar1_xdata.pop(0)
    ret_dict['bar1_xdata'] = bar1_xdata
    ret_dict['bar1_ydata'] = bar1_ydata

    bar2_xdata = []
    bar2_ydata = []
    date_list = []
    bar2_tbname = db.select('''
                                SELECT OUTPUTTABLE FROM FPGROWTH_PARAMETER 
                                    WHERE FPMODELNAME = '%s'
                                ''' % (model))
    bar2_tbname = bar2_tbname[0][0] + '_R'
    bar2_tbname = bar2_tbname.upper()
    ret_sql = db.select('''
                            SELECT MINSUPPORT FROM FPGROWTH_PARAMETER
                                WHERE FPMODELNAME = '%s'
                            ''' % (model))
    min_support = ret_sql[0][0]

    ret_sql = db.select('''
                            SELECT DISTINCT ACT_DATE FROM %s
                            ''' % (bar2_tbname))
    for x in ret_sql:
        date_list.append(x[0])
    date_list.sort()
    for d in date_list:
        ret_sql = db.select('''
                                SELECT DISTINCT APP_TOTAL FROM %s
                                    WHERE ACT_DATE = to_DATE('%s', 'YYYY-MM-DD')
                                ''' % (bar2_tbname,
                                        d.strftime('%Y-%m-%d')))
        people_count = ret_sql[0][0]
        min_threshold = math.ceil(min_support * people_count)
        relation_count = db.select('''
                                        SELECT DISTINCT COUNT(*) FROM %s 
                                            WHERE ACT_DATE = to_DATE('%s', 'YYYY-MM-DD')
                                                AND APP_COUNT >= %d
                                            ''' % (bar2_tbname,
                                                   d.strftime('%Y-%m-%d'),
                                                   min_threshold))
        all_count = db.select('''
                                SELECT DISTINCT COUNT(*) FROM %s 
                                    WHERE ACT_DATE = to_DATE('%s', 'YYYY-MM-DD')
                                    ''' % (bar2_tbname,
                                            d.strftime('%Y-%m-%d')))
        bar2_xdata.append(d.strftime('%Y-%m-%d'))
        bar2_ydata.append(relation_count[0][0] / all_count[0][0])
    ret_dict['bar2_xdata'] = bar2_xdata
    ret_dict['bar2_ydata'] = bar2_ydata

    if chart == '1':
        return JsonResponse(ret_dict)

    return JsonResponse({})