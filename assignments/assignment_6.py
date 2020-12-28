from manimlib.imports import *


class Quadrilaterals(Scene):
    midpoint = lambda self, x, y: (x + y) / 2
    quadrilateral = None

    def construct(self):
        self.quad_intro()
        self.quad_variation()
        self.parallelogram_intro()
        self.rectangle_intro()
        self.rhombus_intro()
        self.trapezium_intro()
        self.kite_intro()

    def kite_intro(self):
        topic = TextMobject("Kite", color=BLUE).scale(1.5)
        topic.to_edge(UP)
        kite = Polygon(
            UL,
            UP + UP,
            UR,
            DOWN,
        )
        kite.shift(DOWN)
        A, B, C, D = kite.get_vertices()

        lines = []
        for index, point in enumerate([(A, B), (B, C), (C, D), (D, A)]):
            index += 1
            line = Line(color=YELLOW_A).scale(0.25)
            line.shift(self.midpoint(*point))
            line.rotate(-PI / 6) if index == 1 else None
            line.rotate(PI / 6) if index == 2 else None
            if index > 2:
                line.set_color(YELLOW_E)
                line1 = line.copy()
                line2 = line.copy().next_to(line1, UP, buff=0.1)
                line = VGroup(line1, line2)
            lines.append(line)
        lines = VGroup(*lines)

        perpendicular_1 = DashedLine(A,C)
        perpendicular_2 = DashedLine(B,D)

        perp_comment = TextMobject("In kite, one of the diagnol separates it into two")
        perp_comment2 = TextMobject("isosceles triangles.")
        perp_comment2.next_to(kite, UP, buff=0.5)
        perp_comment.next_to(perp_comment2, UP)

        area_comment = TextMobject("Area of the kite is given by,")
        area_text = TextMobject("Area(A) = ")
        half_frac_text = TexMobject(r"\frac{1}{2}")
        diagnol1_text = TextMobject("diagnol 1 $\\times$")
        diagnol2_text = TextMobject("diagnol 2")
        area_text.to_edge(DOWN).to_edge(LEFT)
        area_comment.next_to(area_text, UP).to_edge(LEFT)
        processed = [area_text]
        for text in (half_frac_text, diagnol1_text, diagnol2_text):
            text.next_to(processed[-1])
            processed.append(text)

        self.play(Write(topic))
        self.play(ShowCreation(kite))
        self.wait()
        self.play(ShowCreation(lines))
        self.play(ShowCreation(perpendicular_1))
        self.play(ShowCreation(perpendicular_2))
        self.play(Write(perp_comment))
        self.play(Write(perp_comment2))
        self.play(Indicate(lines), Indicate(perpendicular_1))
        self.wait()
        self.play(Write(area_comment))
        self.play(Write(area_text))
        self.play(Write(half_frac_text))
        self.play(ReplacementTransform(perpendicular_1, diagnol1_text))
        self.play(ReplacementTransform(perpendicular_2, diagnol2_text))
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))


    def trapezium_intro(self):
        topic = TextMobject("Trapezium", color=BLUE).scale(1.5)
        topic.to_edge(UP)

        trapezium = Polygon(
            UL,
            UR,
            DR + RIGHT,
            DL + LEFT,
        )
        trapezium.scale(1.3)
        trapezium_orig = trapezium.generate_target()
        trapezium_edge = trapezium.copy().to_edge(LEFT)
        A, B, C, D = trapezium.get_vertices()
        P, Q, R, S = trapezium_edge.get_vertices()

        parallel_comment = TextMobject(
            "Any two opposite sides of a trapezium are parallel."
        )
        parallel_comment.next_to(topic, DOWN, buff=0.5)

        parallel_1 = Line(A, B).to_edge(RIGHT)
        parallel_sign = TextMobject("Parallel(//)")
        parallel_sign.next_to(parallel_1, DOWN, buff=1.0)
        parallel_2 = Line(D, C).next_to(parallel_sign, DOWN, buff=1.0)
        parallels = VGroup(parallel_1, parallel_2)

        perp = DashedLine(A, D + 1.3 * RIGHT)
        perp_label = TexMobject("height")
        perp_label.next_to(perp, buff=0.2)
        side1 = Line(A, B, color=YELLOW)
        side2 = Line(D, C, color=YELLOW)
        sides = VGroup(side1, side2)

        area_comment = TextMobject("Area of the trapezium is given by,")
        area_text = TextMobject("Area(A) = ")
        half_frac_text = TexMobject(r"\frac{1}{2}")
        height_text = TextMobject("height $\\times$")
        sides_sum_text = TextMobject("sum of length of two parallel sides")
        area_text.to_edge(DOWN).to_edge(LEFT)
        area_comment.next_to(area_text, UP).to_edge(LEFT)
        processed = [area_text]
        for text in (half_frac_text, height_text, sides_sum_text):
            text.next_to(processed[-1])
            processed.append(text)

        self.play(Write(topic))
        self.play(ShowCreation(trapezium))
        self.wait()
        self.play(Write(parallel_comment))
        self.play(ReplacementTransform(trapezium, trapezium_edge))
        self.play(ReplacementTransform(Line(P, Q), parallel_1))
        self.play(ReplacementTransform(Line(R, S), parallel_2))
        self.play(Write(parallel_sign))
        self.play(Indicate(parallels))
        self.play(FadeOutAndShift(VGroup(parallels, parallel_sign), RIGHT))
        self.play(ReplacementTransform(trapezium_edge, trapezium_orig))
        self.play(ShowCreation(perp))
        self.play(Write(perp_label))
        self.play(Write(area_comment))
        self.play(Write(area_text))
        self.play(Write(half_frac_text))
        self.play(ReplacementTransform(perp_label, height_text))
        self.play(ShowCreation(sides))
        self.play(ReplacementTransform(sides, sides_sum_text))
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def square_intro(self):
        topic = TextMobject("Square", color=BLUE).scale(1.5)
        topic.to_edge(UP)
        square = Polygon(
            UL,
            UR,
            DR,
            DL,
        )
        square.scale(1.2).shift(DOWN)
        A, B, C, D = square.get_vertices()

        defn_comment = TextMobject(
            "Square is a quadrilateral whose all sides are equal and each"
        )
        defn_comment2 = TextMobject("angle is a right angle.")
        defn_comment.next_to(topic, DOWN, buff=0.5).to_edge(LEFT)
        defn_comment2.next_to(defn_comment, DOWN, buff=0.3)

        lines = []
        for index, point in enumerate([(A, B), (B, C), (C, D), (D, A)]):
            index += 1
            line = Line(color=YELLOW_A).scale(0.25)
            line.shift(self.midpoint(*point))
            line.rotate(PI / 2) if index % 2 != 0 else None
            lines.append(line)
        lines = VGroup(*lines)

        elbows = []
        for corner in ([A, B, C], [B, C, D], [C, D, A], [D, A, B]):
            elbow = Elbow(color=YELLOW)
            elbow.set_points_as_corners(corner)
            elbow.set_width(elbow.width, about_point=corner[1])
            elbow.rotate(PI)
            elbows.append(elbow)
        elbows = VGroup(*elbows)

        length = Line(A, D, color=RED)
        length_label = TexMobject("length")
        length_label.next_to(length, LEFT)
        breadth = Line(D, C, color=YELLOW)
        breadth_label = TexMobject("length")
        breadth_label.next_to(Line(C, D), UP)

        area_comment = TextMobject("Area of the square is given by,")
        area_text = TextMobject("Area(A) = ")
        length_text = TextMobject("length $\\times$")
        breadth_text = TextMobject("length")
        area_text.to_edge(DOWN).to_edge(LEFT)
        area_comment.next_to(area_text, UP).to_edge(LEFT)
        processed = [area_text]
        for text in (length_text, breadth_text):
            text.next_to(processed[-1])
            processed.append(text)

        self.play(Write(topic))
        self.play(ShowCreation(square))
        self.play(Write(defn_comment))
        self.play(Write(defn_comment2))
        self.wait()
        self.play(ShowCreation(lines))
        self.play(Indicate(lines))
        self.play(ShowCreation(elbows))
        self.wait()
        self.play(FadeOut(elbows))
        self.play(ShowCreation(length))
        self.play(Write(length_label))
        self.play(ShowCreation(breadth))
        self.play(Write(breadth_label))
        self.play(Write(area_comment))
        self.play(Write(area_text))
        self.play(ReplacementTransform(length_label, length_text))
        self.play(ReplacementTransform(breadth_label, breadth_text))
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def rhombus_intro(self):
        topic = TextMobject("Rhombus", color=BLUE).scale(1.5)
        topic.to_edge(UP)

        rhombus = Polygon(
            UL,
            UR,
            DR + LEFT,
            DL + LEFT,
        )
        rhombus.scale(1.5)
        A, B, C, D = rhombus.get_vertices()

        defn_comment = TextMobject(
            "Rhombus is a quadrilateral whose all sides are equal."
        )
        defn_comment.next_to(topic, DOWN, buff=0.5).to_edge(LEFT)

        lines = []
        for index, point in enumerate([(A, B), (B, C), (C, D), (D, A)]):
            index += 1
            line = Line(color=YELLOW_A).scale(0.25)
            line.shift(self.midpoint(*point))
            line.rotate(PI / 2) if index % 2 != 0 else None
            lines.append(line)

        lines = VGroup(*lines)
        perp = DashedLine(A, D + 1.5 * RIGHT)
        perp_label = TexMobject("height")
        perp_label.next_to(perp, buff=0.2)
        base = Line(D, C, color=YELLOW)
        base_label = TexMobject("base")
        base_label.next_to(rhombus, DOWN)

        diagnol = Line(A, C, color=YELLOW)
        diagnol2 = Line(B, D, color=YELLOW)

        area_comment = TextMobject("Area of the rhombus is given by,")
        area_text = TextMobject("Area(A) = ")
        base_text = TextMobject("base $\\times$")
        height_text = TextMobject("height")
        area_text.to_edge(DOWN).to_edge(LEFT)
        area_comment.next_to(area_text, UP).to_edge(LEFT)
        processed = [area_text]
        for text in (base_text, height_text):
            text.next_to(processed[-1])
            processed.append(text)

        area_comment2 = TextMobject("Similarly, area of the rhombus is also given by,")
        area_text2 = TextMobject("Area(A) = ")
        half_frac_text = TexMobject(r"\frac{1}{2}")
        diagnol_text = TextMobject("diagnol 1 $\\times$")
        diagnol2_text = TextMobject("diagnol 2")
        area_text2.to_edge(DOWN).to_edge(LEFT)
        area_comment2.next_to(area_text2, UP).to_edge(LEFT)
        processed = [area_text2]

        for text in (half_frac_text, diagnol_text, diagnol2_text):
            text.next_to(processed[-1])
            processed.append(text)

        self.play(Write(topic))
        self.play(ShowCreation(rhombus))
        self.play(Write(defn_comment))
        self.wait()
        self.play(ShowCreation(lines))
        self.play(Indicate(lines))
        self.play(ShowCreation(perp))
        self.play(Write(perp_label))
        self.play(ShowCreation(base))
        self.play(Write(base_label))
        self.play(Write(area_comment))
        self.play(Write(area_text))
        self.play(ReplacementTransform(base_label, base_text))
        self.play(ReplacementTransform(perp_label, height_text))
        self.wait()
        self.play(FadeOut(base), FadeOut(perp))
        self.play(Transform(area_comment, area_comment2))
        self.play(Transform(area_text, area_text2))
        self.play(Transform(VGroup(base_text, height_text), half_frac_text))
        self.play(ShowCreation(diagnol))
        self.play(ShowCreation(diagnol2))
        self.play(ReplacementTransform(diagnol, diagnol_text))
        self.play(ReplacementTransform(diagnol2, diagnol2_text))
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def rectangle_intro(self):
        topic = TextMobject("Rectangle", color=BLUE).scale(1.5)
        topic.to_edge(UP)
        rectangle = Polygon(
            UL + LEFT,
            UR + RIGHT,
            DR + RIGHT,
            DL + LEFT,
        )
        rectangle.shift(DOWN)
        A, B, C, D = rectangle.get_vertices()

        defn_comment = TextMobject(
            "Rectangle is a quadrilateral whose opposite sides are equal"
        )
        defn_comment2 = TextMobject("and each angle is a right angle.")
        defn_comment.next_to(topic, DOWN, buff=1.0).to_edge(LEFT)
        defn_comment2.next_to(defn_comment, DOWN, buff=0.3)

        lines = []
        for index, point in enumerate([(A, B), (B, C), (C, D), (D, A)]):
            index += 1
            line = Line(color=YELLOW_A).scale(0.25)
            line.shift(self.midpoint(*point))
            if index % 2 != 0:
                line.rotate(PI / 2).set_color(YELLOW_E)
                line1 = line.copy()
                line2 = line.copy().next_to(line1, buff=0.1)
                line = VGroup(line1, line2)
            lines.append(line)
        lines = VGroup(*lines)

        equal_1 = Line(A, D).to_edge(RIGHT)
        equal_sign = TextMobject("Equal(=)")
        equal_sign.next_to(equal_1, LEFT)
        equal_2 = Line(B, C).next_to(equal_sign, LEFT)
        equals = VGroup(equal_1, equal_2)

        elbows = []
        for corner in ([A, B, C], [B, C, D], [C, D, A], [D, A, B]):
            elbow = Elbow(color=YELLOW)
            elbow.set_points_as_corners(corner)
            elbow.set_width(elbow.width, about_point=corner[1])
            elbow.rotate(PI)
            elbows.append(elbow)
        elbows = VGroup(*elbows)

        length = Line(A, D, color=RED)
        length_label = TexMobject("length")
        length_label.next_to(length, LEFT)
        breadth = Line(D, C, color=YELLOW)
        breadth_label = TexMobject("breadth")
        breadth_label.next_to(Line(C, D), UP)

        area_comment = TextMobject("Area of the rectangle is given by,")
        area_text = TextMobject("Area(A) = ")
        length_text = TextMobject("length $\\times$")
        breadth_text = TextMobject("breadth")
        area_text.to_edge(DOWN).to_edge(LEFT)
        area_comment.next_to(area_text, UP).to_edge(LEFT)
        processed = [area_text]
        for text in (length_text, breadth_text):
            text.next_to(processed[-1])
            processed.append(text)

        self.play(Write(topic))
        self.play(ShowCreation(rectangle))
        self.play(Write(defn_comment))
        self.play(Write(defn_comment2))
        self.play(ShowCreation(lines))
        self.play(ReplacementTransform(Line(A, D), equal_1))
        self.play(ReplacementTransform(Line(B, C), equal_2))
        self.play(Write(equal_sign))
        self.play(Indicate(equals))
        self.play(FadeOutAndShift(VGroup(equals, equal_sign), RIGHT))
        self.play(ShowCreation(elbows))
        self.play(FadeOut(elbows))
        self.play(FadeOut(VGroup(defn_comment, defn_comment2)))
        self.play(ShowCreation(length))
        self.play(Write(length_label))
        self.play(ShowCreation(breadth))
        self.play(Write(breadth_label))
        self.play(Write(area_comment))
        self.play(Write(area_text))
        self.play(ReplacementTransform(length_label, length_text))
        self.play(ReplacementTransform(breadth_label, breadth_text))
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def parallelogram_intro(self):
        topic = TextMobject("Parallelogram", color=BLUE).scale(1.5)
        topic.to_edge(UP)
        parallelogram = Polygon(
                UL + LEFT,
                UR + RIGHT,
                DR,
                DL + 2 * LEFT,
        )
        A, B, C, D = parallelogram.get_vertices()

        defn_comment = TextMobject(
            "Parallelogram is a quadrilateral whose opposite sides are"
        )
        defn_comment2 = TextMobject(" equal and parallel.")
        defn_comment.next_to(topic, DOWN).to_edge(LEFT)
        defn_comment2.next_to(defn_comment, DOWN, buff=0.3)

        lines = []
        for index, point in enumerate([(A, B), (B, C), (C, D), (D, A)]):
            index += 1
            line = Line(color=YELLOW_A).scale(0.25)
            line.shift(self.midpoint(*point))
            if index % 2 != 0:
                line.rotate(PI / 2).set_color(YELLOW_E)
                line1 = line.copy()
                line2 = line.copy().next_to(line1, buff=0.1)
                line = VGroup(line1, line2)
            lines.append(line)
        lines = VGroup(*lines)

        equal_1 = Line(A, D).to_edge(RIGHT)
        equal_sign = TextMobject("Equal(=)")
        parallel_sign = TextMobject("Parallel(//)")
        equal_sign.next_to(equal_1, LEFT, buff=0)
        parallel_sign.next_to(equal_1, LEFT, buff=0)
        equal_2 = Line(B, C).next_to(parallel_sign, LEFT, buff=0)
        equals = VGroup(equal_1, equal_2)

        perp = DashedLine(A, D - LEFT)
        perp_label = TexMobject("height")
        perp_label.next_to(perp, buff=0.2)
        base = Line(C, D, color=YELLOW)
        base_label = TexMobject("base")
        base_label.next_to(parallelogram, DOWN)

        comment3 = TextMobject("Area of the parallelogram is given by,")
        area_text = TextMobject("Area(A) = ")
        base_text = TextMobject("base $\\times$")
        height_text = TextMobject("height")
        area_text.to_edge(DOWN).to_edge(LEFT)
        comment3.next_to(area_text, UP).to_edge(LEFT)
        processed = [area_text]
        for text in (base_text, height_text):
            text.next_to(processed[-1])
            processed.append(text)

        self.play(Write(topic))
        self.play(ShowCreation(parallelogram))
        self.play(Write(defn_comment))
        self.play(Write(defn_comment2))
        self.play(ShowCreation(lines))
        self.play(ReplacementTransform(Line(A, D), equal_1))
        self.play(ReplacementTransform(Line(B, C), equal_2))
        self.play(Write(equal_sign))
        self.play(Indicate(equals))
        self.play(FadeOutAndShift(equal_sign, RIGHT))
        self.play(Write(parallel_sign))
        self.play(Indicate(equals))
        self.play(FadeOutAndShift(VGroup(equals, parallel_sign), RIGHT))
        self.play(ShowCreation(perp))
        self.play(Write(perp_label))
        self.play(ShowCreation(base))
        self.play(Write(base_label))
        self.play(Write(comment3))
        self.play(Write(area_text))
        self.play(ReplacementTransform(base_label, base_text))
        self.play(ReplacementTransform(perp_label, height_text))
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def quad_variation(self):
        # QUadrilateral
        # A-----------------B
        # |#################|
        # |#################|
        # |#################|
        # D-----------------C
        # Change angles of sides
        A, B, C, D = (
            UL + LEFT,
            UR + RIGHT,
            DR,
            DL,
        )

        a_side = Line(A, B)
        b_side = Line(B, C)
        c_side = Line(C, D)
        d_side = Line(D, A)
        angle_quad_g = VGroup(a_side, b_side, c_side, d_side).set_color(BLUE)

        diagnol_line = Line(A, C, color=YELLOW)
        perpendicular_1 = DashedLine(A, D + LEFT, color=YELLOW)
        perpendicular_2 = DashedLine(B, C + RIGHT, color=YELLOW)
        perpendiculars = VGroup(perpendicular_1, perpendicular_2)
        perpendiculars_base_line = Line(
            D + LEFT, C + RIGHT, color=YELLOW
        )

        area_comment = TextMobject("Area of the quadrilateral is given by,")
        area_text = TextMobject("Area(A) = ")
        half_frac_text = TexMobject(r"\frac{1}{2}")
        diagnol_length_text = TextMobject("diagnol $\\times$")
        perpendicular_sum_text = TextMobject("Sum of length of perpendiculars")
        area_text.to_edge(DOWN).to_edge(LEFT)
        area_comment.next_to(area_text, UP).to_edge(LEFT)
        processed = [area_text]
        for text in (half_frac_text, diagnol_length_text, perpendicular_sum_text):
            text.next_to(processed[-1])
            processed.append(text)

        self.play(ScaleInPlace(self.quadrilateral, 1.5))
        self.play(ScaleInPlace(self.quadrilateral, 0.5))
        self.play(Transform(self.quadrilateral, angle_quad_g))
        self.wait()

        self.play(Write(area_comment))
        self.play(Write(area_text))
        self.play(Write(half_frac_text))
        self.play(ShowCreation(diagnol_line))
        self.play(ReplacementTransform(diagnol_line, diagnol_length_text))
        self.play(ShowCreation(perpendiculars_base_line))
        self.play(ShowCreation(perpendiculars))
        self.play(ReplacementTransform(perpendiculars, perpendicular_sum_text))
        self.play(FadeOut(perpendiculars_base_line))
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def quad_intro(self):
        topic = TextMobject("Quadrilateral", color=BLUE).scale(1.5)
        topic.to_edge(UP)

        big_line = Line(color=BLUE)
        big_line.next_to(topic, DOWN, buff=2.0)
        big_line_target = big_line.generate_target()
        big_line_target.scale(4)

        broken_lines = []
        for i in range(4):
            line = Line(color=BLUE)
            line.next_to(topic, DOWN, buff=2.0).shift(3 * LEFT)
            line.next_to(broken_lines[-1]) if broken_lines else None
            broken_lines.append(line)
        broken_lines_g = VGroup(*broken_lines)

        comment1 = TextMobject("A quadrilateral has four sides")
        comment1.next_to(broken_lines_g, UP, buff=1.0)

        # QUadrilateral
        # A-----------------B
        # |#################|
        # |#################|
        # |#################|
        # D-----------------C
        A, B, C, D = (
            UL,
            UR,
            DR,
            DL,
        )

        a_side = Line(A, B)
        b_side = Line(B, C)
        c_side = Line(C, D)
        d_side = Line(D, A)
        quad_sides = [a_side, b_side, c_side, d_side]
        quad_sides_g = VGroup(*quad_sides).set_color(BLUE)

        comment2 = TextMobject("Quadrilateral is a closed plane")
        comment2.next_to(quad_sides_g, UP, buff=1.0)

        self.play(Write(topic))
        self.play(FadeInFrom(big_line, LEFT_SIDE), run_time=4)
        self.play(MoveToTarget(big_line), run_time=3)
        self.play(ReplacementTransform(big_line, broken_lines_g))
        self.play(Write(comment1), run_time=2)
        self.wait()
        self.play(FadeOut(comment1))
        for line, side in zip(broken_lines, quad_sides):
            self.play(ReplacementTransform(line, side))

        self.play(Write(comment2), run_time=2)
        self.wait()
        self.play(FadeOut(comment2))
        self.quadrilateral = quad_sides_g
