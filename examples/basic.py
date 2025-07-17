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
