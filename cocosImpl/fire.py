# -*- encoding : utf-8 -*-
"""
@File       : fire.py
@Time       :2020/9/16 16:42
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import cocos
from cocos.menu import *
from cocos.particle_systems import *
import time

lizi = None  # 作为全局变量


class GameLayer(cocos.layer.Layer):

    def __init__(self):
        super(GameLayer, self).__init__()
        # 创建初始的粒子系统
        lizi = Spiral()
        lizi.position = 560, 320
        self.add(lizi, name='particle')


class my_menu(cocos.menu.Menu):

    def __init__(self):
        super(my_menu, self).__init__()
        # 菜单项初始化设置
        self.font_item['font_size'] = 20
        self.font_item_selected['font_size'] = 26

        item1 = MenuItem('Fireworks', self.menu_callback1)

        x = 120
        y = 560
        step = 45

        self.create_menu(
            [item1],
            layout_strategy=fixedPositionMenuLayout(
                [(x, y)]))

    def menu_callback1(self):
        bg.remove('particle')  # 使用name移除已有的粒子
        lizi = Fireworks()  # 粒子模式设置
        lizi.total_particles = 200  # 设置属性
        lizi.speed = 800  # 设置属性
        lizi.position = 560, 320
        bg.add(lizi, name='particle')


if __name__ == '__main__':
    # 初始化导演
    cocos.director.director.init(width=1024, height=680, caption="动作")
    # 将背景层  添加到场景
    bg = GameLayer()
    main_scence = cocos.scene.Scene(bg)
    # 添加菜单
    mainmenu = my_menu()
    main_scence.add(mainmenu)
    # 启动场景
    cocos.director.director.run(main_scence)
