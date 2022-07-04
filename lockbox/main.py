# !/usr/bin/env python3

from flask import Flask
from lockbox import Lockbox

#intitalize the lockbox controller on the Raspberry Pi
lb = Lockbox()
lb.setup()
lb.lock_box()

app = Flask(__name__)

def unlock():
    pass

@app.route('/')
def hello_world():
    return 'This is the Lock Box Challenge... will you find out what is inside?'

@app.route('/api/try/<int:lock_code>')
def attempt_unlock(lock_code):
    if lock_code == 42:
        lb.unlock_box()

        return 'Unlocked'

    elif lock_code == 105:
        lb.cycle_lock()

        return 'Cycling lock...'

    elif lock_code == 79:
        lb.lock_box()

        return 'locking box'
    else:
        return 'Invalid attempt.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

