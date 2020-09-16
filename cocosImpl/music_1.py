# -*- encoding : utf-8 -*-
"""
@File       : music_1.py
@Time       :2020/9/16 16:46
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import cocos
from cocos.scenes.transitions import *
from cocos.audio.pygame import music
import setting_sence


# 背景层
class Game_BG(cocos.layer.Layer):
    def __init__(self):
        super(Game_BG, self).__init__()
        d_width, d_height = cocos.director.director.get_window_size()
        # 创建背景精灵
        background = cocos.sprite.Sprite('images/bg.jpg')
        background.position = d_width // 2, d_height // 2
        self.add(background)


if __name__ == '__main__':
    cocos.director.director.init(width=640, height=480, caption="dog and cat", audio_backend='sdl')  # !!!!!指定背景音乐后台 sdl
    bg = Game_BG()
    main_scence = cocos.scene.Scene(bg)

    # 播放背景音乐
    music.load('sound/Hop.mp3'.encode())  # 转为编码
    music.play(loops=-1)  # 播放 循环次数
    music.set_volume(1)  # 声音大小

    cocos.director.director.run(main_scence)
