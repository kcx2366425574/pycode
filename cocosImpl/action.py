# -*- encoding : utf-8 -*-
"""
@File       : action.py
@Time       :2020/9/16 16:11
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

import cocos

hero = None  # 作为全局变量
px = 530
py = 320


class BG(cocos.layer.ColorLayer):  # 可设置颜色的层
    def __init__(self):
        global hero
        super(BG, self).__init__(255, 255, 255, 255)  # 白色的层
        hero = cocos.sprite.Sprite('images/hero.jpg')
        hero.position = px, py
        self.add(hero)


class my_menu(cocos.menu.Menu):
    def __init__(self):
        super(my_menu, self).__init__()

        self.font_item['font_size'] = 11
        self.font_item['color'] = (0, 0, 0, 255)
        self.font_item_selected['font_size'] = 20
        self.font_item_selected['color'] = (255, 74, 62, 255)

        item1 = cocos.menu.MenuItem('Hide', self.menu_callback1)
        item2 = cocos.menu.MenuItem('Show', self.menu_callback2)
        item3 = cocos.menu.MenuItem('ToggleVisibility', self.menu_callback3)
        item4 = cocos.menu.MenuItem('Place', self.menu_callback4)
        item5 = cocos.menu.MenuItem('Right', self.menu_callback5)

        x = 120
        y = 360
        step = 60
        self.create_menu([item1, item2, item3, item4, item5],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout(
                             [(x, y),
                              (x, y - step),
                              (x, y - 2 * step),
                              (x, y - 3 * step),
                              (x, y - 4 * step)
                              ]))

    def menu_callback1(self):
        hero.do(cocos.actions.Hide())

    def menu_callback2(self):
        hero.do(cocos.actions.Show())

    def menu_callback3(self):
        hero.do(cocos.actions.ToggleVisibility())  # 交替的隐藏 出现

    def menu_callback4(self):
        hero.do(cocos.actions.Place((700, 400)))  # 移动位置

    def menu_callback5(self):
        global px
        px += 10
        hero.do(cocos.actions.Place((px, py)))  # 移动位置


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