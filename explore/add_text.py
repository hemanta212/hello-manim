# Adding Text

 #!/usr/bin/env python3

from manimlib.imports import *

class TextAdd(Scene):
    def construct(self):
        name = TextMobject("Hemanta Sharma")
        subname = TextMobject("Pythonista")
        nickname = TextMobject("sharmaji")

        subname.next_to(name, DOWN)
        nickname.next_to(name, DOWN)

        self.add(name, subname)
        self.wait(2)
        self.play(Transform(subname, nickname))
        self.wait(2)
        self.play(ApplyMethod(subname.shift, 3 * DOWN))
        self.play(ApplyMethod(name.move_to, UP))

class TextPlay(Scene):
    def construct(self):
        name = TextMobject("Hemanta Sharma")
        subname = TextMobject("Pythonista")
        nickname = TextMobject("Hemuji")

        subname.next_to(name, DOWN)
        nickname.next_to(name, DOWN)

        self.add(name, subname)
        self.wait(2)
        self.play(ApplyMethod(name.set_color, RED))
        self.wait(2)
        self.play(ApplyMethod(subname.scale,2.75))
        self.wait(2)
        self.play(Transform(subname, nickname))
        self.wait(2)
        self.play(ApplyMethod(subname.set_color, YELLOW))
        self.play(ApplyMethod(subname.shift, 3 * DOWN))
        self.play(ApplyMethod(name.shift, UP))
        self.play(ApplyMethod(name.set_color,BLUE))
        self.play(ApplyMethod(subname.next_to, name.get_corner(DOWN+RIGHT),DOWN))
        self.play(ApplyMethod(subname.match_color,name))
        self.play(FadeOut(name, run_time=3), FadeOut(subname, run_time=2))
