#!/usr/bin/env python3

#AUTHOR: Griffin pundt
#NOTES: This is a script that can both download files from given links,
# and analyze them using exiftool Metadata analysis tool
import os
import time
import pathlib

#function to clear the terminal
def clear_terminal():
	os.system("clear")

#to make it look nicer, adds a little *spice*
def loading_bar(mode):
	if str(mode) == "analyze":
		string = "Analyzing\t"
	else:
		string = "Downloading\t"
	for i in range(30):
		pause(1/10)
		clear_terminal()
		if (i % 8 ) == 0:
			print(string + "|")
		elif (i % 8) == 1:
			print(string + "/")
		elif (i % 8) == 2:
			print(string + "--")
		elif (i % 8) == 3:
			print(string + "\\")
		elif (i % 8) == 4:
			print(string + "|")
		elif (i % 8) == 5:
			print(string + "/")
		elif (i % 8) == 6:
			print(string + "--")
		elif (i % 8) == 7:
			print(string + "\\")

#function that quits the script (called when user wants to quit)
def quit():
	clear_terminal()
	print("Goodbye!")
	pause(3)
	clear_terminal()

#pauses the program to slow down the pace
def pause(seconds: int):
	time.sleep(seconds)

#called if user gives invalid input
def input_error():
	clear_terminal()
	print("The input you used is invalid...")
	print("Please enter a valid command...")
	pause(3)

#called if user gives invalid file
def file_error():
	clear_terminal()
	print("The file you input is either misspelled or does not exist...")
	print("Please enter a valid file...")
	pause(3)

#user chooses how they want to analyze
#mode 1: user will analyze an individual file using ExifTool; Metadata will be displayed for them immediately
#mode 2: user will analyze all files within current folder, and redierect all metadata into a separate file
def analyze_mode():
	clear_terminal()
	print('==================== File Analyzer ====================')
	print("Analyze Individual File:\t\t(1)")
	print("Analyze Folder of Files:\t\t(2)")
	print("Go Back:\t\t(3)")
	mode = input("\nEnter Desired Mode:\t")
	if mode == str(1):
		clear_terminal()
		file = input("Input desired filename:\t")
		if os.path.isfile(file):
			print("Analyzing file " + file + "...")
			pause(2)
			loading_bar("analyze")
			os.system("exiftool -a -b -csv metatata.pdf " + file)
			print("\nCOMMAND EXECUTED...")
		else:
			file_error()
			analyze_mode()
	elif mode == str(2):
		clear_terminal()
		print("This mode will analyze all the files in the current folder. Please make sure analysis.py is located in the correct folder.")
		print("NOTE: if you want to change the output filename, edit the script manually")
		proceed = input("\nDo you wish to continue with the analysis?:\t\t (y/n)\n")
		if proceed == "y":
			folder = str(os.getcwd())
			string = ""
			for file in os.listdir(folder):
				if os.path.isfile(file):
					filename = " " + file
					string += filename
				else:
					print("File " + file + " does not exist... <SKIPPING>")	
					pause(1)

			loading_bar("analyze")
			os.system("exiftool -a -b -csv >>metadata.csv" + string)
			clear_terminal()
			print("COMMAND EXECUTED...")
			print("\nMetadata tags were placed into a CSV file named 'metadata.csv'. Please check your current folder for the file.")
			print("If the file is missing, review the ExifTool documentation and make sure all filetypes are supported...")
			input("\nPress [enter] to continue...")
		elif proceed == "n":
			analyze_mode()
		else:
			input_error()
			analyze_mode()
	elif mode == str(3):
		choose_mode()
	else:
		input_error()
		analyze_mode()


#user chooses how they want to download
#mode 1: user will input a link to download an individual file
#mode 2: user will input a filename containing multiple links, program will attempt to download each link
def download_mode():
	clear_terminal()
	print('==================== File Downloader ====================')
	print("Download Individual File:\t\t(1)")
	print("Download Folder of Files:\t\t(2)")
	print("Go Back:\t\t(3)")
	mode = input("\nEnter Desired mode:\t")
	if mode == str(1):
		clear_terminal()
		file = input("Input link of file to download:\t")
		try:
			clear_terminal()
			print("Downloading file from:\t" + file)
			pause(2)
			os.system("wget -q " + file)
			loading_bar("download")
			clear_terminal()
			print("COMMAND EXECUTED")
			print("Please check the current folder to see if file was downloaded.")
			print("If file is missing, try again and doublecheck that the link is input correctly...")
			input("\nPress [enter] to continue...")
			download_mode()
		except:
			clear_terminal()
			print("COMMAND EXECUTION FAILED...\nTry again")
			pause(3)
			download_mode()
			
	elif mode == str(2):
		clear_terminal()
		filepath = input("Input Filepath to file containing links:\t")
		print("This mode will download all the links located in the file " + filepath + ". Once this process is started, it can't be stopped until it is completed.")
		proceed = input("Do you wish to continue with the download?:\t\t(y/n)\n")
		if proceed == "y":
			try:
				with open(filepath) as file:
					for link in file:
						print("Downloading file from:\t" + str(link))
						os.system("wget -q " + str(link))
				print("FILE DOWNLOADS COMPLETE")
				print("Please check the current folder and see if files were downloaded.")
				print("If file is missing, try again and doublecheck that the link is input correctly...")
				input("\nPress [enter] to continue...")
				download_mode()
			except:
				print("FILE DOWNLOADS FAILED...\nPlease check that the file exists and your input filepath is spelled correctly...")
				pause(3)
				download_mode()
		elif proceed == "n":
			download_mode()
		else:
			input_error()
			download_mode()
	elif mode == str(3):
		choose_mode()
	else:
		input_error()
		choose_mode()

#user chooses which mode they want to use (main menu)
#mode 1: executes analyze_mode function, allowing user to choose which analyzation mode
#mode 2: executes download_mode function, allowing user to choose which download mode
#mode 3: exexutes quit function, quitting the program
def choose_mode():
	clear_terminal()
	print("==================== File Analysis Tool ====================")
	print("================= Created By Griffin Pundt =================")
	print("Analyze Files (Using Exiftool):\t\t(1)")
	print("Download Files:\t\t\t\t(2)")
	print("Quit Program:\t\t\t\t(3)")
	mode = input("\nEnter desired mode:\t")
	if mode == str(1):
		analyze_mode()
	elif mode == str(2):
		download_mode()
	elif mode == str(3):
		quit()
	else:
		input_error()
		choose_mode()

#main will start with choose_mode(), then will branch out to different modes based on user input
def main():
	choose_mode()


main()
