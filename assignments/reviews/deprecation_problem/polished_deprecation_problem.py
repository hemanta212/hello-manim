from manimlib.imports import *


class Example(Scene):
    def construct(self):
        self.question()
        self.answer()

    def question(self):
        t1 = TextMobject("Example")
        self.play(Write(t1))
        self.wait()
        self.clear()

        t2 = (
            TexMobject(
                "\\text{The present price of a motorcycle is Rs.1,40,000.}",
                "\\text{If it depreciates at } 7\\% \\text{ per year, what will be its price after 2 years?}",
            )
            .scale(0.7)
            .arrange(DOWN, aligned_edge=LEFT)
        )

        self.play(Write(t2, run_time=7))
        self.wait()
        self.play(t2.shift, [0, 3.1, 0])
        self.wait()

    def answer(self):
        t1 = TextMobject("Solution:").shift([-4.3, 2.3, 0]).set_color(GREEN)
        self.play(Write(t1))
        self.wait()

        terms = (
            TexMobject(
                "\\text{Initial Value of the Motorcycle} (I_0) = 1,40,000",
                "\\text{Time } (T) = 2 \\text{ years}",
                "\\text{Depreciation Rate } (R) = 7 \\%",
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.8)
            .shift([0, 1, 0])
        )

        self.play(Write(terms, run_time=7))
        self.wait()

        f1 = TexMobject("I", "=", "I_0", "(1 - \\frac{R}{100})^T").shift(
            [-2.2, -0.8, 0]
        )
        f2 = TexMobject("I", "=", "140000", "(1 - \\frac{7}{100})^2").shift(
            [-2, -2.5, 0]
        )
        f3 = TexMobject("I", "=", "140000 \\cross", "(0.93)^2").shift([-2.2, 0, 0])
        f4 = TexMobject("I", "=", "Rs. 121,086").set_color(GREEN).shift([-2.7, -1, 0])
        fText = TextMobject("The price will be Rs. 1,21,086 after 2 years.").shift(
            [0, -2, 0]
        )
        self.play(Write(f1, run_time=3))

        for each in range(len(f2)):
            self.play(ReplacementTransform(f1[each].copy(), f2[each]))

        self.wait()
        self.play(FadeOut(terms), FadeOut(f1))
        self.play(f2.shift, [0, 4, 0])
        self.wait()

        for each in range(len(f3)):
            self.play(ReplacementTransform(f2[each].copy(), f3[each]))
        self.wait()

        self.play(ReplacementTransform(f3.copy(), f4))
        self.wait()

        self.play(Write(fText))
        self.wait()
