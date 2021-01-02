from manimlib.imports import *


class Triangle1(Scene):

    def construct(self):
        topic = TextMobject("Area of triangle", color=BLUE).scale(1.5)
        topic_ = TextMobject("when base and height are given", color=BLUE).scale(1.5)
        topic_.next_to(topic, DOWN)

        triangle = Polygon(
            3.5 * LEFT,
            ORIGIN + 2.5 * UP,
            3.5 * RIGHT,
        )
        A, B, C = triangle.get_vertices()

        label_a, label_b, label_c = (TextMobject(i) for i in "A B C".split())
        label_a.next_to(A, LEFT)
        label_b.next_to(B, buff=0.5)
        label_c.next_to(C)
        labels = VGroup(label_a, label_b, label_c)

        given_comment = TextMobject(r"In the given triangle, $\triangle$ ABC,")
        we_have_text = TextMobject("We have,")
        given_comment.to_edge(UL)
        we_have_text.next_to(given_comment, DOWN, buff=0.3).to_edge(LEFT)

        perp = DashedLine(B, ORIGIN)
        perp_label = TexMobject("height").scale(0.85)
        perp_label.next_to(perp, buff=0.2)
        base = Line(A, C, color=YELLOW)
        base_label = TexMobject("base")
        base_label.next_to(triangle, DOWN)

        comment3 = TextMobject("Area of the triangle is given by,")
        area_text = TextMobject("Area(A) = ")
        frac_text = TexMobject(r"\frac{1}{2} ")
        base_text = TextMobject(r"base $\times$")
        height_text = TextMobject("height")
        equal_sign = TextMobject("=")
        frac_text2 = TexMobject(r"\frac{1}{2} ")
        base_text2 = TextMobject(r"b $\cdot$")
        height_text2 = TextMobject("h")
        area_text.to_edge(DOWN).to_edge(LEFT)
        comment3.next_to(area_text, UP, buff=0.6).to_edge(LEFT)

        processed = [area_text]
        for text in (
            frac_text,
            base_text,
            height_text,
            equal_sign,
            frac_text2,
            base_text2,
            height_text2,
        ):
            text.next_to(processed[-1])
            processed.append(text)

        self.play(Write(topic))
        self.play(Write(topic_))
        self.play(FadeOutAndShiftDown(VGroup(topic, topic_)))
        self.play(ShowCreation(triangle))
        self.play(ShowCreation(labels))
        self.play(Write(given_comment))
        self.play(Write(we_have_text))
        self.play(ShowCreation(perp))
        self.play(Write(perp_label))
        self.play(ShowCreation(base))
        self.play(Write(base_label))
        self.play(Write(comment3))
        self.play(Write(area_text))
        self.play(Write(frac_text))
        self.play(ReplacementTransform(base_label, base_text))
        self.play(ReplacementTransform(perp_label, height_text))
        self.play(Write(equal_sign))
        self.play(Write(frac_text2))
        self.play(Write(base_text2))
        self.play(Write(height_text2))
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))
