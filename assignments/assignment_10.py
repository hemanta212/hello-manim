from manimlib.imports import *


class TriangularPrism(Scene):
    topic = None
    fig = None

    def construct(self):
        self.intro()
        self.triangular_prism()
        self.tri_prism_area_volume()
        self.tri_prism_lateral_area()
        self.tri_prism_total_area_volume()

    def intro(self):
        topic = TextMobject("Triangular Prism: Surface area and volume", color=BLUE)
        self.play(Write(topic))
        self.play(FadeOutAndShiftDown(topic))

    def triangular_prism(self):
        topic = TextMobject("Triangular Prism", color=BLUE)
        topic.scale(1.5).to_edge(UP)

        defn = TextMobject("A triangular prism is a prism with a triangle for a")
        defn2 = TextMobject("cross section.")
        defn.next_to(topic, DOWN, buff=1.0)
        defn2.next_to(defn, DOWN)

        prism = self.build_prism()
        fore_triangle, back_triangle, *_ = prism.submobjects
        prism.next_to(defn2, DOWN, buff=1.0)

        self.play(Write(topic))
        self.wait()
        self.play(ShowCreation(prism))
        self.play(Write(defn))
        self.play(Write(defn2))
        self.play(
            ApplyMethod(fore_triangle.set_fill, ORANGE, 1),
            ApplyMethod(back_triangle.set_fill, ORANGE, 1),
        )
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def tri_prism_area_volume(self):
        topic = TextMobject("Surface Area and Volume", color=BLUE)
        topic.scale(1.5).to_edge(UP)

        prism = self.build_prism()
        fore_triangle, back_triangle, *_ = prism.submobjects
        prism.scale(1.5).next_to(topic, DOWN, 2.5).to_edge(RIGHT)

        A, B, C, D, E, F = (
            *fore_triangle.get_vertices(),
            *back_triangle.get_vertices(),
        )
        a_label, b_label, c_label, d_label, e_label, f_label = (
            TextMobject(i) for i in list("ABCDEF")
        )
        labels = [a_label, d_label, c_label, b_label, e_label, f_label]
        for label, point in zip(labels[3:], [B, E, F]):
            label.next_to(point, DOWN, buff=0.2)
        for label, point in zip(labels[:3], [A, D, C]):
            label.next_to(point, UP, buff=0.2)

        a_side_label, b_side_label, c_side_label, length_label, length_label2 = (
            TexMobject(i) for i in list("abcll")
        )
        side_labels = [
            a_side_label,
            b_side_label,
            c_side_label,
            length_label,
            length_label2,
        ]
        for label in side_labels:
            label.set_color(BLUE).scale(0.8)

        a_side_label.next_to(Line(B, C), UP)
        length_label.next_to(Line(B, E), DOWN, buff=0.1)
        length_label2.next_to(Line(C, F), UP, buff=0.1)
        # I cannot figure out proper alignment so this is bad workaround
        c_side_label.next_to(Line(A, C), LEFT, buff=0.8)
        b_side_label.next_to(Line(A, B), RIGHT, buff=0.8)

        self.play(Write(topic))
        self.play(ShowCreation(prism))
        self.play(ShowCreation(VGroup(*labels)))
        self.add(*side_labels)

        self.topic = topic
        self.fig = prism

    def tri_prism_lateral_area(self):
        topic = self.topic
        prism = self.fig

        fore_triangle, back_triangle, *_ = prism.submobjects
        A, B, C, D, E, F = (
            *fore_triangle.get_vertices(),
            *back_triangle.get_vertices(),
        )

        lateral_surface_area = TextMobject("For lateral surface area:").scale(1.3)
        lateral_surface_area.next_to(topic, DOWN, buff=0.5).to_edge(LEFT)

        texts = [
            (
                "L.S.A = ",
                r"$\square$ ABED + ",
                r"$\square$ ACFD + ",
                r"$\square$ BCEF",
            ),
            (r"= c $\cdot$ $l$ + b $\cdot$ $l$ + a $\cdot$ $l$",),
            (r"= (a + b + c) $\cdot$ $l$",),
            (r"= Perimeter of triangular base", r"$\times$ $l$"),
            (r"$\therefore$ L.S.A = ", r"p $\cdot$ $l$"),
        ]
        first_row = self.make_row(texts[0])
        first_row.next_to(lateral_surface_area, DOWN, buff=0.3).to_edge(LEFT)
        lateral_first_line = first_row.submobjects
        proof_lines = [first_row]
        for text in texts[1:]:
            row = self.make_row(text)
            row.next_to(proof_lines[-1], DOWN, buff=0.3).to_edge(LEFT)
            proof_lines.append(row)

        rect_abed = Polygon(A, B, E, D, fill_color=YELLOW_A, fill_opacity=1.0)
        rect_acfd = Polygon(A, C, F, D, fill_color=YELLOW_A, fill_opacity=1.0)
        rect_befc = Polygon(B, E, F, C, fill_color=YELLOW_A, fill_opacity=1.0)
        rects = [rect_abed, rect_acfd, rect_befc]

        self.play(Write(lateral_surface_area))
        self.play(Write(lateral_first_line[0]))
        for text, rect in zip(lateral_first_line[1:], rects):
            self.play(Write(text))
            self.play(ShowCreationThenDestruction(rect), run_time=2)
        self.play(ShowCreationThenDestruction(VGroup(*rects)), run_time=3)
        for line in proof_lines[1:]:
            self.play(Write(line), run_time=2)
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*proof_lines, lateral_surface_area)))

    def tri_prism_total_area_volume(self):
        topic = self.topic
        prism = self.fig

        fore_triangle, back_triangle, *_ = prism.submobjects
        A, B, C, D, E, F = (
            *fore_triangle.get_vertices(),
            *back_triangle.get_vertices(),
        )

        total_surface_area = TextMobject("For total surface area:").scale(1.3)
        total_surface_area.next_to(topic, DOWN, buff=0.5).to_edge(LEFT)

        texts = [
            (
                "T.S.A = ",
                r"2 $\cdot$ $\triangle$ Triangular base area + ",
                r"L.S.A",
            ),
            (
                r"$\therefore$ T.S.A = ",
                r"2 $\cdot$ $\triangle$ A + ",
                r"p $\cdot$ $l$",
            ),
        ]

        first_row = self.make_row(texts[0])
        first_row.next_to(total_surface_area, DOWN, buff=0.3).to_edge(LEFT)
        total_first_line = first_row.submobjects
        proof_lines = [first_row]
        for text in texts[1:]:
            row = self.make_row(text)
            row.next_to(proof_lines[-1], DOWN, buff=0.3).to_edge(LEFT)
            proof_lines.append(row)

        rect_abed = Polygon(A, B, E, D, fill_color=YELLOW_A, fill_opacity=1.0)
        rect_acfd = Polygon(A, C, F, D, fill_color=YELLOW_A, fill_opacity=1.0)
        rect_befc = Polygon(B, E, F, C, fill_color=YELLOW_A, fill_opacity=1.0)
        rects = [rect_abed, rect_acfd, rect_befc]
        tri_abc = Polygon(A, B, C, fill_color=YELLOW_A, fill_opacity=1.0)
        tri_def = Polygon(D, E, F, fill_color=YELLOW_A, fill_opacity=1.0)
        tris = [tri_abc, tri_def]
        figs = [VGroup(*tris), VGroup(*rects)]

        total_volume = TextMobject("For volume of prism").scale(1.3)
        total_volume.next_to(proof_lines[-1], DOWN, buff=1.5).to_edge(LEFT)
        texts = [
            (
                "V = ",
                r"Area of $\triangle$ base $\times$ Length",
            ),
            (
                r"$\therefore$ V = ",
                r"$\triangle$ A $\cdot$ $l$",
            ),
        ]

        first_row = self.make_row(texts[0])
        first_row.next_to(total_volume, DOWN, buff=0.3).to_edge(LEFT)
        proof_lines_vol = [first_row]
        for text in texts[1:]:
            row = self.make_row(text)
            row.next_to(proof_lines_vol[-1], DOWN, buff=0.3).to_edge(LEFT)
            proof_lines_vol.append(row)

        self.play(Write(total_surface_area))
        self.play(Write(total_first_line[0]))
        for text, fig in zip(total_first_line[1:], figs):
            self.play(Write(text))
            self.play(ShowCreationThenDestruction(fig), run_time=2)
        self.play(ShowCreationThenDestruction(VGroup(*figs)), run_time=3)
        for line in proof_lines[1:]:
            self.play(Write(line), run_time=2)
        self.wait(2)

        self.play(Write(total_volume))
        for line in proof_lines_vol:
            self.play(Write(line), run_time=2)
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def build_prism(self):
        fore_triangle = Triangle()
        A, B, C = fore_triangle.get_vertices()
        back_triangle = fore_triangle.copy().move_to(1.3 * RIGHT)
        D, E, F = back_triangle.get_vertices()
        line1, line2, line3 = Line(A, D), Line(B, E), Line(C, F)
        lines = (line1, line2, line3)
        prism = VGroup(fore_triangle, back_triangle, *lines)
        return prism

    def make_row(self, texts):
        txt_objs = [TextMobject(i) for i in texts]
        first = txt_objs[0]
        if len(txt_objs) == 1:
            return VGroup(first)

        processed = [first]
        for text in txt_objs[1:]:
            text.next_to(processed[-1])
            processed.append(text)
        row = VGroup(*processed)
        return row
