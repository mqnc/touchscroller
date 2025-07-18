# touchscroller

Simulate smooth multi-touch scrolling on Linux with [uinput](https://pypi.org/project/python-uinput/).

On many Linuxes you can only scroll instantly over several lines. This package lets you script pixel-level scrolling by simulating two fingers on a touchpad.

## Setup

```bash
pip install touchscroller
```

You must have the uinput kernel module loaded to use touchscroller. Two options:

1) Quickly start it for now:

```bash
modprobe -i uinput
```

2) Auto load on start up:

```bash
echo uinput | sudo tee /etc/modules-load.d/uinput.conf > /dev/null
```

You also need permissions to create a uinput device. Three options:

1) Quickly run as root:

```bash
sudo python myscript.py
```

2) Temporary fix until reboot:

```bash
sudo chmod 666 /dev/uinput
```

3) Proper, most annoyingly involved way:

```bash
# create a udev rule
echo 'KERNEL=="uinput", GROUP="input", MODE="0660"' | sudo tee /etc/udev/rules.d/99-uinput.rules > /dev/null

# add current user to 'input' group
sudo usermod -aG input "$USER"

# reload udev rules and trigger
sudo udevadm control --reload-rules
sudo udevadm trigger

echo 'all done, now reboot or log out and back in'
```

## Usage:

```py
from touchscroller import TouchScroller

ts = TouchScroller()

directions = [
    (3, 0), (2, 2), (0, 3), (-2, 2),
    (-3, 0), (-2, -2), (0, -3), (2, -2)
]

ts = TouchScroller()
with ts.touch() as touch:
    for dx, dy in directions:
        for _ in range(30):
            touch.move(dx, dy)

```