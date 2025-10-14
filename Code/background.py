#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.const import WIN_WIDTH
from Code.entity import Entity


class Background(Entity):
    def __init__(self,name=str,position=tuple):
        super().__init__(name=name,position=position)

    def move(self, ):
        self.rect.centerx -=1
        if self.rect.right<=0:
            self.rect.left=WIN_WIDTH

