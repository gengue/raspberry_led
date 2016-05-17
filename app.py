import time
import datetime

from flask import Flask
from flask import request, render_template
from flask import jsonify

# import RPi.GPIO as GPIO


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')



@app.route("/toggle_led", methods=['POST'])
def toggle():
    # GPIO.setmoode(GPIO.BCM)
    # GPIO.setwarnings(false)
    # GPIO.setup(18,GPIO.OUT)

    time.sleep(1)
    if request.form.get('action')=='true':
        # GPIO.output(18,GPIO.HIGH)
        print('led on')
    else:
        # GPIO.output(18,GPIO.LOW)
        print('led off')

    return jsonify( {
        'ip': request.remote_addr,
        'user_agent': request.headers.get('User-Agent'),
        'datetime': datetime.datetime.now(datetime.timezone.utc)
    }), 200
    # return "Togge!"

if __name__ == "__main__":
    app.debug = True
    app.run()
