# -*- coding: utf-8 -*-
"""
Created on Tue Mar  21 12:02:48 2017

@author: srlin
"""
#Proj08 by Sayem Lincoln
#uncomment for testing with run_file.py
#==============================================================================
# import sys
# def input( prompt=None ):
#     if prompt != None:
#         print( prompt, end="" )
#     aaa_str = sys.stdin.readline()
#     aaa_str = aaa_str.rstrip( "\n" )
#     print( aaa_str )
#     return aaa_str
#==============================================================================
    
import pylab

REGION_LIST = ['Far_West',
			   'Great_Lakes',
			   'Mideast',
			   'New_England',
			   'Plains',
			   'Rocky_Mountain',
			   'Southeast',
			   'Southwest',
			   'all']
LOWER_REGIONS = [reg.lower() for reg in REGION_LIST]
VALUES_LIST = ['Pop', 'GDP', 'PI', 'Sub', 'CE', 'TPI', 'GDPp', 'PIp']
VALUES_NAMES = ['Population(m)', 'GDP(b)', 'Income(b)', 'Subsidies(m)', 'Compensation(b)', 'Taxes(b)', 'GDP per capita',
				'Income per capita']
PROMPT1 = "Specify a region from this list -- Far_West, Great_Lakes, Mideast, New_England, Plains, Rocky_Mountain, Southeast, Southwest, all: "
PROMPT2 = "Specify x and y values, space separated from Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp: "


def plot_regression(x, y):
	"""Draws a regression line for values in lists x and y.
	   x and y must be the same length."""
	xarr = pylab.array(x)  # numpy array
	yarr = pylab.array(y)  # numpy arry
	m, b = pylab.polyfit(xarr, yarr, deg=1)  # creates line, only takes numpy arrays
	# as parameters
	pylab.plot(xarr, m * xarr + b, '-')  # plotting the regression line


def plot(x, y, data):  
	#Plot the values in the parameters.
	

	x_data_idx = VALUES_LIST.index(x) #indexing x
	y_data_idx = VALUES_LIST.index(y) #indexing y
	
	x_label = VALUES_NAMES[x_data_idx] 
	y_label = VALUES_NAMES[y_data_idx]
	
	pylab.xlabel(x_label)   # label x axis
	pylab.ylabel(y_label)   # label y axis
	pylab.title("{} vs {}".format(x_label, y_label))   

	x_data = [data[state][x_data_idx] for state in data]
	y_data = [data[state][y_data_idx] for state in data]
	
	for i,state in enumerate(data.keys()): #loop for state 
		pylab.scatter(x_data[i], y_data[i])
		pylab.annotate(state, (x_data[i],y_data[i]))

	plot_regression(x_data,y_data)

	pylab.show()                # displays the plot


def open_file():
	#Asks user for file name and returns file object
	while True:
		file_name = input("Input file name: ")
		try:
			file = open(file_name)
			return file
		except:
			print("Error opening file. Please try again.")


def get_region_data(file):
	#Takes data file, asks user for region and returns dictionary with region data

	data = {}

	while True:
		region = input(PROMPT1).lower()
		if region in LOWER_REGIONS:
			break
		else:
			print("Error in region name. Please try again.")

	file.readline()  # skip first line
	while True:
		raw_data = file.readline().rstrip()
		if not raw_data:
			break
		raw_data = raw_data.split(',')
		if region == 'all' or raw_data[1].lower() == region:
			state = raw_data[0]
			state_data = [float(number) for number in raw_data[2:]]
			state_data.append(state_data[1] / state_data[0] * 1000)  # calculate GDPp
			state_data.append(state_data[2] / state_data[0] * 1000)  # calculate PIp
			data[state] = state_data

	return data


def print_data(data):
	#Takes region data and represents it
	states = list(data.keys())
	gdpp_sorted = sorted(states, key=lambda x: data[x][6])  #sorting gdpp
	pip_sorted = sorted(states, key=lambda x: data[x][7])   #sorting pip
	print("State with the highest GDP per capita: {} - ${:,.2f}"  #print statement
		  .format(gdpp_sorted[-1], data[gdpp_sorted[-1]][6]))

	print("State with the lowest GDP per capita: {} - ${:,.2f}"  #print statement
		  .format(gdpp_sorted[0], data[gdpp_sorted[0]][6]))

	print("State with the highest Income per capita: {} - ${:,.2f}"  #print statement
		  .format(pip_sorted[-1], data[gdpp_sorted[-1]][7]))

	print("State with the lowest Income per capita: {} - ${:,.2f}"  #print statement
		  .format(pip_sorted[0], data[gdpp_sorted[0]][7]))

	print()
	print("{:^20}{:^14}{:^11}{:^10}{:^11}"                          # header
		  "{:^17}{:^10}{:^15}{:^16}".format("State", *VALUES_NAMES))

	for state in sorted(data.keys()):
		print("{:^20}{:^14,.2f}{:^11,.2f}{:^10,.2f}{:^11,.2f}"
			  "{:^17,.2f}{:^10,.2f}{:^15,.2f}{:^16,.2f}".format(state, *data[state]))


def plot_data(data):
	#Takes data, asks user for x, y axis and plots data
	while True:
		vals = input(PROMPT2)
		try: 
			x, y = vals.split()#splitting values
		except:
			print("Invalid input. Try again.")
			continue
		if x in VALUES_LIST and y in VALUES_LIST: #condtion
			break
		else:
			print("Invalid input. Try again.")
	plot(x, y, data)


def main():
	#main function. Implements algorithm in header
       #calling functions
	csv_file = open_file()
	reg_data = get_region_data(csv_file)
	print_data(reg_data)

	if input("Input 'yes' if you want to plot results: ") == 'yes':
		plot_data(reg_data)

if __name__ == "__main__":
    main()
    
# Questions
# Q1: 5
# Q2: 3
# Q3: 4
# Q4: 6
# Q5: 7