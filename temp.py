from manimlib.imports import *


class Test(Scene):

    def construct(self):
        topic = TextMobject("Area of Right angled triangle", color=BLUE).scale(1.5)

        triangle = Polygon(
            LEFT,
            LEFT + UP,
            RIGHT,
        )
        triangle.scale(1.5)
        A, B, C = triangle.get_vertices()

        label_a, label_b, label_c = (TextMobject(i) for i in "A B C".split())
        label_a.next_to(A, LEFT)
        label_b.next_to(B, UP, buff=0.3)
        label_c.next_to(C)
        labels = VGroup(label_a, label_b, label_c)

        given_comment = TextMobject(r"In the given triangle, $\triangle$ ABC,")
        we_have_text = TextMobject(r"We have, $\angle BAC = 90^{\circ}$")
        given_comment.to_edge(UL)
        we_have_text.next_to(given_comment, DOWN, buff=0.3).to_edge(LEFT)

        square = Polygon(
            A + 0.2 * UP,
            A + 0.2 * UR,
            A + 0.2 * RIGHT,
            A,
            color = YELLOW)

        height = DashedLine(B, A, color=YELLOW)
        height_label = TexMobject("height")
        height_label.next_to(height, LEFT, buff=0.2)
        
        base = Line(A, C, color=ORANGE)
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

        perp = DashedLine(B, A, color=YELLOW)
        perp_label = TexMobject("perpendicular")
        perp_label.next_to(perp, LEFT, buff=0.2)
        base_label_ = TexMobject("base")
        base_label_.next_to(triangle, DOWN)
      
        comment4 = TextMobject(
            r"Notice, in $\triangle$ ABC, AB = perpendicular(p) and AC = base(b)"
        )
        area_text3 = TextMobject("Area(A) = ")
        frac_text3 = TexMobject(r"\frac{1}{2} ")
        perp_text3 = TextMobject(r"perpendicular $\times$")
        base_text3 = TextMobject("base")
        equal_sign2 = TextMobject("=")
        frac_text4 = TexMobject(r"\frac{1}{2} ")
        perp_text4 = TextMobject(r"p $\cdot$")
        base_text4 = TextMobject("b")
        area_text3.to_edge(DOWN).to_edge(LEFT)
        comment4.next_to(area_text3, UP, buff=0.6).to_edge(LEFT)

        processed2 = [area_text3]
        for text in (
            frac_text3,
            perp_text3,
            base_text3,
            equal_sign2,
            frac_text4,
            perp_text4,
            base_text4,
        ):
            text.next_to(processed2[-1])
            processed2.append(text)


        self.play(Write(topic))
        self.play(FadeOutAndShiftDown(topic))
        self.play(ShowCreation(triangle))
        self.play(ShowCreation(labels))
        self.play(Write(given_comment))
        self.play(Write(we_have_text))
        self.play(ShowCreation(square))
        self.play(ShowCreation(height))
        self.play(Write(height_label))
        self.play(ShowCreation(base))
        self.play(Write(base_label))
        self.play(Write(comment3))
        self.play(Write(area_text))
        self.play(Write(frac_text))
        self.play(ReplacementTransform(base_label, base_text))
        self.play(ReplacementTransform(height_label, height_text))
        self.play(Write(equal_sign))
        self.play(Write(frac_text2))
        self.play(Write(base_text2))
        self.play(Write(height_text2))
        self.play(FadeOut(VGroup(base, height)),
                  FadeOutAndShiftDown(VGroup(comment3, *processed)))
        self.wait(2)
        self.play(Write(comment4))
        self.play(ShowCreation(perp))
        self.play(Write(perp_label))
        self.play(ShowCreation(base))
        self.play(Write(base_label_))
        self.play(Write(area_text3))
        self.play(Write(frac_text3))
        self.play(ReplacementTransform(perp_label, perp_text3))
        self.play(ReplacementTransform(base_label_, base_text3))
        self.play(Write(equal_sign2))
        self.play(Write(frac_text4))
        self.play(Write(perp_text4))
        self.play(Write(base_text4))
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))
