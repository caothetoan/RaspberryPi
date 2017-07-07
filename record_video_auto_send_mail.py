#!/usr/bin/bash
#By toanct
import time
import os, subprocess
import re, serial
import smtplib
from email import Encoders
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
 
 
def send_mail(file):    
    UserName = "haylamvietnam@gmail.com"
    Password = "KhatVongIT86c"
    Recipient = "Raspberry Pi 3"
    
    msg = MIMEMultipart()
    msg['From'] = UserName
    msg['To'] = Recipient
    msg['Subject'] = "Raspberry Pi 3 Hourly report"        
    text = "Hourly video from the office. Time: " + datetime.now().strftime("%Y_%m_%d_%H_%M_%S.h264")
    msg.attach( MIMEText(text) ) 
    
    part = MIMEBase("application", "octet-stream")
    fo=open(file,"rb")
    part.set_payload(fo.read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"'  %os.path.basename(file))
    msg.attach(part)
 
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(UserName, Password)
    s.sendmail(UserName, Recipient, msg.as_string())
    s.close()
 
 
def main(): 
 
    camera = PiCamera()
    print "Pi Camera is ready."
 
    try:       
        # Loop until users quit with CTRL-C
        while True :  
                time.sleep(60*30)
                print "Start recording movie"
                filename = datetime.now().strftime("%Y_%m_%d_%H_%M_%S.h264")
                camera.start_recording(filename)
                time.sleep(20)
                camera.stop_recording()
                path_of_movie = os.path.abspath(filename)
                   
                #Sending email
                try:
                    send_mail(path_of_movie)
                    print "Sending email done. Ready to read new temperature."
                except IOError:
                    print "Something wrong. Mail not sent."
                time.sleep(0.01)
    
    except KeyboardInterrupt:
        print "Quit program"
        
        
if __name__ == "__main__":
    main()