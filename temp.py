from manimlib.imports import *


class Test(Scene):
    scalar_topic = None

    def construct(self):
        self.topic()
        self.intro()
        self.vector_intro_graph()
        self.algebric_calc()
        self.geometric_interpretation()
        self.geometric_calc()
        self.case_of_perpendicularity()
        # self.angle_of_vectors()
        self.wait(3)

    def topic(self):
        title = TextMobject("Product of Vectors", color=BLUE)
        title.scale(1.5)
        self.play(Write(title), run_time=3)
        self.wait(1)
        self.play(title.to_edge, UP)

        types = (
            "The product of vectors can be calculated in two ways",
            "1. Scalar Product (Dot Product)",
            "2. Vector Product (Cross Product)",
        )
        types_text = VGroup(*[TextMobject(i) for i in types])
        types_text.arrange(DOWN, center=False).shift(UP)
        self.play(Write(types_text), run_time=8)

        self.scalar_topic = types_text[1]
        self.play(FadeOut(title), FadeOut(types_text[0]), FadeOut(types_text[2]))

    def intro(self):
        text = TextMobject("Scalar Product of Two Vectors", color=BLUE)
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
            "= $a_1 a_2$ + $b_1 b_2$",
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
        grid = NumberPlane(background_line_style={"stroke_color": WHITE})

        va = Vector(direction=UR, color=GREEN).scale(2).shift(UR / 2)
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
        tex_parts = [
            TexMobject(i) for i in ["(2i", "+", "2j)", r"\cdot", "(2i", "+", "0j)"]
        ]
        vec_parts = [tex for n, tex in enumerate(tex_parts) if n % 2 == 0]
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

        conclusion = TextMobject(
            r"$\therefore$ the scalar product of $\vec{A}$ and $\vec{B}$ is 4."
        )
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
        title = TextMobject("Geometric Interpretation", color=BLUE)
        title.scale(1.5).to_edge(UP)
        self.play(Write(title), run_time=3)
        self.wait(1)

        types = (
            "Scalar product can be geometrically explained through",
            "the concept of projection.",
            r"Scalar product of two vectors, $\vec{A}$ and $\vec{B}$ is given by",
            r"$\vec{A} \cdot \vec{B}$ = (length of proj. of $\vec{A}$)(length of $\vec{B}$)",
            r"alternatively, $\vec{A} \cdot \vec{B}$ = (length of proj. of $\vec{B}$)(length of $\vec{A}$)",
            "Let us now obtain scalar product of two vectors,",
            r"$\vec{A}$=2i+2j and $\vec{B}$=3i+0j",
        )
        types_text = VGroup(*[TextMobject(i) for i in types])
        types_text.arrange(DOWN, center=False, buff=0.325)
        types_text.next_to(title, DOWN, buff=1.0)
        self.play(Write(types_text), run_time=20)
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    @staticmethod
    def get_projection(vector_to_project, stable_vector):
        v1, v2 = stable_vector, vector_to_project
        return v1 * np.dot(v1, v2) / (get_norm(v1) ** 2)

    def get_vect_mob_projection(self, vector_to_project, stable_vector):
        return Vector(
            self.get_projection(vector_to_project.get_end(), stable_vector.get_end()),
            color=vector_to_project.get_color(),
        ).fade()

    def geometric_calc(self):
        grid = NumberPlane(background_line_style={"stroke_color": GREY})

        va = Vector(direction=UR, color=GREEN).scale(2).shift(UR / 2)
        vb = Vector(color=BLUE).scale(3, about_edge=LEFT)

        va_tex = TexMobject("\\vec{A}")
        vb_tex = TexMobject("\\vec{B}")
        va_tex.next_to(va.get_end(), UR)
        vb_tex.next_to(vb.get_end(), UR)

        va_perp_drop = Line(va.get_end(), va.get_end() + 2 * DOWN, color=BLUE)
        va_proj = Vector(va_perp_drop.get_end(), color=va.get_color()).fade()

        vb_proj = self.get_vect_mob_projection(vb, va)
        vb_perp_drop = Line(vb.get_end(), vb_proj.get_end(), color=BLUE)

        a_b = TexMobject(r"\vec{A} \cdot \vec{B} =").to_edge(UL)

        va_proj_brace = Brace(va_proj, DOWN)
        va_proj_tex = va_proj_brace.get_text("Length of proj. of $\\vec{A}$")
        vb_brace = Brace(vb, DOWN)
        vb_brace_tex = vb_brace.get_text("Length of $\\vec{B}$")

        va_tar = va_proj_tex.generate_target().next_to(a_b)
        vb_brace_tex.generate_target().next_to(va_tar)
        va_dot_vb_g = VGroup(va_proj_tex, vb_brace_tex)
        va_dot_vb_exp = TextMobject(
            "(Length of proj. of $\\vec{A}$) $\\cdot$ "
            "(Length of $\\vec{B}$)"
        ).next_to(a_b)

        alternatively = TextMobject("Alternatively,", color=BLUE).scale(1.5).to_edge(UL)

        vb_proj_brace = Brace(vb_proj, UL)
        vb_proj_tex = TextMobject("Length of proj. of $\\vec{B}$").scale(0.8)
        vb_proj_tex.rotate(va.get_angle()).move_to(vb_proj_brace).shift(UL / 2)
        va_brace = Brace(va, UL)
        va_brace_tex = TextMobject("Length of $\\vec{A}$").scale(0.8)
        va_brace_tex.rotate(va.get_angle()).move_to(va_brace).shift(UL / 2)

        vb_tar = vb_proj_tex.generate_target().rotate(-va.get_angle()).next_to(a_b)
        va_brace_tex.generate_target().rotate(-va.get_angle()).next_to(vb_tar)
        vb_dot_va_g = VGroup(a_b, vb_proj_tex, va_brace_tex)
        vb_dot_va_exp = TextMobject(
            r"$\vec{A} \cdot \vec{B}$ = "
            "(Length of proj. of $\\vec{B}$) $\\cdot$ "
            "(Length of $\\vec{A}$)"
        ).to_edge(UL)

        self.play(ShowCreation(grid))
        self.wait()

        self.play(ShowCreation(va))
        self.play(Write(va_tex))
        self.wait()

        self.play(ShowCreation(vb))
        self.play(Write(vb_tex))
        self.wait()

        self.play(Write(a_b))
        self.wait()

        self.play(ShowCreation(va_perp_drop))
        self.play(ReplacementTransform(va.copy(), va_proj))
        self.wait()

        self.play(ShowCreation(va_proj_brace))
        self.play(ShowCreation(va_proj_tex))
        self.wait()
        self.play(FadeOut(va_proj_brace))
        self.play(MoveToTarget(va_proj_tex))
        self.wait()
        self.play(ShowCreation(vb_brace))
        self.play(ShowCreation(vb_brace_tex))
        self.play(MoveToTarget(vb_brace_tex), FadeOut(vb_brace))
        self.play(ReplacementTransform(va_dot_vb_g, va_dot_vb_exp))
        self.wait()

        self.play(FadeOut(a_b), ReplacementTransform(va_dot_vb_exp, alternatively))
        self.play(FadeOut(VGroup(va_perp_drop, va_proj)))
        self.play(Uncreate(alternatively))
        self.play(Write(a_b))

        self.play(ShowCreation(vb_perp_drop))
        self.play(ReplacementTransform(vb.copy(), vb_proj))
        self.wait()

        self.play(ShowCreation(vb_proj_brace))
        self.play(ShowCreation(vb_proj_tex))
        self.wait()
        self.play(FadeOut(vb_proj_brace))
        self.play(MoveToTarget(vb_proj_tex))
        self.wait()
        self.play(ShowCreation(va_brace))
        self.play(ShowCreation(va_brace_tex))
        self.play(MoveToTarget(va_brace_tex))
        self.play(ReplacementTransform(vb_dot_va_g, vb_dot_va_exp))
        self.wait()
        self.play(FadeOut(Group(*self.mobjects)))

    def case_of_perpendicularity(self):
        grid = NumberPlane(background_line_style={"stroke_color": GREY})

        va = Vector(direction=UR, color=GREEN).scale(2).shift(UR / 2)
        vb = Vector(color=BLUE).scale(3, about_edge=LEFT)

        va_tex = TexMobject("\\vec{A}")
        vb_tex = TexMobject("\\vec{B}")
        va_tex.next_to(va.get_end(), UL)
        vb_tex.next_to(vb.get_end(), UR)

        va_extension = Line(va.get_start(), va.get_end()).scale(5)
        vb_obtuse = vb.generate_target().rotate(-PI/2, about_edge=LEFT)

        vb_proj = self.get_vect_mob_projection(vb_obtuse, va)
        vb_perp_drop = Line(vb_obtuse.get_end(), vb_proj.get_end(), color=BLUE)

        a_b = TexMobject(r"\vec{A} \cdot \vec{B} =").to_edge(UL)

        vb_dot_va_exp = TextMobject(
            "- ", " (Length of proj. of $\\vec{B}$) $\\cdot$ "
            "(Length of $\\vec{A}$)"
        ).next_to(a_b)

        vb_dot_va_exp[0].set_color(YELLOW).scale(2)

        case_of_perp = TextMobject("Case of perpendicularity", color=BLUE).scale(1.5)
        case_of_perp.to_edge(UL)
        vb_right = vb.copy().rotate(-PI/4, about_edge=LEFT)

        vb_dot_va_exp_right = TextMobject(
            "0 $\\cdot$ "
            "(Length of $\\vec{A}$)"
        ).next_to(a_b)

        vb_dot_va_exp_right2 = TextMobject(
            "0"
        ).next_to(a_b)

        vb_tex.add_updater(lambda x: x.next_to(vb.get_end(), UR))

        self.add(grid, va, va_tex, vb, vb_tex, a_b)

        self.play(ShowCreation(va_extension))
        self.play(MoveToTarget(vb))
        self.play(ShowCreation(vb_perp_drop))
        self.play(ReplacementTransform(vb.copy(), vb_proj))
        self.wait()
        self.play(Write(vb_dot_va_exp))
        self.wait()
        self.play(Indicate(vb_dot_va_exp[0]))
        self.wait()
        self.play(FadeOut(VGroup(vb_perp_drop, vb_proj, vb_dot_va_exp, a_b)))

        self.play(Write(case_of_perp))
        self.wait()
        
        self.play(Transform(vb, vb_right))
        self.wait()

        self.play(ReplacementTransform(case_of_perp, a_b))
        self.play(Write(vb_dot_va_exp_right))
        self.wait()
        self.play(ReplacementTransform(vb_dot_va_exp_right, vb_dot_va_exp_right2))
        self.wait()
