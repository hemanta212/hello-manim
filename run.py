#!/usr/bin/env python3
from manimlib.imports import *

class TextAdd(Scene):
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
        self.play(ApplyMethod(name.to_edge,UP))
        self.play(ApplyMethod(name.set_color,BLUE))
        self.play(ApplyMethod(subname.next_to, name.get_corner(DOWN+RIGHT),DOWN))
        self.play(ApplyMethod(subname.match_color,name))
        self.play(FadeOut(name, run_time=3), FadeOut(subname, run_time=2))


class AddingMoreText(Scene):
    #Playing around with text properties
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author=TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote,quote2),
        ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))

        self.play(ApplyMethod(author.scale,1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))
