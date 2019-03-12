# Date: Fall 2017
# Author: Michael Berk
# Description: This file will be used to acquire draft data from MLB.com

#libraries
import datetime
import time

import selenium as sl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
d = webdriver.Chrome()

#Create the url array
origionalURL = "http://mlb.mlb.com/mlb/events/draft/y2007/drafttracker.jsp?p=0&s=30&sc=pick_number&so=ascending&st=number&ft=RD&fv=15"
urls = [origionalURL]
year = ["2007","2008","2009","2010","2011"]
years = ["2012","2013"]
#change year
for i in years:
	#change round
	array = ["PICK,TEAM,LAST,FIRST,SCHOOL,POS,HANDED,HEIGHT,WEIGHT,BDAY,YEAR"]
	for j in range (1,41):
		temp = origionalURL
		temp = temp[:-1]
		if (temp[-1] != "="):
			temp = temp[:-1]
		preYear = temp[:37]
		postYear = temp[41:]
		temp = preYear + i + postYear
		temp += str(j)
		print temp
		d.get(temp)
		for y in range(1,100):
			string = ""
			for x in range(1,11):
				try:
					p = ".//*[@id='mc']/table/tbody/tr[2]/td/table/tbody/tr["+str(y)+"]/td["+str(x)+"]"
					path = ".//*[@id='mc']/div[3]/table/tbody/tr[2]/td/table/tbody/tr["+str(y)+"]/td["+str(x)+"]"
					t = d.find_element_by_xpath(path).text
					print "tt" + t + "tt"
					string += t 
					if (x != 10):
						string += ","
				except:
					print "Could not find row"
					break

			if "Comments:" not in string:
				if (string != ""):
					isValid = True
					for c in string:
						if (ord(c) < 1) or (ord(c) > 126):
							print "ERROR!!!!!!!!!!!"
							print string
							isValid = False
							print "ERROR!!!!!!!!!!!"
					if isValid:
						array.append(string)
						print "ll" + string + "ll"
	name = "/Users/michaelberk/Documents/MLB/DraftData/" + i + ".csv"	
	f = open(name,"w").close()
	f = open(name,"a")
	for i in range(0, len(array)):
		f.write(array[i]+"\n")
	f.close()














	
