# Importing needed libraries
from flask import *
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Homepage route
@app.route('/')
def home():
    return render_template('login.html')
    
    

# Login form route
@app.route('/getOTP', methods=['POST'])
def getOTP():
    random_number = generateOTP()  # Generate random number
    session['otp'] = str(random_number)  # Store the generated OTP in a session variable
    return render_template('enterOTP.html', random_number=random_number)
    
    
    #this function for send the OTP code to client
	
#	number = request.form['number']
#	val = getOTPApi(number)
#	if val:
#		return render_template('enterOTP.html')




# Validate OTP route
@app.route('/validateOTP', methods=['POST'])
def validateOTP():
    entered_otp = request.form['otp']  # Get entered OTP from the form
    generated_otp = session.get('otp')  # Retrieve the stored OTP from the session

    if entered_otp == generated_otp:
        message = "You are Authorized. Thank you."
    else:
        message = "You are not Authorized. Try again later."

    return render_template('result.html', message=message)


# Generate random number for OTP
def generateOTP():
    return random.randint(100000, 999999)
    
    
#using virtual service provider(twilio) can send the genarated OTP to client

#def getOTPApi(number):
#	account_sid = 'ACbfd86d77349eae0f9a4d62f9fa982153'
#	auth_token = 'd479912913b2cd591871e0bc01195bf8'
#	client = Client(account_sid, auth_token)
#	otp = genarateOTP()
#	body = 'Your OTP is ' + str(otp)
#	message = client.message.create(
#					from='+442033223576',
#					body=body,
#					to=number
#					)
#	if message.sid:
#		return True
#	else:
#		False




# Running Flask server
if __name__ == '__main__':
    app.run(debug=True)
