#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TouchAction() :

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return(x, y)

    # 使用touchAction来移动屏幕
    def toachSweip(self, x, y, x1, y1):
        action = TouchAction(self.driver)
        action.press(x=x, y=y).wait(ms=200).move_to(x=x1, y=y1).release()
        action.perform()
        






