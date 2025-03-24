"""Here are some more challenges. You'll need to use all the skills you learnt."""

# A swiss speed camera, looking at lots of cars...

def swiss_speedcamera(speeds: list[int], units: str) -> str:
    ...

def test_speedcamera_list():
    speeds = [1,119,120,121,200]
    assert swiss_speedcamera(speeds, "kph") == ["OK","OK","OK","NAUGHTY","NAUGHTY"]

def test_speedcamera_mph():
    speeds = [1,74, 75, 76]
    assert swiss_speedcamera(speeds, "mph") == ["OK","OK","NAUGHTY","NAUGHTY"]


# A speedcamera that works in any country...

def test_international_camera_switzerland():
    speeds = [1,119,120,121,129,130,131,200]
    assert camera(speeds, 120) == ["OK","OK","OK","NAUGHTY","NAUGHTY","NAUGHTY","NAUGHTY","NAUGHTY"]

def test_international_camera_austria():
    speeds = [1,119,120,121,129,130,131,200]
    assert camera(speeds, 130) == ["OK","OK","OK","OK","OK","NAUGHTY","NAUGHTY","NAUGHTY"]