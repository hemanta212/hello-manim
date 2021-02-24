from manimlib.imports import *


class Set3(Scene):
    def construct(self):
        self.one()
        self.two()
        self.three()

    def one(self):
        a = (
            TextMobject(
                "Find set A having elements described by {n | n is an odd prime till 15}"
            )
            .scale(0.8)
            .shift(np.array([0, 2.5, 0]))
            .to_edge(LEFT)
        )
        a1 = (
            TextMobject("and find its cardinality.")
            .scale(0.8)
            .next_to(a, DOWN, buff=0.2)
            .to_edge(LEFT)
        )
        a2 = (
            TextMobject("Solution:")
            .scale(0.8)
            .next_to(a1, DOWN, buff=0.5)
            .to_edge(LEFT)
        )
        a3 = (
            TextMobject("A = \{2,3,5,7,11,13\}")
            .scale(0.8)
            .next_to(a2, DOWN, buff=0.2)
            .to_edge(LEFT)
        )
        a4 = (
            TextMobject("Cardinality of A (n(A)) = 6")
            .scale(0.8)
            .next_to(a3, DOWN, buff=0.2)
            .to_edge(LEFT)
        )
        self.play(Write(a), run_time=5)
        self.play(Write(a1))
        self.wait(3)
        for text in (a2, a3, a4):
            self.play(Write(text))
        self.wait(3)
        self.play(FadeOutAndShiftDown(VGroup(a, a1, a2, a3, a4)))

    def two(self):
        rec = Rectangle(height=3.5, width=4.5)
        cir1 = Circle(radius=1.2).shift(np.array([0.7, 0, 0]))
        cir2 = Circle(radius=1.2).shift(np.array([-0.7, 0, 0]))

        arr1 = Arrow(np.array([3, 0, 0]), np.array([2, 0, 0]), buff=0)
        arr2 = Arrow(np.array([-0.7, -2.5, 0]), np.array([-0.7, -1.2, 0]), buff=0)
        arr3 = Arrow(np.array([1, -2, 0]), np.array([0, 0, 0]), buff=0)
        arr4 = Arrow(np.array([3, 1.2, 0]), np.array([2.3, 1.2, 0]), buff=0)
        # arr4=Arrow(np.array([3,1.2,0]),np.array([2.3,1.2,0]),buff=0)

        arr11 = TextMobject("n(I)=450").scale(0.7).shift(np.array([3.8, 0, 0]))
        arr21 = TextMobject("n(T)=400").scale(0.7).shift(np.array([-0.7, -2.7, 0]))
        arr31 = TextMobject("n(T$\\cap$I)=150").scale(0.7).shift(np.array([1, -2.2, 0]))
        arr41 = TextMobject("n(U)=850").scale(0.7).shift(np.array([3.8, 1.2, 0]))

        b = (
            TextMobject(
                "A survey carried among 850 customers shows that 400 of them like to watch"
            )
            .scale(0.8)
            .shift(np.array([0, 3.4, 0]))
            .to_edge(LEFT)
        )
        b1 = (
            TextMobject(
                "their favorite shows in televisions, 450 like to watch it in their iPhones"
            )
            .scale(0.8)
            .next_to(b, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        b2 = (
            TextMobject(
                "and 150 like to enjoy it in both platforms. Represent the information in "
            )
            .scale(0.8)
            .next_to(b1, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        b2_1 = (
            TextMobject("a Venn–diagram and find:")
            .scale(0.8)
            .next_to(b2, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        b3 = (
            TextMobject(
                "i. the number of people who like to watch it on Television only."
            )
            .scale(0.7)
            .next_to(b2_1, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        b4 = (
            TextMobject(
                "ii. the number of people who like to watch either on their Television or iPhone."
            )
            .scale(0.7)
            .next_to(b3, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        b5 = (
            TextMobject("iii. the number of customers who used neither of them. ")
            .scale(0.7)
            .next_to(b4, DOWN, buff=0.1)
            .to_edge(LEFT)
        )

        n = (
            TextMobject("Solution: ")
            .scale(0.8)
            .next_to(b5, DOWN, buff=0.3)
            .to_edge(LEFT)
        )
        n1 = TextMobject("Let, ").scale(0.8).next_to(n, DOWN, buff=0.1).to_edge(LEFT)
        n2 = (
            TextMobject("T = set of customers who like to")
            .scale(0.8)
            .next_to(n1, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n2_1 = (
            TextMobject("watch it on Television")
            .scale(0.8)
            .next_to(n2, DOWN, buff=0.1)
            .align_to(n2[0][2], LEFT)
        )
        n3 = (
            TextMobject("I = set of customers who like to")
            .scale(0.8)
            .next_to(n2_1, DOWN, buff=0.2)
            .to_edge(LEFT)
        )
        n3_1 = (
            TextMobject("watch it on their iPhones")
            .scale(0.8)
            .next_to(n3, DOWN, buff=0.1)
            .align_to(n3[0][2], LEFT)
        )
        n4 = (
            TextMobject("Then, by question, ")
            .scale(0.8)
            .next_to(n3_1, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n5 = (
            TextMobject("n(U) = 850, n(T) = 400, n(I) = 450 ")
            .scale(0.8)
            .next_to(n4, DOWN, buff=0.3)
            .to_edge(LEFT)
        )
        n6 = (
            TextMobject("n(T$\\cap$I) = 150 ")
            .scale(0.8)
            .next_to(n5, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n7 = (
            TextMobject("(i). $n_0$(T) = ? ")
            .scale(0.8)
            .next_to(n, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n8 = (
            TextMobject("(ii) n(TUI) = ? ")
            .scale(0.8)
            .next_to(n7, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n9 = TextMobject("(iii) n(TUI) = ? ").scale(0.8).next_to(n7, RIGHT, buff=0.5)
        n10 = TextMobject("Now, ").scale(0.8).next_to(n8, DOWN, buff=0.1).to_edge(LEFT)
        n11 = (
            TextMobject("(i) no(T) = n(T) - n(T$\\cap$I)")
            .scale(0.8)
            .next_to(n10, DOWN, buff=0.3)
            .to_edge(LEFT)
        )
        n11_1 = (
            TextMobject("= 400 – 150 = 250")
            .scale(0.8)
            .next_to(n11, DOWN, buff=0.1)
            .align_to(n11[0][8], LEFT)
            .set_color(YELLOW)
        )
        n12 = (
            TextMobject("(ii) n(TUI) = n(T) + n(I) - n(T$\\cap$I) ")
            .scale(0.8)
            .next_to(n11_1, DOWN, buff=0.3)
            .to_edge(LEFT)
        )
        n13 = (
            TextMobject("=400 +450 – 150 = 700")
            .scale(0.8)
            .next_to(n12, DOWN, buff=0.1)
            .align_to(n12[0][10], LEFT)
            .set_color(YELLOW)
        )
        n14 = (
            TextMobject("(iii) n(TUI) = n(U) – n(TUI) ")
            .scale(0.8)
            .next_to(n, DOWN, buff=0.3)
            .to_edge(LEFT)
        )
        n15 = (
            TextMobject("= 850 – 700 =150 ")
            .scale(0.8)
            .next_to(n14, DOWN, buff=0.1)
            .align_to(n14[0][11], LEFT)
            .set_color(YELLOW)
        )

        for text in (b, b1, b2):
            self.play(Write(text), run_time=5)
        self.play(Write(b2_1))
        for text in (b3, b4, b5):
            self.play(Write(text), run_time=5)
        self.wait(3)

        U = TextMobject("U").scale(0.7).move_to(np.array([2, 1.5, 0]))
        I = TextMobject("I").scale(0.7).move_to(np.array([0.7, 1.54, 0]))
        T = TextMobject("T").scale(0.7).move_to(np.array([-0.7, 1.54, 0]))

        group = VGroup(
            U, I, T, rec, cir1, cir2, arr1, arr2, arr3, arr4, arr11, arr21, arr31, arr41
        )
        group.shift(2 * RIGHT + 1 * DOWN).scale(0.8)

        for i in (rec, cir1, cir2):
            self.play(ShowCreation(i))

        self.play(FadeIn(VGroup(U, I, T)))

        fadeins = (arr1, arr2, arr3, arr4, arr11, arr21, arr31, arr41)
        for i in fadeins:
            self.play(FadeIn(i))

        self.play(Write(n))
        n_1_to_6 = (n1, n2, n2_1, n3, n3_1, n4, n5, n6)
        for i in n_1_to_6:
            self.play(Write(i), run_time=3)

        self.wait(2)
        self.play(FadeOutAndShift(VGroup(*n_1_to_6)))
        n_7_to_13 = (n7, n8, n9, n10, n11, n11_1, n12, n13)
        for i in n_7_to_13:
            self.play(Write(i), run_time=3)

        self.wait(2)
        self.play(FadeOutAndShift(VGroup(*n_7_to_13)))
        self.play(Write(n14))
        self.play(Write(n15))
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(n, n14, n15)))
        self.play(FadeOutAndShiftDown(group))
        self.play(FadeOutAndShiftDown(VGroup(b, b1, b2, b2_1, b3, b4, b5)))

    def three(self):
        rec = Rectangle(height=4.5, width=4.5).shift(np.array([0, -0.5, 0]))
        cir1 = Circle(radius=1.2).shift(np.array([0.7, 0, 0]))
        cir2 = Circle(radius=1.2).shift(np.array([-0.7, 0, 0]))
        cir3 = Circle(radius=1.2).shift(np.array([0, -1, 0]))

        U = TextMobject("U").scale(0.7).move_to(np.array([2, 1.5, 0]))
        A = TextMobject("E").scale(0.7).move_to(np.array([0.7, 1.54, 0]))
        B = TextMobject("M").scale(0.7).move_to(np.array([-0.7, 1.54, 0]))
        C = TextMobject("C").scale(0.7).move_to(np.array([-0.5, -2.5, 0]))

        arrA = Arrow(np.array([4, 0, 0]), np.array([2, 0, 0]), buff=0, stroke_width=3)
        arranb = Arrow(
            np.array([3, 2, 0]), np.array([0, 0.5, 0]), buff=0, stroke_width=3
        )
        arrB = Arrow(np.array([-4, 0, 0]), np.array([-2, 0, 0]), buff=0, stroke_width=3)
        arrbnc = Arrow(
            np.array([-3, -0.5, 0]), np.array([-0.7, -0.5, 0]), buff=0, stroke_width=3
        )
        arrC = Arrow(
            np.array([3, -1.4, 0]), np.array([1.2, -1.4, 0]), buff=0, stroke_width=3
        )
        arranc = Arrow(
            np.array([2.5, -0.5, 0]), np.array([0.7, -0.5, 0]), buff=0, stroke_width=3
        )
        arruni = Arrow(
            np.array([3.2, -2.2, 0]), np.array([1.4, -2.2, 0]), buff=0, stroke_width=3
        )

        A_1 = TextMobject("n(E)=35").scale(0.6).shift(np.array([4.6, 0, 0]))
        AnB = TextMobject("n(M $\\cap$ E)=11").scale(0.6).shift(np.array([4, 2, 0]))
        B_1 = TextMobject("n(M)=42").scale(0.6).shift(np.array([-4.6, 0, 0]))
        BnC = TextMobject("n(M $\\cap$ C)=9").scale(0.6).shift(np.array([-4, -0.5, 0]))
        C_1 = TextMobject("n(C)=30").scale(0.6).shift(np.array([3.6, -1.4, 0]))
        AnC = (
            TextMobject("n(E $\\cap$ C)=10").scale(0.6).shift(np.array([3.6, -0.5, 0]))
        )
        uni1 = (
            TextMobject("n($\overline{E \\cap M \\cap C}$)=20")
            .scale(0.6)
            .shift(np.array([3.9, -2.5, 0]))
        )

        c = (
            TextMobject(
                "Among the students in an examination, 42\% offered Mathematics, 35\% offered"
            )
            .scale(0.7)
            .shift(np.array([0, 3.5, 0]))
            .to_edge(LEFT)
        )
        c1 = (
            TextMobject(
                "English and 30\% offered Computer. If 20\% offered none of these subjects,"
            )
            .scale(0.7)
            .next_to(c, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        c2 = (
            TextMobject(
                "9\% offered Mathematics and Computer, 10\% offered English and Computer"
            )
            .scale(0.7)
            .next_to(c1, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        c3 = (
            TextMobject(
                "and 11\% offered Mathematics and English. Draw a Venn diagram and find "
            )
            .scale(0.7)
            .next_to(c2, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        c4 = (
            TextMobject("(i) the percent of students offering all three subjects.")
            .scale(0.7)
            .next_to(c3, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        c5 = (
            TextMobject("(ii) the percent of students offering Mathematics only.")
            .scale(0.7)
            .next_to(c4, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        c6 = (
            TextMobject(
                "(iii) the number of students offering English and Computer only if"
            )
            .scale(0.7)
            .next_to(c5, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        c7 = (
            TextMobject("attended the examination. ")
            .scale(0.7)
            .next_to(c6, DOWN, buff=0.1)
            .align_to(c6[0][5], LEFT)
        )
        n = (
            TextMobject("Solution: ")
            .scale(0.7)
            .next_to(c7, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n1 = (
            TextMobject("In the Venn-diagram, let M, E and C denote")
            .scale(0.7)
            .next_to(n, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n2 = (
            TextMobject("the sets of students who offered the subjects")
            .scale(0.7)
            .next_to(n1, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n2_1 = (
            TextMobject("Mathematics, English and Computer ")
            .scale(0.7)
            .next_to(n2, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n2_2 = (
            TextMobject("respectively.")
            .scale(0.7)
            .next_to(n2_1, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n3 = (
            TextMobject("Now, let n(U) = 100. Then,")
            .scale(0.7)
            .next_to(n2_2, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n4 = (
            TextMobject("n(M) = 42, n(E) = 35, n(C) = 30")
            .scale(0.7)
            .next_to(n3, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n5 = (
            TextMobject("n(M$\\cap$E) = 11, n(E$\\cap$C) =10, (M$\\cap$C) = 9,")
            .scale(0.7)
            .next_to(n4, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n6 = (
            TextMobject("and, n(MUEUC) = 20")
            .scale(0.7)
            .next_to(n5, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n7 = (
            TextMobject("(i) n(M$\\cap$E$\\cap$C) = ? ")
            .scale(0.7)
            .next_to(n, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n8 = (
            TextMobject("(ii) $n_0$(M) = ? ")
            .scale(0.7)
            .next_to(n7, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n9 = (
            TextMobject("(iii) $n_0$(E$\\cap$C) = ? ")
            .scale(0.7)
            .next_to(n8, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n10 = (
            TextMobject("Now, n(MUEUC) = n(U) - n(MUEUC) ")
            .scale(0.7)
            .next_to(n9, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n11 = (
            TextMobject("= 100 -20 = 80 ")
            .scale(0.7)
            .next_to(n10, DOWN, buff=0.1)
            .align_to(n10[0][12], LEFT)
            .set_color(YELLOW)
        )
        n12 = (
            TextMobject("Percent of students who offered at ")
            .scale(0.7)
            .next_to(n11, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n12_1 = (
            TextMobject("least one subject=80%")
            .scale(0.7)
            .next_to(n12, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n13 = (
            TextMobject("i.We have,")
            .scale(0.7)
            .next_to(n12_1, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n14 = (
            TextMobject("n(MUEUC) =n(M) + n(E) + n(C) - n(M$\\cap$E)")
            .scale(0.7)
            .next_to(n, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n14_1 = (
            TextMobject("- n(E$\\cap$C) - n(C$\\cap$M) + n(M$\\cap$E$\\cap$C)")
            .scale(0.7)
            .next_to(n14, DOWN, buff=0.1)
            .align_to(n14[0][9], LEFT)
        )
        n15 = (
            TextMobject("or, 80 = 42 + 35 + 30 - 11  ")
            .scale(0.7)
            .next_to(n14_1, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n15_1 = (
            TextMobject("– 10 -9 + n(M$\\cap$E$\\cap$C)")
            .scale(0.7)
            .next_to(n14_1, DOWN, buff=0.1)
            .align_to(n15[0][7], LEFT)
        )
        n16 = (
            TextMobject("or, n(M$\\cap$E$\\cap$C) = 80 – 107 + 30 = 3")
            .scale(0.7)
            .next_to(n15_1, DOWN, buff=0.1)
            .to_edge(LEFT)
            .set_color(YELLOW)
        )
        n17 = (
            TextMobject("Therefore, 3\% students offered all three subjects.")
            .scale(0.7)
            .next_to(n16, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n18 = (
            TextMobject(
                "ii.$n_0$(M)=n(M)–n(M$\\cap$E)–n(M$\\cap$C)+n(M$\\cap$E$\\cap$C)"
            )
            .scale(0.7)
            .next_to(n17, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n19 = (
            TextMobject("= 42 – 11 – 9 + 3 = 25 ")
            .scale(0.7)
            .next_to(n18, DOWN, buff=0.1)
            .align_to(n18[0][8], LEFT)
            .set_color(YELLOW)
        )
        n20 = (
            TextMobject("Therefore, 25\% students offered Mathematics only. ")
            .scale(0.7)
            .next_to(n19, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n21 = (
            TextMobject("iii.$n_0$(E$\\cap$C) = n(E$\\cap$C) – n(M$\\cap$E$\\cap$C) ")
            .scale(0.7)
            .next_to(n, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n22 = (
            TextMobject("= 10 – 3 = 7 ")
            .scale(0.7)
            .next_to(n21, DOWN, buff=0.1)
            .align_to(n21[0][11], LEFT)
            .set_color(YELLOW)
        )
        n23 = (
            TextMobject("Therefore, percent of students who ")
            .scale(0.7)
            .next_to(n22, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n23_1 = (
            TextMobject("offered English and Computer only is 7\%.")
            .scale(0.7)
            .next_to(n23, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n24 = (
            TextMobject("The number of students who offered ")
            .scale(0.7)
            .next_to(n23_1, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n24_1 = (
            TextMobject("English and Computer only is ")
            .scale(0.7)
            .next_to(n24, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n25 = (
            TextMobject("7\% of 200 ")
            .scale(0.7)
            .next_to(n24_1, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n26 = (
            TextMobject("=7 * $\\frac{200}{100}$")
            .scale(0.7)
            .next_to(n25, DOWN, buff=0.1)
            .to_edge(LEFT)
        )
        n27 = TextMobject("=14").scale(0.7).next_to(n26, DOWN, buff=0.1).to_edge(LEFT)
        n28 = (
            TextMobject("So,$n_0$(E$\\cap$C) = 14 ")
            .scale(0.7)
            .next_to(n26, RIGHT, buff=0.8)
            .set_color(YELLOW)
        )

        writes = (c, c1, c2, c3, c4, c5, c6, c7)
        for i in writes:
            self.play(Write(i), run_time=5)
        self.wait(3)

        group1 = VGroup(
            rec,
            cir1,
            cir2,
            cir3,
            U,
            A,
            B,
            C,
            arrA,
            A_1,
            arrB,
            B_1,
            arranb,
            AnB,
            arrbnc,
            C_1,
            BnC,
            arranc,
            arrC,
            AnC,
            arruni,
            uni1,
        )

        group1.shift(3 * RIGHT + 1 * DOWN).scale(0.7)
        show_creations = (
            rec,
            cir1,
            cir2,
            cir3,
        )
        for i in show_creations:
            self.play(ShowCreation(i))
        self.play(FadeIn(VGroup(U, A, B, C)))
        self.wait(2)

        self.play(
            FadeIn(
                VGroup(
                    arrA,
                    A_1,
                    arrB,
                    B_1,
                    arranb,
                    C_1,
                    AnB,
                    arrbnc,
                    arrC,
                    BnC,
                    arranc,
                    AnC,
                    arruni,
                    uni1,
                )
            )
        )

        self.wait(2)

        self.play(Write(n))
        n_1_to_6 = (
            n1,
            n2,
            n2_1,
            n2_2,
            n3,
            n4,
            n5,
            n6,
        )
        for i in n_1_to_6:
            self.play(Write(i), run_time=5)

        self.wait(2)
        self.play(FadeOutAndShift(VGroup(*n_1_to_6)))
        n_7_to_13 = (
            n7,
            n8,
            n9,
            n10,
            n11,
            n12,
            n12_1,
            n13,
        )
        for i in n_7_to_13:
            self.play(Write(i), run_time=3)

        self.wait(2)
        self.play(FadeOutAndShift(VGroup(*n_7_to_13)))

        n_14_to_20 = (
            n14,
            n14_1,
            n15,
            n16,
            n17,
            n18,
            n19,
            n20,
        )
        for i in n_14_to_20:
            self.play(Write(i), run_time=3)
        self.wait(2)
        self.play(FadeOutAndShift(VGroup(*n_14_to_20)))

        n_21_to_28 = (
            n21,
            n22,
            n23,
            n23_1,
            n24,
            n24_1,
            n25,
            n26,
            n27,
            n28,
        )
        for i in n_21_to_28:
            self.play(Write(i), run_time=3)
        self.wait(3)
