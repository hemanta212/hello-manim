from manimlib.imports import *


class Test(Scene):
    co_ordinate = lambda self, x, y: np.array([x, y, 0])
    quad_sides = None
    quadrilateral = None

    def construct(self):
        self.quad_intro()
        self.quad_variation()

    def quad_variation(self):
        co_ordinate = self.co_ordinate

        # Change angles of sides
        a_side = Line(co_ordinate(-3, 1), co_ordinate(3, 1))
        b_side = Line(co_ordinate(-3, 1), co_ordinate(-2, -1))
        c_side = Line(co_ordinate(-2, -1), co_ordinate(2, -1))
        d_side = Line(co_ordinate(3, 1), co_ordinate(2, -1))
        angle_quad_g = VGroup(a_side, b_side, c_side, d_side).set_color(BLUE)

        diagnol_line = Line(co_ordinate(-3, 1), co_ordinate(2, -1)).set_color(YELLOW)
        perpendicular_1 = Line(co_ordinate(-3, 1), co_ordinate(-3, -1), color=YELLOW)
        perpendicular_2 = Line(co_ordinate(3, 1), co_ordinate(3, -1), color=YELLOW)
        perpendiculars = VGroup(perpendicular_1, perpendicular_2)

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

        # self.play(ReplacementTransform(self.quadrilateral, large_quad_g))
        self.play(ScaleInPlace(self.quadrilateral, 1.5))
        self.play(ScaleInPlace(self.quadrilateral, 0.5))
        self.play(ReplacementTransform(self.quadrilateral, angle_quad_g))
        self.wait()

        self.play(Write(comment1))
        self.play(Write(area_text))
        self.play(Write(half_frac_text))
        self.play(ShowCreation(diagnol_line))
        self.play(ReplacementTransform(diagnol_line, diagnol_length_text))
        self.play(ShowCreation(perpendiculars))
        self.play(ReplacementTransform(perpendiculars, perpendicular_sum_text))
        self.wait(2)

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
        a_side = Line(co_ordinate(-2, 0), co_ordinate(2, 0))
        b_side = Line(co_ordinate(-2, 0), co_ordinate(-2, -2))
        c_side = Line(co_ordinate(-2, -2), co_ordinate(2, -2))
        d_side = Line(co_ordinate(2, 0), co_ordinate(2, -2))
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
