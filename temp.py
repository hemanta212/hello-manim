from manimlib.imports import *


class Test(Scene):

    theorem1_para = None

    def construct(self):
        self.theorem1()
        self.theorem1_proof()

    def theorem1_proof(self):
        topic = TextMobject("Proof of Theorem 1", color=BLUE).scale(1.2)
        topic.to_edge(UL)

        self.theorem1_para.next_to(topic, buff=1.0).shift(DOWN)
        para, para2, *labels2 = self.theorem1_para.submobjects
        A, D, C, B = para.get_vertices()
        F, E, C, B = para2.get_vertices()

        self.play(Write(topic))
        self.play(Write(self.theorem1_para))

        col_1_data = (
            "S.N.",
            "1.",
            "i)",
            "ii)",
            "iii)",
        )

        col_2_data = (
            "Statements",
            r"In $\triangle$ ABF and $\triangle$ CDE",
            "AB = DC (S)",
            r"$\angle$ BAF = $\angle$ CDE (A)",
            "BF = CE (S)",
        )

        col_3_data = (
            "Reasons",
            "{{GAP}}",
            "Opposite side of $\square$ ABCD",
            "Corresponding angle, AB || DC",
            "Opposite side of $\square$ BCEF",
        )

        tri_ABF, tri_CDE = Polygon(A, B, F, color=GREEN), Polygon(C, D, E, color=YELLOW)
        abf_cde_triangles = VGroup(tri_ABF, tri_CDE)
        line_ab, line_dc = Line(A, B, color=GREEN), Line(D, C, color=YELLOW)
        ab_dc_lines = VGroup(line_ab, line_dc)
        angle_baf = Elbow(color=GREEN).set_points_as_corners([B, A, F])
        angle_cde = Elbow(color=YELLOW).set_points_as_corners([C, D, E])
        baf_cde_angles = VGroup(angle_baf, angle_cde)
        line_bf, line_ce = Line(B, F, color=GREEN), Line(C, E, color=YELLOW)
        bf_ce_lines = VGroup(line_bf, line_ce)

        animations = [
            ([Animation(self.theorem1_para)], 0.01),
            ([ShowCreationThenFadeOut(abf_cde_triangles)], 3),
            ([ShowCreationThenFadeOut(ab_dc_lines)], 3),
            ([ShowCreationThenFadeOut(baf_cde_angles)], 3),
            ([ShowCreationThenFadeOut(bf_ce_lines)], 3),
        ]
        col_1 = self.makeColGroup(col_1_data)
        col_2 = self.makeColGroup(col_2_data)
        col_3 = self.makeColGroup(col_3_data)
        col_1.to_edge(LEFT)
        col_2.next_to(col_1)
        col_3.next_to(col_2)
        row_objs = [col_1.submobjects, col_2.submobjects, col_3.submobjects, animations]
        written = []
        for sn, stat, reason, (anims, run_time) in zip(*row_objs):
            for obj in (sn, stat, reason):
                obj = obj.set_color(BLACK) if "{{GAP}}" in obj.tex_string else obj
                written.append(obj)
            self.play(Write(sn))
            self.play(Write(stat))
            self.play(Write(reason))
            for anim in anims:
                self.play(anim, run_time=run_time)

        self.play(FadeOutAndShiftDown(VGroup(*written[3:])))

        col_1_data = (
            "S.N.",
            "2.",
            "3.",
            "4.",
            "5.",
        )

        col_2_data = (
            "Statements",
            r"$\therefore$ $\triangle$ ABF $\cong$ $\triangle$ CDE",
            r"$\triangle$ ABF = $\triangle$ CDE",
            (
                r"$\triangle$ ABF + $\square$ BCDF",
                r"= $\triangle$ CDE + $\square$ BCDE",
            ),
            r"$\square$ ABCD = $\square$ BCEF",
        )

        col_3_data = (
            "Reasons",
            "S.A.S axiom",
            "Area of congruent triangles is equal",
            r"Adding same $\square$ BCDF both sides",
            "Whole part axiom",
        )

        tri_ABF.set_fill(color=YELLOW, opacity=1)
        tri_CDE.set_fill(color=YELLOW, opacity=1)
        quad_bcdf = Polygon(B, C, D, F, fill_color=YELLOW, fill_opacity=1.0)
        abf_bcdf, cde_bcdf = VGroup(tri_ABF, quad_bcdf), VGroup(tri_CDE, quad_bcdf)
        para_abcd = Polygon(A, B, C, D, fill_color=YELLOW, fill_opacity=1.0)
        para_bcef = Polygon(B, C, E, F, fill_color=YELLOW, fill_opacity=1.0)

        animations = [
            ([Animation(self.theorem1_para)], 0.01),
            ([Animation(self.theorem1_para)], 0.01),
            ([ShowCreationThenFadeOut(abf_cde_triangles)], 3),
            (
                [
                    ShowCreationThenFadeOut(quad_bcdf),
                    ShowCreationThenFadeOut(abf_bcdf),
                    ShowCreationThenFadeOut(cde_bcdf),
                ],
                3,
            ),
            (
                [
                    ShowCreationThenFadeOut(para_abcd),
                    ShowCreationThenFadeOut(para_bcef),
                ],
                3,
            ),
        ]

        col_1 = self.makeColGroup(col_1_data)
        col_2 = self.makeColGroup(col_2_data)
        col_3 = self.makeColGroup(col_3_data)
        col_1.to_edge(LEFT)
        col_2.next_to(col_1)
        col_3.next_to(col_2)
        row_objs = [col_1.submobjects, col_2.submobjects, col_3.submobjects, animations]
        written = []
        for sn, stat, reason, (anims, run_time) in zip(*row_objs):
            written.append(VGroup(sn, stat, reason))
            if not written[1:]:
                continue
            self.play(Write(sn))
            self.play(Write(stat))
            self.play(Write(reason))
            for anim in anims:
                self.play(anim, run_time=run_time)

        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def theorem1(self):
        topic = TextMobject("Theorem 1", color=BLUE).scale(1.5)
        topic.to_edge(UP)

        statement_t = TextMobject("Statement:")
        statement = TextMobject(
            "Parallelograms standing on the same base and lying between"
        )
        statement_ = TextMobject("the same parallels are equal in area.")
        statement_t.next_to(topic, DOWN, buff=0.3).to_edge(LEFT)
        statement.next_to(statement_t, DOWN, buff=0.2).to_edge(LEFT)
        statement_.next_to(statement, DOWN, buff=0.2).to_edge(LEFT)

        parallelogram = Polygon(
            UL + LEFT + LEFT / 2,
            UR + RIGHT + LEFT / 2,
            DR + RIGHT,
            DL + LEFT,
        )
        parallelogram.shift(DOWN)
        A, D, C, B = parallelogram.get_vertices()

        parallelogram2 = Polygon(
            UL + LEFT + RIGHT / 2,
            UR + RIGHT + RIGHT / 2,
            DR + RIGHT,
            DL + LEFT,
        )
        parallelogram2.shift(DOWN)
        F, E, C, B = parallelogram2.get_vertices()

        A_label, D_label, C_label, B_label, F_label, E_label = (
            TextMobject(i) for i in "A D C B F E".split(" ")
        )
        A_label.next_to(A, UP, buff=0.2)
        F_label.next_to(F, UP, buff=0.2)
        D_label.next_to(D, UP, buff=0.2)
        E_label.next_to(E, UP, buff=0.2)
        B_label.next_to(B, DOWN, buff=0.2)
        C_label.next_to(C, DOWN, buff=0.2)
        labels = (A_label, D_label, C_label, B_label, F_label, E_label)

        figure_g = VGroup(parallelogram, parallelogram2, *labels)
        figure_g_tar = figure_g.generate_target()
        figure_g_tar.next_to(statement_, DOWN, buff=0.2).to_edge(RIGHT)

        para, para2, *labels2 = figure_g_tar.submobjects
        A, D, C, B = parallelogram.get_vertices()
        F, E, C, B = parallelogram2.get_vertices()

        given = TextMobject("Given: Parallelograms ABCD and")
        given2 = TextMobject("BCEF are standing on the same")
        given3 = TextMobject("base BC and lying between the")
        given4 = TextMobject("same parallels AE and BC as shown.")
        given.next_to(statement_, DOWN, buff=0.5).to_edge(LEFT)
        given2.next_to(given, DOWN, buff=0.2).to_edge(LEFT)
        given3.next_to(given2, DOWN, buff=0.2).to_edge(LEFT)
        given4.next_to(given3, DOWN, buff=0.2).to_edge(LEFT)

        to_prove_t = TextMobject("To Prove:")
        ABCD_label, BCEF_label = TextMobject("ABCD = "), TextMobject("BCEF (in area)")
        to_prove_t.next_to(given4, DOWN, buff=0.5).to_edge(LEFT)
        ABCD_fig = parallelogram.copy().scale(0.2)
        ABCD_fig.to_edge(DL)

        to_prove_processed = [ABCD_fig]
        for i in (ABCD_label, ABCD_fig.copy(), BCEF_label):
            i.next_to(to_prove_processed[-1])
            to_prove_processed.append(i)

        self.theorem1_para = figure_g

        angle = Arc(
            radius=0.5,
            start_angle=Line(A, B).get_angle(),
            angle=Line(B, C).get_angle(),
            color=YELLOW,
        )
        self.play(ShowCreation(angle))

        self.play(Write(topic))
        self.play(Write(statement_t))
        self.play(Write(statement))
        self.play(Write(statement_))
        self.play(ShowCreation(parallelogram), run_time=2)
        self.play(ShowCreation(parallelogram2), run_time=2)
        self.add(*labels)
        self.wait()
        self.play(MoveToTarget(figure_g))
        self.wait()
        for i in [given, given2, given3, given4]:
            self.play(Write(i))
        self.play(Write(to_prove_t))
        for i in to_prove_processed:
            self.play(ShowCreation(i))
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def makeColGroup(self, texts, tex_class=TextMobject, spacing=0.5, text_scale=1.0):
        text_objects = []
        for text in texts:
            obj = None
            if isinstance(text, str):
                singlify = lambda x: [f"{i} " for i in x.split(" ")]
                obj = TextMobject(*singlify(text))
            elif isinstance(text, TexMobject):
                obj = text
            elif isinstance(text, tuple):
                objects = [tex_class(i).scale(0.75) for i in text]
                processed = [objects[0]]
                for i in objects[1:]:
                    i.next_to(processed[-1], DOWN, buff=0.2)
                    processed.append(i)
                obj = VGroup(*processed)
            else:
                AssertionError(f"Unsupported type of {type(text)}: {text}")

            obj.scale(text_scale)
            text_objects.append(obj)

        first = text_objects[0]
        processed = [first]
        for obj in text_objects[1:]:
            obj.next_to(processed[-1], DOWN, buff=spacing)
            processed.append(obj)

        return VGroup(*processed)
