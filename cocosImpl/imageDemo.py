# -*- encoding : utf-8 -*-
"""
@File       : imageDemo.py
@Time       :2020/9/11 15:48
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import cocos


# 背景层
class GameBG(cocos.layer.Layer):
    def __init__(self):
        super(GameBG, self).__init__()
        d_width, d_height = cocos.director.director.get_window_size()
        # 创建背景精灵
        background = cocos.sprite.Sprite('images/dog_and_cat.jpg')
        background.position = d_width // 2, d_height // 2
        self.add(background)


# 自定义菜单类
class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super(MainMenu, self).__init__()

        # 也可以改变图片项的大小
        # 改变字体
        self.font_item['font_size'] = 66
        # 选中时
        self.font_item_selected['font_size'] = 66
        # 改变颜色 rgba
        self.font_item['color'] = (255, 255, 255, 25)
        # 选中时
        self.font_item_selected['color'] = (25, 255, 255, 255)

        menu_start = cocos.menu.ImageMenuItem('images/start_up.jpg', self.menu_start_callback)
        menu_setting = cocos.menu.ImageMenuItem('images/set_up.jpg', self.menu_setting_callback)
        help_setting = cocos.menu.ImageMenuItem('images/help.jpg', self.menu_help_callback)
        # 创建菜单（添加项的列表，自定义布局位置）
        self.create_menu([menu_start, menu_setting, help_setting],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout([(500, 339), (500, 220), (500, 100)]),
                         selected_effect=cocos.menu.zoom_in(),
                         unselected_effect=cocos.menu.zoom_out())

    def menu_start_callback(self):
        pass

    def menu_help_callback(self):
        pass

    def menu_setting_callback(self):
        pass


if __name__ == '__main__':
    # 初始化导演
    cocos.director.director.init(width=640, height=480, caption="dog and cat")

    # 将背景层  添加到场景
    bg = GameBG()
    main_scence = cocos.scene.Scene(bg)
    # 添加菜单
    mainmenu = MainMenu()
    main_scence.add(mainmenu)
    # 启动场景
    cocos.director.director.run(main_scence)
