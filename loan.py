loan_value = 80 * (10 ** 6)
remains = loan_value
monthy_paid = 1.5 * 10 ** 6
total_paid = 0

month = 0
year = 0
profit = 9.5 / 100.0

while remains > monthy_paid:
	remains -= monthy_paid
	total_paid += monthy_paid
	month += 1

	if month == 12:
		year += 1
		month = 0
		remains += remains * profit

	print(year, month, total_paid, remains)

total_paid += remains
month += 1
total_paid = int(total_paid)
print(((total_paid * 1.0 / loan_value) - 1) * 100 , total_paid, year, month)


