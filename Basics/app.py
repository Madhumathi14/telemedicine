from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/loginandsignup')
def about():
    return render_template("login and signup.html")

@app.route("/bookappointment",methods=['GET','POST'])
def booka():
    return render_template("Book an Appointment-2.html")

@app.route("/payfee",methods=['GET','POST'])
def bookb():
    return render_template("payment.html")


@app.route("/bookcaretaker",methods=['GET','POST'])
def bookc():
    return render_template("Book a Caretaker.html")

@app.route("/doctortimeslot",methods=['GET','POST'])
def bookd():
    return render_template("doctortimeslot.html")

@app.route("/howtopaythefee",methods=['GET','POST'])
def booke():
    return render_template("how to pay the fee and types of modes how the fee can be oaid.html")

@app.route("/howtojoiningvideocall",methods=['GET','POST'])
def bookf():
    return render_template("videocall.html") 

@app.route("/pastreports",methods=['GET','POST'])
def bookg():
    return render_template("pnp.html") 

@app.route("/patientmedication",methods=['GET','POST'])
def bookh():
    return render_template("Patient Report and Medication.html") 

@app.route("/booking",methods=['GET','POST'])
def booki():
    return render_template("booking.html") 

@app.route("/checkup",methods=['GET','POST'])
def bookj():
    return render_template("Doctor's Checkup Reports & Consultaion Info.html") 

@app.route("/doctors",methods=['GET','POST'])
def bookk():
    return render_template("Doctors slot.html") 

@app.route("/joinvideo",methods=['GET','POST'])
def bookl():
    return render_template("joining a video call.html") 

@app.route("/login",methods=['GET','POST'])
def bookm():
    return render_template("login.html") 

@app.route("/patient",methods=['GET','POST'])
def bookn():
    return render_template("paitent.html") 

@app.route("/tele",methods=['GET','POST'])
def booko():
    return render_template("Telemedicine Appointment Booking.html") 

@app.route("/phonenumber",methods=['GET','POST'])
def bookp():
    return render_template("docinfo.html") 

if __name__ == '__main__':
    app.run(debug=True)
