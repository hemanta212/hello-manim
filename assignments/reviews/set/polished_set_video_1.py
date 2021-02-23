from manimlib.imports import *


class Set(Scene):
    def construct(self):
        self.set_defn()
        self.cardinality_and_equivalency()
        self.venn_diagram()

    def set_defn(self):
        t1 = TextMobject("Set").set_color(PURPLE_A).shift(np.array([0, 3, 0]))
        t2 = (
            TextMobject("Set is a mathematical abstraction for a collection of things.")
            .scale(0.8)
            .next_to(t1, DOWN, buff=0.3)
        )
        t3 = (
            TextMobject("Eg, let A be a set of 5 natural numbers. Then A=")
            .scale(0.8)
            .next_to(t2, DOWN, buff=0.3)
            .align_to(t2, LEFT)
        )
        t4 = TextMobject("\{1,2,3,4,5\}").next_to(t3, RIGHT, buff=0.2)
        t5 = Circle(radius=1.5).next_to(t3, DOWN, buff=0.2)
        t5_A = TextMobject("A").shift(np.array([-2, 0.9, 0]))
        t5_1 = TextMobject("1").shift(np.array([-1, 0.2, 0]))
        t5_2 = TextMobject("2").next_to(t5_1, RIGHT, buff=0.6)
        t5_3 = TextMobject("3").shift(np.array([-1.3, -0.5, 0]))
        t5_4 = TextMobject("4").next_to(t5_3, RIGHT, buff=0.4)
        t5_5 = TextMobject("5").next_to(t5_4, RIGHT, buff=0.5)
        self.play(DrawBorderThenFill(t1), run_time=2)
        self.play(Write(t2), run_time=5)
        self.wait()
        self.play(Write(t3), run_time=5)
        self.wait()
        self.play(ShowCreation(t4))
        self.play(
            ReplacementTransform(t4[0][0], t5), ReplacementTransform(t4[0][10], t5)
        )
        self.play(
            FadeIn(t5_A),
            FadeOut(t4),
            ReplacementTransform(t4[0][1], t5_1),
            ReplacementTransform(t4[0][3], t5_2),
            ReplacementTransform(t4[0][5], t5_3),
            ReplacementTransform(t4[0][7], t5_4),
            ReplacementTransform(t4[0][9], t5_5),
        )
        self.wait(2)

        t6 = (
            TextMobject("Set builder notation is another way to represent sets.")
            .scale(0.8)
            .next_to(t5, DOWN, buff=0.5)
            .align_to(t2, LEFT)
        )
        t7 = (
            TextMobject("\{n | n is a Natural number less then 6\} = \{1,2,3,4,5\}")
            .scale(0.8)
            .set_color(YELLOW)
            .next_to(t6, DOWN, buff=0.2)
            .align_to(t2, LEFT)
        )
        self.play(Write(t6), run_time=7)
        self.wait()
        self.play(Write(t7), run_time=5)
        self.wait()
        t8 = (
            TextMobject(
                "Note: a set with no element can be represented as \{\} or $\\emptyset$."
            )
            .scale(0.8)
            .next_to(t7, DOWN, buff=0.2)
            .align_to(t2, LEFT)
        )
        self.play(Write(t8), run_time=6)
        self.wait(2)
        group = VGroup(
            t1, t2, t3, t4, t5, t5_A, t5_1, t5_2, t5_3, t5_4, t5_5, t6, t7, t8
        )
        self.play(FadeOutAndShift(group, direction=DOWN))

    def cardinality_and_equivalency(self):
        n1 = (
            TextMobject("Cardinality and Equivalency")
            .set_color(PURPLE_A)
            .shift(np.array([-4, 3, 0]))
            .to_edge(LEFT)
        )
        n2 = (
            TextMobject(
                "The cardinality of a set is the total number of elements in the set."
            )
            .scale(0.8)
            .next_to(n1, DOWN, buff=0.2)
            .to_edge(LEFT)
        )
        n3 = (
            TextMobject("It is denoted as n(A) or |A|.")
            .scale(0.8)
            .next_to(n2, DOWN, buff=0.2)
            .to_edge(LEFT)
        )
        n4 = (
            TextMobject("Equivalency of Set")
            .set_color(PURPLE_A)
            .scale(0.8)
            .next_to(n3, DOWN, buff=0.4)
            .to_edge(LEFT)
        )
        n5 = (
            TextMobject(
                "Equivalency is a measure to compare the cardinality of two sets."
            )
            .scale(0.8)
            .next_to(n4, DOWN, buff=0.2)
            .to_edge(LEFT)
        )
        n6 = (
            TextMobject(
                "If the cardinal numbers of the given sets are equal, then they are called"
            )
            .scale(0.8)
            .next_to(n5, DOWN, buff=0.2)
            .to_edge(LEFT)
        )
        n7 = (
            TextMobject("equivalent sets.")
            .scale(0.8)
            .next_to(n6, DOWN, buff=0.2)
            .to_edge(LEFT)
        )
        n8 = (
            TextMobject("Equality of Set")
            .set_color(PURPLE_A)
            .scale(0.8)
            .next_to(n7, DOWN, buff=0.4)
            .to_edge(LEFT)
        )
        n9 = (
            TextMobject(
                "Equality is a measure to compare each element of given two or more sets."
            )
            .scale(0.8)
            .next_to(n8, DOWN, buff=0.2)
            .to_edge(LEFT)
        )
        n10 = (
            TextMobject(
                "If the cardinal numbers as well as the inner elements of the given sets"
            )
            .scale(0.8)
            .next_to(n9, DOWN, buff=0.2)
            .to_edge(LEFT)
        )
        n11 = (
            TextMobject("are equal to each other, then they are said to be equal sets.")
            .scale(0.8)
            .next_to(n10, DOWN, buff=0.2)
            .to_edge(LEFT)
        )

        self.play(DrawBorderThenFill(n1), run_time=2)
        self.play(Write(n2), run_time=6)
        self.play(Write(n3), run_time=3)
        self.wait()
        self.play(FadeInFrom(n4, direction=UP), run_time=3)
        self.play(Write(n5), run_time=6)
        self.wait()
        self.play(Write(n6), run_time=6)
        self.play(Write(n7), run_time=3)
        self.wait()
        self.play(FadeInFrom(n8, direction=UP))
        self.play(Write(n9), run_time=6)
        self.wait()
        self.play(Write(n10), run_time=6)
        self.play(Write(n11), run_time=7)
        self.wait(2)

        group1 = VGroup(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11)
        self.play(FadeOutAndShift(group1, direction=DOWN))
        cir1 = Circle(radius=1.5).shift(np.array([-2, 0, 0]))
        cir2 = Circle(radius=1.5).shift(np.array([2, 0, 0]))
        m = TextMobject("=").scale(1)
        m_1 = TexMobject("\\equiv").scale(1)
        cross = Cross(mobject=m, stroke_color=RED, stroke_width=1)
        m11 = TextMobject("1").shift(np.array([-2.5, 0.5, 0]))
        m12 = TextMobject("2").next_to(m11, RIGHT, buff=0.8)
        m13 = TextMobject("3").shift(np.array([-3, -0.5, 0]))
        m14 = TextMobject("4").next_to(m13, RIGHT, buff=0.7)
        m15 = TextMobject("5").next_to(m14, RIGHT, buff=0.7)

        m21 = TextMobject("1").shift(np.array([1.5, 0.5, 0]))
        m22 = TextMobject("3").next_to(m21, RIGHT, buff=0.8)
        m23 = TextMobject("5").shift(np.array([1, -0.5, 0]))
        m24 = TextMobject("7").next_to(m23, RIGHT, buff=0.7)
        m25 = TextMobject("9").next_to(m24, RIGHT, buff=0.7)

        m211 = TextMobject("1").shift(np.array([1.5, 0.5, 0]))
        m221 = TextMobject("2").next_to(m21, RIGHT, buff=0.8)
        m231 = TextMobject("3").shift(np.array([1, -0.5, 0]))
        m241 = TextMobject("4").next_to(m23, RIGHT, buff=0.7)
        m251 = TextMobject("5").next_to(m24, RIGHT, buff=0.7)
        m1 = (
            TextMobject("Note : Two equal sets are always equivalent.")
            .set_color(YELLOW)
            .shift(np.array([-1, -2, 0]))
        )

        self.play(ShowCreation(cir1))
        self.play(ShowCreation(cir2))
        self.play(FadeIn(m11), FadeIn(m12), FadeIn(m13), FadeIn(m14), FadeIn(m15))
        self.play(FadeIn(m21), FadeIn(m22), FadeIn(m23), FadeIn(m24), FadeIn(m25))

        self.play(ShowCreation(m))
        self.play(FadeIn(cross))
        self.wait(1)
        group1_1 = VGroup(m, cross)
        self.play(ReplacementTransform(group1_1, m_1))
        note = (
            TextMobject("Note : $\\equiv$ represents Equivalence Sign")
            .scale(0.8)
            .shift(np.array([0, -3, 0]))
            .set_color(YELLOW)
        )
        self.play(FadeIn(note))
        self.wait(2)
        self.play(FadeOut(m_1), FadeOut(note))

        self.play(
            Transform(m21, m211),
            Transform(m22, m221),
            Transform(m23, m231),
            Transform(m24, m241),
            Transform(m25, m251),
        )
        m = TextMobject("=").scale(1)
        m.shift(np.array([0, 0.3, 0]))
        m_1.next_to(m, DOWN, buff=0.5)
        self.play(FadeIn(m))
        self.play(FadeIn(m_1))
        self.play(FadeIn(m1))
        self.wait(2)
        group2 = VGroup(
            cir1,
            cir2,
            m,
            m_1,
            cross,
            m1,
            m11,
            m12,
            m12,
            m13,
            m14,
            m15,
            m21,
            m22,
            m23,
            m24,
            m25,
        )
        self.play(FadeOutAndShift(group2, direction=DOWN))

    def venn_diagram(self):
        l = TextMobject("Venn Diagram").set_color(PURPLE_A).shift(np.array([0, 3.5, 0]))
        self.play(DrawBorderThenFill(l))

        rec = Rectangle(height=3.5, width=4.5)
        cir1 = Circle(radius=1.2).shift(np.array([0.7, 0, 0]))
        cir2 = Circle(radius=1.2).shift(np.array([-0.7, 0, 0]))

        self.play(ShowCreation(rec))
        self.play(ShowCreation(cir1))
        self.play(ShowCreation(cir2))

        arr1 = Arrow(np.array([0, -2, 0]), np.array([0, 0, 0]), buff=0)
        arr2 = Arrow(np.array([3, 1, 0]), np.array([1.5, 0, 0]), buff=0)
        arr3 = Arrow(np.array([-3, 1, 0]), np.array([-1.5, 0, 0]), buff=0)
        arr4 = Arrow(np.array([-2.8, -1, 0]), np.array([-1.6, -1, 0]), buff=0)

        arr1_1 = (
            TextMobject("Elements shared by set A and B")
            .scale(0.6)
            .shift(np.array([0, -2.3, 0]))
        )
        arr1_2 = (
            TextMobject("Elements in set A").scale(0.6).shift(np.array([4.2, 1, 0]))
        )
        arr1_3 = (
            TextMobject("Elements in set B").scale(0.6).shift(np.array([-4.2, 1, 0]))
        )
        arr1_4 = (
            TextMobject("Elements outside A and B")
            .scale(0.6)
            .shift(np.array([-5, -1, 0]))
        )
        arr1_5 = (
            TextMobject("but inside universal set")
            .scale(0.6)
            .next_to(arr1_4, DOWN, buff=0.2)
            .align_to(arr1_4, LEFT)
        )

        self.play(FadeIn(arr1), FadeIn(arr2), FadeIn(arr3), FadeIn(arr4))
        labels = [arr1_1, arr1_2, arr1_3, arr1_4, arr1_5]
        for label in labels:
            self.play(Write(label), run_time=3)
        self.wait(3)

        l1 = (
            TextMobject("U=\{The set of natural numbers from 1 to 10\}")
            .scale(0.6)
            .shift(np.array([-2, 3, 0]))
        )
        l2 = (
            TextMobject("A=\{The set of even nunbers from 1 to 5\}")
            .scale(0.6)
            .next_to(l1, DOWN, buff=0.1)
            .align_to(l1, LEFT)
        )
        l3 = (
            TextMobject("B=\{The set of odd numbers from 1 to 7\}")
            .scale(0.6)
            .next_to(l2, DOWN, buff=0.1)
            .align_to(l1, LEFT)
        )
        s11 = TextMobject("2").scale(0.6).shift(np.array([0.7, 0.5, 0]))
        s12 = TextMobject("3").scale(0.6).next_to(s11, RIGHT, buff=0.5)
        s13 = TextMobject("5").scale(0.6).shift(np.array([0.7, -0.3, 0]))
        s14 = TextMobject("7").scale(0.6).next_to(s13, RIGHT, buff=0.5)
        s21 = TextMobject("1").scale(0.6).shift(np.array([-1.3, 0.5, 0]))
        s22 = TextMobject("3").scale(0.6).next_to(s21, RIGHT, buff=0.5)
        s23 = TextMobject("5").scale(0.6).shift(np.array([-1.3, -0.3, 0]))
        s24 = TextMobject("7").scale(0.6).next_to(s23, RIGHT, buff=0.5)

        s31 = TextMobject("9").scale(0.6).shift(np.array([-1.3, -1.3, 0]))

        self.play(FadeIn(TextMobject("U").scale(0.7).move_to(np.array([2, 1.5, 0]))))
        self.play(FadeIn(TextMobject("A").scale(0.7).move_to(np.array([0.7, 1.54, 0]))))
        self.play(
            FadeIn(TextMobject("B").scale(0.7).move_to(np.array([-0.7, 1.54, 0])))
        )

        self.play(Write(l1), run_time=4)
        self.play(Write(l2), run_time=4)
        self.play(Write(l3), run_time=4)

        self.play(
            ReplacementTransform(arr2, s11),
            ReplacementTransform(arr1_2[0][0:4], s12),
            ReplacementTransform(arr1_2[0][4:8], s13),
            ReplacementTransform(arr1_2[0][8:16], s14),
        )
        self.play(
            ReplacementTransform(arr3, s21),
            ReplacementTransform(arr1_3[0][0:6], s22),
            ReplacementTransform(arr1_3[0][6:12], s23),
            ReplacementTransform(arr1_3[0][12:16], s24),
        )
        self.play(
            ReplacementTransform(arr4, s31),
            ReplacementTransform(arr1_4, s31),
            ReplacementTransform(arr1_5, s31),
        )
        self.play(FadeOut(arr1), FadeOut(arr1_1))
        self.play(
            ApplyMethod(s12.move_to, np.array([0, 0.5, 0])),
            ApplyMethod(s22.move_to, np.array([0, 0.5, 0])),
        )
        self.play(
            ApplyMethod(s13.next_to, s12, DOWN, buff=0),
            ApplyMethod(s23.next_to, s22, DOWN, buff=0),
        )
        self.play(
            ApplyMethod(s14.next_to, s13, DOWN, buff=0),
            ApplyMethod(s24.next_to, s23, DOWN, buff=0),
        )
        self.play(
            ApplyMethod(s11.move_to, np.array([1.1, 0, 0])),
            ApplyMethod(s21.move_to, np.array([-1.1, 0, 0])),
        )
        self.wait(4)
