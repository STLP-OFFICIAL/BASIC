# Basic package installer tool

import os
import sys
import time

os.system("clear")

print("\n\n\n")
ab="		System loading..."
for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)
print("\n\n\n")

time.sleep(2)
os.system("clear")
print("\n\n")
ab="	\033[1;32mSuccessfully Loaded\n"
for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)
name = input("	\033[1;34mYour Name: ")

ab="	\033[1;33mHey \033[1;32m"+name+", \033[1;33mBe Ethical..."
for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

print("\n\n")
time.sleep(2)
os.system("clear")

print("""\033[1;36m

  ____________________.____   __________ 
 /   _____/\\__    ___/|    |  \\______   \\
 \\_____  \\   |    |   |    |   |     ___/
 /        \\  |    |   |    |___|    |    
/_______  /  |____|   |_______ \\____|    
        \\/                    \\/         
\033[1;33m=================================
\033[1;32m Owner  : STLP TEAM
 GitHub : something
 Facebook: STLP
Use only for educational purposes
\033[1;33m=================================\033[0m


""")











#import os
print("\033[1;32m")
os.system("pkg up")
print("\033[1;33m")
os.system("pkg install git")
print("\033[1;31m")
os.system("pkg install ruby")
os.system("gem install lolcat")
os.system("pip install requests")

print("All package installed successfully!")
