class Storage(dict):
    """
    copied form web.py
    """
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, k:
            raise AttributeError, k

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            raise AttributeError, k

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'

constants = Storage({
    "regions": {
        "left": 1,
        "middle": 2,
        "right": 3
    },
        "colors": {
            "off": 0,
            "red": 1,
            "orange": 2,
            "yellow": 3,
            "green": 4,
            "sky": 5,
            "blue": 6,
            "purple": 7,
            "white": 8
        },
        "levels": {
            "light": 3,
            "low": 2,
            "med": 1,
            "high": 0
        },
        "modes": {
            "0":0, # no effect
            "normal": 1,
            "gaming": 2, # left to right
            "breathe": 3, # no effect
            "demo": 4, # decresing light to none
            "wave": 5, # no effect
            "6":6, # no effect
            "7":7
        }
})
