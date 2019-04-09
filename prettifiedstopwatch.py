#!python3
#prettified stopwatch. copies result to clipboard

import time, pyperclip

input()
print('Timer started.')
starttime = time.time()
lap = 1
lasttime = starttime
textinfo = []

try:
    while True:
        input()
        laptime = round(time.time() - lasttime, 2)
        totaltime = round(time.time() - starttime, 2)
        totaltime += laptime
        print('Lap #%s:'.ljust(6) %lap + str(totaltime).center(6) + '(' + str(laptime).rjust(6) + ')')
        textinfo.append('Lap #%s:'.ljust(6) %lap + str(totaltime).center(6) + '(' + str(laptime).rjust(6) + ')')
        lap += 1
        lasttime = time.time()
except KeyboardInterrupt:
              print('Done, info copied to clipboard.')
textoutput = '\n'.join(textinfo)
pyperclip.copy(textoutput)

