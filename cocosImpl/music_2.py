# -*- encoding : utf-8 -*-
"""
@File       : music_2.py
@Time       :2020/9/16 16:47
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

import cocos
from cocos.scenes.transitions import *
from cocos.audio.pygame import music
from cocos.audio.effect import Effect

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


# 自定义菜单类
class main_menu(cocos.menu.Menu):
    def __init__(self):
        super(main_menu, self).__init__()

        # 也可以改变图片项的大小
        # 改变字体
        self.font_item['font_size'] = 66
        # 选中时
        self.font_item_selected['font_size'] = 66
        # 改变颜色 rgba
        self.font_item['color'] = (255, 255, 255, 25)
        # 选中时
        self.font_item_selected['color'] = (215, 255, 255, 255)

        menu_start = cocos.menu.ImageMenuItem('images/start-up.png', self.menu_start_callback)
        menu_setting = cocos.menu.ImageMenuItem('images/setting-up.png', self.menu_setting_callback)
        help_setting = cocos.menu.ImageMenuItem('images/help-up.png', self.menu_help_callback)
        # 创建菜单（添加项的列表，自定义布局位置）
        self.create_menu([menu_start, menu_setting, help_setting],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout([(500, 339), (500, 220), (500, 100)]),
                         selected_effect=cocos.menu.zoom_in(),
                         unselected_effect=cocos.menu.zoom_out())

    def menu_start_callback(self):
        yinxiao = Effect('sound/Blip.wav')  # 音效
        yinxiao.play()

        pass

    def menu_help_callback(self):
        pass

    def menu_setting_callback(self):
        set_sence = setting_sence.create()

        donghua = RotoZoomTransition(set_sence, 1.5)  # 导包！！

        cocos.director.director.push(donghua)


if __name__ == '__main__':
    # 初始化导演
    cocos.director.director.init(width=640, height=480, caption="dog and cat", audio_backend='sdl')
    # 将背景层  添加到场景
    bg = Game_BG()
    main_scence = cocos.scene.Scene(bg)
    # 添加菜单
    mainmenu = main_menu()
    main_scence.add(mainmenu)

    # 播放背景音乐
    music.load('sound/Hop.mp3'.encode())  # 需要转为编码
    music.play(loops=-1)  # 播放 循环次数
    music.set_volume(1)  # 声音大小

    # 启动场景
    cocos.director.director.run(main_scence)
