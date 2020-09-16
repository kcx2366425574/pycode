# -*- encoding : utf-8 -*-
"""
@File       : jingling.py
@Time       :2020/9/16 15:54
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import cocos
import pyglet


# 背景层
class la(cocos.layer.Layer):
    def __init__(self):
        super(la, self).__init__()
        # 获得尺寸
        self.width, self.height = cocos.director.director.get_window_size()
        # 背景精灵
        background = cocos.sprite.Sprite('images/background.jpg')
        background.position = self.width // 2, self.height // 2
        self.add(background, z=-1)  # z=前后顺序 小的往屏里
        # 山
        mountain1 = cocos.sprite.Sprite('images/mountain1.jpg', position=(360, 500), scale=0.6)  # scale缩放
        self.add(mountain1, 1)
        mountain2 = cocos.sprite.Sprite('images/mountain2.jpg', position=(800, 500), scale=0.6)  # scale缩放
        self.add(mountain2, 1)
        # hero
        hero = cocos.sprite.Sprite('images/hero.jpg', position=(800, 160), scale=0.6)  # scale缩放
        self.add(hero, 2)


if __name__ == '__main__':
    # 初始化导演
    cocos.director.director.init(width=1024, height=680, caption="hero")

    lay = la()
    main_scence = cocos.scene.Scene(lay)
    # 添加菜单

    # 启动场景
    cocos.director.director.run(main_scence)
