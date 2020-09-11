# -*- encoding : utf-8 -*-
"""
@File       : helloDemo.py
@Time       :2020/9/11 15:23
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
import cocos


class Hello(cocos.layer.Layer):
    def __init__(self):
        super(Hello, self).__init__()
        # 创建标签
        label = cocos.text.Label('Hello', font_name='Times New Roman', font_size=32,
                                 anchor_x='center', anchor_y='center')
        # 获得导演窗口的宽度和高度，是一个二元组
        width, height = cocos.director.director.get_window_size()

        # 设置标签的位置
        label.position = width // 2, height // 2  # //整数除法 去掉小数部分

        # 添加标签到HelloWorld层
        self.add(label)


if __name__ == '__main__':
    # 初始化导演
    cocos.director.director.init(width=640, height=480, caption="hello world")
    # 创建层的实例
    layer = Hello()
    # 创建场景   添加层进来
    main_scence = cocos.scene.Scene(layer)
    # 启动场景
    cocos.director.director.run(main_scence)
