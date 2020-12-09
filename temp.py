from manimlib.imports import *


class Test(Scene):
    def construct(self):
        self.intro()

    def intro(self):
        topic = TexMobject(r"\chemfig{H_2O}")
        self.play(Write(topic))
        self.wait(2)
