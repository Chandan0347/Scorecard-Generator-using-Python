#importing required libraries
import os
import re
import pandas as pd
import numpy as np
from datetime import datetime
start_time = datetime.now()
# Clearing screen 
os.system('cls')
# Change the directory if required
os.chdir(r"C:\Users\Chandan\OneDrive\Documents\GitHub\2001CB21_2022\tut08")

# Function defination
def scorecard():
	# Creating dictionary for storing pakistan data of diffrent attributes like score, batting, bowling, extras
	dict_pak ={
		'score': 0,
		'batting':{
			'extras':0,
			'wide':0,
			'nb':0,
			'byes':0,
			'lb':0,
			'p':0,
			'Rizwan':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},
			'Babar Azam':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Fakhar Zaman':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Iftikhar Ahmed':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Khushdil':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Shadab Khan':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Asif Ali':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Mohammad Nawaz':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Haris Rauf':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Naseem Shah':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Dahani':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},
		},
		'bowling':{
			'Rizwan':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},
			'Babar Azam':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Fakhar Zaman':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Iftikhar Ahmed':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Khushdil':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Shadab Khan':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Asif Ali':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Mohammad Nawaz':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Haris Rauf':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Naseem Shah':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Dahani':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},
		},
	}

	# Creating dictionary for storing India data of different attributes like score, batting, bowling, extras
	dict_ind ={'score':0,
		'batting':{
			'extras':0,
			'wide':0,
			'nb':0,
			'byes':0,
			'lb':0,
			'p':0,
			'Rohit':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},
			'Rahul':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Kohli':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Jadeja':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Suryakumar Yadav':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Hardik Pandya':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Karthik':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Arshdeep Singh':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Chahal':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Bhuvneshwar':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},'Avesh Khan':{
				'runs':0,
				'balls':0,
				'fours':0,
				'six':0,
				'out':False,
				'status':'Did not bat'
			},
		},
		'bowling':{
			'Rohit':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},
			'Rahul':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Kohli':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Jadeja':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Suryakumar Yadav':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Hardik Pandya':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Karthik':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Avesh Khan':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Chahal':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Bhuvneshwar':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},'Arshdeep Singh':{
				'over':'0',
				'maiden':0,
				'runs':0,
				'wicket':0,
				'nb':0,
				'wd':0
			},
		},
	}
	
	# Try block for if there is any error
	try:
		# Reading the input file pakistan innings 1 and storing it as list
		pak_inn_lines = open('pak_inns1.txt').read().splitlines()
		# counting neew lines in it and removing it
		new_lines = pak_inn_lines.count('')
		for i in range(new_lines):
			pak_inn_lines.remove('')
	# Except block for escape statements
	except:
		print("Please Check if any file is open!")
		print("Please Close the file.")
		print("Restart the programme.")
		print("Or check the correct directory is opened in python code")
		exit()
	# List for storing fall of wickets
	pak_fow = []
	# Variables for storing pak wickets, runs in 6 over
	pak_wickets =0
	curr_over = 0.0
	runs_in_6_over_pak =0

	# Try block if there is any error
	try:
		# Iterating through each line and analysing it
		for line in pak_inn_lines:
			# Creating Pattern 
			pattern  = re.compile(r'([0-9]+\.[1-6]) ([A-Za-z ]+[A-Za-z]*) to ([A-Za-z ]+[A-Za-z]*), (no run|1 run|FOUR|wide|out|2 runs|SIX|leg byes, (1 run|2 runs|3 runs|FOUR|SIX)|3 runs|(byes), ([1-9]) (run|runs)|([0-9]) wides),* (Lbw|(Caught by) ([A-Za-z ]+[A-Za-z]*)|Bowled)*')
			# Finding matches in line
			matches= pattern.finditer(line)
			# For matches different conditions are created for storing score
			for match in matches:
				# Storing over going on
				over = float(dict_ind['bowling'][match.group(2)]['over'])
				# Incrementing over
				if curr_over==5.6 :
					runs_in_6_over_pak = dict_pak['score']
				# Different conditions for commentry
				if match.group(4)=='no run':
					dict_pak['batting'][match.group(3)]['balls'] += 1
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_ind['bowling'][match.group(2)]['over'])
					dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_pak['batting'][match.group(3)]['status'] = 'not out'
				elif match.group(4)=='1 run':
					dict_pak['batting'][match.group(3)]['runs'] += 1
					dict_pak['batting'][match.group(3)]['balls'] += 1
					dict_pak['batting'][match.group(3)]['status'] = 'not out'
					dict_ind['bowling'][match.group(2)]['runs'] += 1
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_ind['bowling'][match.group(2)]['over'])
					dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_pak['score'] += 1
				elif match.group(4)=='2 runs':
					dict_pak['batting'][match.group(3)]['runs'] += 2
					dict_pak['batting'][match.group(3)]['balls'] += 1
					dict_pak['batting'][match.group(3)]['status'] = 'not out'
					dict_ind['bowling'][match.group(2)]['runs'] += 2
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_ind['bowling'][match.group(2)]['over'])
					dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_pak['score'] += 2
				elif match.group(4)=='3 runs':
					dict_pak['batting'][match.group(3)]['runs'] += 3
					dict_pak['batting'][match.group(3)]['balls'] += 1
					dict_pak['batting'][match.group(3)]['status'] = 'not out'
					dict_ind['bowling'][match.group(2)]['runs'] += 3
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_ind['bowling'][match.group(2)]['over'])
					dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_pak['score'] += 3
				elif match.group(4)=='FOUR':
					dict_pak['batting'][match.group(3)]['runs'] += 4
					dict_pak['batting'][match.group(3)]['balls'] += 1
					dict_pak['batting'][match.group(3)]['fours'] += 1
					dict_pak['batting'][match.group(3)]['status'] = 'not out'
					dict_ind['bowling'][match.group(2)]['runs'] += 4
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_ind['bowling'][match.group(2)]['over'])
					dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_pak['score'] += 4
				elif match.group(4)=='SIX':
					dict_pak['batting'][match.group(3)]['runs'] += 6
					dict_pak['batting'][match.group(3)]['balls'] += 1
					dict_pak['batting'][match.group(3)]['six'] += 1
					dict_pak['batting'][match.group(3)]['status'] = 'not out'
					dict_ind['bowling'][match.group(2)]['runs'] += 6
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_ind['bowling'][match.group(2)]['over'])
					dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					
					if (over*10)%10 ==5:
						dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_pak['score'] += 6
				elif match.group(4)=='out':
					dict_pak['batting'][match.group(3)]['balls'] += 1
					dict_pak['batting'][match.group(3)]['out'] = True
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					# Different conditions for out and storing its status
					if match.group(10)=='Bowled':
						dict_pak['batting'][match.group(3)]['status']=f'b {match.group(2)}'
						pak_wickets +=1
						pak_fow.append(f"{dict_pak['score']}-{pak_wickets} ({match.group(3)}, {curr_over})")
					elif match.group(10)=='Lbw':
						dict_pak['batting'][match.group(3)]['status']=f'lbw {match.group(2)}'
						pak_wickets +=1
						pak_fow.append(f"{dict_pak['score']}-{pak_wickets} ({match.group(3)}, {curr_over})")
					elif match.group(11)=='Caught by':
						dict_pak['batting'][match.group(3)]['status']=f'c {match.group(12)} b {match.group(2)}'
						pak_wickets +=1
						pak_fow.append(f"{dict_pak['score']}-{pak_wickets} ({match.group(3)}, {curr_over})")
					
					over = float(dict_ind['bowling'][match.group(2)]['over'])
					dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_ind['bowling'][match.group(2)]['wicket'] += 1
				elif match.group(4)=='wide':
					dict_pak['batting'][match.group(3)]['status'] ='not out'
					dict_pak['batting']['wide'] += 1
					dict_ind['bowling'][match.group(2)]['runs'] += 1
					dict_ind['bowling'][match.group(2)]['wd'] += 1
					dict_pak['batting']['extras'] += 1
					dict_pak['score'] += 1
				
				elif match.group(6)=='byes':
					runs = int(match.group(7))
					dict_pak['batting'][match.group(3)]['balls'] += 1
					dict_pak['batting']['byes'] += 1
					dict_pak['batting'][match.group(3)]['status'] = 'not out'
					dict_pak['score'] += runs
					dict_pak['batting']['extras'] += runs
					over = float(dict_ind['bowling'][match.group(2)]['over'])
					dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_ind['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
	# Except block for escape statements
	except:
		print("Some error in code occured")
		exit()

	# Storing total pak overs
	pak_over = curr_over
	
	# Try block for if file is not found
	try:
		# Reading India Innings file and storing it in list
		ind_inn_lines = open('india_inns2.txt').read().splitlines()
		new_lines = ind_inn_lines.count('')
		for i in range(new_lines):
			ind_inn_lines.remove('')
	# Except block for escape statements
	except:
		print("Please Check if any file is open!")
		print("Please Close the file.")
		print("Restart the programme.")
		print("Or check the correct directory is opened in python code")
		exit()

	# Creating list for fall of wickets
	ind_fow = []
	# Creating different variables for analysis
	ind_wickets =0
	curr_over = 0.0
	runs_in_6_over_ind =0

	# Try block for if there is any error 
	try:
		# Iterating through each line
		for line in ind_inn_lines:
			# Creating regex pattern for matching
			pattern  = re.compile(r'([0-9]+\.[1-6]) ([A-Za-z ]+[A-Za-z]*) to ([A-Za-z ]+[A-Za-z]*), (no run|1 run|FOUR|wide|out|2 runs|SIX|leg byes, (1 run|2 runs|3 runs|FOUR|SIX)|3 runs|(byes), ([1-9]) (run|runs)|([0-9]) wides),* (Lbw|(Caught by) ([A-Za-z ]+[A-Za-z]*)|Bowled)*')
			# Finding Matches
			matches= pattern.finditer(line)
			# Iterating for matches
			for match in matches:
				# Storing overs of current bowler
				over = float(dict_pak['bowling'][match.group(2)]['over'])
				# Updating current over
				if curr_over== 5.6 :
					runs_in_6_over_ind = dict_ind['score']
				# Different conditions for Analysis
				if match.group(4)=='no run':
					dict_ind['batting'][match.group(3)]['balls'] += 1
					
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_pak['bowling'][match.group(2)]['over'])
					dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_ind['batting'][match.group(3)]['status'] = 'not out'
				elif match.group(4)=='1 run':
					dict_ind['batting'][match.group(3)]['runs'] += 1
					dict_ind['batting'][match.group(3)]['balls'] += 1
					dict_ind['batting'][match.group(3)]['status'] = 'not out'
					dict_pak['bowling'][match.group(2)]['runs'] += 1
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_pak['bowling'][match.group(2)]['over'])
					dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_ind['score'] += 1
				elif match.group(4)=='2 runs':
					dict_ind['batting'][match.group(3)]['runs'] += 2
					dict_ind['batting'][match.group(3)]['balls'] += 1
					dict_ind['batting'][match.group(3)]['status'] = 'not out'
					dict_pak['bowling'][match.group(2)]['runs'] += 2
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_pak['bowling'][match.group(2)]['over'])
					dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_ind['score'] += 2
				elif match.group(4)=='3 runs':
					dict_ind['batting'][match.group(3)]['runs'] += 3
					dict_ind['batting'][match.group(3)]['balls'] += 1
					dict_ind['batting'][match.group(3)]['status'] = 'not out'
					dict_pak['bowling'][match.group(2)]['runs'] += 3
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_pak['bowling'][match.group(2)]['over'])
					dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_ind['score'] += 3
				elif match.group(4)=='FOUR':
					dict_ind['batting'][match.group(3)]['runs'] += 4
					dict_ind['batting'][match.group(3)]['balls'] += 1
					dict_ind['batting'][match.group(3)]['fours'] += 1
					dict_ind['batting'][match.group(3)]['status'] = 'not out'
					dict_pak['bowling'][match.group(2)]['runs'] += 4
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_pak['bowling'][match.group(2)]['over'])
					dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_ind['score'] += 4
				elif match.group(4)=='SIX':
					dict_ind['batting'][match.group(3)]['runs'] += 6
					dict_ind['batting'][match.group(3)]['balls'] += 1
					dict_ind['batting'][match.group(3)]['six'] += 1
					dict_ind['batting'][match.group(3)]['status'] = 'not out'
					dict_pak['bowling'][match.group(2)]['runs'] += 6
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					over = float(dict_pak['bowling'][match.group(2)]['over'])
					dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					
					if (over*10)%10 ==5:
						dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_ind['score'] += 6
				elif match.group(4)=='out':
					dict_ind['batting'][match.group(3)]['balls'] += 1
					dict_ind['batting'][match.group(3)]['out'] = True
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					# Creating different conditions for out and storing status
					if match.group(10)=='Bowled':
						dict_ind['batting'][match.group(3)]['status']=f'b {match.group(2)}'
						ind_wickets +=1
						ind_fow.append(f"{dict_ind['score']}-{ind_wickets} ({match.group(3)}, {curr_over})")
					elif match.group(10)=='Lbw':
						dict_ind['batting'][match.group(3)]['status']=f'lbw {match.group(2)}'
						ind_wickets +=1
						ind_fow.append(f"{dict_ind['score']}-{ind_wickets} ({match.group(3)}, {curr_over})")
					elif match.group(11)=='Caught by':
						dict_ind['batting'][match.group(3)]['status']=f'c {match.group(12)} b {match.group(2)}'
						ind_wickets +=1
						ind_fow.append(f"{dict_ind['score']}-{ind_wickets} ({match.group(3)}, {curr_over})")
					
					over = float(dict_pak['bowling'][match.group(2)]['over'])
					dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					dict_pak['bowling'][match.group(2)]['wicket'] += 1
				elif match.group(4)=='wide':
					dict_ind['batting'][match.group(3)]['status'] ='not out'
					dict_ind['batting']['wide'] += 1
					dict_pak['bowling'][match.group(2)]['runs'] += 1
					dict_pak['bowling'][match.group(2)]['wd'] += 1
					dict_ind['batting']['extras'] += 1
					dict_ind['score'] += 1
				elif match.group(4)[2:]=='wides':
					dict_ind['batting'][match.group(3)]['status'] ='not out'
					dict_ind['batting']['wide'] += int(match.group(9))
					dict_pak['bowling'][match.group(2)]['runs'] += int(match.group(9))
					dict_pak['bowling'][match.group(2)]['wd'] += int(match.group(9))
					dict_ind['batting']['extras'] += int(match.group(9))
					dict_ind['score'] += int(match.group(9))
				
				elif match.group(4)[0:8]=='leg byes':
					dict_ind['batting'][match.group(3)]['balls'] += 1
					
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
					if match.group(5) == '1 run':
						dict_ind['batting'][match.group(3)]['status'] ='not out'
						dict_ind['batting']['lb'] += 1
						dict_ind['batting']['extras'] += 1
						dict_ind['score'] += 1
					elif match.group(5) == '2 runs':
						dict_ind['batting'][match.group(3)]['status'] ='not out'
						dict_ind['batting']['lb'] += 2
						dict_ind['batting']['extras'] += 2
						dict_ind['score'] += 2
					elif match.group(5) == '3 runs':
						dict_ind['batting'][match.group(3)]['status'] ='not out'
						dict_ind['batting']['lb'] += 3
						dict_ind['batting']['extras'] += 3
						dict_ind['score'] += 3
					elif match.group(5) == 'FOUR':
						dict_ind['batting'][match.group(3)]['status'] ='not out'
						dict_ind['batting']['lb'] += 4
						dict_ind['batting']['extras'] += 4
						dict_ind['score'] += 4
					elif match.group(5) == 'SIX':
						dict_ind['batting'][match.group(3)]['status'] ='not out'
						dict_ind['batting']['lb'] += 6
						dict_ind['batting']['extras'] += 6
						dict_ind['score'] += 6
					
				
				elif match.group(6)=='byes':
					runs = int(match.group(7))
					dict_ind['batting'][match.group(3)]['balls'] += 1
					dict_ind['batting']['byes'] += 1
					dict_ind['batting'][match.group(3)]['status'] = 'not out'
					dict_ind['score'] += runs
					dict_ind['batting']['extras'] += runs
					over = float(dict_pak['bowling'][match.group(2)]['over'])
					if (curr_over*10)%10 ==6:
						curr_over = (round((curr_over + 0.5),1))
					else:
						curr_over = round((curr_over +0.1),1)
					dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.1),1))
					if (over*10)%10 ==5:
						dict_pak['bowling'][match.group(2)]['over'] = str(round((over + 0.5),1))
	# Except block for escaping
	except:
		print("Some error occured in code.")
		exit()
	# Storing current overs of india
	ind_over = curr_over
	# Try block for if there any erroe in code
	try:
		# Creating new dataframe
		df = pd.DataFrame()
		df['c1']=np.nan
		df['c2']=np.nan
		df['c3']=np.nan
		df['c4']=np.nan
		df['c5']=np.nan
		df['c6']=np.nan
		df['c7']=np.nan
		df['c8']=np.nan
		
		# Creating structure of scorecard
		df.loc[2,'c3']='India Vs Pakistan Scorecard'

		df.loc[4,'c1']='Pakistan Innings'
		# Appending total runs in scorecard
		df.loc[4,'c8']= f"{dict_pak['score']}-{pak_wickets} ({pak_over} Ov))"
		df.loc[5,'c1']='Batter'
		df.loc[5,'c4']="R"
		df.loc[5,'c5']="B"
		df.loc[5,'c6']="4s"
		df.loc[5,'c7']="6s"
		df.loc[5,'c8']="SR"

		# Creating Pakistan dictionary of batsman for matching
		dict_batsman_pak ={
			'Rizwan':'Rizwan (wk)',
			'Babar Azam':'Babar Azam (c)',
			'Fakhar Zaman':'Fakhar Zaman',
			'Iftikhar Ahmed':'Iftikhar Ahmed',
			'Khushdil':'Khushdil',
			'Shadab Khan':'Shadab Khan',
			'Asif Ali':'Asif Ali',
			'Mohammad Nawaz':'Nawaz',
			'Haris Rauf':'Haris Rauf',
			'Naseem Shah':'Naseem Shah',
			'Dahani':'S Dahani'
		}
		# Creating India Bowling Dictionary
		dict_bowler_ind={
			'Bhuvneshwar':'Bhuvneshwar',
			'Arshdeep Singh':'Arshdeep Singh',
			'Hardik Pandya':'Hardik Pandya',
			'Avesh Khan':'Avesh Khan',
			'Chahal':'Chahal',
			'Jadeja':'Ravindra Jadeja',

		}
		i=6
		# Appending Pakistan Innings Stats
		for key in dict_batsman_pak:
			df.loc[i,'c1']= dict_batsman_pak[key]
			df.loc[i,'c2']= dict_pak['batting'][key]['status']
			df.loc[i,'c4']=dict_pak['batting'][key]['runs']
			df.loc[i,'c5']=dict_pak['batting'][key]['balls']
			df.loc[i,'c6']=dict_pak['batting'][key]['fours']
			df.loc[i,'c7']=dict_pak['batting'][key]['six']
			sr = dict_pak['batting'][key]['runs']*100/dict_pak['batting'][key]['balls']
			df.loc[i,'c8']='{:.2f}'.format(round(sr,2))
			i+=1
		df.loc[i,'c1']='Extras'
		df.loc[i,'c4']= f"{dict_pak['batting']['extras']} (b {dict_pak['batting']['byes']}, lb {dict_pak['batting']['lb']}, w {dict_pak['batting']['wide']}, nb {dict_pak['batting']['nb']}, p {dict_pak['batting']['p']})"
		df.loc[i+1,'c1']='Total'
		df.loc[i+1,'c4']=f"{dict_pak['score']} ({pak_wickets} wkts, {pak_over} Ov)"

		# Appending Fall of wickets
		df.loc[i+3,'c1']="Fall of Wickets"
		for j in range(0,pak_wickets,4):
			
			if j==pak_wickets:
				i=i+1
				break
			df.loc[i+4,f'c1']=pak_fow[j]
			if j+1==pak_wickets:
				i=i+1
				break
			df.loc[i+4,f'c2']=pak_fow[j+1]
			if j+2==pak_wickets:
				i=i+1
				break

			df.loc[i+4,f'c3']=pak_fow[j+2]
			if j+3==pak_wickets:
				i=i+1
				break
			df.loc[i+4,f'c4']=pak_fow[j+3]
			
			i+=1
		i = i+4
		
		# Appending India's Bowling performance to stat
		df.loc[i+1,'c1']='Bowler'
		df.loc[i+1,'c2']='O'
		df.loc[i+1,'c3']='M'
		df.loc[i+1,'c4']='R'
		df.loc[i+1,'c5']='W'
		df.loc[i+1,'c6']='NB'
		df.loc[i+1,'c7']='WD'
		df.loc[i+1,'c8']='ECO'
		i=i+2
		for key in dict_bowler_ind:
			df.loc[i,'c1']= dict_bowler_ind[key]
			df.loc[i,'c2']= dict_ind['bowling'][key]['over']
			df.loc[i,'c3']=dict_ind['bowling'][key]['maiden']
			df.loc[i,'c4']=dict_ind['bowling'][key]['runs']
			df.loc[i,'c5']=dict_ind['bowling'][key]['wicket']
			df.loc[i,'c6']=dict_ind['bowling'][key]['nb']
			df.loc[i,'c7']=dict_ind['bowling'][key]['wd']
			over = dict_ind['bowling'][key]['over']
			over = float(over)
			
			if (over*10)%10==0:
				eco = dict_ind['bowling'][key]['runs']/over
			else:
				pct = ((over*10)%10)/6.0
				over = int(over)+ pct
				eco = dict_ind['bowling'][key]['runs']/over
			df.loc[i,'c8']='{:<04}'.format(round(eco,1))
			i+=1

		i=i+2
		
		# Appending Powerplay runs
		df.loc[i,'c1']='Powerplays'
		df.loc[i,'c2']='Overs'
		df.loc[i,'c3']='Runs'
		i=i+1
		df.loc[i,'c1']='Mandatory'
		df.loc[i,'c2']='0.1-6'
		df.loc[i,'c3']=f'{runs_in_6_over_pak}'
		df.loc[i+1,'c1']=''
		i=i+2

		# Creating India's Innings
		df.loc[i,'c1']='India Innings'
		df.loc[i,'c8']= f"{dict_ind['score']}-{ind_wickets} ({ind_over} Ov))"
		df.loc[i+1,'c1']='Batter'
		df.loc[i+1,'c4']="R"
		df.loc[i+1,'c5']="B"
		df.loc[i+1,'c6']="4s"
		df.loc[i+1,'c7']="6s"
		df.loc[i+1,'c8']="SR"
		i= i+2
		# Creating dictionary for India's batting
		dict_batsman_ind ={
			'Rohit':'Rohit Sharma (c)',
			'Rahul':'KL Rahul',
			'Kohli':'Virat Kohli',
			'Jadeja':'Ravindra Jadeja',
			'Suryakumar Yadav':'Suryakumar Yadav',
			'Hardik Pandya':'Hardik Pandya',
			'Karthik':'Dinesh Karthik (wk)',

		}
		# Creating dictionary for Pak's bowling
		dict_bowler_pak={
			'Naseem Shah':'Naseem Shah',
			'Dahani':'Shahnawaz Dahani',
			'Haris Rauf':'Haris Rauf',
			'Shadab Khan':'Shadab Khan',
			'Mohammad Nawaz':'Mohammad Nawaz',
		}
		# Appending India's Batting stat
		for key in dict_batsman_ind:
			df.loc[i,'c1']= dict_batsman_ind[key]
			df.loc[i,'c2']= dict_ind['batting'][key]['status']
			df.loc[i,'c4']=dict_ind['batting'][key]['runs']
			df.loc[i,'c5']=dict_ind['batting'][key]['balls']
			df.loc[i,'c6']=dict_ind['batting'][key]['fours']
			df.loc[i,'c7']=dict_ind['batting'][key]['six']
			sr = dict_ind['batting'][key]['runs']*100/dict_ind['batting'][key]['balls']
			df.loc[i,'c8']='{:.2f}'.format(round(sr,2))
			i+=1
		

		df.loc[i,'c1']='Extras'
		df.loc[i,'c4']= f"{dict_ind['batting']['extras']} (b {dict_ind['batting']['byes']}, lb {dict_ind['batting']['lb']}, w {dict_ind['batting']['wide']}, nb {dict_ind['batting']['nb']}, p {dict_ind['batting']['p']})"
		df.loc[i+1,'c1']='Total'
		df.loc[i+1,'c4']=f"{dict_ind['score']} ({ind_wickets} wkts, {ind_over} Ov)"
		df.loc[i+2,'c1']= "Did not Bat"
		
		df.loc[i+2,'c2']='Bhuvneshwar Kumar'
		df.loc[i+2,'c3']='Avesh Khan'
		df.loc[i+2,'c4']='Yuzvendra Chahal'
		df.loc[i+2,'c5']='Arshdeep Singh'

		# Appending Fall of wickets
		df.loc[i+3,'c1']="Fall of Wickets"
		
		for j in range(0,ind_wickets,4):
			
			if j==ind_wickets:
				i=i+1
				break
			df.loc[i+4,f'c1']=ind_fow[j]
			if j+1==ind_wickets:
				i=i+1
				break
			df.loc[i+4,f'c2']=ind_fow[j+1]
			if j+2==ind_wickets:
				i=i+1
				break

			df.loc[i+4,f'c3']=ind_fow[j+2]
			if j+3==ind_wickets:
				i=i+1
				break
			df.loc[i+4,f'c4']=ind_fow[j+3]
			
			i+=1
		i = i+4

		# Appending Pak's Bowling stats
		df.loc[i+1,'c1']='Bowler'
		df.loc[i+1,'c2']='O'
		df.loc[i+1,'c3']='M'
		df.loc[i+1,'c4']='R'
		df.loc[i+1,'c5']='W'
		df.loc[i+1,'c6']='NB'
		df.loc[i+1,'c7']='WD'
		df.loc[i+1,'c8']='ECO'
		i=i+2
		for key in dict_bowler_pak:
			df.loc[i,'c1']= dict_bowler_pak[key]
			df.loc[i,'c2']= dict_pak['bowling'][key]['over']
			df.loc[i,'c3']=dict_pak['bowling'][key]['maiden']
			df.loc[i,'c4']=dict_pak['bowling'][key]['runs']
			df.loc[i,'c5']=dict_pak['bowling'][key]['wicket']
			df.loc[i,'c6']=dict_pak['bowling'][key]['nb']
			df.loc[i,'c7']=dict_pak['bowling'][key]['wd']
			over = dict_pak['bowling'][key]['over']
			over = float(over)
			
			if (over*10)%10==0:
				eco = dict_pak['bowling'][key]['runs']/over
			else:
				pct = ((over*10)%10)/6.0
				over = int(over)+ pct
				eco = dict_pak['bowling'][key]['runs']/over
			df.loc[i,'c8']='{:<04}'.format(round(eco,1))
			i+=1

		i=i+2
		
		df.loc[i,'c1']='Powerplays'
		df.loc[i,'c2']='Overs'
		df.loc[i,'c3']='Runs'
		i=i+1
		df.loc[i,'c1']='Mandatory'
		df.loc[i,'c2']='0.1-6'
		df.loc[i,'c3']=f'{runs_in_6_over_ind}'
		
		i=i+2

		# Renaming columns
		df.rename(columns = {'c1':''}, inplace = True)
		df.rename(columns = {'c2':''}, inplace = True)
		df.rename(columns = {'c3':''}, inplace = True)
		df.rename(columns = {'c4':''}, inplace = True)
		df.rename(columns = {'c5':''}, inplace = True)
		df.rename(columns = {'c6':''}, inplace = True)
		df.rename(columns = {'c7':''}, inplace = True)
		df.rename(columns = {'c8':''}, inplace = True)
		
		# Try block if file is open somewhere
		try:
			# Creating csv file for Scorecard.csv
			df.to_csv('Scorecard.csv',index= False)
			print("Your Scorecard is ready.")
			print("Please Check Scorecard.csv")
		# Except block for escape statements
		except:
			print("Please Check if any file is open!")
			print("Please Close the file.")
			print("Restart the programme.")
			print("Or check the correct directory is opened in python code")
			exit()
	# Except block if there is any error in code
	except:
		print("There is some error in code. Please Check!")
		exit()

# Function Call
scorecard()

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
