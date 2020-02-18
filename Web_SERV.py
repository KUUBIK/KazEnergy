from flask import Flask, escape, request, render_template, jsonify, url_for, redirect
import random
import json
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
db = mongo.db.data

dataToCar = good_car = {
    "id":1,
    "Бак": "Исправен",
    "Номер машины": "1",
    "Неисправности": "Невыявленно"
}

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['uname']
        passw = request.form['passw']
        # db = mongo.db.data
        # db.insert(dataToCar)
        # print(db)
        if name == "a" and passw == "1":
            print("good")
            return redirect('admin')
        else:
            return render_template("register.html")
    else:
        print('no')
        return render_template("register.html")


@app.route('/admin', methods=['GET', 'POST'])
def get_tasks():
    if request.method == 'POST':
        uname = request.form['comment']
        print(uname)
        dataToMongo = db.find({'_id':int(uname)})
        print(dataToMongo)
        for i in dataToMongo:
            print(i)
            return render_template('task.html', employee = i)
    return render_template('adminPage.html')



if __name__ == '__main__':
    app.run(debug=True)

