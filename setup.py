import urllib.request
import urllib.parse
import re
import webbrowser
import pafy  # video api
import datetime, time
from subprocess import Popen
from ftplib import FTP # import file from ftp
import os


port=21
password='ftp_login_password'

os.chdir("C:\Files") #dirSave (where the file is stored
ftp = FTP("111.111.1.1")  #ip for python ot connect
ftp.login('username_ftp',password)
print ("File List:")
files = ftp.dir()

directory = "/files/" #dir (specifies the directory of the ftp)
filematch = '*filename.txt*' # file name

ftp.cwd(directory)

for filename in ftp.nlst(filematch): # Loop - looking for matching files
    fhandle = open(filename, 'wb')
    print ('Getting ' + filename) #for confort sake, shows the file that's being retrieved
    ftp.retrbinary('RETR ' + filename, fhandle.write)
    fhandle.close()

ftp.delete("/files/filename.txt")


store = [] #empty list
music_lenght = [] #empty list for lenght of videos



def linkConvert(music_name):
    query_string = urllib.parse.urlencode( {"search_query": music_name} )
    html_content = urllib.request.urlopen( "http://www.youtube.com/results?" + query_string )
    search_results = re.findall( r'href=\"\/watch\?v=(.{11})', html_content.read().decode() )
    result = ("http://www.youtube.com/watch?v=" + search_results[0])
    if result in store:
        print( "Music already exists" )
        print( music_name )  # Prints music name that already exists
    elif result not in store:
        store.append( result )
    return print( store )


def Remove_Empty_Lines(filename):
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.writelines(line for line in lines if line.strip())  # for each line if
        file.truncate()

Remove_Empty_Lines("D:\Tranferencias\musicas.txt)


file = open( "C:\Files\*filename.txt", "r", encoding="UTF-8")
for line in file:  # for each line on the file pass the line into the function
    linkConvert( line )



#This could be a list or a dic but I made this way to be sure ... probably I'm gona change it
run_once = 0
run_once1 = 0
run_once2 = 0
run_once3 = 0
run_once4 = 0
run_once5 = 0
run_once6 = 0
run_once7 = 0
run_once8 = 0

# 9:20-9:30
future = datetime.datetime.now()+ datetime.timedelta(seconds=600) # this is the future I stored the first delta in here (put the first interval time in here)

print("The Program is starting")
time.sleep(3)



while True:  #make a eternal loop
 if datetime.datetime.now() < future:  #This is a precaution to make sure the loop only starts at the correct time (like a safety net)
  for music in store:  #loop for each music in the list
   if datetime.datetime.now() < future:  # if the time at the start of the loop is less than the future the music is gona start
       video = pafy.new( music )
       delay = video.length + 5  #delay of each music passing through the loop
       Popen( ['start', 'chrome', music], shell=True )  #opens in the browser
       print( "Waiting ",delay," seconds for the music to stop" )
       time.sleep( delay )
       Popen( 'taskkill /F /IM chrome.exe', shell=True )   #closes the browser
       # 10:20-10:35
       future2 = datetime.datetime.now() + datetime.timedelta(seconds=3905)   #defines the second future (delta time of the delay[this is the lenght of the break - 10min but needs to be added the class duration. 10min in seconds + 50min in seconds + 5s of delay)
       print("This is the datetime of future2: ",datetime.datetime.now())  #just to check if everything is going according to plan (to be deleted)
       print("This is future2: ",future2)  #same as the last (to be deleted)
   elif datetime.datetime.now() < future2: # if the time atm is less than the future true green light to start the next condition
       time.sleep( 5 )
       print( "This is future2: ", future2) #checkpoint (to be deleted - tbd)
       pause = datetime.datetime.now() + datetime.timedelta(seconds=3000) # this is important, this is the pause of the loop. Insert on the seconds the time you want the loop to stop (50min in seconds to be more precise)
       #this is the the snippet to pause the script
       if run_once == 0:
        while pause > datetime.datetime.now():
          print( "Time is over, first break" )
          print("Restarting 3000s/50min")
          time.sleep(3000) #insert the time of wanted pause here aswell in seconds
          run_once = 1
       print( "This is future2: ", future2 ) #checkpoint (tbd)
       video = pafy.new( music )
       delay = video.length + 5
       Popen( ['start', 'chrome', music], shell=True )
       print("Waiting ",delay," seconds for the music to stop")
       time.sleep( delay )
       Popen( 'taskkill /F /IM chrome.exe', shell=True )
       # 11: 25 - 11:35
       future3 = datetime.datetime.now() + datetime.timedelta(seconds=3605)  #defines the second future (delta time of the delay[this is the lenght of the interval - 10min but needs to be added the class duration. 10min in seconds + 50min in seconds + 5s of delay)
       print("This is the datetime of the future3: ",datetime.datetime.now())  #checkpoint (tbd)
       print("This is future3: ",future3)  #checkpoint (tbd)
   elif datetime.datetime.now() < future3: # if the time atm is less than the future true green light to start the next condition
       time.sleep( 5 )
       print( "This is future3: ",future3 )  #checkpoint (tbd)
       pause = datetime.datetime.now() + datetime.timedelta( seconds=3000 ) #break
       if run_once1 == 0:
           while pause > datetime.datetime.now():
               print( "Time is over, second break" )
               print( "Restarting 3000s/50min" )
               time.sleep( 3000 ) #break
               run_once1 = 1
       print("This is future3: ",future3)  #checkpoint (tbd)
       video = pafy.new( music )
       delay = video.length + 5
       Popen( ['start', 'chrome', music], shell=True )
       print("Waiting ",delay," seconds for the music to stop")
       time.sleep( delay )
       Popen( 'taskkill /F /IM chrome.exe', shell=True )
       # 12: 25 - 12:30
       future4 = datetime.datetime.now() + datetime.timedelta(seconds=3305)  #defines the second future (delta time of the delay[this is the lenght of the interval - 10min but needs to be added the class duration. 10min in seconds + 50min in seconds + 5s of delay) ex. 3605
       print("This is datetime of future4: ",future4)  #checkpoint (tbd)
       print("This is future4: ",future4)  #checkpoint (tbd)
   elif datetime.datetime.now() >= future and datetime.datetime.now() >= future2 and datetime.datetime.now() >= future3 and datetime.time.now() < future4: # if the time atm is less than the future true green light to start the next condition (this gets a somewhat useless check of the last futures. Using as a precaution [to be deleted in the final version])
       time.sleep( 5 )
       print( "This is future4: ", future4 )  #checkpoint (tbd)
       pause = datetime.datetime.now() + datetime.timedelta( seconds=3000 ) #break
       if run_once2 == 0:
           while pause > datetime.datetime.now():
               print( "Time is over, third break" )
               print( "Restarting 3000s/50min" )
               time.sleep( 3000 )  #break
               run_once2 = 1
       print( "This is future4: ", future4 )  #checkpoint (tbd)
       video = pafy.new( music )
       delay = video.length + 5
       Popen( ['start', 'chrome', music], shell=True )
       print( "Waiting ", delay, " seconds for the music to stop" )
       time.sleep( delay )
       Popen( 'taskkill /F /IM chrome.exe', shell=True )
       # 13:20-13:30
       future5 = datetime.datetime.now() + datetime.timedelta( seconds= 3605 )  #defines the second future (delta time of the delay[this is the lenght of the interval - 10min but needs to be added the class duration. 10min in seconds + 50min in seconds + 5s of delay)
       print( "This is datetime of future5: ", future5 )  #checkpoint (tbd)
       print( "This is future5: ", future5 )  #checkpoint (tbd)
   elif datetime.datetime.now() >= future and datetime.datetime.now() >= future2 and datetime.datetime.now() >= future3 and datetime.time.now() >= future4 and datetime.datetime.now() < future5: # if the time atm is less than the future true green light to start the next condition (this gets a somewhat useless check of the last futures. Using as a precaution [to be deleted in the final version])
       time.sleep( 5 )
       print( "This is future5: ", future5 )  #checkpoint (tbd)
       pause = datetime.datetime.now() + datetime.timedelta( seconds=3000 ) #break
       if run_once3 == 0:
           while pause > datetime.datetime.now():
               print( "Time is over, fourth break" )
               print( "Restarting 3000s/50min" )
               time.sleep( 3000 )  #break
               run_once3 = 1
       print( "This is future5: ", future5 ) #checkpoint (tbd)
       video = pafy.new( music )
       delay = video.length + 5
       Popen( ['start', 'chrome', music], shell=True )
       print( "Waiting ", delay, " seconds for the music to stop" )
       time.sleep( delay )
       Popen( 'taskkill /F /IM chrome.exe', shell=True )
       # 14:20-14:30
       future6 = datetime.datetime.now() + datetime.timedelta( seconds=3605 )  #defines the second future (delta time of the delay[this is the lenght of the interval - 10min but needs to be added the class duration. 10min in seconds + 50min in seconds + 5s of delay)
       print( "This is datetime of future6: ", future6 )  #checkpoint (tbd)
       print( "This is future6: ", future6 )  #checkpoint (tbd)
   elif datetime.datetime.now() >= future and datetime.datetime.now() >= future2 and datetime.datetime.now() >= future3 and datetime.time.now() >= future4 and datetime.datetime.now() >= future5 and datetime.datetime.now() < future6: # if the time atm is less than the future true green light to start the next condition (this gets a somewhat useless check of the last futures. Using as a precaution [to be deleted in the final version])
       time.sleep( 5 )
       print( "This is future6: ", future6 )  #checkpoint (tbd)
       pause = datetime.datetime.now() + datetime.timedelta( seconds=3000 ) #break
       if run_once4 == 0:
           while pause > datetime.datetime.now():
               print( "Time is over, fifth break " )
               print( "Restarting 3000s/50min" )
               time.sleep( 3000 ) #break
               run_once4 = 1
       print( "This is future6: ", future6 )  #checkpoint (tbd)
       video = pafy.new( music )
       delay = video.length + 5
       Popen( ['start', 'chrome', music], shell=True )
       print( "Waiting ", delay, " seconds for the music to stop" )
       time.sleep( delay )
       Popen( 'taskkill /F /IM chrome.exe', shell=True )
       # 15: 20 - 15:30
       future7 = datetime.datetime.now() + datetime.timedelta( seconds=3605 )  #defines the second future (delta time of the delay[this is the lenght of the break - 10min but needs to be added the class duration. 10min in seconds + 50min in seconds + 5s of delay)
       print( "This is datetime of future7: ", future7 )  #checkpoint (tbd)
       print( "This is future7: ", future7 )  #checkpoint (tbd)
   elif datetime.datetime.now() >= future and datetime.datetime.now() >= future2 and datetime.datetime.now() >= future3 and datetime.time.now() >= future4 and datetime.datetime.now() >= future5 and datetime.datetime.now() >= future6 and datetime.datetime.now() < future7:# if the time atm is less than the future true green light to start the next condition (this gets a somewhat useless check of the last futures. Using as a precaution [to be deleted in the final version])
       time.sleep( 5 )
       print( "This is future7: ", future7 )  #checkpoint (tbd)
       pause = datetime.datetime.now() + datetime.timedelta( seconds=3000 ) #break
       if run_once5 == 0:
           while pause > datetime.datetime.now():
               print( "Time is over, sixth break" )
               print( "Restarting 3000s/50min" )
               time.sleep( 3000 )  #break
               run_once5 = 1
       print( "This is future7: ", future7 )  #checkpoint (tbd)
       video = pafy.new( music )
       delay = video.length + 5
       Popen( ['start', 'chrome', music], shell=True )
       print( "Waiting ", delay, " seconds for the music to stop" )
       time.sleep( delay )
       Popen( 'taskkill /F /IM chrome.exe', shell=True )
       # 16:20-16:35
       future8 = datetime.datetime.now() + datetime.timedelta( seconds=3605 )  #defines the second future (delta time of the delay[this is the lenght of the break - 10min but needs to be added the class duration. 10min in seconds + 50min in seconds + 5s of delay)
       print( "This is datetime of future8: ", future8 )  #checkpoint (tbd)
       print( "This is future8: ", future8 )  #checkpoint (tbd)
   elif datetime.datetime.now() >= future and datetime.datetime.now() >= future2 and datetime.datetime.now() >= future3 and datetime.time.now() >= future4 and datetime.datetime.now() >= future5 and datetime.datetime.now() >= future6 and datetime.datetime.now() >= future7 and datetime.datetime.now() < future8:# if the time atm is less than the future true green light to start the next condition (this gets a somewhat useless check of the last futures. Using as a precaution [to be deleted in the final version])
       time.sleep( 5 )
       print( "This is future8: ", future8 )   #checkpoint (tbd)
       pause = datetime.datetime.now() + datetime.timedelta( seconds=3000 ) #break
       if run_once6 == 0:
           while pause > datetime.datetime.now():
               print( "Time is over, seventh braek" )
               print( "Restarting 3000s/50min" )
               time.sleep( 3000 ) #break
               run_once6 = 1
       print( "This is future8: ", future8 )  #checkpoint (tbd)
       video = pafy.new( music )
       delay = video.length + 5
       Popen( ['start', 'chrome', music], shell=True )
       print( "Waiting ", delay, " seconds for the music to stop" )
       time.sleep( delay )
       Popen( 'taskkill /F /IM chrome.exe', shell=True )
       # 17:25-17:30
       future9 = datetime.datetime.now() + datetime.timedelta( seconds=3305 )  #defines the second future (delta time of the delay[this is the lenght of the break - 10min but needs to be added the class duration. 10min in seconds + 50min in seconds + 5s of delay)
       print( "This is datetime of future9: ", future9 )  #checkpoint (tbd)
       print( "This is future9: ", future9 )  #checkpoint (tbd)
   elif datetime.datetime.now() >= future and datetime.datetime.now() >= future2 and datetime.datetime.now() >= future3 and datetime.time.now() >= future4 and datetime.datetime.now() >= future5 and datetime.datetime.now() >= future6 and datetime.datetime.now() >= future7 and datetime.datetime.now() >= future8 and datetime.datetime.now() < future9:  # if the time atm is less than the future true green light to start the next condition (this gets a somewhat useless check of the last futures. Using as a precaution [to be deleted in the final version])
       time.sleep( 5 )
       print( "This is future9: ", future9 )  # checkpoint (tbd)
       pause = datetime.datetime.now() + datetime.timedelta( seconds=3000 )
       if run_once7 == 0:
           while pause > datetime.datetime.now():
               print( "Time is over" )
               print( "Restarting 3000s/50min" )
               time.sleep( 3000 )
               run_once7 = 1
       print( "This is future9: ", future9 )  # checkpoint (tbd)
       video = pafy.new( music )
       delay = video.length + 5
       Popen( ['start', 'chrome', music], shell=True )
       print( "Waiting ", delay, " seconds for the music to stop" )
       time.sleep( delay )
       Popen( 'taskkill /F /IM chrome.exe', shell=True )
   elif datetime.datetime.now() > future9:
       print("The Time is over for today... turning off the program...")
 break
