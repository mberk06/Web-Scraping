# Date: Spring 2018
# Author: Michael Berk
# Description: This file will read in the box scores from NBA.com to be used for team analysis - I will be attempting to predict spreads based on this data

#Set up
import datetime
from datetime import date, timedelta
import time

import selenium as sl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By


########################################################################
#Constants
d = webdriver.Chrome("/Users/michaelberk/Documents/Selenium/chromedriver")
waitTime = 3  
d.implicitly_wait(waitTime)   
baseURL = "http://stats.nba.com/scores#!/"

#get range of dates 
openingDay = datetime.datetime(2017, 10, 17)
today = datetime.datetime.today()
allDates = [openingDay + timedelta(days=x) for x in range((today-openingDay).days + 1)]
allDates = ["{:%m/%d/%Y}".format(date) for date in allDates]

class NBAScrape():

	#Variables
	def __init__(self):
		self.data = []

	#############################################
	#Purpose: iterate through the box score buttons and call "getBoxScore()" to get the box score
	#Parameters: NA
	#Return: NA
	def runIt(self):
            #iterate through all dates of 2016-2017 season
            for date in allDates:
                    print("gettting date: " + str(date))
                    d.get(baseURL + date)
                    time.sleep(waitTime)
    
                    #wait for the page to loaded
                    loaded = False
                    while (loaded):
                            try:
                                    testElem = d.find_element_by_xpath(".//*[@id='scoresPage']/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/a[1]")
                                    loaded = True 
                            except:
                                    time.sleep(0.25)

                    for i in range(3,18):	
                            #scroll to the top of the page
                            d.execute_script("window.scrollTo(0, 0)")
            
                            #try to click the box score button
                            try:
                                    d.find_element_by_xpath(".//*[@id='scoresPage']/div[2]/div[1]/div/div/div["+str(i)+"]/div[2]/div[1]/div/div[2]/div/a[1]").click()
                                    array = self.getBoxScore(date)
                                    self.data.append(array[0])
                                    self.data.append(array[1])
                                    d.back()
                            except:
                                    print("runIt: could not find box score button")
                                    break
            #write to file
            self.writeToFile()

	#Purpose: get team, oppTeam, and game totals and return them
	#Parameters: NA
	#Return: array of length 2 with each teams stat line in place array of length 2 with each teams stat line in place
	def getBoxScore(self, date):	
		while (not self.boxScoreIsLoaded()):
			time.sleep(0.1)

		#get teams
		team1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a").text
		team2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[1]/div[1]/a").text

		#get stat totals team 1
		fgm1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[3]").text
		fga1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[4]").text
		x3pm1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[6]").text
		x3pa1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[7]").text
		fta1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[9]").text
		ftm1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[10]").text
		oreb1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[12]").text
		dreb1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[13]").text
		reb1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[14]").text
		ast1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[15]").text
		tov1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[16]").text
		stl1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[17]").text
		blk1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[18]").text
		pf1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[19]").text
		pts1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[20]").text
		pm1 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[1]/div[2]/div[1]/table/tfoot/tr/td[21]").text

		#get stat totals team 2
		fgm2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[3]").text
		fga2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[4]").text
		x3pm2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[6]").text
		x3pa2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[7]").text
		fta2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[9]").text
		ftm2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[10]").text
		oreb2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[12]").text
		dreb2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[13]").text
		reb2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[14]").text
		ast2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[15]").text
		tov2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[16]").text
		stl2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[17]").text
		blk2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[18]").text
		pf2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[19]").text
		pts2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[20]").text
		pm2 = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/nba-stat-table[2]/div[2]/div[1]/table/tfoot/tr/td[21]").text

		#get stat lines
		stats1 = team1 + "@" + team2 + "@" + fgm1 + "@" + fga1 + "@" + x3pm1 + "@" + x3pa1 + "@" + fta1 + "@" + ftm1 + "@" + oreb1 + "@" + dreb1 + "@" + reb1 + "@" + ast1 + "@" + tov1 + "@" + stl1 + "@" + blk1 + "@" + pf1 + "@" + pts1 + "@" + pm1 + "@" + "FALSE" + "@" + date
		stats2 = team2 + "@" + team1 + "@" + fgm2 + "@" + fga2 + "@" + x3pm2 + "@" + x3pa2 + "@" + fta2 + "@" + ftm2 + "@" + oreb2 + "@" + dreb2 + "@" + reb2 + "@" + ast2 + "@" + tov2 + "@" + stl2 + "@" + blk2 + "@" + pf2 + "@" + pts2 + "@" + pm2 + "@" + "TRUE" + "@" + date
		
		#return stat lines
		print(stats1)
		print(stats2)
		return [stats1, stats2]
	
	def writeToFile(self):
		f = open("/Users/michaelberk/Documents/NBA Data/2017-2018TeamTotals.txt", "w").close()
		f = open("/Users/michaelberk/Documents/NBA Data/2017-2018TeamTotals.txt","a")
		for i in range(0, len(self.data)):
			f.write(self.data[i] + '\n')
		f.close()
		
	#Purpose: go to given url
	#Parameters: desired url 
	#Return: NA
	def getURL(self, URL):
		d.get(URL)

	#Purpose: count the number of games played on given date 
        #Parameters: NA 
	#Return: number of games on given date 
	def countGames(self):
		num = 0
		for i in range(3,20):
			try:
				d.find_element_by_xpath(".//*[@id='scoresPage']/div[2]/div[1]/div/div/div["+str(i)+"]/div[1]/div/div[1]")
				num = 1 + num
			except:
				return num
		return -1

	#Purpose: count the number of rows in "data"
	#Parameters: NA
	#Return: number of rows in "data"
	def countDataRows(self):
		return len(data)
	
	#Purpose: check if the box scores list page has been loaded
	#Parameters: NA
	#Return: T if can locate frist elem on top box, F if not
	def boxScoreListIsLoaded(self):
		try:
			d.find_element_by_xpath(".//*[@id='scoresPage']/div[2]/div[1]/div/div/div[3]/div[2]/div[1]/div/div[1]/table/tbody/tr[2]/td[3]")
			return True 
		except:
			return False

	#Purpose: check if the box scores have loaded (this will be used for testing)
	#Parameters: NA
	#Return: T if can locate last elem on bottom box, F if not
	def boxScoreIsLoaded(self):
		try:
			d.find_element_by_xpath("html/body/main/div[2]/div/div/div[4]/div/div[2]/div/div[10]/div[1]")
			return True 
		except:
			return False

c = NBAScrape()
c.runIt()












