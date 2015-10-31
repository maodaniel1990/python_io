import time
import picamera
import MySQLdb


db = MySQLdb.connect("140.121.150.53", "root", "asdasdasd", "world")
curs=db.cursor()


with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    

curs.execute ("SELECT * FROM data")

print "\nDate     	Time		Zone		Temperature"
print "==========================================================="


for reading in curs.fetchall():
    print str(reading[0])+"	"+str(reading[1])+" 	"+\
                reading[2]+"  	"+str(reading[3])
                
            '''
            123
            123
  