# Setup

## MacOs Etherenet Setup

Connect Mac to Raspberry Pi via using dongle and ethernet cable.

Make sure System Preferences -> Sharing -> Internet sharing (USB 10/100/1000 LAN) is enabled

Test connection:
```ping pibox.local```

## Pi Python 3 Setup

Install Rpi,Gpio for python 3 

```
# Add this to ~/.profile
# Python 3 virtual env
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.7

sudo apt-get install rpi.gpio

# One of the commands below is the right one to do...
pip3 install virtualenv
pip3 install venv

# Create a virtual env for the project 
python3 -m venv lockbox

# Activate the venv
source lockbox/bin/activate

# Install Flask
pip install flask

# Run this if you get a pip install 404 error
curl https://bootstrap.pypa.io/get-pip.py | python3

pip install RPi.GPIO
```

# Run the Lockbox

```
cd ~/bin/lockbox/
source lockbox/bin/activate
python3 main.py
```

