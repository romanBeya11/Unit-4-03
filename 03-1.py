# Created by Roman Beya
# Created for ICS3U
# Created on Nov-3-2017
# This program takes a input from a procedure, however, one of the inputs is optional

def display_address(province, city, postal_code, street, apt_number = ''):
	print "I live in the province of {0}\nI live in the city of {1}\nMy postal code is {2}\nMy street is {3}".format(province, city, postal_code, street)
	if not apt_number == '':
		print "My apartment number is {}".format(apt_number)
		
display_address("Ontario", "Ottawa", "K2J 5A7", "Kilbarron", "4A")          
