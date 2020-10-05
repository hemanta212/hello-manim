#!/usr/bin/env python3
from manimlib.imports import *


class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))


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
