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

cluster=MongoClient("mongodb+srv://brijesh:jyoti2020##B@cluster0-cvo7x.mongodb.net/test?retryWrites=true&w=majority")
dbbb=cluster["brijesh"]
secondtaskcol=dbbb["brijesh2"]

@app.route("/index")
def index():
    return render_template("index.html")




@app.route('/')
def indexx():
  flash("this is flash message")
  return redirect(url_for('index'))
@app.route('/index', methods=['GET', 'POST'])
def insert_data():
    if request.method == 'POST':
      first_name = request.form.get('fname')  # access the data inside 
      last_name = request.form.get('lname')
      age = request.form.get('fname1')  # access the data inside 
      sex = request.form.get('lname1')
      fav_no = request.form.get('fname2')  # access the data inside 
      fav_letter = request.form.get('lname2')
      fav_country = request.form.get('fname3')  # access the data inside 
      fav_color= request.form.get('lname3')
      fav_actor = request.form.get('fname4')  # access the data inside 
      fav_actress= request.form.get('lname4')
      fav_movie = request.form.get('fname5')  # access the data inside 
      fav_novel = request.form.get('lname5')
      fav_profession = request.form.get('fname6')  # access the data inside 
      fav_cricketer = request.form.get('lname6')
      fav_state = request.form.get('fname7')  # access the data inside 
      fav_book = request.form.get('lname7')
      
      # todos.append(fname)
      # todos.append(lname)
      new={
            "firstname":first_name,
                "lastname":last_name,
                 "age":age,
                "sex":sex,
                 "fav_no":fav_no,
                "fav_letter":fav_letter,
                 "fav_country":fav_country,
                "fav_color":fav_color,
                 "fav_actor":fav_actor,
                "fav_actress":fav_actress,
                 "fav_movie":fav_movie,
                "fav_novel":fav_novel,
                 "fav_profession":fav_profession,
                "fav_cricketer":fav_cricketer,
                 "fav_state":fav_state,
                "fav_book":fav_book,
                
                            
          }   
      secondtaskcol.insert_one(new)
      
      return redirect(url_for('thanks'))
    
    
          # collection.insert_one(new)
    
@app.route('/index/json', methods=['GET'])
def get_tasks():
    all_tasks = secondtaskcol.find()
    task_list = []

    for task in all_tasks:

      task_list.append({
          'firstname': task['firstname'],
          'lastname': task['lastname'],
           'age': task['age'],
          'sex': task['sex'],
          'fav_no': task['fav_no'],
          'fav_letter': task['fav_letter'],
           'fav_country': task['fav_country'],
          'fav_color': task['fav_color'],
          'fav_actor': task['fav_actor'],
          'fav_actress': task['fav_actress'],
           'fav_movie': task['fav_movie'],
          'fav_novel': task['fav_novel'],
          'fav_profession': task['fav_profession'],
          'fav_cricketer': task['fav_cricketer'],
           'fav_state': task['fav_state'],
          'fav_book': task['fav_book'],
          



      })

    return jsonify({'tasks': task_list})

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'msg': 'This is a Test'})


cursor=secondtaskcol.find()
mongo_docs=list(cursor)


docs = pandas.DataFrame(columns=[])

# for num, doc in enumerate(mongo_docs):
#   doc["_id"] = str(doc["_id"])
#   doc_id = doc["_id"]
#   series_obj = pandas.Series( doc,name=doc_id )
#   print(series_obj)
#   docs = docs.append(series_obj)
for doc in mongo_docs:
  series_obj=pandas.Series(doc)
  docs=docs.append(series_obj,ignore_index=True)


  # docs=docs.drop(['_id'],axis=1)
  

print(docs['age'].count())

@app.route("/thanks")
def thanks():
  return render_template("thanks.html")

@app.route('/pandass')
def panddda():
  return render_template('panda.html',data=docs)

if __name__=='__main__':
  app.debug=False
  app.run()