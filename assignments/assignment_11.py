from manimlib.imports import *


class Cone(Scene):
    topic = None
    figs = None

    def construct(self):
        self.intro()
        self.cone_intro()
        self.cone_area()
        self.lateral_area()
        self.total_area()
        self.volume()

    def intro(self):
        topic = TextMobject("Cone: Surface area and volume", color=BLUE).scale(1.5)
        self.play(Write(topic))
        self.play(FadeOutAndShiftDown(topic))

    def cone_intro(self):
        topic = TextMobject("Cone", color=BLUE)
        topic.scale(1.5).to_edge(UP)

        defn = TextMobject("Cone is a solid or hollow object which tapers from a")
        defn2 = TextMobject("circular or roughly circular base to a point.")

        defn.next_to(topic, DOWN, buff=1.0)
        defn2.next_to(defn, DOWN)

        base_circle = Circle(color=BLUE)
        base_circle.to_edge(DOWN).rotate(PI / 4, axis=LEFT)
        base_circle_center = base_circle.get_center()
        diameter_end1 = base_circle_center + LEFT
        diameter_end2 = base_circle_center + RIGHT
        cone_tip = base_circle_center + 2 * UP
        cone_side1 = Line(diameter_end1, cone_tip, color=BLUE)
        cone_side2 = Line(diameter_end2, cone_tip, color=BLUE)
        cone_triangle = Polygon(diameter_end1, cone_tip, diameter_end2)

        cone = VGroup(
            base_circle.copy().set_fill(opacity=1.0, color=BLUE),
            cone_triangle.set_fill(opacity=1.0, color=BLUE),
        )

        self.play(Write(topic))
        self.wait()
        self.play(Write(defn))
        self.play(Write(defn2))
        self.wait()
        self.play(ShowCreation(base_circle), run_time=2)
        self.play(
            GrowFromPoint(cone_side1, diameter_end1),
            GrowFromPoint(cone_side2, diameter_end2),
            run_time=4,
        )
        self.play(ShowCreationThenFadeOut(cone), run_time=3)
        self.wait(2)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))

    def cone_area(self):
        topic = TextMobject("Surface area of a cone", color=BLUE)
        topic.scale(1.5).to_edge(UP)
        base_circle = Circle(color=BLUE).next_to(topic, DOWN, buff=2.0).to_edge(RIGHT)
        base_circle.rotate(PI / 4, axis=LEFT)
        base_circle_center = base_circle.get_center()
        diameter_end1 = base_circle_center + LEFT
        diameter_end2 = base_circle_center + RIGHT
        cone_tip = base_circle_center + 2 * UP
        cone_side1 = Line(diameter_end1, cone_tip, color=BLUE)
        cone_side2 = Line(diameter_end2, cone_tip, color=BLUE)
        cone_triangle = Polygon(diameter_end1, cone_tip, diameter_end2)
        cone = VGroup(base_circle, cone_triangle)
        circle_center = Point(base_circle_center, color=YELLOW)
        radius_label = TextMobject("r", color=YELLOW).scale(0.8)
        radius_label.next_to(Line(base_circle_center, diameter_end2), UP, buff=0.1)

        sector_radius = cone_side1.get_length()
        sector_angle = (2 * PI) / sector_radius
        sector_line1 = Line()
        sector_line1.set_length(sector_radius)
        sector_line2 = sector_line1.copy()
        sector_line1.set_angle(-PI / 8)
        sector_line2.set_angle(-sector_angle)
        arc = ArcBetweenPoints(
            sector_line1.get_end(), sector_line2.get_end(), angle=-TAU / 4
        )
        sector_arc_label = TexMobject(r"2 \pi r", color=RED).next_to(
            arc, DOWN, buff=0.2
        )
        sector_radius_label = TexMobject("l", color=RED).scale(0.8)
        sector_radius_label.next_to(sector_line2.get_center(), DOWN, buff=0.2)

        sector_o_label, sector_a_label, sector_b_label = [
            TextMobject(i) for i in list("OAB")
        ]
        sector_o_label.next_to(sector_line1.get_start(), UP, buff=0.1)
        sector_a_label.next_to(sector_line1.get_end(), UP, buff=0.1)
        sector_b_label.next_to(sector_line2.get_end(), UP, buff=0.1)
        sector_labels = [
            sector_a_label,
            sector_o_label,
            sector_b_label,
            sector_arc_label,
            sector_radius_label,
        ]
        sector = VGroup(sector_line1, sector_line2, arc, *sector_labels)
        sector.to_edge(DR)
        sector_line = sector.submobjects[0]
        sector_center = Point(sector_line.get_start(), color=YELLOW)

        self.play(Write(topic))
        self.play(ShowCreation(cone))
        self.add(radius_label, circle_center)
        self.play(ReplacementTransform(cone.copy(), sector), run_time=3)
        self.add(sector_center, *sector_labels)

        self.figs = (cone, sector)
        self.topic = topic

    def lateral_area(self):
        topic = self.topic
        cone, sector = self.figs

        lateral_surface_area = TextMobject("For curved surface area:").scale(1.3)
        lateral_surface_area.next_to(topic, DOWN, buff=0.5).to_edge(LEFT)

        texts = [
            ("C.S.A = Area of Sector OAB",),
            (
                r"= ($\frac{length \nobreakspace of \nobreakspace sector}{circumferance \nobreakspace of \nobreakspace circle}$)",
                r"$\times$ Area of circle",
            ),
            (
                r"= ($\frac{2 \pi r}{2 \pi l}$)",
                r"$\times$ $\pi l^2$",
            ),
            (r"$\therefore$ C.S.A = ", r"$\pi$ r $l$"),
        ]
        first_row = self.make_row(texts[0])
        first_row.next_to(lateral_surface_area, DOWN, buff=1.0).to_edge(LEFT)
        proof_lines = [first_row]
        for text in texts[1:]:
            row = self.make_row(text)
            row.next_to(proof_lines[-1], DOWN, buff=0.5).to_edge(LEFT)
            proof_lines.append(row)

        self.play(Write(lateral_surface_area))
        self.wait()
        for index, line in enumerate(proof_lines):
            run_time = 2 if index != 1 else 4
            self.play(Write(line), run_time=run_time)

        self.wait(2)
        self.play(FadeOutAndShiftDown(Group(*proof_lines, lateral_surface_area)))
        self.wait(3)

    def total_area(self):
        topic = self.topic
        cone, sector = self.figs

        total_surface_area = TextMobject("For total surface area:").scale(1.3)
        total_surface_area.next_to(topic, DOWN, buff=0.5).to_edge(LEFT)

        texts = [
            (
                "T.S.A = ",
                "C.S.A +",
                "Area of circular base",
            ),
            (r"= ", r"$\pi$ r $l$ + ", r"$\pi$ $r^2$"),
            (r"$\therefore$ T.S.A = ", r"$\pi$ r ( r + $l$)"),
        ]
        first_row = self.make_row(texts[0])
        first_row.next_to(total_surface_area, DOWN, buff=1.0).to_edge(LEFT)
        first_row_parts = first_row.submobjects
        proof_lines = [first_row]
        for text in texts[1:]:
            row = self.make_row(text)
            row.next_to(proof_lines[-1], DOWN, buff=0.5).to_edge(LEFT)
            proof_lines.append(row)

        base_circle, cone_triangle = cone.submobjects
        filled_triangle, filled_circle = cone_triangle.copy(), base_circle.copy()
        filled_triangle.set_fill(opacity=1.0, color=BLUE)
        filled_circle.set_fill(opacity=1.0, color=BLUE)

        sector_line1, sector_line2, *_ = sector.submobjects
        sector_triangle = Polygon(
            sector_line1.get_start(), sector_line1.get_end(), sector_line2.get_end()
        )
        sector_triangle.set_fill(opacity=1.0, color=BLUE)
        filled_sector = sector.copy()
        filled_sector.set_fill(color=BLUE, opacity=1.0)
        effect_figs = [
            VGroup(filled_sector, sector_triangle, filled_triangle),
            filled_circle,
        ]

        self.play(Write(total_surface_area))
        self.wait()
        self.play(Write(first_row_parts[0]))
        for text, fig in zip(first_row_parts[1:], effect_figs):
            self.play(Write(text))
            self.play(FadeIn(fig))
            self.play(FadeOut(fig))

        for line in proof_lines[1:]:
            self.play(Write(line), run_time=2)
        self.wait(2)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))

    def volume(self):
        cone, _ = self.figs

        topic = TextMobject("Volume of a cone", color=BLUE)
        topic.scale(1.5).to_edge(UP)

        texts = [
            (
                r"Volume = $\frac{1}{3}$ $\times$ ",
                r"Area of circular base $\times$ ",
                "height",
            ),
            (r"= $\frac{1}{3}$ $\times$ ", r"$\pi$ $r^2$ $\times$ h"),
            (r"$\therefore$ V = ", r"$\frac{1}{3}$ $\pi$ $r^2$ h"),
        ]

        first_row = self.make_row(texts[0])
        first_row.next_to(topic, DOWN, buff=1.0).to_edge(LEFT)
        first_row_parts = first_row.submobjects
        proof_lines = [first_row]
        for text in texts[1:]:
            row = self.make_row(text)
            row.next_to(proof_lines[-1], DOWN, buff=0.5).to_edge(LEFT)
            proof_lines.append(row)

        base_circle, cone_triangle = cone.submobjects
        base_center = base_circle.get_center()
        d1_point, cone_tip, d2_point = cone_triangle.get_vertices()

        cone_height = DashedLine(cone_tip, base_center)
        h_label = TextMobject("h").scale(0.75).next_to(cone_height, buff=0.2)
        r_label = TextMobject("r", color=YELLOW).scale(0.8)
        r_label.next_to(Line(base_center, d2_point), UP, buff=0.1)
        base_circle_center = Point(base_center, color=YELLOW)
        perp_drop = VGroup(cone_height, h_label)
        cone_labels = (perp_drop, r_label, base_circle_center)

        filled_base_circle = base_circle.copy()
        filled_base_circle.set_fill(color=BLUE, opacity=1.0)
        filled_perp = Line(cone_tip, base_center, color=YELLOW)
        first_row_objs = [filled_base_circle, filled_perp]

        self.play(Write(topic))
        self.play(ShowCreation(cone))
        self.add(*cone_labels)
        self.wait()
        self.play(Write(first_row_parts[0]))
        for text, fig in zip(first_row_parts[1:], first_row_objs):
            self.play(Write(text))
            self.play(FadeIn(fig))
            self.play(FadeOut(fig))
        for line in proof_lines[1:]:
            self.play(Write(line), run_time=2)
        self.wait(2)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))
        self.wait()

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
