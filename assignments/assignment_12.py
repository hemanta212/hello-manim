from manimlib.imports import *


class Pyramid(Scene):
    topic = None
    fig = None

    def construct(self):
        self.intro()
        self.pyramid_intro()
        self.pyramid_area()
        self.lateral_area()
        self.total_area()
        self.volume()

    def intro(self):
        topic = TextMobject(
            "Square based Pyramid: Surface area and volume", color=BLUE
        ).scale(1.2)
        self.play(Write(topic))
        self.play(FadeOutAndShiftDown(topic))

    def pyramid_intro(self):
        topic = TextMobject("Square based Pyramid", color=BLUE)
        topic.scale(1.5).to_edge(UP)
        defn_texts = (
            "Square based pyramid is a solid having a square base and",
            "four plane triangular faces meeting at a common vertex.",
        )
        defn, defn2 = (TextMobject(i) for i in defn_texts)
        defn.next_to(topic, DOWN, buff=1.0)
        defn2.next_to(defn, DOWN)

        base_square = Square(color=BLUE)
        base_square.to_edge(DOWN).rotate(PI / 2.4, axis=LEFT).rotate(-PI / 6, axis=UP)
        base_square.rotate(DEGREES * 9, axis=IN)
        base_square_center = base_square.get_center()
        A, B, C, D = base_square.get_vertices()
        side_length = base_square.get_width()
        pyramid_tip = base_square_center + 2 * UP + (side_length / 5) * OUT

        triangle_slope1 = Polygon(A, B, pyramid_tip)
        triangle_slope2 = Polygon(B, C, pyramid_tip)
        triangle_slope3 = Polygon(C, D, pyramid_tip)
        triangle_slope4 = Polygon(D, A, pyramid_tip)
        slope_faces = (
            triangle_slope1,
            triangle_slope2,
            triangle_slope3,
            triangle_slope4,
        )
        pyramid = VGroup(base_square, *slope_faces)

        self.play(Write(topic))
        self.wait()
        self.play(Write(defn))
        self.play(Write(defn2))
        self.wait()
        self.play(ShowCreation(base_square), run_time=2)
        self.play(
            GrowFromPoint(triangle_slope1, A),
            GrowFromPoint(triangle_slope2, B),
            GrowFromPoint(triangle_slope3, C),
            GrowFromPoint(triangle_slope4, D),
            run_time=4,
        )
        self.play(Rotating(pyramid, axis=DOWN))
        self.wait(2)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))

    def pyramid_area(self):
        topic = TextMobject("Surface area of a square based pyramid", color=BLUE)
        topic.scale(1.5).to_edge(UP)

        base_square = Square(color=BLUE).scale(1.5)
        base_square.to_edge(DR).rotate(PI / 2.3, axis=LEFT).rotate(-PI / 6, axis=UP)
        base_square.rotate(DEGREES * 9, axis=IN)
        base_square_center = base_square.get_center()
        A, B, C, D = base_square.get_vertices()
        side_length = base_square.get_width()
        pyramid_tip = base_square_center + 3 * UP + (side_length / 5) * OUT

        triangle_slope1 = Polygon(A, B, pyramid_tip)
        triangle_slope2 = Polygon(B, C, pyramid_tip)
        triangle_slope3 = Polygon(C, D, pyramid_tip)
        triangle_slope4 = Polygon(D, A, pyramid_tip)
        slope_faces = (
            triangle_slope1,
            triangle_slope2,
            triangle_slope3,
            triangle_slope4,
        )
        a_label, b_label, c_label, d_label = (TexMobject(i) for i in list("ABCD"))
        a_label.next_to(A, UL, buff=0.1)
        b_label.next_to(B, DOWN, buff=0.1)
        c_label.next_to(C, DOWN, buff=0.1)
        d_label.next_to(D, DOWN, buff=0.1)
        length_label = TexMobject("a", color=RED_A).next_to((C + D) / 2, DR)
        square_labels = [a_label, b_label, c_label, d_label, length_label]

        vertex_label, base_center_label, side_midpoint_label = (
            TexMobject(i) for i in list("OPQ")
        )
        vertex_label.next_to(pyramid_tip, UP, buff=0.1)
        base_center_label.scale(0.5).next_to(base_square_center, DL, buff=0.05)
        side_midpoint = (B + C) / 2
        side_midpoint_label.scale(0.7).next_to(side_midpoint, DR, buff=0.1)
        point_labels = [vertex_label, side_midpoint_label, base_center_label]

        perp = DashedLine(pyramid_tip, base_square_center, color=YELLOW)
        slant = DashedLine(pyramid_tip, side_midpoint, color=RED)
        base_to_slant = DashedLine(base_square_center, side_midpoint)
        perp_label, slant_label, edge_label = (
            TexMobject(i, color=YELLOW).scale(0.7) for i in list("hle")
        )
        perp_label.next_to(perp, LEFT, buff=0.05)
        slant_label.next_to(slant.get_center(), DL, buff=0.1)
        edge_label.scale(1.2).next_to((pyramid_tip + B) / 2, UR, buff=0.1)
        line_labels = [perp_label, slant_label, edge_label]
        pyramid_labels = [*square_labels, *point_labels, *line_labels]
        pyramid = VGroup(
            base_square, *slope_faces, *pyramid_labels, perp, slant, base_to_slant
        )
        pyramid.to_edge(DR)

        self.play(Write(topic))
        self.play(ShowCreation(pyramid))
        self.wait(2)

        self.topic = topic
        self.fig = pyramid

    def lateral_area(self):
        topic = self.topic
        pyramid = self.fig
        pyramid_tar = pyramid.generate_target()
        pyramid_tar.next_to(topic, DOWN, buff=0.3).to_edge(RIGHT)
        pyramid_parts = pyramid_tar.submobjects

        base_square, slope_faces = pyramid_parts[0], pyramid_parts[1:5]
        A, B, C, D = base_square.get_vertices()
        triangular_face2 = slope_faces[1]

        lateral_surface_area = TextMobject("For lateral surface area:").scale(1.3)
        lateral_surface_area.next_to(topic, DOWN, buff=0.5).to_edge(LEFT)
        texts = [
            ("L.S.A = ", r"Area of 4 triangular faces"),
            ("= 4 ", r"$\times$ ($\frac{1}{2}$ a $\times$ $l$)"),
            (r"$\therefore$ L.S.A = ", r"2 a $l$"),
        ]
        first_row = self.make_row(texts[0])
        first_row.next_to(lateral_surface_area, DOWN, buff=1.0).to_edge(LEFT)
        proof_lines = [first_row]
        for text in texts[1:]:
            row = self.make_row(text)
            row.next_to(proof_lines[-1], DOWN, buff=0.5).to_edge(LEFT)
            proof_lines.append(row)

        tri_face = triangular_face2.copy()
        tri_face.next_to(pyramid, LEFT).to_edge(DOWN).rotate(-DEGREES * 15)
        X, Y, Z = tri_face.get_vertices()
        tri_face_perp = DashedLine(Z, Y + RIGHT / 1.7, color=RED)
        tri_face_perp_label = TexMobject("l", color=RED).next_to(
            tri_face_perp, buff=0.1
        )
        tri_face_side_label = TexMobject("a", color=RED).next_to(Line(Y, X), DOWN)
        sample_triangular_face = VGroup(
            tri_face, tri_face_perp, tri_face_perp_label, tri_face_side_label
        )
        all_faces = [i.copy() for i in slope_faces]
        for face in all_faces:
            face.set_fill(color=BLUE, opacity=1.0)

        self.play(MoveToTarget(pyramid))
        self.play(Write(lateral_surface_area))
        self.wait()
        self.play(ReplacementTransform(triangular_face2.copy(), sample_triangular_face))
        self.play(Write(first_row))
        for face in all_faces:
            self.play(ShowCreationThenFadeOut(face))
        for line in proof_lines[1:]:
            self.play(Write(line), run_time=2)
        self.wait(2)
        self.play(
            FadeOutAndShiftDown(
                Group(*proof_lines, lateral_surface_area, sample_triangular_face)
            )
        )

    def total_area(self):
        topic = self.topic
        pyramid = self.fig
        slope_faces = pyramid.submobjects[1:5]

        total_surface_area = TextMobject("For total surface area:").scale(1.3)
        total_surface_area.next_to(topic, DOWN, buff=0.5).to_edge(LEFT)
        texts = [
            ("T.S.A = ", r"L.S.A + Area of base square"),
            ("= 4 ", r"$\times$ ($\frac{1}{2}$ a $\times$ $l$) + ", "$a^2$"),
            (r"$\therefore$ T.S.A = ", r"2 a $l$ + $a^2$"),
        ]
        first_row = self.make_row(texts[0])
        first_row.next_to(total_surface_area, DOWN, buff=1.0).to_edge(LEFT)
        proof_lines = [first_row]
        for text in texts[1:]:
            row = self.make_row(text)
            row.next_to(proof_lines[-1], DOWN, buff=0.5).to_edge(LEFT)
            proof_lines.append(row)
        all_faces = VGroup(*[i.copy() for i in slope_faces])
        for face in all_faces:
            face.set_fill(color=BLUE, opacity=1.0)

        self.play(Write(total_surface_area))
        self.wait()
        self.play(Write(first_row))
        self.play(ShowCreationThenFadeOut(all_faces))
        for line in proof_lines[1:]:
            self.play(Write(line), run_time=2)
        self.wait(2)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))

    def volume(self):
        pyramid = self.fig
        pyramid_parts = pyramid.submobjects

        base_square, slope_face = pyramid_parts[0], pyramid_parts[1]
        base_square_center = base_square.get_center()
        *_, pyramid_tip = slope_face.get_vertices()

        topic = TextMobject("Volume of Square based Pyramid", color=BLUE)
        topic.scale(1.5).to_edge(UP)
        texts = [
            (
                r"Volume = $\frac{1}{3}$ $\times$",
                r"Area of base $\times$",
                "height",
            ),
            (r"= $\frac{1}{3}$ $\times$ $a^2$ $\times$ h",),
            (
                r"$\therefore$ V = ",
                r"$\frac{1}{3}$ $a^2$ h",
            ),
        ]

        first_row = self.make_row(texts[0])
        first_row.next_to(topic, DOWN, buff=1.0).to_edge(LEFT)
        first_row_parts = first_row.submobjects
        proof_lines = [first_row]
        for text in texts[1:]:
            row = self.make_row(text)
            row.next_to(proof_lines[-1], DOWN, buff=0.5).to_edge(LEFT)
            proof_lines.append(row)

        perp_line = Line(pyramid_tip, base_square_center, color=YELLOW)
        filled_base_square = base_square.copy()
        filled_base_square.set_fill(opacity=1.0, color=BLUE)
        first_row_objs = (filled_base_square, perp_line)

        self.play(Write(topic))
        self.play(ShowCreation(pyramid))
        self.wait()
        self.play(Write(first_row_parts[0]))
        for text, obj in zip(first_row_parts[1:], first_row_objs):
            self.play(Write(text))
            self.play(ShowCreationThenFadeOut(obj))
        for line in proof_lines[1:]:
            self.play(Write(line), run_time=3)
        self.wait(2)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))

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
