import time

def session(focus):
    #custom notification
    if focus == 25*60: print('focus session!')
    if focus == 5*60: print('short break!')
    if focus == 15*60: print('long break!')

    #timer
    while focus:
        mins, seg = divmod(focus, 60)
        timer = '{:02d}:{:02d}'.format(mins, seg)
        print(timer, end="\r")
        time.sleep(1)
        focus-=1
    
    print('Your time has finished')


focus_session = 25*60
short_break = 5*60
long_break = 15*60

#loop alternate focus / short, 8 times = 4 pomodoro sets, then long_break

for num in range(1, 5):
    session(int(focus_session))
    session(int(short_break))
session(int(long_break))
