import time
import os
import random
# Loading_Symbols
loading1 = "Loading." + "(|)"
loading2 = "Loading.." + "(/)"
loading3 = "Loading..." + "(-)"
loading4 = "Loading...." + "(\\)"
# Loading_System
Loading_Seconds = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1"]
LoadTime = (random.choice(Loading_Seconds))
while True:
    print(loading1)
    time.sleep(LoadTime)
    os.system('cls')
    print(loading1.replace(loading1, loading2))
    time.sleep(LoadTime)
    os.system('cls')
    print(loading2.replace(loading2, loading3))
    time.sleep(LoadTime)
    os.system('cls')
    print(loading3.replace(loading3, loading4))
    time.sleep(LoadTime)
    os.system('cls')
