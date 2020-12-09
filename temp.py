from manimlib.imports import *


class Test(Scene):
    def construct(self):
        self.intro()

    def intro(self):
        benz = ChemObject("-(-[1]O^{-})=[7]O")
        self.play(Write(benz))
        self.wait(2)
