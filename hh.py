import os
import pymongo
from flask import Flask
from markupsafe import escape
from flask import request,abort ,redirect ,url_for,flash
from flask import render_template,flash,jsonify,send_file
from markupsafe import Markup
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
import functools
from flask_json_schema import JsonSchema

import pandas
import sys





app = Flask(__name__)
app.secret_key="brijeshi skfklajkdfl;asdf "

# client = pymongo.MongoClient("mongodb+srv://brijesh:jyoti2020##B@cluster0-cvo7x.mongodb.net/test?retryWrites=true&w=majority")
# db = client['brijesh']
# secondtaskcol=db['brijesh1']
# tasks_collection=db['brijesh2']

# client = pymongo.MongoClient("mongodb+srv://brijesh:<password>@cluster0-cvo7x.mongodb.net/test?retryWrites=true&w=majority")
# db = client.test
cluster=MongoClient("mongodb+srv://brijesh:jyoti2020##B@cluster0-cvo7x.mongodb.net/test?retryWrites=true&w=majority")
dbbb=cluster["brijesh"]
secondtaskcol=dbbb["brijesh1"]
# derd={"brijesh":"hellow","chauhan":"rythkdfaslf"}
# secondtaskcol.insert_one(derd)



# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)
# client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
# db = client.brjieshdatabase  # Select the database
# tasks_collection = db.hhh # Select the collection name
# secondtaskcol=db.bbb
# todos=[]

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/thanks")
def thanks():
  return render_template("thanks")


@app.route('/')
def indexx():
  flash("this is flash message")
  return redirect(url_for('index'))
@app.route('/index', methods=['GET', 'POST'])
def insert_data():
    if request.method == 'POST':
      fname = request.form.get('fname')  # access the data inside 
      lname = request.form.get('lname')
      fname1 = request.form.get('fname1')  # access the data inside 
      lname1 = request.form.get('lname1')
      fname2 = request.form.get('fname2')  # access the data inside 
      lname2 = request.form.get('lname2')
      fname3 = request.form.get('fname3')  # access the data inside 
      lname3= request.form.get('lname3')
      fname4 = request.form.get('fname4')  # access the data inside 
      lname4= request.form.get('lname4')
      fname5 = request.form.get('fname5')  # access the data inside 
      lname5 = request.form.get('lname5')
      fname6 = request.form.get('fname6')  # access the data inside 
      lname6 = request.form.get('lname6')
      fname7 = request.form.get('fname7')  # access the data inside 
      lname7 = request.form.get('lname7')
          
      # todos.append(fname)
      # todos.append(lname)
      new={
            "firstname":fname,
                "lastname":lname,
                 "firstname1":fname1,
                "lastname1":lname1,
                 "firstname2":fname2,
                "lastname2":lname2,
                 "firstname3":fname3,
                "lastname3":lname3,
                 "firstname4":fname4,
                "lastname4":lname4,
                 "firstname5":fname5,
                "lastname5":lname5,
                 "firstname6":fname6,
                "lastname6":lname6,
                 "firstname7":fname7,
                "lastname7":lname7
                            
          }   
      secondtaskcol.insert_one(new)
    

          # collection.insert_one(new)
          

    return render_template('index.html')
@app.route('/index/colll', methods=['GET'])
def get_tasks():
    all_tasks = secondtaskcol.find()
    task_list = []
    for task in all_tasks:

      task_list.append({
          'firstname': task['firstname'],
          'lastname': task['lastname'],
           'firstname1': task['firstname1'],
          'lastname1': task['lastname1'],
          'firstname2': task['firstname2'],
          'lastname2': task['lastname2'],
           'firstname3': task['firstname3'],
          'lastname3': task['lastname3'],
          'firstname4': task['firstname4'],
          'lastname4': task['lastname4'],
           'firstname5': task['firstname5'],
          'lastname5': task['lastname5'],
          'firstname6': task['firstname6'],
          'lastname6': task['lastname6'],
           'firstname7': task['firstname7'],
          'lastname7': task['lastname7'],



      })

    return jsonify({'tasks': task_list})

@app.route('/index/colll/<task_id>', methods=['GET'])
def get_task(task_id):
    tasks = secondtaskcol.find({'id': task_id})
    if tasks.count() == 0:
        return jsonify({'task': None})
    return jsonify({'task': tasks})    

@app.route('/show')
def show():
  tasks=secondtaskcol.find()
  return render_template('show.html' ,tasks=tasks)



# if (len(initial_tasks)) == 0:
#     tasks_collection.insert({
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#         'done': False
#     })
#     tasks_collection.insert({
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web',
#         'done': False
#     })


# @app.route('/api/tasks', methods=['GET'])
# def get_tasks():
#     all_tasks = tasks_collection.find()
#     task_list = []
#     for task in all_tasks:
#         task_list.append({'title': task['title'], 'description': task['description'], 'id': task['id']})

#     return jsonify({'tasks': task_list})


@app.route('/api/create-task', methods=['GET'])
def create_task():
    tasks = tasks_collection.find()
    new_task = {"id": tasks.count(), "title": "Learn Mongo", "description": "Start with Flask + Mongo", "done": False}
    tasks_collection.insert(new_task)
    all_tasks = tasks_collection.find()
    task_list = []
    for task in all_tasks:
        task_list.append({'title': task['title'], 'description': task['description'], 'id': task['id']})
    return jsonify({'tasks': task_list})


# @app.route('/api/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     tasks = tasks_collection.find({'id': task_id})
#     if tasks.count() == 0:
#         return jsonify({'task': None})
#     return jsonify({'task': tasks[0]})





@app.route('/test', methods=['GET'])
def test():
    return jsonify({'msg': 'This is a Test'})





# @app.route("/survey",method=["POST"])
# def survey():
@app.route('/download')
def download():
  return send_file('templates\GATE_2020_Information_Broucher_Final_v8.pdf')
@app.route('/file')
def thisuu():
  return render_template("pdfopen.html")

cursor=secondtaskcol.find()
mongo_docs=list(cursor)
print("total docs  is {}".format(len(mongo_docs)))
docs = pandas.DataFrame(columns=[])
for num, doc in enumerate(mongo_docs):
  doc["_id"] = str(doc["_id"])
  doc_id = doc["_id"]
  series_obj = pandas.Series( doc,name=doc_id )
  docs = docs.append(series_obj)
#print(docs)  

most_common_first_name_is=docs['firstname'].value_counts()[0]
print(docs['firstname'].value_counts())
@app.route('/pandass')
def panddda():
  return render_template('panda.html',data=most_common_first_name_is)

if __name__=='__main__':
  app.debug=False
  app.run()