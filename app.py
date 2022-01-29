from flask import Flask, jsonify, request # render_template
from flask_cors import CORS
import pymysql

app = Flask(__name__) # object of name app
cors = CORS(app)

@app.route('/users',methods = ['GET'])
def get_users():
    
    #to connect to database
    conn = pymysql.connect(host = 'sql6.freesqldatabase.com',user = 'sql6468352',password = 'q1kNvku6PD',db = 'sql6468352')
    cur = conn.cursor()
    cur.execute("SELECT * FROM first_year")
    output = cur.fetchall()
    
    print(type(output))
    for x in output:
        print(x)
        
    conn.close()
    return jsonify(output)

@app.route('/users',methods = ['DELETE'])
def deleterecord():
    conn = pymysql.connect(host = 'sql6.freesqldatabase.com', user = 'sql6468352', password = 'q1kNvku6PD', db ='sql6468352');
    cur = conn.cursor()
    roll_no = int(request.args.get('roll_no'));

    query  = f"DELETE FROM `1st_year` WHERE roll_no = {roll_no}";
    res = cur.execute(query);
    conn.commit();
    print(cur.rowcount,"records deleted");

    return {"results":"records deleted"}

#for performing insert
@app.route('/users', methods=['POST'])
def insert():
    conn = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6468352', password='q1kNvku6PD', db='sql6468352')
    
    raw_json = request.get_json()
    
    roll_no = raw_json["roll no"]
    name = raw_json["name"]
    age = raw_json["age"]
    city = raw_json["city"]

    insert_sql = f"INSERT INTO first_year (`roll no`, name, age,city) VALUES ('{roll_no}', '{name}', '{age}','{city}')"
    print(insert_sql)
    
    cur = conn.cursor()
    cur.execute(insert_sql)
    conn.commit()
    return {"Result":"Records inserted successfully"}

    
if __name__ == "__main__":   # to generate port
    app.run(debug = True);   # to debug
