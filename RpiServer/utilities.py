from PIL import ImageColor
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    x_v: int
    y: int = 0    
    y_v: int = 0

def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False

def floatTryParse(value):
    try:
        return float(value), True
    except ValueError:
        return value, False

def boolTryParse(value):
    try:
        if (value == 'True'):
            return True, True
        elif (value == 'False'):
            return False, True
        else:
            raise ValueError
    except ValueError:
        return value, False

def colorTryParse(value):
    try:
        tempColor = ImageColor.getcolor(value, "RGBA")
        #ARGB
        color = (255 - tempColor[0], tempColor[1], tempColor[2], tempColor[3])
        return color, True
    except Exception:
        return value, False            