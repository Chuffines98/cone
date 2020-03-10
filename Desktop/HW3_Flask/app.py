# test2 project, app.py
# Mike Colbert 09/20/2019

from flask import Flask, render_template, request
import locale

app = Flask(__name__)
locale.setlocale(locale.LC_ALL, '')  #convert the number into USD
 
# this is the url routing to accept localhost:5000/
@app.route('/', methods=['POST', 'GET'])
def result():
	if request.method == 'POST':   #when the user submits the data
		form = request.form
		principal = float(form["loanAmount"])
		timeToRepay = int(form["timeToRepay"])
		interestRate = float(form["interestRate"])
		interestRate = (interestRate/100/12) # converts to decimal 
		timeToRepay = timeToRepay*12 # convert to months
		'''
		D = 166.7916 (
		((1 + .005) ^360 ) - 1 ) / 
			(.005 (1 + .005) ^360))
		Loan payment (P) = A / D = $599.55 (in this case monthly payment)
		'''
		# math calculation for formula
		num = ((interestRate + 1) **timeToRepay) -1
		print("num", num) 
		denom = (interestRate * (1 + interestRate)**timeToRepay)
		D = (num/ denom)  
		monthlyPayments = principal / D
		monthlyPayments.=locale.currency(monthlyPayments)
		return render_template('index.html', pageTitle="New Title", result=monthlyPayments)
		
	if request.method == 'GET':
		return render_template('index.html', pageTitle="My new title")

	
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')