from manimlib.imports import *


class Test(Scene):
    scalar_topic = None

    def construct(self):
        # self.topic()
        # self.intro()
        self.vector_intro_graph()
        # self.algebric_calc()
        # self.geometric_interpretation()
        # self.geometric_calc()
        self.wait(3)

    def topic(self):
        text = TextMobject(
            "Product of Vectors", color=BLUE
        )
        text.scale(1.5)
        self.play(Write(text), run_time=3)
        self.wait(1)
        self.play(text.to_edge, UP)

        types = (
            "The product of vectors can be calculated in two ways",
            "1. Scalar Product (Dot Product)",
            "2. Vector Product (Cross Product)",
            )
        types_text = VGroup(*[TextMobject(i) for i in types])
        types_text.arrange(DOWN, center=False).shift(UP)
        self.play(Write(types_text), run_time=8)

        self.scalar_topic = types_text[1]
        self.play(FadeOut(text), FadeOut(types_text[0]), FadeOut(types_text[2]))


    def intro(self):
        text = TextMobject(
            "Scalar Product of Two Vectors", color=BLUE
        )
        text.scale(1.5).to_edge(UP)

        # TODO REMOVE THISK
        if self.scalar_topic:
            self.play(ReplacementTransform(self.scalar_topic, text))
        else:
            self.play(Write(text))

        self.wait(1)
        intro = (
            "If A ($a_1$, $b_1$) and B ($a_2$, $b_2$) be two",
            "Vectors then their scalar product is given by",
            "A $\cdot$ B = ($a_1$, $b_1$) $\cdot$ ($a_2$, $b_2$)",
            "= $a_1 a_2$ + $b_1 b_2$"
            )
        intro_text = VGroup(*[TextMobject(i) for i in intro])
        intro_text.arrange(DOWN, center=False).shift(UP)
        self.play(Write(intro_text), run_time=8)

        for_eg_text = TextMobject(
           "Let us take two vectors A = 2i + 2j and B = 2i, ",
        )
        for_eg_text.to_edge(DOWN).shift(UP)
        self.play(Write(for_eg_text), run_time=3)
        
        self.wait(3)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))


    def vector_intro_graph(self):
        grid = NumberPlane(background_line_style={'stroke_color':WHITE})

        va = Vector(direction=UR, color=GREEN).scale(2).shift(UR/2)
        vb = Vector(color=BLUE).scale(2, about_edge=LEFT)

        va_coor_tex = TexMobject("A \ \ (2, 2)")
        vb_coor_tex = TexMobject("B \ \ (2, 0)")
        va_coor_tex.next_to(va.get_end(), UR)
        vb_coor_tex.next_to(vb.get_end(), UR)

        va_tex, vb_tex = TexMobject("2i+2j"), TexMobject("2i+0j")
        arrow = TexMobject(r"\rightarrow").scale(1.5)
        va_arrow, vb_arrow = arrow.copy(), arrow.copy()

        va_arrow.next_to(va_coor_tex)
        vb_arrow.next_to(vb_coor_tex)
        va_tex.next_to(va_arrow).set_color(GREEN)
        vb_tex.next_to(vb_arrow).set_color(BLUE)

        self.play(ShowCreation(grid))
        self.wait()

        self.play(ShowCreation(va))
        self.play(Write(va_coor_tex))
        self.wait()

        self.play(ShowCreation(vb))
        self.play(Write(vb_coor_tex))
        self.wait()

        self.play(ShowCreation(va_arrow))
        self.play(Write(va_tex))
        self.wait()

        self.play(ShowCreation(vb_arrow))
        self.play(Write(vb_tex))

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))
