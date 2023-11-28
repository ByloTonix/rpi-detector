<h1 align="center">Raspberry Pi Camera Detector</h1>
<h4 align="center">Raspberry Pi Camera Detector is a Python script with which you can use a Raspberry Pi and a CSI camera for it as a motion detector.</h4>

## Warnings:
- Make sure you are using **Raspberry Pi OS Legacy (based on Buster)** or older. It is possible to work on Raspberry Pi OS Bullseye when using the Legacy version of the Pycamera driver. There may be problems with other distributions.

## Requirements:
- Raspberry Pi 2B and newer
- Any CSI-compatible camera

## Setup:
- In the Raspberry Pi Configuration Tool, enable the camera operation:

```sh
sudo raspi-config
```

- Install the necessary dependencies:
```sh
sudo apt install python3-opencv -y
sudo apt install git --no-install-recommends -y
```

- Download the script:
```sh
git clone https://github.com/ByloTonix/rpi-detector/
cd rpi-detector
sudo chmod +x detector.py
mkdir images
```

## Usage:
- After completing the configuration, go to the directory with the script and run it:
```sh
cd ~/rpi-detector
./detector.sh
```
