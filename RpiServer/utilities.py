from PIL import ImageColor

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

def colorTryParse(value):
    try:
        return ImageColor.getcolor(value, "RGB"), True
    except Exception:
        return value, False            