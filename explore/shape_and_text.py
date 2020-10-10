# Shapes And Text

 #!/usr/bin/env python3

from manimlib.imports import *

class ShapesAndText(Scene):
    def construct(self):
        square = Square(side_length=5, fill_color=BLUE_A, fill_opacity=0.5)
        label = TextMobject("Pykancha")
        label.scale(2)
        label.bg = BackgroundRectangle(label, fill_color=GREY, fill_opacity=0.3)
        label_group=VGroup(label.bg,label)  #Order matters

        label2=TextMobject("Boxed text",color=BLACK)
        label2.set_color(WHITE)
        label2.scale(2)
        label2.bg=SurroundingRectangle(label2,color=BLUE,fill_color=RED, fill_opacity=.5)
        label2_group=VGroup(label2,label2.bg)
        label2_group.next_to(label_group,DOWN)

        label3=TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN+LEFT)

        self.add(square)
        self.play(FadeIn(label_group, run_time=5))
        self.play(Rotate(label.bg, PI/2))
        self.play(FadeOut(label2_group, run_time=2))
        self.play(GrowFromCenter(label3, run_time=2))
