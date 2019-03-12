# Date: Spring 2016
# Author: Michael Berk
# Description: This file will webscrape the box scores from mlb.com


#import libraries
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

 #Constants
waitTime = 4
d.implicitly_wait(10)
d.get("https://www.mlb.com/scores")

#Parameters: date wanted
#Return: NA
#Purpose: change the page so that the current date is correct
def getDate(date):
	#handle dates
	wantedDate = datetime.datetime.strptime(date,"%m.%d.%Y")
	currentDate = datetime.datetime.now() 

	#keep searching for date until correct one is found
	while currentDate.month != wantedDate.month or currentDate.day != wantedDate.day:
		#if need to go back
		if (currentDate > wantedDate):
			currentDate -= datetime.timedelta(days = 1) 
			d.find_element_by_xpath(".//*[@id='scores_index']/main/div/div/div/div/div[3]/div[1]/div[1]/div[1]/button").click()
			print currentDate
		else:
			currentDate += datetime.timedelta(days = 1) 
			d.find_element_by_xpath(".//*[@id='scores_index']/main/div/div/div/div/div[3]/div[1]/div[1]/div[3]/button").click()
			print currentDate
			
#Parameters: NA
#Return: list of all box score buttons 
#Purpose: get all box score buttons on a page
def getBoxButtons():
	#wiat for page to load
	backButton = WebDriverWait(d, 15).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='scores_index']/main/div/div/div/div/section[1]/ul[1]/li[1]/button")))
	
	#get all buttons (this handles the page loading)
	allButtons = []
	for i in range(1,100):
		allButtons = d.find_elements_by_tag_name("button")	
		print len(allButtons)
	boxButtons = []

	#get box score buttons
	for b in range(0,len(allButtons)):
		print allButtons[b].text
		if allButtons[b].text.replace(" ","") == "Box":
			boxButtons.append(allButtons[b])
			print True

	#return box buttons
	return boxButtons

#Parameters: NA 
#Return: a tuple containing an array with batter data and an array containing batter hitting data (2B) - triples are not in the data
#Purpose: get all batters box score data
def getBatters():
	#set up array and wait
	batters = []
	extraBatters = []
	elem = WebDriverWait(d, 15).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='boxscore']/div/div/div[2]/section[1]/section/table/thead/tr/th[1]")))

	#iterate through teams
	for j in range(1,3):
		#get header
		header = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/div[1]/section[" + str(j) + "]/section/table/thead/tr").text.upper().replace(" ","@")
		header = header.replace("@BATTERS","")
		header += "@" + "TEAM" + "@" + "OPPTEAM"
		print header
		batters.append(header)

		#iterate through rows
		for i in range(1,100):
			elem = WebDriverWait(d, 15).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='boxscore']/div/div/div[1]/section["+str(j)+"]/section/table/thead/tr/th[1]")))
			try:
				#get team and oppteam
				team = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/div[1]/section["+str(j)+"]/section/table/thead/tr/th[1]").text.upper()
				oppTeam = ""
				if j == 1:
					oppTeam = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/div[1]/section["+str(2)+"]/section/table/thead/tr/th[1]").text.upper()
				elif j == 2:
					oppTeam = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/div[1]/section["+str(1)+"]/section/table/thead/tr/th[1]").text.upper()

				#get batter data
				batterRow = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/div[1]/section["+str(j)+"]/section/table/tbody/tr[" +str(i) + "]").text.upper()
				batterRow = batterRow.replace(" ","@")	
				batterRow = batterRow.replace(" BATTERS","")	
				batterRow = batterRow + "@" + team + "@" + oppTeam
				batterRow = batterRow.replace(u'\xc1',"A")	
				batterRow = batterRow.replace(u'\xcd',"I")	
				batterRow = batterRow.replace(u'\xd1',"N")	
				batterRow = batterRow.replace(u'\xc9',"E")	
				batterRow = batterRow.replace(u'\xd3',"O")	
				batters.append(batterRow)
				print batterRow
			except:
				print "getBatters: could not find row"
				break

		#get the extra batter data
		extra = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/div[1]/section["+str(j)+"]/section/div[2]").text.upper()
		extraBatters.append(extra)
		print extra

	return [batters, extraBatters]

#Parameters: NA 
#Return: a tuple containing an array with pitcher data and an array containing batter hitting data (2B) - triples are not in the data
#Purpose: get all batters box score data
def getPitchers():
	#set up array and wait
	pitchers = []
	extraPitchers = []
	elem = WebDriverWait(d, 15).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='boxscore']/div/div/div[2]/section[1]/section/table/thead/tr/th[1]")))

	#iterate through teams
	for j in range(1,3):
		#get header
		header = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/div[2]/section["+str(j)+"]/section/table/thead/tr").text.upper().replace(" ","@")
		header = header.replace("@PITCHERS","")
		header += "@" + "TEAM" + "@" + "OPPTEAM"
		print header
		pitchers.append(header)

		#iterate through rows
		for i in range(1,100):
			elem = WebDriverWait(d, 15).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='boxscore']/div/div/div[1]/section["+str(j)+"]/section/table/thead/tr/th[1]")))
			try:
				#get team and oppteam
				team = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/div[2]/section["+str(j)+"]/section/table/thead/tr/th[1]").text.upper()
				oppTeam = ""
				if j == 1:
					oppTeam = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/div[2]/section["+str(2)+"]/section/table/thead/tr/th[1]").text.upper()
				elif j == 2:
					oppTeam = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/div[2]/section["+str(1)+"]/section/table/thead/tr/th[1]").text.upper()

				#get pitcher data
				pitcherRow = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/div[2]/section["+str(j)+"]/section/table/tbody/tr["+str(i)+"]").text.upper()
				pitcherRow = pitcherRow.replace(" ","@")	
				pitcherRow = pitcherRow.replace(" PITCHERS","")	
				pitcherRow = pitcherRow.replace(u'\xc1',"A")	
				pitcherRow = pitcherRow.replace(u'\xd1',"N")	
				pitcherRow = pitcherRow.replace(u'\xc9',"E")	
				pitcherRow = pitcherRow.replace(u'\xd3',"O")	
				pitcherRow = pitcherRow.replace(u'\xcd',"I")	
				pitcherRow = pitcherRow + "@" + team + "@" + oppTeam
				pitchers.append(pitcherRow)
				print pitcherRow
			except:
				print "getPitchers: could not find row"
				break

	#get the extra pitcher data
	extra = d.find_element_by_xpath(".//*[@id='boxscore']/div/div/section[1]/div").text.upper()
	extraPitchers.append(extra)
	print extra

	return [pitchers, extraPitchers]

#Parameters: name that will be used in the file path, data, date for filename
#Return: NA 
#Purpose: write to file based on array and name
def writeToFile(fileName, array, date):
	goodDate = date[:-5]
	fullName = fileName + goodDate 
	print "-----------------------------------------"
	print "Writing to file: " + fullName
	print "-----------------------------------------"
	f = open("/Users/michaelberk/Documents/MLB/2017 Data/"+fileName+"/"+fullName+".txt", "w").close()
	f = open("/Users/michaelberk/Documents/MLB/2017 Data/"+fileName+"/"+fullName+".txt", "a")

	for a in array:
		f = open("/Users/michaelberk/Documents/MLB/2017 Data/"+fileName+"/"+fullName+".txt", "a")
		print a
		f.write(a+"\n")
	f.close()

#Parameters: NA 
#Return: NA
#Purpose: handle popups
def handlePopups():
	#handle "take survey" popup
	try:
		d.implicitly_wait(1)
		d.find_element_by_xpath(".//*[@id='scores_index']/div[7]/div[1]/button").click()
		d.implicitly_wait(10)
	except:
		print "No \"Take Survey\" Popup"

#Parameters: array to be printed
#Return: NA
#Purpose: print contents of list
def printList(l): 
	print "Started printing list"
	for e in l:
		print e
	print "Finished printing list"

#Parameters: date wanted, formatted: 05.12.17
#Return: NA
#Purpose: get the box score for a specified date
def getBoxScore(date):
	#set up arrays
	batters = []
	extraBatters = []
	pitchers = []
	extraPitchers = []

	#go to correct page
	getDate(date)

	#handle popups
	handlePopups()

	#get the box score buttons
	boxButtons = getBoxButtons()

	for i in range(0, len(boxButtons)):
		#handle popups
		handlePopups()
		
		#handle popups
		handlePopups()

		#get the box score buttons
		boxButtons = getBoxButtons()

		#click the box score button
		boxButtons[i].click()

		#getBatters and pitchers
		b = getBatters()
		p = getPitchers()
		batters = batters + b[0]
		extraBatters = extraBatters + b[1]
		pitchers = pitchers + p[0]
		extraPitchers = extraPitchers + p[1]

		#go back
		d.back()
		getDate(date)


	#write to file
	writeToFile("BatterBox", batters, date)
	writeToFile("PitcherBox", pitchers, date)
	writeToFile("BatterBoxExtra", extraBatters, date)
	writeToFile("PitcherBoxExtra", extraPitchers, date)
	

#get boxes
dates = ["06.15.2017","06.16.2017","06.17.2017","06.18.2017","06.19.2017","06.20.2017",]
for ddd in dates:
	getBoxScore(ddd)

d.quit()


