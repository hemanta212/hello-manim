#!/usr/bin/env python3
from manimlib.imports import *

class TextPlay(Scene):
    def construct(self):
        name = TextMobject("Hemanta Sharma")
        subname = TextMobject("Pythonista")
        nickname = TextMobject("Hemuji")

        subname.next_to(name, DOWN)
        nickname.next_to(name, DOWN)

        self.add(name, subname)
        self.wait(2)
        self.play(Transform(subname, nickname))
        self.wait(2)
        self.play(ApplyMethod(subname.shift, 3 * DOWN))
        self.play(ApplyMethod(name.move_to, UP))
