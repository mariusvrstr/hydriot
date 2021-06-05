# Raspbery Pi Agent

Build using Python 3.9.1

## Dependancies

1. Set the default python version to 3.9.1

```Console

python -m site
pip config set global.target /home/pi/.local/lib/python3.7/site-packages
echo "alias python=/bin/python3" >> ~/.bashrc
source ~/.bashrc

python -m ensurepip

```

2. Update PIP (`python -m pip install --upgrade pip`)
3. Update the wheels (`python -m pip install --upgrade pip setuptools wheel`)
2. Install to the default Python by including python -m not just pip

```Console
python -m pip install dependency-injector
python -m pip install asyncio
python -m pip install wiringpi
python -m pip install smbus
python -m pip install requests
python -m pip install sip
python -m pip install PyQt5
```