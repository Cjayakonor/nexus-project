#!/usr/bin/python3

import csv
import random

'''Write a program to randomly pick an EIT from a csv file to pitch an idea.
'''

# read from the csv file
# put the data into a dictionary
# parameters: class, no_of_pitches
# use random module available in python
# pick up an idea
# after a selection is made, write name to a file
# once all EITs have pitched, reset line for pitching

try:
	with open('eits-2018.csv') as file:
		reader = csv.DictReader(file)

		eits = [eit for eit in reader]

		# for eit in reader:
		# 	eits.append(eit)
	
	pitchee = eits[random.randrange(0, len(eits))]

	print("Name: {name}\nClass: {klass}".format(**pitchee))

except Exception as e:
	print('No file was found', e)
