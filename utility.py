from db import execute_cur

operator_match = {
    'gte': '>=',
    'gt': '>',
    'eq': '=',
    'lte': '<=',
    'le': '<',
    'neq': '!='
}

# aggregates?departments=IT
def get_agg_data(filter_key, filter_val):

    #print(filter_key, filter_val)
    sql_query = "select sum(amount) from expanses where {0}='{1}'".format(filter_key, filter_val)

    expanse_data = 0
    try:
        data = execute_cur(sql_query)
        for val in data:
            expanse_data += val[0]
    except:
        pass
    return expanse_data

# expanses_data?sort=member_name&order=asc
def get_expanse_sort(payload):
    sort_key = payload.get('sort')
    order_key = payload.get('order')

    sql_query = "select * from expanses order by {0} {1}".format(sort_key, order_key)
    expanse_data = []
    try:
        data = execute_cur(sql_query)
        for expanse in data:
            expanse_data.append(expanse)
    except:
        pass
    return expanse_data

# expanses_data?amount_gte=1400&member_name=Sam
def get_expanse(payload):

    flag = ''
    sql_query = 'select * from expanses where '

    for key, val in payload.items():
        if 'amount' in key:
            amount_key = key.split('_')
            if len(amount_key) > 1:
                flag = amount_key[1]
                flag_val = operator_match.get(flag)
                flag_key = amount_key[0]
                sql_query = sql_query + '{0} {1} {2} and '.format(flag_key, flag_val, val)
            else:
                sql_query = sql_query + '{0} = {1} and '.format(key, val)
        else:
            sql_query = sql_query + "{0} = '{1}' and ".format(key, val)

    try:
        data = execute_cur(sql_query[:-5])
        expanse_data = []
        for expanse in data:
            expanse_data.append(expanse)        
    except:
        pass
    return expanse_data




