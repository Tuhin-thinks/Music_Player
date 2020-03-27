from playsound import playsound
import os
import datetime
import random

def choice(len,done):
    value_1=random.randint(0,len)
    if value_1 in done:
        choice(len,done)
    else:
        return value_1

if __name__=='__main__':
    print('Current Working Directory:',os.getcwd())
    count=0
    c=0
    a=datetime.datetime.now()
    done=[]
    l=os.listdir() # list of musics
    for i in range(len(l)):
        if os.path.isfile(l[i]) and l[i].endswith('.mp3') or l[i].endswith('.wav'):
            count+=1
            if count==1:
                a = datetime.datetime.now()
            value=choice(len(l)-1,done) # due to this line, everytime you start you get some randomly chosen song.

            print(count,'. playing::::: ',l[value])
            try:
                playsound(l[value])
                done.append(value)
            except:
                done.append(value)

            # if count==1 : # you can actually restrict how many songs you want to play !
            #     break
#    b=datetime.datetime.now()
#    c=b-a
#    seconds=c.microseconds/1000000
#    print(seconds/60,'minutes of music played !')
