import signal
import os 

#store PIDS to be killed

cmd = 'ps -eo pid --sort -%cpu | head -2 > temp.txt'
#run ps script
os.system(cmd)

f = open("temp.txt", "r")

#skip first line
a = f.readline()


a = int(f.readline())
print(a)
f.close()
# delete temp file
os.system('rm temp.txt')
# kills proccesses

os.kill(a, signal.SIGKILL)
