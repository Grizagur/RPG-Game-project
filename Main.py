import cocos
#from cocos.director import director
import cocos.director

import pyglet
from pyglet.window import key
from pyglet.gl import *

fe = 1.0e-4
consts = {
    "window": {
        "width": 800,
        "height": 600,
        "vsync": True,
        "resizable": True
    },

    "view": {
        # as the font file is not provided it will decay to the default font;
        # the setting is retained anyway to not downgrade the code
        "font_name": 'Axaxax',
        "palette": {
            'bg': (0, 65, 133),
            'player': (237, 27, 36),
            'wall': (247, 148, 29),
            'gate': (140, 198, 62),
            'food': (140, 198, 62)
        }
    }
}




def main():
    # make window
    cocos.director.director.init(**consts['window'])
    #pyglet.font.add_directory('.') # adjust as necessary if font included
    scene = cocos.scene.Scene()
    player = pyglet.resource.image('player7.png')
    scene.add(cocos.text.Label("Hello world!", position = (100, 200)))
    scene.add(cocos.sprite.Sprite(player, position = (200,200)))
    cocos.director.director.run(scene) 

main()