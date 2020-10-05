
import decimal
from random import randint
from datetime import datetime, timedelta, date

ledger = [] #complete ledger (multiple transactions)

def research_questions():

	global testingDate

	print('Hi there. Let\'s generate you some transactions. I\'m going to ask you some quick questions.') 
	
	print('What day (dd) is the testing happening?')
	print('eg 20/04/2020')
	research_day = int(input(':> '))

	print('Month (mm)?')
	research_month = int(input(':> '))

	print('Year (yyyy)?')
	research_year = int(input(':> '))

	print('Finally, how many transactions do you need?')
	trans_quant = int(input(':> '))

	print(f'Great. The date of your testing is {research_day}/{research_month}/{research_year}, and you need {trans_quant} transactions.') 
	print(f'Is this correct (y/n)?')

	research_date_conf = input(':> ')

	if research_date_conf == 'n':
		print(' ')
		print('Okay, let\'s try again.')		
		print(' ')
		research_questions()

	if research_date_conf == 'y':
		try:
			testingDate = date(research_year, research_month, research_day) #Send user test date to variable
			create_ledger(trans_quant)
		
		except ValueError: #Error to pick up incorrect dates
			print(' ')
			print('Sorry, I\'m having trouble... Looks like that date isn\'t correct.')
			print(' ')
			print('Please try again')
			print(' ')
			research_questions()

def summary():

	print('')
	print('I\'ve saved these transactions into a CSV file which should be alongside this script.')
	print('')
	print('Good luck with your prototype and testing, hope you learn something interesting :-)')
	print('@Swain0')
	print('')

def create_date():	

	''' Create date for transaction'''
	raw_date = testingDate - timedelta(randint(1, 60)) # Alter days value each loop 
	return raw_date

def create_amount():
	
	''' Create amount up to 25.00 '''
	raw_number = randint(1000, 2500) / 100
	return raw_number

def quantize_amount(n):
	
	''' Clean up floats and missing zeros from whole numbers '''
	n = decimal.Decimal(n).quantize(decimal.Decimal('0.00'))	
	return n

def create_ledger(trans_quant):

	account_balance = 1500 #Set beginning balance of the account

	f = open("transaction_list.csv", "w")
	header = "Date, Amount, Balance\n" 
	f.write(header)

	''' Generate ledger '''	
	for n in range(trans_quant):

		transaction = [create_date(), create_amount()]
		ledger.append(transaction)

	''' Sort dates and format style to match destination'''	
	ledger.sort(key=lambda date: date[0], reverse=True)

	for i in range(len(ledger)):
		
		''' Calculate account balance '''
		tup = ledger[i]		
		account_balance -= tup[1]

		''' Print acct' balance and prepare for writing '''

		final_date = tup[0].strftime('%d %b %y') #Converts datetime to string for formatting and write
		final_amount = str(f'£{quantize_amount(tup[1])}')
		final_balance = str(f'£{quantize_amount(account_balance)}')

		f.write(final_date + ',' + final_amount + ',' + final_balance + "\n")
		print(final_date, final_amount, final_balance)

	f.close()
	summary()

research_questions()





