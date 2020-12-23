from manimlib.imports import *


class Test(Scene):
    co_ordinate = lambda self, x, y: np.array([x, y, 0])
    quad_sides = None
    quadrilateral = None

    def construct(self):
        #self.quad_intro()
        #self.quad_variation()
        #self.parallelogram_intro()
        self.rectangle_intro()

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

        comment1 = TextMobject(
            "Rectangle is a quadrilateral whose opposite sides are"
        )
        comment2 = TextMobject(" equal and each angle is 90 degrees.")
        comment1.next_to(topic, DOWN).to_edge(LEFT)
        comment2.next_to(comment1, DOWN, buff=0.3)

        equal_1 = Line(A, B).to_edge(RIGHT)
        equal_sign = TextMobject("Equal(=)")
        equal_sign.next_to(equal_1, LEFT)
        equal_2 = Line(C, D).next_to(parallel_sign, LEFT)
        equals = VGroup(equal_1, equal_2)

        perp = DashedLine(A, B - co_ordinate(-1, 0))
        perp_label = TexMobject("height").scale(0.7)
        perp_label.next_to(perp, buff=0.2)
        base = Line(B, C, color=YELLOW)
        base_label = TexMobject("base")
        base_label.next_to(rectangle, DOWN)

        comment3 = TextMobject("Area of the rectangle is given by,")
        area_text = TextMobject("Area(A) = ")
        base_text = TextMobject("base $\\times$")
        height_text = TextMobject("height")
        area_text.to_edge(DOWN).to_edge(LEFT)
        comment3.next_to(area_text, UP).to_edge(LEFT)
        processed = [area_text]
        for i in (base_text, height_text):
            i.next_to(processed[-1])
            processed.append(i)

        self.play(Write(topic))
        self.play(ShowCreation(rectangle))
        self.play(Write(comment1))
        self.play(Write(comment2))
        self.play(ReplacementTransform(Line(A, B), equal_1))
        self.play(ReplacementTransform(Line(C, D), equal_2))
        self.play(Write(equal_sign))
        self.play(Indicate(equals))
        self.play(FadeOutAndShift(VGroup(equals, equal_sign), RIGHT))
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

        comment1 = TextMobject(
            "Parallelogram is a quadrilateral whose opposite sides are"
        )
        comment2 = TextMobject(" equal and parallel.")
        comment1.next_to(topic, DOWN).to_edge(LEFT)
        comment2.next_to(comment1, DOWN, buff=0.3)

        equal_1 = Line(A, B).to_edge(RIGHT)
        equal_sign = TextMobject("Equal(=)")
        parallel_sign = TextMobject("Parallel(//)")
        equal_sign.next_to(equal_1, LEFT)
        parallel_sign.next_to(equal_1, LEFT)
        equal_2 = Line(C, D).next_to(parallel_sign, LEFT)
        equals = VGroup(equal_1, equal_2)

        perp = DashedLine(A, B - co_ordinate(-1, 0))
        perp_label = TexMobject("height").scale(0.7)
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
        for i in (base_text, height_text):
            i.next_to(processed[-1])
            processed.append(i)

        self.play(Write(topic))
        self.play(ShowCreation(parallelogram))
        self.play(Write(comment1))
        self.play(Write(comment2))
        self.play(ReplacementTransform(Line(A, B), equal_1))
        self.play(ReplacementTransform(Line(C, D), equal_2))
        self.play(Write(equal_sign))
        self.play(Indicate(equals))
        self.play(FadeOutAndShift(equal_sign, RIGHT))
        self.play(Write(parallel_sign))
        self.play(Indicate(equals))
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
        perpendicular_1 = Line(A, co_ordinate(-3, -1), color=YELLOW)
        perpendicular_2 = Line(B, co_ordinate(3, -1), color=YELLOW)
        perpendiculars = VGroup(perpendicular_1, perpendicular_2)
        perpendiculars_base_line = Line(
            co_ordinate(-3, -1), co_ordinate(3, -1), color=YELLOW
        )

        comment1 = TextMobject("The area of the quadrilateral will be,")
        area_text = TextMobject("Area(A) = ")
        half_frac_text = TexMobject(r"\frac{1}{2}")
        diagnol_length_text = TextMobject("Diagnol length + ")
        perpendicular_sum_text = TextMobject("Sum of perpendiculars")
        area_text.to_edge(DOWN).to_edge(LEFT)
        comment1.next_to(area_text, UP).to_edge(LEFT)
        processed = [area_text]
        for i in (half_frac_text, diagnol_length_text, perpendicular_sum_text):
            i.next_to(processed[-1])
            processed.append(i)

        self.play(ScaleInPlace(self.quadrilateral, 1.5))
        self.play(ScaleInPlace(self.quadrilateral, 0.5))
        self.play(Transform(self.quadrilateral, angle_quad_g))
        self.wait()

        self.play(Write(comment1))
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
