#https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972


from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['DEBUG'] = True

@app.route("/")
def main():
    #return "Welcome!"
    return render_template('doctors_index.html')

@app.route('/enternew')
def new_student():
   return render_template('doctors_new.html')

@app.route('/booking',methods = ['POST', 'GET'])
def addrebooking():
    print("booking started")
    hour = request.form['hour']
    print("hour:", hour)
    return render_template("doctor_booked.html",msg = msg)

@app.route('/adddoctor',methods = ['POST', 'GET'])
def addrec():
   msg = "start"
   print("start addrec(), request.method:", request.method)
   if request.method == 'GET':
      print("request.method is GET")
   else:
      print("request.method is POST")
      try:
         print("get values from request.")
         name = request.form['name']
         print("name:", name)
         starttime = request.form['starttime']
         print("starttime:", starttime)
         endtime = request.form['endtime']
         print("endtime:", endtime)

         with sql.connect("database.db") as con:
            print("sql connection made")
            cur = con.cursor()
            cur.execute("INSERT INTO doctors(name, start_time, end_time) \
               values  (?, ?, ?) ", (name, starttime, endtime) )
            print("sql executed.")
            con.commit()
            msg = "Record successfully added"
            print("method addrec() commit successfully completed.")
      except Exception as e:
         msg = "error in insert operation"
         print("Exception:", e)
         print("try catch caught error in method addrec()")
         con.rollback()

      finally:
         return render_template("aa_result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
    '''
   con = sql.connect("database.db")

   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from doctors")

   rows = cur.fetchall();
   print("rows:", rows)
   for row in rows:
       print(row)
   '''
    conn = sql.connect('database.db', detect_types=sql.PARSE_DECLTYPES|sql.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute('''SELECT * FROM doctors''')
    rows = c.fetchall()
    for row in rows:
       print(row)
       #print(row[2], type(row[2]), row[3])

    conn.close()
    return render_template("doctors_list.html",rows = rows)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
