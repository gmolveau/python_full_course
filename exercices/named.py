from collections import namedtuple

Color = namedtuple('Color',['hue', 'saturation', 'luminosity'])
p = Color(170, 0.1, 0.6)
if p.saturation >= 0.5:
    print('Whew, that is bright!')
if p.luminiosity >= 0.5:
    print('Wow, that is light')