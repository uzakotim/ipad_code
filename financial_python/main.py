import csv


def convertStringToInt(string):
	number = 0.0
	negative = False
	if string[0] == '-':
		negative= True

	array = []
	for char in string:
		if char != ' ':
			array.append(char)
	number_of_dec = len(array)-1-array.index(',')
	array.remove(',')
	if negative:
		array.remove('-')

	i = 0
	for elem in reversed(array):
		number+= int(elem)*10**(i-number_of_dec)
		i+=1
	if negative: return -number
	else: return number

def main():

	character = '*'
	rows = []	
	# reading 
	with open("file.csv",'r',encoding='latin-1') as file:
		csvreader = csv.reader(file,delimiter=';')
		header = next(csvreader)
		for row in csvreader:
			index = row.index('CZK')
			rows.append(row[index-1])
	# processing
	numbers =[]
	for row in rows:
		number = convertStringToInt(row)
		numbers.append(number)

	total_spending = sum([x for x in numbers if x<0])	
	total_income = sum([x for x in numbers if x>0])

	total_cash_flow = total_income+total_spending
	max_spending = min([x for x in numbers if x<0])
	min_spending = max([x for x in numbers if x<0])

	# OUTPUT
	output = ''
	border = ''
	line_max = '| '+'Maximal Spending' +' |'
	len_line_max = len(line_max)
	line_min = '| '+'Minimal Spending' +' |'
	len_line_min = len(line_min)

	line_total = '| '+ ' '*(len_line_min-len("| Total Spending |"))+'Total Spending' +' |'
	len_line_total = len(line_total)

	border+=character
	border += (len_line_max-2)*'-'
	border += character

	#Maximal spending

	output+=border
	output+='\n'
	output+=line_max
	output+='\n'
	output+= '|' + ' '*(len_line_max-len(str(max_spending))-3) + str(max_spending) + ' |'
	output+='\n'
	# output+=border
	# output+='\n'

	#Minimal spending
	border  = ''
	border +=character
	border += (len_line_max-2)*'-'
	border += character

	output+=border
	output+='\n'
	output+=line_min
	output+='\n'
	output+= '|' + ' '*(len_line_min-len(str(min_spending))-3) + str(min_spending) + ' |'
	output+='\n'
	# output+=border
	# output+='\n'

	#Total spending
	border  = ''
	border +=character
	border += (len_line_min-2)*'-'
	border += character

	output+=border
	output+='\n'
	output+=line_total
	output+='\n'
	output+= '|' + ' '*(len_line_min-len(str(total_spending))-3) + str(total_spending) + ' |'
	output+='\n'
	# output+=border
	# output+='\n'

	line_total = '| '+ ' '*(len_line_min-len("| Total Income |"))+'Total Income' +' |'
	len_line_total = len(line_total)

	#Total income
	border  = ''
	border +=character
	border += (len_line_total-2)*'-'
	border +=character

	output+=border
	output+='\n'
	output+=line_total
	output+='\n'
	output+= '|' + ' '*(len_line_total-len(str(total_income))-3) + str(total_income) + ' |'
	output+='\n'
	# output+=border
	# output+='\n'

	#Cash Flow
	cash_flow = '| '+ ' '*(len_line_min-len("| Cash Flow |"))+'Cash Flow' +' |'
	len_cash_flow = len(cash_flow)


	border  = ''
	border +=character
	border += (len_cash_flow-2)*'-'
	border +=character

	output+=border
	output+='\n'
	output+=cash_flow
	output+='\n'
	output+= '|' + ' '*(len_cash_flow-len(str(total_cash_flow))-3) + str(total_cash_flow) + ' |'
	output+='\n'
	percentage = 0
	try:
		percentage = round((total_cash_flow/total_income)*100,2)
	except:
		if n == 1:
			percentage = round((total_cash_flow/1000)*100,2)
		if n == 2:
			percentage = round((total_cash_flow/24500)*100,2)


	output+= '|' + ' '*(len_cash_flow-len(str(percentage))-4)+ str(percentage)+ '%' + ' |'
	output+='\n'
	output+=border
	output+='\n'
	
	print(output)

if __name__ == "__main__":
	main()