from manimlib.imports import *


# class VectorExcercises(Scene):
class Test(Scene):
    def construct(self):
        self.intro()
        self.example3()
        self.example4()
        self.wait(3)

    def intro(self):
        title = TextMobject("Vector: Worked out examples", color=BLUE)
        title.scale(1.5)
        self.play(Write(title), run_time=3)
        self.wait(1)
        self.play(FadeOutAndShift(title, UP))

    def example3(self):
        ques = TextMobject(
            "Q. Prove that in any triangle $c^2 = a^2 + b^2 - 2abcosC$", color=BLUE
        ).scale(1.2)
        ques_top = ques.generate_target().scale(0.8).to_edge(UP, buff=0.1)

        triangle = Triangle()
        A, B, C = triangle.scale(1.2).get_vertices()

        label_A, label_B, label_C = (TexMobject(i).scale(0.8) for i in "ABC")
        label_A.next_to(A, UP)
        label_B.next_to(B, DR, buff=0.1)
        label_C.next_to(C, DL, buff=0.1)
        labels = VGroup(label_A, label_B, label_C)

        ex_AB = Line(A, B, color=BLUE).scale(1.5)
        ex_AC = Line(A, C, color=BLUE).scale(1.5)
        ex_BC = Line(B, C, color=BLUE).scale(1.5)
        sides = VGroup(ex_AB, ex_AC, ex_BC)

        vec_tex = lambda x: TexMobject("\\vec{" + x + "}")
        vec_label_a, vec_label_b, vec_label_c = (vec_tex(i).scale(0.8) for i in "abc")
        vec_label_a.next_to(midpoint(B, C), DOWN, buff=0.2)
        vec_label_b.next_to(midpoint(A, C), RIGHT, buff=0.2)
        vec_label_c.next_to(midpoint(A, B), LEFT, buff=0.2)
        vec_labels = VGroup(vec_label_a, vec_label_b, vec_label_c)

        angle_PI_min_C = ArcBetweenPoints(C + RIGHT / 3, C + (UP + LEFT / 2) / 3)
        PI_min_C_tex = TexMobject("\\pi - C").scale(0.8).next_to(C, UR)
        PI_min_C = VGroup(angle_PI_min_C, PI_min_C_tex)

        figure = VGroup(triangle, labels, sides, vec_labels, PI_min_C)
        figure_pos = figure.generate_target().to_edge(UR, buff=0.1).shift(DOWN / 1.5)

        texts = (
            "In any triangle ABC, let $\\vec{BC} = \\vec{a}$,",
            "$\\vec{CA} = \\vec{b}$, and $\\vec{AB} = \\vec{c}$.",
            "By the definition of vector addition,",
            "$\\vec{AB} = \\vec{AC}\ +\ \\vec{CB}$",
            "$\\vec{c} = -\ \\vec{b}\ -\ \\vec{a}$",
            "or, $c^2 = (\\vec{b}\ +\ \\vec{a})^2$",
            " $= a^2\ +\ 2 \\vec{a} \\vec{b}\ +\ b^2$",
            " $= a^2\ +\ b^2 +\ 2abcos(\\pi - C)$",
            "Thus, we got $c^2\ =\ a^2\ +\ b^2\ -\ 2abcosC$",
        )
        texts_g = VGroup(*[TextMobject(i).scale(0.95) for i in texts])
        texts_g.arrange(DOWN, center=False).to_edge(UL).shift(DOWN / 3)

        last_calc, last_line = -2, -1
        texts_g[last_calc].shift(RIGHT)
        texts_g[last_line].shift(2 * RIGHT)

        self.play(Write(ques), run_time=3)
        self.wait(3)
        self.play(MoveToTarget(ques))

        self.play(ShowCreation(figure), run_time=5)
        self.wait(2)
        self.play(MoveToTarget(figure))
        self.wait(3)

        for line in texts_g:
            self.play(Write(line), run_time=3)

        self.wait(3)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))

    def example4(self):
        ques = TextMobject(
            "Q. Prove that the angle in the semi-circle is a right angle.", color=BLUE
        ).scale(1.1)
        ques_top = ques.generate_target().scale(0.8).to_edge(UP, buff=0.1)

        d1, d2 = 1.5 * LEFT, 1.5 * RIGHT
        semi_circle = ArcBetweenPoints(d1, d2, angle=-PI)
        center = midpoint(d1, d2)
        point_O = SmallDot(center)
        point_P = (UP / 1.2 + RIGHT / 2) * 1.5

        diameter_line = Line(d1, d2, color=BLUE)
        line_AP = Line(d1, point_P, color=BLUE)
        line_BP = Line(d2, point_P, color=BLUE)
        line_OP = Line(center, point_P, color=BLUE)
        lines = VGroup(diameter_line, line_AP, line_BP, line_OP)

        label_A, label_B, label_O, label_P = (TexMobject(i).scale(0.8) for i in "ABOP")
        label_O.next_to(center, DOWN, buff=0.1)
        label_A.next_to(d1, DOWN, buff=0.1)
        label_B.next_to(d2, DOWN, buff=0.1)
        label_P.next_to(point_P, UR, buff=0.1)
        labels = VGroup(label_A, label_O, label_P, label_B)

        figure = VGroup(semi_circle, point_O, lines, labels)
        figure_pos = figure.generate_target().to_edge(UR, buff=0.1).shift(DOWN / 1.5)

        texts = (
            "Let APB be an angle in the semi-circle.",
            "Let O be the origin.",
            "If $\\vec{OA} = \\vec{a}$, then $\\vec{OB} = -\\vec{a}$ also, let $\\vec{OP} = \\vec{r}$",
            "Then,",
            "$\\vec{PA} = \\vec{PO}\ +\ \\vec{OA}\ =\ -\\vec{r}\ +\ \\vec{a}$",
            "And, $\\vec{PB} = \\vec{PO}\ +\ \\vec{OB}\ =\ -\\vec{r}\ -\ \\vec{a}$",
            "Now,",
            "$\\vec{PA} \\cdot \\vec{PB} = (-\\vec{r}\ +\ \\vec{a}) \\cdot (-\\vec{r}\ -\ \\vec{a})$",
            " = $r^2 - a^2$ [OA = OP]",
            " = 0",
            "Thus, angle APB = $90^{\\circ}$",
        )
        texts_g = VGroup(*[TextMobject(i).scale(0.8) for i in texts])
        texts_g.arrange(DOWN, center=False).to_edge(UL).shift(DOWN / 3)

        second_last_calc, last_calc, last_line = -3, -2, -1
        texts_g[second_last_calc].shift(RIGHT / 2)
        texts_g[last_calc].shift(LEFT)
        texts_g[last_line].shift(3 * RIGHT)

        self.play(Write(ques), run_time=3)
        self.wait(3)
        self.play(MoveToTarget(ques))

        self.play(ShowCreation(figure), run_time=5)
        self.wait(2)
        self.play(MoveToTarget(figure))
        self.wait(3)

        for line in texts_g:
            self.play(Write(line), run_time=3)

        self.wait(3)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))
