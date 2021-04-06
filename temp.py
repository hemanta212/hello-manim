from manimlib.imports import *


class Test(Scene):
    scalar_topic = None

    def construct(self):
        # self.topic()
        self.intro()
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
        for_eg_text.to_edge(DOWN)
        self.play(Write(for_eg_text), run_time=3)
        
        self.wait(3)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))
