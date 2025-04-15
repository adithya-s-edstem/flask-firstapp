from flask import Flask, jsonify, redirect, render_template, request, send_from_directory, url_for, Response
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/')
def index():
  return render_template('index.html')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#   if request.method == 'GET':
#     return render_template('index.html')
#   elif request.method == 'POST':
#     if 'username' in request.form.keys() and 'password' in request.form.keys():
#       username = request.form['username']
#       password = request.form.get('password') # both are valid
#       if username == 'test' and password == 'test':
#         return "Success"
#       else:
#         return "Failure"
#     else:
#       return "Invalid form data"
    
# @app.route('/file_upload', methods=['POST'])
# def file_upload():
#   file = request.files['file']
#   if file.content_type == 'text/plain':
#     return file.read().decode()
#   elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
#     df = pd.read_excel(file)
#     return df.to_html()
  
# @app.route('/convert_csv', methods=["POST"])
# def convert_csv():
#   file = request.files.get('file')
#   df = pd.read_excel(file)
#   response = Response(
#     df.to_csv(),
#     mimetype='text/csv',
#     headers={
#       'Content-Disposition': 'attachment; filename=result.csv'
#     }
#   )
#   return response

# @app.route('/convert_csv_two', methods=["POST"])
# def convert_csv_two():
#   file = request.files['file']

#   df = pd.read_excel(file)

#   if not os.path.exists('downloads'):
#     os.makedirs('downloads')

#   filename = f"{uuid.uuid4()}.csv"
#   df.to_csv(os.path.join('downloads', filename))
#   return render_template('download.html', filename=filename)

# @app.route('/download/<filename>')
# def download(filename):
#   return send_from_directory('downloads', filename, download_name='result.csv')

# @app.route('/handle_post', methods=["POST"])
# def handle_post():
#   greeting = request.json['greeting']
#   name = request.json['name']

#   with open('file.txt', 'w') as f:
#     f.write(f"{greeting}, {name}")

#   return jsonify({'message': 'Successfully written!'})

# @app.route('/')
# def index():
#   mylist= [10, 20, 30, 40, 50]
#   return render_template('index.html', list=mylist)

# @app.route('/other')
# def other():
#   some_text = "Hello world"
#   return render_template('other.html', text=some_text)

# @app.template_filter('reverse_string')
# def reverse_string(s):
#   return s[::-1]

# @app.template_filter('repeat')
# def repeat(s, times = 2):
#   return s * times

# @app.template_filter('alternate_case')
# def alternate_case(s):
#   return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

# @app.route('/redirect_endpoint')
# def redirect_endpoint():
#   return redirect(url_for('other'))

# @app.route('/')
# def index():
#   return "<h1>Hello World</h1>"

# @app.route('/hello', methods=['POST', 'GET'])
# def hello():
#   if request.method == 'GET':
#     return "You made a GET request"
#   elif request.method == 'POST':
#     return "You made a POST request"

# @app.route('/hello')
# def hello():
#   response = make_response()
#   response.status_code = 202
#   response.headers['content-type'] = 'application/octet-stream'
#   return response

# @app.route('/greet/<name>')
# def greet(name):
#   return f"Hello {name}"

# @app.route('/add/<int:number1>/<int:number2>')
# def add(number1, number2):
#   return f"{number1} + {number2} is equal to {number1 + number2}"

# @app.route('/handle_url_params')
# def handle_params():
#   if 'greeting' in request.args.keys() and 'name' in request.args.keys():
#     greeting = request.args.get('greeting')
#     name = request.args.get('name')
#     return f"{greeting} {name}"
#   else:
#     return "Some parameters are missing"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
