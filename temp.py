from manimlib.imports import *


class Test(Scene):
    scalar_topic = None

    def construct(self):
        # self.topic()
        # self.intro()
        # self.vector_intro_graph()
        # self.algebric_calc()
        self.geometric_interpretation()
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
            r"If $\vec{A}$ ($a_1$, $b_1$) and $\vec{B}$ ($a_2$, $b_2$) be two",
            "vectors then their scalar product is given by",
            r"$\vec{A} \cdot \vec{B}$ = ($a_1$, $b_1$) $\cdot$ ($a_2$, $b_2$)",
            "= $a_1 a_2$ + $b_1 b_2$"
            )
        intro_text = VGroup(*[TextMobject(i) for i in intro])
        intro_text.arrange(DOWN, center=False).shift(UP)
        self.play(Write(intro_text), run_time=8)

        for_eg_text = TextMobject(
           r"Let us take two vectors $\vec{A}$ = 2i + 2j and $\vec{B}$ = 2i, ",
        )
        for_eg_text.to_edge(DOWN).shift(UP)
        self.play(Write(for_eg_text), run_time=3)
        
        self.wait(3)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))


    def vector_intro_graph(self):
        grid = NumberPlane(background_line_style={'stroke_color':WHITE})

        va = Vector(direction=UR, color=GREEN).scale(2).shift(UR/2)
        vb = Vector(color=BLUE).scale(2, about_edge=LEFT)

        va_coor_tex = TexMobject("\\vec{A} \ \ (2, 2)")
        vb_coor_tex = TexMobject("\\vec{B} \ \ (2, 0)")
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

    def algebric_calc(self):
        title = TextMobject("Solving algebraically, ")
        title.to_edge(UL)

        a_b = TexMobject(r"\vec{A} \cdot \vec{B} =").to_edge(UL).shift(DOWN)
        tex_parts = [TexMobject(i) for i in ["(2i", "+", '2j)', r'\cdot', '(2i', '+', '0j)']]
        vec_parts = [tex for n, tex in enumerate(tex_parts) if n%2==0]
        i_parts = VGroup(vec_parts[0], vec_parts[2]).set_color(BLUE)
        j_parts = VGroup(vec_parts[1], vec_parts[3]).set_color(ORANGE)

        row_one = [a_b]
        for tex in tex_parts:
            tex.next_to(row_one[-1])
            row_one.append(tex)

        a_b2 = a_b.copy().shift(DOWN)
        i_dest = TexMobject(r"(2i \cdot 2i) \ + \ ", color=BLUE).next_to(a_b2)
        j_dest = TexMobject(r"(2j \cdot 0j)", color=ORANGE).next_to(i_dest)
        two_row = VGroup(a_b2, i_dest, j_dest)

        a_b3 = a_b2.copy().shift(DOWN)
        new_row = VGroup(a_b3, TexMobject("4").next_to(a_b3))

        conclusion = TextMobject(r"$\therefore$ the scalar product of $\vec{A}$ and $\vec{B}$ is 4.")
        conclusion.next_to(new_row, DOWN, buff=1.0).to_edge(LEFT)

        self.play(Write(title), run_time=3)
        self.wait()
        self.play(Write(VGroup(*row_one)))

        self.play(ReplacementTransform(a_b.copy(), a_b2))
        self.wait()
        self.play(ReplacementTransform(i_parts.copy(), i_dest))
        self.wait()
        self.play(ReplacementTransform(j_parts.copy(), j_dest))
        self.wait()

        self.play(ReplacementTransform(two_row.copy(), new_row))
        self.play(Write(conclusion), run_time=5)

        self.wait(3)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))

    def geometric_interpretation(self):
        text = TextMobject(
            "Geometric Interpretation", color=BLUE
        )
        text.scale(1.5).to_edge(UP)
        self.play(Write(text), run_time=3)
        self.wait(1)

        types = (
            "Scalar product can be geometrically explained through",
            "the concept of projection.",
            r"Scalar product of two vectors, $\vec{A}$ and $\vec{B}$ is given by",
            r"$\vec{A} \cdot \vec{B}$ = (length of proj. of $\vec{A}$)(length of $\vec{B}$)",
            r"alternatively, $\vec{A} \cdot \vec{B}$ = (length of proj. of $\vec{B}$)(length of $\vec{A}$)"
            )
        types_text = VGroup(*[TextMobject(i) for i in types])
        types_text.arrange(DOWN, center=False).shift(2 * UP)
        self.play(Write(types_text), run_time=20)
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))
