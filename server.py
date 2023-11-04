import pandas as pd
from flask import Flask, render_template, request
from Database import area_data
import csv
from hinjewadi01 import model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")



@app.route("/predict", methods=['GET', 'POST'])
def predict():

    return render_template("predict.html",area_data=area_data)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

@app.route('/area/<int:num>',  methods=['GET', 'POST'])
def area(num):
    area = area_data[num]
    current_area = area[0]
    print(current_area)
    if request.method == 'POST':

        form_data = {

            'bedroom': int(request.form['Bedrooms']),
            # 'area': request.form['area'],
            'area': int(request.form['SquareFeet']),
            # 'amount': int(request.form['Amount']),
            'furnishing': request.form['furniture'],
            # 'floor': int(request.form['Floor']),
            'parking': int(request.form['Parking']),
            'propertyage': int(request.form['PropertyAge']),

        }
        form = {

            'bedroom': int(request.form['Bedrooms']),
            'area': int(request.form['SquareFeet']),
            'amount': int(request.form['Amount']),
            'furnishing': request.form['furniture'],
            'floor': int(request.form['Floor']),
            'parking': int(request.form['Parking']),
            'propertyage': int(request.form['PropertyAge']),
        }

        price = 0
        with open("test.csv", 'w', newline='') as csvfile:

            fieldnames = form_data.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


            writer.writeheader()

            writer.writerow(form_data)
        test = pd.read_csv("test.csv")

        if(current_area == "Hinjewadi"):
            price = int((model.predict(test))[0])


        return render_template('result.html', area=area, area_data=area_data, price =price,num=num, form_data=form_data, form = form)
    return render_template('area.html', area = area, area_data = area_data, num=num)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
