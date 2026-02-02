# NASCAR-Flags

A raspberry Pi based LED driver for syncing with the NASCAR race flags.

# Requirements

- Raspberry pi 3b based
- Written in python
- Interpret flags from live nascar races
- Drive an LED strip with different patterns based on the flag code

# API To get NASCAR from

cf.nascar.com/live/feed/live-flag/data.json

# FLag key

1 - Green - Solid green
2 - Yellow - Flashing yellow
3 - Red - Solid red
4 - Finish - Checkered white and black (off)

## Development Commands

```bash
cd ~/nascar_led

# Only needed first time
sudo ./bin/pip install rpi_ws281x

sudo ./bin/python test.py

```