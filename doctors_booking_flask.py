#https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972


from flask import Flask, render_template, request
import sqlite3 as sql
import doctor_config

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

@app.route('/booktime',methods = ['POST', 'GET'])
def booktime():
    print("booktime started")
    msg = "ok"
    if request.method == 'GET':
        print("request.method is GET")
        return("returned from get method in /booktime.")
    else:
        print("request.method is POST")
        try:
            print("get values from request.")
            patientname = request.form['patientname']
            print("patientname:", patientname)
            patientemail = request.form['patientemail']
            print("patientemail:", patientemail)
            patientMobile = request.form['patientMobile']
            print("patientMobile:", patientMobile)
            year = request.form['year']
            print("year:", year)
            month = request.form['month']
            print("month:", month)
            day = request.form['day']
            print("day:", day)
            hour = request.form['hour']
            print("hour:", hour)
            doctorsid = request.form['id']
            print("doctorsid:", doctorsid)
            #The TIMESTAMP field accepts a sring in ISO 8601 format 'YYYY-MM-DD HH:MM:SS
            #conn.execute("INSERT INTO logs(message, timestamp) values (?, ?)", ("message: error",'2012-12-25 23:59:59'))
            appointmenttime = year + "-" + month + "-" + day + " "+ hour + ":00:00"
            print("appointmenttime:", appointmenttime)
            with sql.connect("database.db") as con:
                print("sql connection made")
                cur = con.cursor()
                cur.execute("INSERT INTO booking(doctorsid, patientname, start_time, patientemail, patientMobile) \
                   values  (?, ?, ?, ?, ?) ", (doctorsid, patientname, appointmenttime, patientemail, patientMobile) )
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
            return render_template("booked.html",msg = msg)
            con.close()


@app.route('/booking',methods = ['POST', 'GET'])
def booking():
    print("booking started")
    year = request.args['year']
    print("year:", year)
    month = request.args['month']
    print("month:", month)
    day = request.args['day']
    print("day:", day)
    hour = request.args['hour']
    print("hour:", hour)
    id = request.args['id']
    print("id:", id)
    '''
    patientname = request.form['patientname']
    print("patientname:", patientname)
    patientemail = request.form['patientemail']
    print("patientemail:", patientemail)
    patientMobile = request.form['patientMobile']
    print("patientMobile:", patientMobile)
    '''
    #CREATE TABLE doctors(id integer primary key, name TEXT
    #get doctors name from database using id
    conn = sql.connect('database.db', detect_types=sql.PARSE_DECLTYPES|sql.PARSE_COLNAMES)
    print("sql connection made")
    c = conn.cursor()
    query = "SELECT name FROM doctors WHERE id = "+id
    print ("query:", query)
    c.execute(query)
    rows = c.fetchall()
    print("results from ")
    for row in rows:
       print(row)
       #print(row[2], type(row[2]), row[3])
    conn.close()
    #booking(id, doctorsid, patientname, start_time, patientemail, patientMobile)'
    msg = "ok"
    return render_template("doctor_booking.html",year=year, month=month, day=day, hour=hour, msg = msg, id=id)

@app.route('/adddoctor',methods = ['POST', 'GET'])
def addrec():
   msg = "start"
   print("start addrec(), request.method:", request.method)
   if request.method == 'GET':
       print("request.method is GET")
       return("get method called.")
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
    print("method /list start")
    conn = sql.connect('database.db', detect_types=sql.PARSE_DECLTYPES|sql.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute('''SELECT * FROM doctors''')
    rows = c.fetchall()
    start_time   = doctor_config.STARTHOUR
    end_time = doctor_config.ENDHOUR
    print("start_time:", start_time)
    print("end_time:", end_time)
    for row in rows:
       print(row)
       #print(row[2], type(row[2]), row[3])
    conn.close()
    return render_template("doctors_list.html",rows = rows, end_time=end_time, start_time=start_time)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
