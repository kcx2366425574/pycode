# -*- encoding : utf-8 -*-
"""
@File       : zippo.py
@Time       :2020/9/16 16:45
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
from cocos.euclid import Point2
from cocos.sprite import *
from cocos.scene import *
from cocos.layer import *
from cocos.particle_systems import *
from cocos.director import *


# 自定义GameLayer层类
class GameLayer(Layer):

    def __init__(self):
        super(GameLayer, self).__init__()
        # 获得窗口的宽度和高度
        s_width, s_height = director.get_window_size()

        # 创建背景精灵
        background = Sprite('images/zippo.jpg')
        background.position = s_width // 2, s_height // 2
        # 添加背景精灵
        self.add(background, 0)

        ps = Fire()
        ps.gravity = Point2(45, 600)  # x,y轴重力加速度  x正值为右边  y正值为上
        ps.radial_accel = 60
        ps.size = 220
        ps.size_var = 50
        ps.tangential_accel = 20
        ps.tangential_accel_var = 10
        ps.life = 0.99
        ps.life_var = 0.45
        ps.emission_rate = 200
        ps.position = 270, 580

        self.add(ps)


if __name__ == '__main__':
    # 初始化导演，设置窗口的高、宽、标题
    director.init(width=640, height=960, resizable=True, caption='粒子系统示例')

    # 创建主场景，并添加GameLayer对象到主场景
    main_scene = Scene(GameLayer())

    # 开始启动main_scene场景
    director.run(main_scene)
