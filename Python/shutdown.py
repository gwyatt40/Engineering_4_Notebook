# import time and GPIO 
import time
import RPi.GPIO as GPIO 
# set pin 
reset_shutdown_pin = 18 # changed from original pin
# suppress warnings
GPIO.setwarnings(False)
# GPIO Mode for pin numbers 
GPIO.setmode(GPIO.BCM)
# use internal pull up resistor 
GPIO.setup(reset_shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# define restart function 
def restart():
    print("restarting Pi")
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
# define shutdown function 
def shut_down():
    print("shutting down")
    command = "/usr/bin/sudo /sbin/shutdown -h now" #shutdown command 
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
while True:
    # delay so doesn't use too much processing power 
    time.sleep(0.5)
    # waits for button press w/ debounce 
    channel = GPIO.wait_for_edge(reset_shutdown_pin, GPIO.FALLING, bouncetime=200)
    if channel is None:
        print('Timeout occurred')
    else:
        print('Edge detected on channel', channel)
        # For troubleshooting, uncomment this line to output button status on 
command line
        #print('GPIO state is = ', GPIO.input(reset_shutdown_pin))
        counter = 0
        while GPIO.input(reset_shutdown_pin) == False:
            # For troubleshooting, uncomment this line to view the counter. If it 
reaches a value above 4, we will restart.
            #print(counter)
            counter += 1
            time.sleep(0.5)
            # long button press = shutdown 
            if counter > 4:
                shut_down() # run shutdown function 
        # short button press = restart
        restart() # run restart function 
	
