from manimlib.imports import *


class Test(Scene):
    co_ordinate = lambda self, x, y: np.array([x, y, 0])
    quad_sides = None
    quadrilateral = None

    def construct(self):
        # self.quad_intro()
        # self.quad_variation()
        # self.parallelogram_intro()
        # self.rectangle_intro()
        # self.rhombus_intro()
        self.square_intro()

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
            midpoint = lambda x, y: (x + y) / 2
            line = Line(color=YELLOW_A).scale(0.25)
            line.shift(midpoint(*point))
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
            midpoint = lambda x, y: (x + y) / 2
            line = Line(color=YELLOW_A).scale(0.25)
            line.shift(midpoint(*point))
            line.rotate(PI / 2) if index % 2 != 0 else None
            lines.append(line)

        lines = VGroup(*lines)
        perp = DashedLine(A, D + 1.5 * RIGHT)
        perp_label = TexMobject("height")
        perp_label.next_to(perp, buff=0.2)
        base = Line(D, C, color=YELLOW)
        base_label = TexMobject("base")
        base_label.next_to(rhombus, DOWN)

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
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def rectangle_intro(self):
        topic = TextMobject("Rectangle", color=BLUE).scale(1.5)
        topic.to_edge(UP)

        co_ordinate = self.co_ordinate
        rectangle = Polygon(
            co_ordinate(-2, 0),
            co_ordinate(2, 0),
            co_ordinate(2, -2),
            co_ordinate(-2, -2),
        )
        A, B, C, D = rectangle.get_vertices()

        defn_comment = TextMobject(
            "Rectangle is a quadrilateral whose opposite sides are equal"
        )
        defn_comment2 = TextMobject("and each angle is a right angle.")
        defn_comment.next_to(topic, DOWN, buff=1.0).to_edge(LEFT)
        defn_comment2.next_to(defn_comment, DOWN, buff=0.3)

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

        co_ordinate = self.co_ordinate
        parallelogram = Polygon(
            co_ordinate(-5, 1),
            co_ordinate(-6, -1),
            co_ordinate(-3, -1),
            co_ordinate(-2, 1),
        )
        A, B, C, D = parallelogram.get_vertices()

        defn_comment = TextMobject(
            "Parallelogram is a quadrilateral whose opposite sides are"
        )
        defn_comment2 = TextMobject(" equal and parallel.")
        defn_comment.next_to(topic, DOWN).to_edge(LEFT)
        defn_comment2.next_to(defn_comment, DOWN, buff=0.3)

        equal_1 = Line(A, B).to_edge(RIGHT)
        equal_sign = TextMobject("Equal(=)")
        parallel_sign = TextMobject("Parallel(//)")
        equal_sign.next_to(equal_1, LEFT)
        parallel_sign.next_to(equal_1, LEFT)
        equal_2 = Line(C, D).next_to(parallel_sign, LEFT)
        equals = VGroup(equal_1, equal_2)

        perp = DashedLine(A, B - co_ordinate(-1, 0))
        perp_label = TexMobject("height")
        perp_label.next_to(perp, buff=0.2)
        base = Line(B, C, color=YELLOW)
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
        self.play(ReplacementTransform(Line(A, B), equal_1))
        self.play(ReplacementTransform(Line(C, D), equal_2))
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
        co_ordinate = self.co_ordinate

        # Change angles of sides
        # QUadrilateral
        # A-----------------B
        # |#################|
        # |#################|
        # |#################|
        # D-----------------C
        A, B, C, D = (
            co_ordinate(-3, 1),
            co_ordinate(3, 1),
            co_ordinate(2, -1),
            co_ordinate(-2, -1),
        )

        a_side = Line(A, B)
        b_side = Line(B, C)
        c_side = Line(C, D)
        d_side = Line(D, A)
        angle_quad_g = VGroup(a_side, b_side, c_side, d_side).set_color(BLUE)

        diagnol_line = Line(A, C, color=YELLOW)
        perpendicular_1 = DashedLine(A, co_ordinate(-3, -1), color=YELLOW)
        perpendicular_2 = DashedLine(B, co_ordinate(3, -1), color=YELLOW)
        perpendiculars = VGroup(perpendicular_1, perpendicular_2)
        perpendiculars_base_line = Line(
            co_ordinate(-3, -1), co_ordinate(3, -1), color=YELLOW
        )

        area_comment = TextMobject("Area of the quadrilateral is given by,")
        area_text = TextMobject("Area(A) = ")
        half_frac_text = TexMobject(r"\frac{1}{2}")
        diagnol_length_text = TextMobject("Diagnol length + ")
        perpendicular_sum_text = TextMobject("Sum of perpendiculars")
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
            line.next_to(big_line_target.start, LEFT).shift(LEFT + UP)
            line.next_to(broken_lines[-1]) if broken_lines else None
            broken_lines.append(line)
        broken_lines_g = VGroup(*broken_lines)

        comment1 = TextMobject("A quadrilateral has four sides")
        comment1.next_to(broken_lines_g, UP, buff=1.0)

        co_ordinate = self.co_ordinate
        # QUadrilateral
        # A-----------------B
        # |#################|
        # |#################|
        # |#################|
        # D-----------------C
        A, B, C, D = (
            co_ordinate(-2, 0),
            co_ordinate(2, 0),
            co_ordinate(2, -2),
            co_ordinate(-2, -2),
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
        self.quad_sides = quad_sides
        self.quadrilateral = quad_sides_g
