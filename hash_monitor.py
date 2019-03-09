# Obvious stuff
import hashlib
import smtplib
import socket

# File to monitor
file_name = '/var/www/wordpress/wp-config.php' 

# Correct md5
md5_original = 'blahbahblah' 

# SMTP setup 
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login('example@email.com', 'pass')


# Open in binary mode and calculate MD5
with open(file_name, "rb") as file_to_check:
    # Read contents of the file
    data = file_to_check.read()    
    # Calculate MD5
    md5_returned = hashlib.md5(data).hexdigest()

# Compare original MD5 with current hash
if md5_original == md5_returned:
    print (str(file_name) + " MD5 matched. ")
else:
    print (str(file_name) + " MD5 mismatch. ")
    # Send email
    alert = 'Subject:' + socket.getfqdn() + ' MD5 alert\n\n' + str(file_name) + ' MD5 verification failed!\n\nCurrent MD5 hash: ' + str(md5_returned) + '\nExpected MD5 hash: ' + str(md5_original) + '\n\nServer may have been modified or hacked! '
    server.sendmail("no-reply@email.com","your@email.com", alert)

