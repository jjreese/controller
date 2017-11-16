from inputs import get_gamepad
import socket
import sched, time

TCP_IP = '10.139.65.151'
TCP_PORT = 44 #45? 80?
MESSAGE = ""
SECRETCODE = '^1234'

def Data_Pull(sc):
    global MESSAGE
    OLD_MESSAGE = ''
    if OLD_MESSAGE is "":
        OLD_MESSAGE = MESSAGE
        
    events = get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)
        if event.code == "ABS_Y":
            if event.state >= 10000:
                MESSAGE  = "f4"
                #output Forwards
            elif event.state <= -10000:
                    MESSAGE  = "b4"
                    #output Backwards
                
        elif event.code == "ABS_RX":
            if event.state >= 10000:
                    MESSAGE  = "r4"
                    #output Right
            elif event.state <= -10000:
                    MESSAGE  = "l4"
                   #output Left
                    
        elif event.code == "BTN_EAST":
            if event.state == 1:
                MESSAGE = "q1"
                #return;
        elif event.code == "BTN_TL":
            if event.state == 1:
                MESSAGE = "s1"

        elif event.code == "BTN_TR":
            if event.state == 1:
                MESSAGE = "z1"
        else:
            MESSAGE = ""

    if MESSAGE != "":        
            #print OLD_MESSAGE != MESSAGE
            #print OLD_MESSAGE
            #print MESSAGE
            OLD_MESSAGE = MESSAGE
        
            #Send Message over Server Here
            SEND_MESSAGE = SECRET_CODE + MESSAGE
            s.send(SEND_MESSAGE)
            print SEND_MESSAGE
        
    t.enter(.125,1,Data_Pull, (sc,))




s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
print "CONNECTED!"
t = sched.scheduler(time.time,time.sleep)


    

t.enter(.125,1,Data_Pull, (t,))
t.run()
                

        
