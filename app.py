import psycopg2
import sys
from  flask import Flask,render_template
from flask import jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def homepage():
	return "add '/amzn', '/nord', '/mfa' to url for corresponding data"

@app.route("/amzn")
def send_data():
	con = psycopg2.connect("host='localhost' dbname='stock_project2' user='postgres' password='postgres'")
	cur = con.cursor()
	cur.execute("""select * from  amazon_table""")
	columns = ("date", "open", "high", "low", "close", "volume")
	results = {}
	for row in cur.fetchall():
		results[str(row[0])] = (dict(zip(columns, row)))
	amazon_data = results
	return jsonify(amazon_data)

@app.route("/nord")
def send_data2():
	con = psycopg2.connect("host='localhost' dbname='stock_project2' user='postgres' password='postgres'")
	cur2 = con.cursor()
	cur2.execute("""select * from  nordstroms_table""")
	columns = ("date", "open", "high", "low", "close", "volume")
	results2 = {}
	for row in cur2.fetchall():
		results2[str(row[0])] = (dict(zip(columns, row)))
	nord_data = results2
	return jsonify(nord_data)

@app.route("/mfa")
def send_data3():
	con = psycopg2.connect("host='localhost' dbname='stock_project2' user='postgres' password='postgres'")
	cur3 = con.cursor()
	cur3.execute("""select * from  mfa_table""")
	columns = ("date", "open", "high", "low", "close", "volume")
	results3 = {}
	for row in cur3.fetchall():
		results3[str(row[0])] = (dict(zip(columns, row)))
	mfa_data = results3
	return jsonify(mfa_data)

# @app.route("/analysis")
# def send_data3():
# 	con = psycopg2.connect("host='localhost' dbname='stock_project2' user='postgres' password='postgres'")
# 	cur4 = con.cursor()
# 	cur4.execute("""select * from  corporate_analysis""")
# 	columns = ("company", "analysis")
# 	results4 = {}
# 	for row in cur4.fetchall():
# 		results4[str(row[0])] = (dict(zip(columns, row)))
# 	corporate_analysis = results3
# 	return jsonify(corporate_analysis)

if __name__ == "__main__":
	app.run(debug=True)