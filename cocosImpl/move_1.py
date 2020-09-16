# -*- encoding : utf-8 -*-
"""
@File       : move_1.py
@Time       :2020/9/16 16:39
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

import cocos
from cocos.menu import *

hero = None  # 作为全局变量


class BG(cocos.layer.ColorLayer):  # 可设置颜色的层
    def __init__(self):
        global hero
        super(BG, self).__init__(255, 255, 255, 255)  # 白色的层
        hero = cocos.sprite.Sprite('images/hero.jpg')
        hero.position = 530, 320
        self.add(hero)


class my_menu(cocos.menu.Menu):
    def __init__(self):
        super(my_menu, self).__init__()
        # 菜单项初始化设置
        self.font_item['font_size'] = 20
        self.font_item['color'] = (0, 0, 0, 255)
        self.font_item_selected['color'] = (0, 0, 0, 255)
        self.font_item_selected['font_size'] = 26

        item1 = MenuItem('MoveBy', self.menu_callback1)
        item2 = MenuItem('MoveTo', self.menu_callback2)
        item3 = MenuItem('JumpBy', self.menu_callback3)
        item4 = MenuItem('JumpTo', self.menu_callback4)
        item5 = MenuItem('ScaleBy', self.menu_callback5)
        item6 = MenuItem('ScaleTo', self.menu_callback6)
        item7 = MenuItem('RotateBy', self.menu_callback7)
        item8 = MenuItem('RotateTo', self.menu_callback8)
        item9 = MenuItem('FadeTo', self.menu_callback9)
        item10 = MenuItem('FadeIn', self.menu_callback10)
        item11 = MenuItem('FadeOut', self.menu_callback11)

        x = 120
        y = 560
        step = 45

        self.create_menu(
            [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11],
            layout_strategy=fixedPositionMenuLayout(
                [(x, y), (x, y - step), (x, y - 2 * step), (x, y - 3 * step), (x, y - 4 * step),
                 (x, y - 5 * step), (x, y - 6 * step), (x, y - 7 * step), (x, y - 8 * step),
                 (x, y - 9 * step), (x, y - 10 * step)]))

    def menu_callback1(self):
        hero.do(cocos.actions.MoveBy((100, 100), duration=2))  # 位置 duration执行时间

    def menu_callback2(self):
        hero.do(cocos.actions.MoveTo((200, 200), duration=2))

    def menu_callback3(self):
        hero.do(cocos.actions.JumpBy((100, 200), duration=2))  # 跳

    def menu_callback4(self):
        hero.do(cocos.actions.JumpTo((200, 200), duration=2))

    def menu_callback5(self):
        hero.do(cocos.actions.ScaleBy(0.5, duration=2))  # 缩放

    def menu_callback6(self):
        hero.do(cocos.actions.ScaleTo(2, duration=2))

    def menu_callback7(self):
        hero.do(cocos.actions.RotateBy(180, duration=2))  # 旋转角度

    def menu_callback8(self):
        hero.do(cocos.actions.RotateTo(20, duration=2))

    def menu_callback9(self):
        hero.do(cocos.actions.FadeTo(80, 2))  # 80%透明 两秒钟

    def menu_callback10(self):
        hero.do(cocos.actions.FadeIn(2))  # 渐入

    def menu_callback11(self):
        hero.do(cocos.actions.FadeOut(2))  # 淡出


if __name__ == '__main__':
    # 初始化导演
    cocos.director.director.init(width=1024, height=680, caption="动作")
    # 将背景层  添加到场景
    bg = BG()
    main_scence = cocos.scene.Scene(bg)
    # 添加菜单
    mainmenu = my_menu()
    main_scence.add(mainmenu)
    # 启动场景
    cocos.director.director.run(main_scence)
