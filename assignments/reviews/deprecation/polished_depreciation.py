from manimlib.imports import *


class Depreciation(Scene):
    def construct(self):
        self.start()
        self.formula()

    def start(self):
        q = TextMobject("Have you bought a mobile phone, laptop, or computer?").scale(
            0.8
        )
        self.play(Write(q, run_time=4))
        self.wait()

        self.play(q.shift, [0, 2, 0])
        self.wait()

        t2 = VGroup(
            TextMobject("Suppose, you buy a laptop at Rs. 50,000.").scale(0.8),
            TextMobject(
                "Do you think you can sell it in the same price after you buy and use it?"
            ).scale(0.8),
        ).arrange(DOWN, aligned_edge=LEFT)

        for each in t2:
            self.play(Write(each, run_time=4))

        self.wait()

        self.remove(q, t2[0])

        self.play(t2.shift, [0, 2, 0])
        self.wait()

        t3 = TextMobject(
            "Buyers would not be willing to buy a second hand product at the price in which they can buy a new one itself."
        ).scale(0.8)

        self.play(Write(t3, run_time=5))
        self.wait()

        self.remove(t2)
        self.play(t3.shift, [0, 2, 0])

        t4 = VGroup(
            TextMobject(
                "This is to show you, the price of your laptop depreciates years after you start using it."
            ),
            TextMobject(
                "Or simply, you can usually only sell your laptop at a decreased price than at its original price."
            ),
        ).arrange(DOWN, aligned_edge=LEFT)
        t4.scale(0.8)

        for each in t4:
            self.play(Write(each, run_time=4))
            self.wait()

        self.wait()
        self.clear()

        t5 = VGroup(
            TextMobject(
                "This depreciation can be calculated with mathematical formulas."
            ),
            TextMobject(
                "Before we get to know the formulas, let us learn the basic terms associated with calculating depreciation."
            ),
        ).arrange(DOWN, aligned_edge=LEFT)
        t5.scale(0.8)

        for each in t5:
            self.play(Write(each, run_time=4))
            self.wait(2)
        self.clear()

    def formula(self):
        terms = VGroup(
            TexMobject("\\text{Initial Value of an Item } (I_0)"),
            TexMobject("\\text{Final Value of an Item } (I)"),
            TexMobject("\\text{Rate of Depreciation } (R)"),
            TexMobject("\\text{Time Interval } (T)"),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)

        for each in terms:
            self.play(FadeIn(each))
            self.wait()

        self.clear()

        t1 = (
            TexMobject(
                "\\text{Suppose, a laptop worth } I_0 \\text{ depreciates at a constant rate of } R \\text{ for } T \\text{ consecutive years, } ",
                "\\text{we may calculate the final depreciated value  of this item by this simple formula: }",
            )
            .scale(0.7)
            .arrange(DOWN, aligned_edge=LEFT)
        )
        t1.shift([0, 3, 0])

        self.play(Write(t1, run_time=10))
        self.wait(2)

        f1 = TexMobject("I", "=", "I_0", "(1 - \\frac{R}{100})^T")

        self.play(Write(f1, run_time=4))
        self.wait(2)

        self.play(FadeOut(t1))
        t2 = TextMobject("For the decreased value:").shift([0, 3, 0])
        self.play(Write(t2))
        self.wait()

        f2 = TexMobject(
            "or, ", "I_0", "-", "I", "=", "I_0", "-", "I_0", "(1 - \\frac{R}{100})^T"
        )

        f3 = TexMobject(
            "or, ", "I_0", "-", "I", "=", "I_0", "(1 - (1 - \\frac{R}{100})^T)"
        )
        self.play(ReplacementTransform(f1, f2))
        self.wait(2)

        self.play(f2.shift, [0, 1.5, 0])

        self.play(ReplacementTransform(f2[0].copy(), f3[0]))
        self.play(ReplacementTransform(f2[1].copy(), f3[1]))
        self.play(ReplacementTransform(f2[2].copy(), f3[2]))
        self.play(ReplacementTransform(f2[3].copy(), f3[3]))
        self.play(ReplacementTransform(f2[4].copy(), f3[4]))
        self.play(ReplacementTransform(f2[5].copy(), f3[5]))
        self.play(ReplacementTransform(f2[7].copy(), f3[6]))

        self.wait(2)
        self.clear()

        t3 = TextMobject(
            "If the rate of depreciation is different for different years:"
        )
        t3.shift([0, 3, 0])
        self.play(Write(t3), run_time=3)

        f4 = VGroup(
            TexMobject("I ="),
            TexMobject("l_0"),
            TexMobject("(1 - \\frac{R(1)}{100})"),
            TexMobject("(1 - \\frac{R(2)}{100})"),
            TexMobject("(1 - \\frac{R(3)}{100})"),
            TexMobject("..."),
            TexMobject("(1 - \\frac{R(t)}{100})"),
        ).arrange(RIGHT)

        for each in f4:
            self.play(FadeIn(each, LEFT), run_time=2)

        self.wait()
        self.play(f4.shift, [0, 1, 0])

        f5 = (
            TexMobject("\\text{Here, }", "R(1)", "R(2)", "R(3)", "...", "R(t)")
            .arrange(RIGHT, buff=1.2)
            .shift([0, -0.5, 0])
        )
        t4 = TextMobject("represent depreciation rates for t consecutive years.").scale(
            0.8
        )
        t4.shift([0, -1.5, 0])

        for each in f5:
            self.play(Write(each), run_time=2)

        self.play(Write(t4, run_time=4))
        self.wait()
