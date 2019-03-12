# Date: Winter 2016
# Author: Michael Berk
# Description: This file will read in the box scores from NBA.com (for DK)

#Set up
import numpy as np
import pandas as pd
import datetime
import time

import selenium as sl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import selenium.webdriver.support.ui as ui
d = webdriver.Chrome()

########################################################################
#Constants
waitTime = 6 
d.implicitly_wait(waitTime)

########################################################################
#Get the traditional stats from todays box score

#longDate = ["10/25/2016","10/26/2016","10/27/2016","10/28/2016","10/29/2016","10/30/2016","10/31/2016","11/01/2016","11/02/2016","11/03/2016","11/04/2016","11/05/2016","11/06/2016","11/07/2016","11/08/2016","11/09/2016","11/10/2016","11/11/2016","11/12/2016","11/13/2016","11/14/2016","11/15/2016","11/16/2016","11/17/2016","11/18/2016","11/19/2016","11/20/2016","11/21/2016","11/22/2016","11/23/2016"]


#shortDate = ["10.25","10.26","10.27","10.28","10.29","10.30","10.31","11.01","11.02","11.03","11.04","11.05","11.06","11.07","11.08","11.09","11.10","11.11","11.12","11.13","11.14","11.15","11.16","11.17","11.18","11.19","11.20","11.21","11.22","11.23"]

#for t in range(1,len(longDate)):
	
#Go to the URL:  http://stats.nba.com/scores/#!/10/11/2016
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
format1 = ("%m/%d/%Y")
date = yesterday.strftime(format1)
#date = longDate[t]
#date = "11/28/2016"
print date
URL = "http://stats.nba.com/scores/#!/" + date
d.get(URL)

#Set up the arrays
StatsPlayers = ["PLAYER"]
Teams = ["TEAM"]
OppTeams = ["OPPTEAM"]
Points = ["PTS"]
Rebounds = ["RB"]
Assists = ["AST"]
Blocks = ["BLKS"]
Steals = ["STLS"]
Turnovers = ["TO"]
FGP = ["FGP"]
ThreeP = ["X3P"]
ThreePM = ["X3PM"]
Mins = ["MIN"]
Fouls = ["FLS"]

for i in range(3,25):
	try:
		d.find_element_by_xpath(".//*[@id='scoresPage']/div[2]/div[1]/div/div/div[" + str(i) + "]/div[2]/div[1]/div/div[2]/div/a[1]").click()
	except:
		print "Could not find box score button"
		break
	for l in range (1,3):
		counter = 0
		for j in range(1,30):
			try:
				d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[1]")
				counter += 1
			except:
				break
		if (counter == 0):
			raise ValueError("Box score has no players") 
		print "Number of players in box score: " + str(counter)
		for j in range(1,counter + 1):
			#Player:
			players = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[1]")
			StatsPlayers.append(players.text.upper()) 
			print players.text + date

			#Team:
			teams = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/div[" + str(l + 5) + "]")
			Teams.append(teams.text.upper())
			print teams.text

			#Opp Team:
			if (l == 1):
				oppTeams = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/div[" + str(7) + "]")
				OppTeams.append(oppTeams.text.upper())
				print oppTeams.text
			elif (l == 2):
				oppTeams = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/div[" + str(6) + "]")
				OppTeams.append(oppTeams.text.upper())
				print oppTeams.text


			try:
				#Points:
				points = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[20]")
				Points.append(points.text)
				print points.text

				#Rebounds: 
				rebounds = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[14]")
				Rebounds.append(rebounds.text)
				print rebounds.text
				
				#Assists:
				assists = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[15]")
				Assists.append(assists.text)
				print assists.text

				#Blocks:
				blocks = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[18]")
				Blocks.append(blocks.text)
				print blocks.text

				#Steals:
				steals = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[17]")
				Steals.append(steals.text)
				print steals.text

				#Turnovers:
				turnovers = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[16]")
				Turnovers.append(turnovers.text)
				print turnovers.text

				#FGP:
				fgp = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[5]")
				FGP.append(fgp.text)
				print fgp.text

				#3PP:
				threeP = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[8]")
				ThreeP.append(threeP.text)
				print threeP.text

				#3PM:
				threePM = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[6]")
				ThreePM.append(threePM.text)
				print threePM.text

				#Mins:
				mins = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[2]")
				minsValue = mins.text.replace(":", ".")
				Mins.append(minsValue)
				print mins.text

				#Fouls:
				fouls = d.find_element_by_xpath("html/body/main/div[2]/div/div/div[3]/div/div[2]/div/nba-stat-table[" + str(l) + "]/div[1]/div[1]/table/tbody/tr[" + str(j) + "]/td[19]")
				Fouls.append(fouls.text)
				print fouls.text
			except:
				Points.append(0)
				Rebounds.append(0)
				Assists.append(0)
				Blocks.append(0)
				Steals.append(0)
				Turnovers.append(0)
				FGP.append(0)
				ThreeP.append(0)
				ThreePM.append(0)
				Mins.append(0)
				Fouls.append(0)
				pass

	d.get("http://stats.nba.com/scores/#!/" + date)


########################################################################
#Opp Team
d.get("http://www.basketball-reference.com/leagues/NBA_2017.html")

#Set up the arrays
DefenseTeams = ["OPPTEAM"]
AllowedPPG = ["ALLOWEDPPG"]
TeamRB = ["TEAMRB"]
TeamSteals = ["TEAMSTL"]

#Iterate through rows
for i in range(1, 31):
	#Team:
	defenseteams = d.find_element_by_xpath(".//*[@id='opponent-stats-base']/tbody/tr["+str(i)+"]/td[1]")
	DefenseTeams.append(defenseteams.text.upper())
	print defenseteams.text

	#Team allowed ppg:
	allowedppg = d.find_element_by_xpath(".//*[@id='opponent-stats-base']/tbody/tr["+str(i)+"]/td[24]")
	AllowedPPG.append(float(allowedppg.text))
	print allowedppg.text

	#Team rebounds:
	teamrb = d.find_element_by_xpath(".//*[@id='opponent-stats-base']/tbody/tr["+str(i)+"]/td[18]");
	TeamRB.append(float(teamrb.text))
	print teamrb.text

	#Team Steals:
	teamsteals = d.find_element_by_xpath(".//*[@id='opponent-stats-base']/tbody/tr["+str(i)+"]/td[20]")
	TeamSteals.append(float(teamsteals.text))
	print teamsteals.text

########################################################################
'''#OppTeam Continued
d.get("http://www.rotowire.com/daily/nba/defense-vspos.htm")

#Set up the arrays
defenseVsPosition = ["DVPosition"]

#Iterate through rows
for i in range(1, 31):
	#Team:
	defenseteams = d.find_element_by_xpath(".//*[@id='opponent-stats-base']/tbody/tr["+str(i)+"]/td[1]")
	DefenseTeams.append(defenseteams.text.upper())
	print defenseteams.text
'''
########################################################################
#Injury
d.get("http://www.rotowire.com/basketball/injuries.htm")

#Set up arrays
InjuryPlayers = ["PLAYER"]
Sidelined = ["SIDELINED"]

for i in range(1,500):
	try:
		d.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div[4]/div[2]/div["+str(i)+"]/div[2]/div[1]")
	except:
		break

	#Player:
	injuryplayers = d.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div[4]/div[2]/div["+str(i)+"]/div[2]/div[1]")
	InjuryPlayers.append(injuryplayers.text.upper())
	print injuryplayers.text

	#Injury Status:
	sidelined = d.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div[4]/div[2]/div["+str(i)+"]/div[1]/p[2]")
	Sidelined.append(sidelined.text.upper())
	print sidelined.text
					

########################################################################
#Advanced Predictors:
#http://stats.nba.com/league/player/#!/advanced/?sort=OFF_RATING&dir=1

#Go to url
d.get('http://stats.nba.com/league/player/#!/advanced/?sort=OFF_RATING&dir=1')

#Set up arrays
AdvancedPlayers = ["PLAYER"]
TSP = ["TSP"]
OffRating = ["OFFRATING"]
TRB = ["TRB"]
Pace = ["PACE"]

#Iterate through the pages
for j in range(1,11):

	#Iterate through the rows
	for i in range(1,52):

		#Make sure element can be located
		try:
			d.find_element_by_xpath(".//*[@id='main-container']/div/div/div[3]/div/div/div/div/div[5]/div[2]/table/tbody/tr["+str(i)+"]/td[1]")
		except:
			break
		#Players:
		advancedplayer = d.find_element_by_xpath(".//*[@id='main-container']/div/div/div[3]/div/div/div/div/div[5]/div[2]/table/tbody/tr["+str(i)+"]/td[1]")
		AdvancedPlayers.append(advancedplayer.text.upper())
		print advancedplayer.text

		#TSP (TS%): True Shooting %: 
		tsp = d.find_element_by_xpath(".//*[@id='main-container']/div/div/div[3]/div/div/div/div/div[5]/div[2]/table/tbody/tr["+str(i)+"]/td[19]")
		TSP.append(float(tsp.text))
		print tsp.text

		#Off Rating:
		offrating = d.find_element_by_xpath(".//*[@id='main-container']/div/div/div[3]/div/div/div/div/div[5]/div[2]/table/tbody/tr["+str(i)+"]/td[8]")
		OffRating.append(float(offrating.text))
		print offrating.text

		#TRB: Total Rebound %: 
		trb = d.find_element_by_xpath(".//*[@id='main-container']/div/div/div[3]/div/div/div/div/div[5]/div[2]/table/tbody/tr["+str(1)+"]/td[16]")
		TRB.append(float(trb.text))
		print trb.text
		
		#PACE: 
		pace = d.find_element_by_xpath(".//*[@id='main-container']/div/div/div[3]/div/div/div/div/div[5]/div[2]/table/tbody/tr["+str(i)+"]/td[21]")
		Pace.append(float(pace.text))
		print pace.text

	#go to the next window
	p = d.find_element_by_xpath(".//*[@id='main-container']/div/div/div[3]/div/div/div/div/div[5]/div[2]/table/tbody/tr[1]/td[1]").text
	d.find_element_by_xpath(".//*[@id='main-container']/div/div/div[3]/div/div/div/div/div[5]/div[1]/div[2]").click()
	n = d.find_element_by_xpath(".//*[@id='main-container']/div/div/div[3]/div/div/div/div/div[5]/div[2]/table/tbody/tr[1]/td[1]").text
	if (n == p):
		break


########################################################################
#Set up arrays to write
Box = [StatsPlayers, Teams, OppTeams, Points, Rebounds, Assists, Blocks, Steals, Turnovers, FGP, ThreeP, ThreePM, Mins, Fouls] 
OppTeam = [DefenseTeams, AllowedPPG, TeamRB, TeamSteals]
Injury = [InjuryPlayers, Sidelined]
Advanced = [AdvancedPlayers, TSP, OffRating, TRB, Pace]

########################################################################
#write to files
format1 = ("%m.%d")
fileDay = yesterday.strftime(format1)
#fileDay = "11.28" 

boxName = "boxScore" + fileDay 
print boxName
BoxFile = open("/Users/michaelberk/Documents/NBA Data/2016-2017 Season/boxScore/" + boxName + ".txt","w").close()
BoxFile = open("/Users/michaelberk/Documents/NBA Data/2016-2017 Season/boxScore/" + boxName + ".txt","a")
for i in range(0, len(StatsPlayers)):
	BoxFile.write(str(Box[0][i])+"@"+str(Box[1][i])+"@"+str(Box[2][i])+"@"+str(Box[3][i])+"@"+str(Box[4][i])+"@"+str(Box[5][i])+"@"+str(Box[6][i])+"@"+str(Box[7][i])+"@"+str(Box[8][i])+"@"+str(Box[9][i])+"@"+str(Box[10][i])+"@"+str(Box[11][i])+"@"+str(Box[12][i])+"@"+str(Box[13][i])+"\n")
BoxFile.close()

oppTeamName = "oppTeam" + fileDay 
print oppTeamName
OppTeamFile = open("/Users/michaelberk/Documents/NBA Data/2016-2017 Season/oppTeam/" + oppTeamName + ".txt","w").close()
OppTeamFile = open("/Users/michaelberk/Documents/NBA Data/2016-2017 Season/oppTeam/" + oppTeamName + ".txt","a")
for i in range(0, len(DefenseTeams)):
	OppTeamFile.write(str(OppTeam[0][i])+"@"+str(OppTeam[1][i])+"@"+str(OppTeam[2][i])+"@"+str(OppTeam[3][i])+"\n")
OppTeamFile.close()

injuryName = "injury" + fileDay 
print injuryName 
InjuryFile = open("/Users/michaelberk/Documents/NBA Data/2016-2017 Season/injury/" + injuryName + ".txt","w").close()
InjuryFile = open("/Users/michaelberk/Documents/NBA Data/2016-2017 Season/injury/" + injuryName + ".txt","a")
for i in range(0, len(Sidelined)):
	InjuryFile.write(str(Injury[0][i])+"@"+str(Injury[1][i])+"\n")
InjuryFile.close()

advancedName = "advanced" + fileDay 
print advancedName
AdvancedFile = open("//Users/michaelberk/Documents/NBA Data/2016-2017 Season/advanced/" + advancedName + ".txt","w").close()
AdvancedFile = open("//Users/michaelberk/Documents/NBA Data/2016-2017 Season/advanced/" + advancedName + ".txt","a") 
for i in range(0, len(AdvancedPlayers)): 
	AdvancedFile.write(str(Advanced[0][i])+"@"+str(Advanced[1][i])+"@"+str(Advanced[2][i])+"@"+str(Advanced[3][i])+"@"+str(Advanced[4][i])+"\n") 
AdvancedFile.close()








