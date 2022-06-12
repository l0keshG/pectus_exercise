from flask import Flask, request, jsonify, make_response
from utility import get_agg_data, get_expanse_sort, get_expanse


app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

# expanses_data?sort=member_name&order=asc
# expanses_data?amount_gte=1400&member_name=Sam
@app.route('/expanses_data')
def get_expense_data():
   
   payload = dict(request.args)
   if 'sort' in payload.keys():
      res = get_expanse_sort(payload)
   else:
      res = get_expanse(payload)

   response = make_response(
                jsonify(
                    {"response": res}
                ),
                200,
            )
   response.headers["Content-Type"] = "application/json"
   return response

# expanses_data?sort=member_name&order=asc
@app.route('/aggregates')
def get_aggregate_data():
   arg = request.args
   dic = dict(arg)
   filter_key = ''
   filter_val = ''
   for key, val in dic.items():
      filter_key = key
      filter_val = val

   val = get_agg_data(filter_key, filter_val)

   response = make_response(
                jsonify(
                    {"response": val, "key": filter_val}
                ),
                200,
            )
   response.headers["Content-Type"] = "application/json"
   return response


# partial execution
# @app.route('/upload_csv_info')
# def upload_csv_info():

#    flag = update_table_with_csv_data()
#    if flag == 201:
#       return 'Data updated to DB successfully'
   
#    else:
#       return 'Error updating the DB'


if __name__ == '__main__':
   app.run(debug=True)