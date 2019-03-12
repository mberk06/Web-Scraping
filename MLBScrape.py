# Date: 2017 MLB Season
# Author: Michael Berk
# Description: this code will web scrape mlb team data usign selenium python

#########################################################
####################### Setup ###########################
#########################################################
#this section will set up the libraries, create constants, and get the date

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

#Constants
waitTime = 3
d.implicitly_wait(waitTime)
dateFormat = "%a,%b%d,%Y"

#########################################################
######################## Helpers ########################
#########################################################
badTeams = ["MIAMI@MARLINS","LOS@ANGELES@ANGELS","BOSTON@RED@SOX","SEATTLE@MARINERS","DETROIT@TIGERS","WASHINGTON@NATIONALS","CHICAGO@CUBS","ST.@LOUIS@CARDINALS","OAKLAND@ATHLETICS","HOUSTON@ASTROS","CINCINNATI@REDS","CHICAGO@WHITE@SOX","BALTIMORE@ORIOLES","NEW@YORK@METS","ARIZONA@DIAMONDBACKS","KANSAS@CITY@ROYALS","TAMPA@BAY@RAYS","NEW@YORK@YANKEES","MINNESOTA@TWINS","ATLANTA@BRAVES","PHILADELPHIA@PHILLIES","LOS@ANGELES@DODGERS","COLORADO@ROCKIES","PITTSBURGH@PIRATES","TEXAS@RANGERS","SAN@FRANCISCO@GIANTS","MILWAUKEE@BREWERS","TORONTO@BLUE@JAYS","CLEVELAND@INDIANS","SAN@DIEGO@PADRES","TOR@BLUE@JAYS"]
goodTeams = ["MIAMI MARLINS","LOS ANGELES ANGELS","BOSTON RED SOX","SEATTLE MARINERS","DETROIT TIGERS","WASHINGTON NATIONALS","CHICAGO CUBS","ST LOUIS CARDINALS","OAKLAND ATHLETICS","HOUSTON ASTROS","CINCINNATI REDS","CHICAGO WHITE SOX","BALTIMORE ORIOLES","NEW YORK METS","ARIZONA DIAMONDBACKS","KANSAS CITY ROYALS","TAMPA BAY RAYS","NEW YORK YANKEES","MINNESOTA TWINS","ATLANTA BRAVES","PHILADELPHIA PHILLIES","LOS ANGELES DODGERS","COLORADO ROCKIES","PITTSBURGH PIRATES","TEXAS RANGERS","SAN FRANCISCO GIANTS","MILWAUKEE BREWERS","TORONTO BLUE JAYS","CLEVELAND INDIANS","SAN DIEGO PADRES","TOR@BLUE JAYS"] 

def cleanTeams(array):
	a = array
	for i in range(0,len(array)):
		for j in range(0,len(badTeams)):
			a[i] = a[i].upper()
			a[i] = a[i].replace(badTeams[j],goodTeams[j])
	return a

def cleanPlayers(array):
	a = array
	for i in range(0,len(array)):
		#replace bad players	
		a[i] = a[i].replace("DE@LA@ROSA, J","DE LA ROSA, J")
		a[i] = a[i].replace("DE@LA@ROSA,@J","DE LA ROSA@J")
		a[i] = a[i].replace("DE@LA@ROSA,@JORGE","DE LA ROSA@JORGE")
		a[i] = a[i].replace("LA@STELLA, T","LA STELLA, T")
		a[i] = a[i].replace("LA@STELLA,@T","LA STELLA,@T")
		a[i] = a[i].replace("LA@STELLA,@T","LA STELLA@T")
		a[i] = a[i].replace("VAN@SLYKE, S","VAN SLYKE@S")
		a[i] = a[i].replace("VAN@SLYKE,@S","VAN SLYKE@S")
		a[i] = a[i].replace("SCOTT@VAN@SLYKE","SCOTT@VAN SLYKE")
		a[i] = a[i].replace("KIM, HYUN@SOO","KIM HYUN SOO")
		a[i] = a[i].replace("KIM,@HYUN@SOO","KIM@HYUN SOO")
		a[i] = a[i].replace("HYUN@SOO@KIM","KIM@HYUN SOO")
		a[i] = a[i].replace("OH,@SEUNG@HWAN","OH,@SEUNG HWAN")
		a[i] = a[i].replace("DE@JONG,@CHASE","DE JONG@CHASE")
		a[i] = a[i].replace("DE@JONG,@C","DE JONG@C")
		a[i] = a[i].replace("DE@JONG, C","DE JONG C")
		
	return a

#########################################################
######## Get Box Scores for Batters and Pitchers ########
#########################################################
def getBoxScore(date):
	#create batter return array and pitcher return array - include team batter = [] pitcher = [] 
	#go to selected date on mlb.com
	d.get("URL")

	#get all div tags and save those with "Box" as text
	divs = d.find_elements_by_tag_name("div")
	boxes = []
	for d in divs:
		if (d.text == "Box"):
			boxes.append(d) 
	
	#iterate through saved div tags
	for b in boxes:
		#click on div tag
		b.click()

		#read batter box score

		#read pitcher box score

		#go back to webpage
		d.back()

	#return the data as a tuple
	return [batter, pitcher]

#########################################################
################ MLB.com Stats for Hitters ##############
#########################################################
def getYesterdayBatter(HomeOrAway):
	#data list
	yesterdayBatter = ["RK.B.YEST@LAST.B.YEST@FIRST.B.YEST@TEAM.B.YEST@POS.B.YEST@G.B.YEST@AB.B.YEST@R.B.YEST@H.B.YEST@X2B.B.YEST@X3B.B.YEST@HR.B.YEST@RBI.B.YEST@BB.B.YEST@SO.B.YEST@SB.B.YEST@CS.B.YEST@AVG.B.YEST@OBP.B.YEST@SLG.B.YEST@OPSRK.B.YEST@LAST.B.YEST@FIRST.B.YEST@TEAM.B.YEST@POS.1.B.YEST@IBB.B.YEST@HBP.B.YEST@SAC.B.YEST@SF.B.YEST@TB.B.YEST@XBH.B.YEST@GDP.B.YEST@GO.B.YEST@AO.B.YEST@GO_AO.B.YEST@NP.B.YEST@PA.B.YEST"]
	for i in range(0,1300):
		yesterdayBatter.append("XXX")

	#Go to webpage - URL is up to date
	d.get("http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+hitting&game_type='R'&season=2017&season_type=ANY&league_code='MLB'&sectionType=sp&statType=hitting&page=1&ts=1491923486084")

	#Make sure that the page loaded is "Yesterday" games
	d.find_element_by_xpath(".//*[@id='d1']").click()

	#Get Home or Away
	dropDown = Select(d.find_element_by_id('sp_hitting_hitting_splits'))
	if (HomeOrAway == "Home"):
		dropDown.select_by_visible_text("Home Games")
	elif (HomeOrAway == "Away"):
		dropDown.select_by_visible_text("Away Games")
	elif (HomeOrAway == ""):
		print "getYesterdayBatter: No split selected"
	else:
		print "ERROR: incorrect parameter"
		return yesterdayBatter 
	
	for l in range(0,100):
		#Create scale and starting value
		scale = l * 50
		startingVal = 1

		#Get Stats and put them into list 
		time.sleep(waitTime)
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")

		#Read data
		for i in range(startingVal,len(rows)):
			table = d.find_element_by_id("datagrid")
			rows = table.find_elements_by_tag_name("tr")
			yesterdayBatter[i + scale] = rows[i].text.upper().replace(" ","@")
			yesterdayBatter[i + scale] = yesterdayBatter[i + scale].replace("@@","@")	
			yesterdayBatter[i + scale] = yesterdayBatter[i + scale].replace("@JR"," JR")
			yesterdayBatter[i + scale] = yesterdayBatter[i + scale].replace("@SR"," SR")

		#Get Other Statistics
		d.find_element_by_xpath(".//*[@id='stats_next']").click()
		time.sleep(waitTime)
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
		for i in range(startingVal,len(rows)):
			table = d.find_element_by_id("datagrid")
			rows = table.find_elements_by_tag_name("tr")
			yesterdayBatter[i + scale] += rows[i].text.upper().replace(" ","@")
			yesterdayBatter[i + scale] = yesterdayBatter[i + scale].replace("@@","@")	
			yesterdayBatter[i + scale] = yesterdayBatter[i + scale].replace(u"\u25BC","")	
			yesterdayBatter[i + scale] = yesterdayBatter[i + scale].replace(u"\u25B2","")	
			yesterdayBatter[i + scale] = yesterdayBatter[i + scale].replace("@JR"," JR")
			yesterdayBatter[i + scale] = yesterdayBatter[i + scale].replace("@SR"," SR")
			print yesterdayBatter[i + scale]

		#Go to next page 	 
		try:
			d.find_element_by_class_name("paginationWidget-next").click()
		except:
			break

	#Clean and return list
	yesterdayBatter = [x for x in yesterdayBatter if x != "XXX"]
	return yesterdayBatter

def getLast7Batter(HomeOrAway):	
	#data list
	last7Batter = ["RK.B.LW@LAST.B.LW@FIRST.B.LW@TEAM.B.LW@POS.B.LW@G.B.LW@AB.B.LW@R.B.LW@H.B.LW@X2B.B.LW@X3B.B.LW@HR.B.LW@RBI.B.LW@BB.B.LW@SO.B.LW@SB.B.LW@CS.B.LW@AVG.B.LW@OBP.B.LW@SLG.B.LW@OPSRK.B.LW@LAST.B.LW@FIRST.B.LW@TEAM.B.LW@POS.1.B.LW@IBB.B.LW@HBP.B.LW@SAC.B.LW@SF.B.LW@TB.B.LW@XBH.B.LW@GDP.B.LW@GO.B.LW@AO.B.LW@GO_AO.B.LW@NP.B.LW@PA.B.LW"]
	for i in range(0,1300):
		last7Batter.append("XXX")

	#Go to webpage - URL is up to date 
	d.get("http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+hitting&game_type='R'&season=2017&season_type=ANY&league_code='MLB'&sectionType=sp&statType=hitting&page=1&ts=1491923486084")

	#Make sure that the page loaded is "Last 7" games
	d.find_element_by_xpath(".//*[@id='d7']").click()

	#Get Home or Away
	dropDown = Select(d.find_element_by_id('sp_hitting_hitting_splits'))
	if (HomeOrAway == "Home"):
		dropDown.select_by_visible_text("Home Games")
	elif (HomeOrAway == "Away"):
		dropDown.select_by_visible_text("Away Games")
	elif (HomeOrAway == ""):
		print "getLast7Batter: No split selected"
	else:
		print "ERROR: incorrect parameter"
		return last7Batter 
	
	for l in range(0,100):
		#Create scale and starting value
		scale = l * 50
		startingVal = 1

		#Get Stats and put them into list 
		time.sleep(waitTime)
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")

		#Read data
		time.sleep(waitTime)
		for i in range(startingVal,len(rows)):
			table = d.find_element_by_id("datagrid")
			rows = table.find_elements_by_tag_name("tr")
			last7Batter[i + scale] = rows[i].text.upper().replace(" ","@")
			last7Batter[i + scale] = last7Batter[i + scale].replace("@@","@")	
			last7Batter[i + scale] = last7Batter[i + scale].replace("@JR"," JR")
			last7Batter[i + scale] = last7Batter[i + scale].replace("@SR"," SR")

		#Get Other Statistics
		d.find_element_by_xpath(".//*[@id='stats_next']").click()
		time.sleep(waitTime)
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
		for i in range(startingVal,len(rows)):
			table = d.find_element_by_id("datagrid")
			rows = table.find_elements_by_tag_name("tr")
			last7Batter[i + scale] += rows[i].text.upper().replace(" ","@")
			last7Batter[i + scale] = last7Batter[i + scale].replace("@@","@")	
			last7Batter[i + scale] = last7Batter[i + scale].replace(u"\u25BC","")	
			last7Batter[i + scale] = last7Batter[i + scale].replace(u"\u25B2","")	
			last7Batter[i + scale] = last7Batter[i + scale].replace("@JR"," JR")
			last7Batter[i + scale] = last7Batter[i + scale].replace("@SR"," SR")
			print last7Batter[i + scale]

		#Go to next page 	 
		try:
			d.find_element_by_class_name("paginationWidget-next").click()
		except:
			break

	#Clean and return list
	last7Batter = [x for x in last7Batter if x != "XXX"]
	return last7Batter

def getLastMonthBatter(split):
	#data list
	lastMonthBatter = ["RK.B.LM@LAST.B.LM@FIRST.B.LM@TEAM.B.LM@POS.B.LM@G.B.LM@AB.B.LM@R.B.LM@H.B.LM@X2B.B.LM@X3B.B.LM@HR.B.LM@RBI.B.LM@BB.B.LM@SO.B.LM@SB.B.LM@CS.B.LM@AVG.B.LM@OBP.B.LM@SLG.B.LM@OPSRK.B.LM@LAST.B.LM@FIRST.B.LM@TEAM.B.LM@POS.1.B.LM@IBB.B.LM@HBP.B.LM@SAC.B.LM@SF.B.LM@TB.B.LM@XBH.B.LM@GDP.B.LM@GO.B.LM@AO.B.LM@GO_AO.B.LM@NP.B.LM@PA.B.LM"]
	for i in range(0,1300):
		lastMonthBatter.append("XXX")

	#Go to webpage - URL is up to date 
	d.get("http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+hitting&game_type='R'&season=2017&season_type=ANY&league_code='MLB'&sectionType=sp&statType=hitting&page=1&ts=1491924143972")
	
	#Get vs. Left or vs. Right
	dropDown = Select(d.find_element_by_id('sp_hitting_hitting_splits'))
	if (split == "Left"):
		dropDown.select_by_visible_text("vs Left")
	elif (split == "Right"):
		dropDown.select_by_visible_text("vs Right")
	elif (split == "Home"):
		dropDown.select_by_value('h')
	elif (split == "Away"):
		dropDown.select_by_visible_text("Away Games")
	elif (split == ""):
		print "getLastMonthBatter: No split selected"
	else:
		print "ERROR: incorrect parameter"
		return lastMonthBatter

	#Make sure that the page loaded is "Last Month" games
	d.find_element_by_xpath(".//*[@id='d30']").click()
	
	for l in range(0,100):
		#Create scale and starting value
		scale = l * 50
		startingVal = 1

		#Read data
		time.sleep(waitTime)
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
		for i in range(startingVal,len(rows)):
			while (True):
				try:
					table = d.find_element_by_id("datagrid")
					rows = table.find_elements_by_tag_name("tr")
					break
				except:
					continue
			lastMonthBatter[i + scale] = rows[i].text.upper().replace(" ","@")
			lastMonthBatter[i + scale] = lastMonthBatter[i + scale].replace("@@","@")	
			lastMonthBatter[i + scale] = lastMonthBatter[i + scale].replace("@JR"," JR")
			lastMonthBatter[i + scale] = lastMonthBatter[i + scale].replace("@SR"," SR")

		#Get Other Statistics
		d.find_element_by_xpath(".//*[@id='stats_next']").click()
		time.sleep(waitTime)
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
	
		for i in range(startingVal,len(rows)):
			while (True):
				try:
					table = d.find_element_by_id("datagrid")
					rows = table.find_elements_by_tag_name("tr")
					break
				except:
					continue
			lastMonthBatter[i + scale] += rows[i].text.upper().replace(" ","@")
			lastMonthBatter[i + scale] = lastMonthBatter[i + scale].replace("@@","@")	
			lastMonthBatter[i + scale] = lastMonthBatter[i + scale].replace(u"\u25BC","")	
			lastMonthBatter[i + scale] = lastMonthBatter[i + scale].replace(u"\u25B2","")	
			lastMonthBatter[i + scale] = lastMonthBatter[i + scale].replace("@JR"," JR")
			lastMonthBatter[i + scale] = lastMonthBatter[i + scale].replace("@SR"," SR")
			print lastMonthBatter[i + scale]

		#Go to next page 	 
		try:
			d.find_element_by_class_name("paginationWidget-next").click()
		except:
			break
		time.sleep(waitTime)
	
	#Clean and return list
	lastMonthBatter = [x for x in lastMonthBatter if x != "XXX"]
	return lastMonthBatter

def getYTDBatter(split):
	#data list
	YTDBatter = ["RK.B.YTD@LAST.B.YTD@FIRST.B.YTD@TEAM.B.YTD@POS.B.YTD@G.B.YTD@AB.B.YTD@R.B.YTD@H.B.YTD@X2B.B.YTD@X3B.B.YTD@HR.B.YTD@RBI.B.YTD@BB.B.YTD@SO.B.YTD@SB.B.YTD@CS.B.YTD@AVG.B.YTD@OBP.B.YTD@SLG.B.YTD@OPSRK.B.YTD@LAST.B.YTD@FIRST.B.YTD@TEAM.B.YTD@POS.1.B.YTD@IBB.B.YTD@HBP.B.YTD@SAC.B.YTD@SF.B.YTD@TB.B.YTD@XBH.B.YTD@GDP.B.YTD@GO.B.YTD@AO.B.YTD@GO_AO.B.YTD@NP.B.YTD@PA.B.YTD"]
	for i in range(0,1300):
		YTDBatter.append("XXX")

	#Go to webpage - URL is up to date 
	d.get("http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+hitting&game_type=%27R%27&season=2017&season_type=ANY&league_code=%27MLB%27&sectionType=sp&statType=hitting&page=1&ts=1492984354504&timeframe=&split=&last_x_days=&playerType=ALL")
	
	#Make sure that the page loaded is "YTD" games
	d.find_element_by_xpath(".//*[@id='h0']").click()
	
	#Get vs. Left or vs. Right and change column names
	dropDown = Select(d.find_element_by_id('sp_hitting_hitting_splits'))
	if (split == "Left"):
		dropDown.select_by_visible_text("vs Left")
	elif (split == "Right"):
		dropDown.select_by_visible_text("vs Right")
	elif (split == "Home"):
		dropDown.select_by_value('h')
	elif (split == "Away"):
		dropDown.select_by_visible_text("Away Games")
	elif (split == ""):
		print "getLastMonthBatter: No split selected"
	else:
		print "ERROR: incorrect parameter"
		return YTDBatter

	for l in range(0,100):
		#Create scale and starting value
		scale = l * 50
		startingVal = 1

		#Read data
		time.sleep(waitTime)
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
		for i in range(startingVal,len(rows)):
			while (True):
				try:
					table = d.find_element_by_id("datagrid")
					rows = table.find_elements_by_tag_name("tr")
					break
				except:
					continue
			YTDBatter[i + scale] = rows[i].text.upper().replace(" ","@")
			YTDBatter[i + scale] = YTDBatter[i + scale].replace("@@","@")	
			YTDBatter[i + scale] = YTDBatter[i + scale].replace("@JR"," JR")
			YTDBatter[i + scale] = YTDBatter[i + scale].replace("@SR"," SR")

		#Get Other Statistics
		d.find_element_by_xpath(".//*[@id='stats_next']").click()
		time.sleep(waitTime)
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
	
		for i in range(startingVal,len(rows)):
			while (True):
				try:
					table = d.find_element_by_id("datagrid")
					rows = table.find_elements_by_tag_name("tr")
					break
				except:
					continue
			YTDBatter[i + scale] += rows[i].text.upper().replace(" ","@")
			YTDBatter[i + scale] = YTDBatter[i + scale].replace("@@","@")	
			YTDBatter[i + scale] = YTDBatter[i + scale].replace(u"\u25BC","")	
			YTDBatter[i + scale] = YTDBatter[i + scale].replace(u"\u25B2","")	
			YTDBatter[i + scale] = YTDBatter[i + scale].replace("@JR"," JR")
			YTDBatter[i + scale] = YTDBatter[i + scale].replace("@SR"," SR")
			print YTDBatter[i + scale]

		#Go to next page 	 
		try:
			d.find_element_by_class_name("paginationWidget-next").click()
		except:
			break
		time.sleep(waitTime)
	
	#Clean and return list
	YTDBatter = [x for x in YTDBatter if x != "XXX"]
	return YTDBatter

#########################################################
######## Rotowire Advanced Hitter Stats #################
#########################################################
def getAdvancedBatter():
	#Create return list
	advancedBatter = ["LAST.AB@FIRST.AB@TEAM.AB@POS.AB@G.AB@AB.AB@P/PA.AB@BUNTS.AB@GIDP.AB@IBB.AB@BB.AB@K.AB@BBP.AB@BB/K.AB@CTP.AB@SBOP.AB@AVG.AB@BABIP.AB"]

	#Get URL - URL is up to date 
	d.get("http://www.rotowire.com/baseball/player_ex_stats.htm")
	time.sleep(waitTime * 3)

	#Read data from table
	for i in range(1,1300):
		try:
			row = d.find_element_by_xpath("html/body/div[3]/div[9]/div/table/tbody/tr["+str(i)+"]").text.upper()
			row = row.replace(" ","@")
			row = row.replace("@@","@")
			row = row.replace("@JR"," JR")
			row = row.replace("@SR"," SR")
			advancedBatter.append(row)
			print (advancedBatter[i])
		except:
			print "Could not find row"
			break

	#Return list
	return advancedBatter

#########################################################
######## Rotowire Batter Pitcher Matchups ###############
#########################################################
def getBatterPitcherMatchup():
	#Create return list
	batter = ["FIRST.BPM@LAST.BPM@POS.BPM@TEAM.BPM@ISHOME.BPM@GAMEDATE.BPM@GAMETIME.BPM@AM/PM.BPM@OPP.BPM@PITCHERFIRST.BPM@PITCHERLAST.BPM@AB.BPM@H.BPM@XBH.BPM@HR.BPM@RBI.BPM@BB.BPM@K.BPM@AVG.BPM@OBP.BPM@SLG.BPM@OPS.BPM"]
	pitcher = ["FIRST.PBM@LAST.PBM@TEAM.PBM@ISHOME.PBM@GAMEDATE.PBM@GAMETIME.PBM@AM/PM.PBM@OPP.PBM@BATTERS.PBM@AB.PBM@H.PBM@XBH.PBM@HR.PBM@RBI.PBM@BB.PBM@K.PBM@AVG.PBM@OBP.PBM@SLG.PBM@OPS.PBM"]

	#Get URL - URL is up to date
	d.get("http://www.rotowire.com/baseball/matchup.htm")
	time.sleep(waitTime * 3)

	#Make the min and max ab's 0
	minimum = d.find_element_by_xpath("html/body/div[3]/div[3]/form/div[1]/div[2]/div[1]/input")
	minimum.clear()	
	minimum.send_keys("0")
	maximum = d.find_element_by_xpath("html/body/div[3]/div[3]/form/div[2]/div[2]/div[1]/input")
	maximum.clear()	
	maximum.send_keys("0")
	
	#Change the hot and cold parameters
	for l in range(1,3):
		for i in range(1,4):
			for j in range(1,3):
				box = d.find_element_by_xpath("html/body/div[3]/div[3]/form/div["+str(l)+"]/div[2]/div[2]/div["+str(j)+"]/input["+str(i)+"]")
				box.clear()
				box.send_keys("0")
	maximum.send_keys(Keys.RETURN)

	#Read data from table
	for i in range(1,1300):
		try:
			row = d.find_element_by_xpath("html/body/div[3]/div[4]/div/div[2]/table/tbody/tr["+str(i)+"]").text.upper()
			row = row.replace(" ","@")
			row = row.replace("@@","@")
			row = row.replace("@BATTERS","")
			row = row.replace("RED@SOX","RED SOX")
			row = row.replace("WHITE@SOX","WHITE SOX")
			row = row.replace("@JR"," JR")
			row = row.replace("@SR"," SR")
			row = batter.append(row)
			print (batter[i])
		except:
			print "Could not find row"
			break

	for i in range(1,1300):
		try:
			row = d.find_element_by_xpath("html/body/div[3]/div[8]/div/div[2]/table/tbody/tr["+str(i)+"]").text.upper()
			row = row.replace(" ","@")
			row = row.replace("@@","@")
			row = row.replace("@BATTERS","")
			row = row.replace("RED@SOX","RED SOX")
			row = row.replace("WHITE@SOX","WHITE SOX")
			row = row.replace("@JR"," JR")
			row = row.replace("@SR"," SR")
			pitcher.append(row)
			print (pitcher[i])
		except:
			print "Could not find row"
			break
	#Return list
	return [batter,pitcher]

#########################################################
################## MLB.com Pitcher Stats ################
#########################################################

def getPitcherTraditional(split):
	#Set up return array
	PitcherTraditional = ["RK.P.YTD@LAST.P.YTD@FIRST.P.YTD@TEAM.P.YTD@W.P.YTD@L.P.YTD@ERA.P.YTD@G.P.YTD@GS.P.YTD@SV.P.YTD@SVO.P.YTD@IP.P.YTD@H.P.YTD@R.P.YTD@ER.P.YTD@HR.P.YTD@BB.P.YTD@SO.P.YTD@AVG.P.YTD@WHIP.P.YTD@RK.P.YTD@LAST.P.YTD@FIRST.P.YTD@TEAM.P.YTD@CG.P.YTD@SHO.P.YTD@HB.P.YTD@IBB.P.YTD@GF.P.YTD@HLD.P.YTD@GIDP.P.YTD@GO.P.YTD@AO.P.YTD@WP.P.YTD@BK.P.YTD@SB.P.YTD@CS.P.YTD@PK.P.YTD@TBF.P.YTD@NPIRK.P.YTD@Player.P.YTD@Team.P.YTD@WPCT.P.YTD@GO_AO.P.YTD@OBP.P.YTD@SLG.P.YTD@OPS.P.YTD@K_9.P.YTD@BB_9.P.YTD@H_9.P.YTD@K_BB.P.YTD@P_IP.P.YTD"]
	for i in range(0, 1300):
		PitcherTraditional.append("XXX")	

	#Go to webpage - URL up to date 
	d.get("http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+pitching&game_type=%27R%27&season=2017&season_type=ANY&lea++++gue_code=%27MLB%27&sectionType=sp&statType=pitching&page=1&ts=1491156011066&league_code=%27MLB%27&playerType=QUALIFIER&sportCode=%27mlb%27&split=&team_id=&active_sw=&position=%271%27&page_type=SortablePlayer&sortOrder=%27asc%27&sortColumn=era&results=&perPage=50&timeframe=&last_x_days=&extended=0")

	#Get vs. Left or vs. Right
	dropDown = Select(d.find_element_by_id("sp_pitching_pitching_splits"))
	if (split == "Left"):
		dropDown.select_by_visible_text("vs Left")
	elif (split == "Right"):
		dropDown.select_by_visible_text("vs Right")
	elif (split == "Home"):
		dropDown.select_by_visible_text("Home Games")
	elif (split == "Away"):
		dropDown.select_by_visible_text("Away Games")
	elif (split == ""):
		print "PitcherTraditional: no split selected"
	else:
		print "ERROR: incorrect parameter"
		return PitcherTraditional 
	
	for l in range(0,100):
		#Create scale and starting value
		scale = l * 50
		startingVal = 1 

		#Locate table
		time.sleep(waitTime)
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")

		#Read data
		for i in range(startingVal, len(rows)):
			table = d.find_element_by_id("datagrid")
			rows = table.find_elements_by_tag_name("tr")
			PitcherTraditional[i + scale] = rows[i].text.upper().replace(" ","@")
			PitcherTraditional[i + scale] = PitcherTraditional[i + scale].replace("@@","@")  
			PitcherTraditional[i + scale] = PitcherTraditional[i + scale].replace("@JR"," JR")
			PitcherTraditional[i + scale] = PitcherTraditional[i + scale].replace("@SR"," SR")

		#Get Other Statistics 
		for j in range(1,3):
			d.find_element_by_xpath(".//*[@id='stats_next']").click()
			time.sleep(waitTime)
			table = d.find_element_by_id("datagrid")
			rows = table.find_elements_by_tag_name("tr")
			for i in range(startingVal,len(rows)):
				table = d.find_element_by_id("datagrid")
				rows = table.find_elements_by_tag_name("tr")
				PitcherTraditional[i + scale] += rows[i].text.upper().replace(" ","@")
				PitcherTraditional[i + scale] = PitcherTraditional[i + scale].replace("@@","@")	
				PitcherTraditional[i + scale] = PitcherTraditional[i + scale].replace(u"\u25BC","")	
				PitcherTraditional[i + scale] = PitcherTraditional[i + scale].replace(u"\u25B2","")	
				PitcherTraditional[i + scale] = PitcherTraditional[i + scale].replace("@JR"," JR")
				PitcherTraditional[i + scale] = PitcherTraditional[i + scale].replace("@SR"," SR")
				if (j == 2):
					print PitcherTraditional[i + scale]

		#Go to next page 	 
		try:
			d.find_element_by_class_name("paginationWidget-next").click()
		except:
			break
		time.sleep(waitTime)
	
	#Clean and return list
	PitcherTraditional = [x for x in PitcherTraditional if x != "XXX"]
	return PitcherTraditional 

#########################################################
######### MLB.com Team Pitching Handedness ##############
#########################################################
#must get pitcherhandedness from mlb.com - have to do the origional hard way to get all pitchers

def getPitcherHandedness():
	#Setup dataset
	pitcherHandedness = ["LAST.PH@FIRST.PH@TEAM.PH@HANDED.PH"]
	pitcherNames = ["Name"]

	#Go to webpage
	d.get("http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+pitching&game_type=%27R%27&season=2017&season_type=ANY&league_code=%27MLB%27&sectionType=sp&statType=pitching&page=1&ts=1493577333962")

	#select all players instead of qualifiers
	d.find_element_by_xpath(".//*[@id='sp_pitching-0']/fieldset[5]/label[1]/span").click()
	time.sleep(waitTime)

	#get pitcher names
	for l in range(0,100):
		#Create scale and starting value
		scale = l * 50
		startingVal = 2 

		#Locate table
		time.sleep(waitTime)
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")

		#Read data
		for i in range(startingVal, len(rows)):
			table = d.find_element_by_id("datagrid")
			rows = table.find_elements_by_tag_name("tr")
			names = d.find_elements_by_class_name("dg-name_display_last_init")
			name = names[i].text.upper().replace(" ","@")
			name = name[1:]
			name = name.replace("@@","@")  
			name = name.replace("@JR"," JR")
			name = name.replace("@SR"," SR")
			name = name.replace("@JR."," JR.")
			name = name.replace("@SR."," SR.")
			print name
			pitcherNames.append(name)

		#Go to next page 	 
		try:
			d.find_element_by_class_name("paginationWidget-next").click()
		except:
			break

	#Go to webpage
	d.get("http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+pitching&game_type=%27R%27&season=2017&season_type=ANY&league_code=%27MLB%27&sectionType=sp&statType=pitching&page=1&ts=1493577333962")
	time.sleep(waitTime)

	#select all players instead of qualifiers
	d.find_element_by_xpath(".//*[@id='sp_pitching-0']/fieldset[5]/label[1]/span").click()

	#iterate through players 
	for l in range(0,len(pitcherNames)):
		#get page numer
		pageNumber = l/50
		row = l - (pageNumber * 50)
		
		#look for element until it is found
		notFound = True
		while (notFound):
			#Go to correct page 	 
			try:
				for j in range(0,pageNumber): 
					d.find_element_by_class_name("paginationWidget-next").click()
			except:
				print "getPitcherHandedness: NEXT PAGE NOT CLICKED"
				break
			time.sleep(waitTime / 4)

			try:
				#click on pitcher name and get team
				teams = d.find_elements_by_class_name("dg-team_abbrev")
				team = teams[row].text.upper()
				names = d.find_elements_by_class_name("dg-name_display_last_init")
				name = names[row].text.upper().replace(" ", "@")
				name = name[1:]
				name = name.replace("@@","@")  
				name = name.replace("@JR"," JR")
				name = name.replace("@SR"," SR")
				name = name.replace("@JR."," JR.")
				name = name.replace("@SR."," SR.")


				action = webdriver.common.action_chains.ActionChains(d)
				action.move_to_element_with_offset(names[row], 10, 15)
				action.click()
				action.perform()
				
				#get handedness
				handed = d.find_element_by_xpath(".//*[@id='player-header']/div/div/ul/li[2]").text
				fullRow = name + "@" + team + "@" + handed
				#check if all pitcher have been found
				print "name: " + name
				print "pitcherName: " + pitcherNames[l - pageNumber - 1]
 				if pitcherNames[l - pageNumber - 1] == name:
					notFound = False
					pitcherHandedness.append(fullRow)
					print "getPitcherHandedness: player added"
				print fullRow

				#go back
				d.back()
			except:
				print "getPitcherHandedness: could not find row"
				d.get("http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+pitching&game_type=%27R%27&season=2017&season_type=ANY&league_code=%27MLB%27&sectionType=sp&statType=pitching&page=1&ts=1493577333962")
				time.sleep(waitTime)

				#select all players instead of qualifiers
				d.find_element_by_xpath(".//*[@id='sp_pitching-0']/fieldset[5]/label[1]/span").click()

				d.switch_to.window
				break

	#return the array
	return pitcherHandedness
	

#########################################################
######### MLB.com Advanced Pitcher Stats ################
#########################################################

def getAdvancedPitcher():
	#Create return list
	advancedPitcher = ["LAST.AP@FIRST.AP@TEAM.AP@G.AP@IP.AP@GS.AP@QS.AP@QSP.AP@K/BB.AP@K/9.AP@BB/9.AP@HR/9.AP@BABIP.AP@STRP.AP@FBMPH.AP@ERA.AP@FIP.AP"]

	#Get URL
	d.get("http://www.rotowire.com/baseball/player_ex_stats.htm?pos=P")
	time.sleep(waitTime * 3)

	#Read data from table
	for i in range(1,1300):
		try:
			row = d.find_element_by_xpath("html/body/div[3]/div[9]/div/table/tbody/tr["+str(i)+"]").text.upper()
			row = row.replace(" ","@")
			row = row.replace("@@","@")
			row = row.replace("@JR"," JR")
			row = row.replace("@SR"," SR")
			advancedPitcher.append(row)
			print (advancedPitcher[i])
		except:
			print "Could not find row"
			break

	#Return list
	return advancedPitcher
	
#########################################################
############## MLB.com Team Hitting #####################
#########################################################
def getTeamHitting(split):
	#data list
	teamHitting = ["RK.TH@TEAM.TH@LEAGUE.TH@G.TH@AB.TH@R.TH@H.TH@X2B.TH@X3B.TH@HR.TH@RBI.TH@BB.TH@SO.TH@SB.TH@CS.TH@AVG.TH@OBP.TH@SLG.TH@OPSRK.TH@TEAM.1.TH@LEAGUE.1.TH@IBB.TH@HBP.TH@SAC.TH@SF.TH@TB.TH@XBH.TH@GDP.TH@GO.TH@AO.TH@GO_AO.TH@NP.TH@PA.TH"]
	for i in range(0,1300):
		teamHitting.append("XXX")

	#Go to webpage - URL is up to date
	d.get("http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Team+hitting&game_type=%27R%27&season=2017&season_type=ANY&league++++_code=%27MLB%27&sectionType=st&statType=hitting&page=1&ts=1491156093698&league_code=%27MLB%27&playerType=QUALIFIER&sportCode=%27mlb%27&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder=%27desc%27&sortColumn=avg&results=&perPage=50&timeframe=&last_x_days=&extended=0")
	#Get Home or Away
	dropDown = Select(d.find_element_by_id('st_hitting_hitting_splits'))
	if (split == "Home"):
		dropDown.select_by_visible_text("Home Games")
	elif (split == "Away"):
		dropDown.select_by_visible_text("Away Games")
	elif (split == "Left"):
		dropDown.select_by_visible_text("vs Left")
	elif (split == "Right"): 
		dropDown.select_by_visible_text("vs Right")
	elif (split == ""):
		print "TeamHitting: no split"
	else:
		print "ERROR: incorrect parameter"
		return teamHitting 
	
	#Get Stats and put them into list 
	time.sleep(waitTime)
	table = d.find_element_by_id("datagrid")
	rows = table.find_elements_by_tag_name("tr")

	#Read data
	time.sleep(waitTime)
	for i in range(1,len(rows)):
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
		teamHitting[i] = rows[i].text.upper().replace(" ","@")
		teamHitting[i] = teamHitting[i].replace(",@",", ")	
		teamHitting[i] = teamHitting[i].replace("@@","@")	

	#Get Other Statistics
	d.find_element_by_xpath(".//*[@id='stats_next']").click()
	time.sleep(waitTime)
	table = d.find_element_by_id("datagrid")
	rows = table.find_elements_by_tag_name("tr")
	for i in range(1,len(rows)):
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
		teamHitting[i] += rows[i].text.upper().replace(" ","@")
		teamHitting[i] = teamHitting[i].replace(",@",", ")	
		teamHitting[i] = teamHitting[i].replace("@@","@")	
		teamHitting[i] = teamHitting[i].replace(u"\u25BC","")	
		teamHitting[i] = teamHitting[i].replace(u"\u25B2","")	
		print teamHitting[i]

	#Clean and return list
	teamHitting = [x for x in teamHitting if x != "XXX"]
	return teamHitting

#########################################################
############## MLB.com Team Pitching ####################
#########################################################
def getTeamPitching(split):
	#data list
	teamPitching = ["RK.TP@TEAM.TP@LEAGUE.TP@W.TP@L.TP@ERA.TP@G.TP@GS.TP@SV.TP@SVO.TP@IP.TP@H.TP@R.TP@ER.TP@HR.TP@BB.TP@SO.TP@AVG.TP@WHIPRK.TP@TEAM.1.TP@LEAGUE.1.TP@CG.TP@SHO.TP@HB.TP@IBB.TP@GF.TP@HLD.TP@GIDP.TP@GO.TP@AO.TP@WP.TP@BK.TP@SB.TP@CS.TP@PK.TP@TBF.TP@NPRK.TP@TEAM.2.TP@LEAGUE.2.TP@WPCT.TP@GO_AO.TP@OBP.TP@SLG.TP@OPS.TP"]
	for i in range(0,1300):
		teamPitching.append("XXX")

	#Go to webpage - URL is up to date 
	d.get("http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Team+pitching&game_type=%27R%27&season=2017&season_type=ANY&leagu++++e_code=%27MLB%27&sectionType=st&statType=pitching&page=1&ts=1491156164202&league_code=%27MLB%27&playerType=QUALIFIER&sportCode=%27mlb%27&split=&team_id=&active_sw=&position=%271%27&page_type=SortablePlayer&sortOrder=%27asc%27&sortColumn=era&results=&perPage=50&timeframe=&last_x_days=&extended=0")

	#Get Home or Away
	dropDown = Select(d.find_element_by_id('st_pitching_pitching_splits'))
	if (split == "Home"):
		dropDown.select_by_visible_text("Home Games")
	elif (split == "Away"):
		dropDown.select_by_visible_text("Away Games")
	elif (split == "Left"):
		dropDown.select_by_visible_text("vs Left")
	elif (split == "Right"):
		dropDown.select_by_visible_text("vs Right")
	elif (split == ""):
		print "TeamPitching: no split"
	else:
		print "ERROR: incorrect parameter"
		return teamPitching 
	
	#Get Stats and put them into list 
	time.sleep(waitTime)
	table = d.find_element_by_id("datagrid")
	rows = table.find_elements_by_tag_name("tr")

	#Read data
	time.sleep(waitTime)
	for i in range(0,len(rows)):
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
		teamPitching[i] = rows[i].text.upper().replace(" ","@")
		teamPitching[i] = teamPitching[i].replace(",@",", ")	
		teamPitching[i] = teamPitching[i].replace("@@","@")	

	#Get Other Statistics
	d.find_element_by_xpath(".//*[@id='stats_next']").click()
	time.sleep(waitTime)
	table = d.find_element_by_id("datagrid")
	rows = table.find_elements_by_tag_name("tr")
	for i in range(0,len(rows)):
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
		teamPitching[i] += rows[i].text.upper().replace(" ","@")
		teamPitching[i] = teamPitching[i].replace(",@",", ")	
		teamPitching[i] = teamPitching[i].replace("@@","@")	
		teamPitching[i] = teamPitching[i].replace(u"\u25BC","")	
		teamPitching[i] = teamPitching[i].replace(u"\u25B2","")	

	#Get Other Statistics
	d.find_element_by_xpath(".//*[@id='stats_next']").click()
	time.sleep(waitTime)
	table = d.find_element_by_id("datagrid")
	rows = table.find_elements_by_tag_name("tr")
	for i in range(0,len(rows)):
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
		teamPitching[i] += rows[i].text.upper().replace(" ","@")
		teamPitching[i] = teamPitching[i].replace(",@",", ")	
		teamPitching[i] = teamPitching[i].replace("@@","@")	
		teamPitching[i] = teamPitching[i].replace(u"\u25BC","")	
		teamPitching[i] = teamPitching[i].replace(u"\u25B2","")	
		print teamPitching[i]

	#Clean and return list
	teamPitching = [x for x in teamPitching if x != "XXX"]
	return teamPitching

#########################################################
############## MLB.com Team Fielding ####################
#########################################################
def getTeamFielding():
	#data list
	teamFielding = ["RK.TF@TEAM.TF@LEAGUE.TF@G.TF@GS.TF@INN.TF@TC.TF@PO.TF@A.TF@E.TF@DP.TF@SB.TF@CS.TF@SBPCT.TF@PB.TF@C_WP.TF@FPCT.TF@DER.TF"]
	for i in range(1,1300):
		teamFielding.append("XXX")

	#Go to webpage - URL is up to date 
	d.get("http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Team+fielding&game_type=%27R%27&season=2017&season_type=ANY&leagu++++e_code=%27MLB%27&sectionType=st&statType=fielding&page=1&ts=1491156203075&league_code=%27MLB%27&playerType=QUALIFIER&sportCode=%27mlb%27&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder=%27desc%27&sortColumn=fpct&results=&perPage=50&timeframe=&last_x_days=&extended=0")

	#Get Stats and put them into list 
	time.sleep(waitTime)
	table = d.find_element_by_id("datagrid")
	rows = table.find_elements_by_tag_name("tr")

	#Read data
	time.sleep(waitTime)
	for i in range(1,len(rows)):
		table = d.find_element_by_id("datagrid")
		rows = table.find_elements_by_tag_name("tr")
		teamFielding[i] = rows[i].text.upper().replace(" ","@")
		teamFielding[i] = teamFielding[i].replace(",@",", ")	
		teamFielding[i] = teamFielding[i].replace("@@","@")	
		teamFielding[i] = teamFielding[i].replace(u"\u25BC","")	
		teamFielding[i] = teamFielding[i].replace(u"\u25B2","")	
		print teamFielding[i]

	#Clean and return list
	teamFielding = [x for x in teamFielding if x != "XXX"]
	return teamFielding

#########################################################
################## Write to Files #######################
#########################################################
#Create the date for the file name
format1 = "%m.%d"
def writeToFile(fileName, array):
	today = datetime.datetime.now().strftime(format1)
	fullName = fileName + today
	fileName = fileName.replace("Home","")
	fileName = fileName.replace("Away","")
	fileName = fileName.replace("VsLeft","")
	fileName = fileName.replace("VsRight","")
	print "-----------------------------------------"
	print "Writing to file: " + fullName
	print "-----------------------------------------"
	f = open("/Users/michaelberk/Documents/MLB/2017 Data/"+fileName+"/"+fullName+".txt", "w").close()
	f = open("/Users/michaelberk/Documents/MLB/2017 Data/"+fileName+"/"+fullName+".txt", "a")
	for i in range(0, len(array)):	
		f.write(array[i]+"\n")	
	f.close()

#########################################################
################## Call Functions #######################
#########################################################
#Get data from sites and write them to files
#Get data about batters - splits on YTD 
PitcherHandedness = getPitcherHandedness()
writeToFile("PitcherHandedness", PitcherHandedness)
TeamHittingHome = cleanTeams(getTeamHitting("Home"))
writeToFile("TeamHittingHome",TeamHittingHome)
TeamHittingAway = cleanTeams(getTeamHitting("Away"))
writeToFile("TeamHittingAway",TeamHittingAway)
TeamHittingVsLeft = cleanTeams(getTeamHitting("Left"))
writeToFile("TeamHittingVsLeft",TeamHittingVsLeft)
TeamHittingVsRight = cleanTeams(getTeamHitting("Right"))
writeToFile("TeamHittingVsRight",TeamHittingVsRight)

TeamPitchingHome = cleanTeams(getTeamPitching("Home"))
writeToFile("TeamPitchingHome",TeamPitchingHome)
TeamPitchingAway = cleanTeams(getTeamPitching("Away"))
writeToFile("TeamPitchingAway",TeamPitchingAway)
TeamPitchingVsLeft = cleanTeams(getTeamPitching("Left"))
writeToFile("TeamPitchingVsLeft",TeamPitchingVsLeft)
TeamPitchingVsRight = cleanTeams(getTeamPitching("Right"))
writeToFile("TeamPitchingVsRight",TeamPitchingVsRight)

TeamFielding = cleanTeams(getTeamFielding())
writeToFile("TeamFielding",TeamFielding)
print datetime.datetime.now()
