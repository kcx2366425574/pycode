# -*- encoding : utf-8 -*-
"""
@File       : mouseDemo.py
@Time       :2020/9/11 15:59
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
        # 开启事件处理层
        # ！！！！！！！！！！！！！！！！！！！！
        cocos.layer.Layer.is_event_handler = True

        self.label = cocos.text.Label('Hello',
                                      font_name='Times New Roman',
                                      font_size=32,
                                      anchor_x='center', anchor_y='center')
        # 获得导演窗口的宽度和高度，是一个二元组
        width, height = cocos.director.director.get_window_size()
        # 设置标签的位置
        self.label.position = width // 2, height // 2  # //整数除法 去掉小数部分
        # 添加标签到HelloWorld层
        self.add(self.label)

    def on_mouse_press(self, x, y, button, modifiiers):
        if button == pyglet.window.mouse.LEFT:
            self.label.element.text = '鼠标左键按下'
        if button == pyglet.window.mouse.RIGHT:
            self.label.element.text = '鼠标右键放下'

    def on_mouse_release(self, x, y, button, modifiiers):
        if button == pyglet.window.mouse.LEFT:
            self.label.element.text = '鼠标左键释放'
        if button == pyglet.window.mouse.RIGHT:
            self.label.element.text = '鼠标右键释放'

    def on_mouse_drag(self, x, y, dx, dy, button, modifiiers):
        # 使用modifiiers
        if modifiiers & pyglet.window.key.MOD_CTRL:
            self.label.element.text = 'ctrl+鼠标左键拖拽'


if __name__ == '__main__':
    # 初始化导演
    cocos.director.director.init(width=640, height=480, caption="dog and cat")

    lay = la()
    main_scence = cocos.scene.Scene(lay)
    # 添加菜单

    # 启动场景
    cocos.director.director.run(main_scence)
