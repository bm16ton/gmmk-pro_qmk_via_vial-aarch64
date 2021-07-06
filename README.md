qmk via vial for gmmk pro for ubuntu 20.04 arm64. This wanted very old versions
of libs IE pyqt5 sip etc. Using python 3.8. I simply replaced the version numbers with the currently
available ones. Didnt keep track or notes but hopefuly most of what needed is;

### Add udev rule;
sudo mkdir -p /etc/udev/rules.d/

echo 'KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0666", TAG+="uaccess", TAG+="udev-acl"' | sudo tee /etc/udev/rules.d/92-viia.rules

sudo udevadm control --reload-rules

sudo udevadm trigger

### install qmk;
sudo python3 -m pip install qmk

### Install requirements;
sudo python install requirements.txt

### qmk setup;
cd gmmk-vial

qmk setup

### make via firmware;
make gmmk/pro:via

### Load the newly created .bin in the qmk/vial folder,with this firmware vial should work;
### One stock firmware plug keyboard in while holding SPACEBAR and B to enter bootloader,
### on other firmwares take back of keyboard, press and hold the button just below the f3 and plugin
### keyboard to enter bootloader;
dfu-util -a 0 --dfuse-address 0x08000000 -R -D gmmk_pro_via.bin

### Run vial
fbs run

This firmware is setup insecure so no key combo is required for changes, Once
vial starts all changes should be immediate.
