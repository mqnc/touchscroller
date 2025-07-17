# touchscroller

Simulate smooth multi-touch scrolling on Linux with `uinput`.

## Install

```bash
pip install touchscroller
```

## Usage

Note that you must have the uinput kernel module loaded to use touchscroller. To load the module, run:

```bash
modprobe -i uinput
```

If you would like to have uinput to be loaded on every system boot, add uinput to `/etc/modules`.

Example:

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