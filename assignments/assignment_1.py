from manimlib.imports import *


class M1M2Setup(Scene):
    def construct(self):
        m1_body = Circle()
        m1_center = Dot(point=m1_body.get_center())
        m1_text = TexMobject("M_{1}")
        m1 = VGroup(m1_body, m1_center, m1_text)

        m2_body = Circle()
        m2_center = Dot(point=m1_body.get_center())
        m2_text = TexMobject("M_{2}")
        m2 = VGroup(m2_body, m2_center, m2_text)

        line = Line(1.5 * LEFT, 1.5 * RIGHT)
        line_text = TextMobject("R")
        line_text.next_to(line, UP)

        self.play(ShowCreation(m1_body), run_time=3)
        self.add(m1_center)
        self.play(Write(m1_text), run_time=3)
        self.play(m1.to_edge, LEFT)

        self.play(ShowCreation(m2_body), run_time=3)
        self.add(m2_center)
        self.play(Write(m2_text), run_time=3)
        self.play(m2.to_edge, RIGHT)

        self.play(ShowCreation(line))

        self.play(
            ApplyMethod(m1.move_to, line.start),
            ApplyMethod(m2.move_to, line.end),
            run_time=3,
        )

        self.play(
            ApplyMethod(m1_text.next_to, m1, UP),
            ApplyMethod(m2_text.next_to, m2, UP),
            Write(line_text),
            run_time=3,
        )


class SpecialCases(PiCreatureScene):
    def construct(self):
        self.show_formula()
        self.list_cases()

    def show_formula(self):
        formula = TexMobject(r"F = G \frac{M_{1} \cdot M_{2}}{R^2}")
        self.say(formula)
        self.blink()
        self.say("")

    def list_cases(self):
        title = TextMobject("What happens when?")
        cases = [
            "Masses are doubled",
            "Distance is doubled",
            "Both masses and the distance is doubled",
            "Masses are doubled and the distance is halved",
        ]
        title.move_to(2 * RIGHT)
        title.to_edge(UP)
        self.play(Write(title))
        cases_obj = [title]
        for case in cases:
            sentence = TextMobject(case)
            sentence.scale(0.75)
            dot = Dot()
            dot.next_to(sentence, LEFT)
            point = VGroup(sentence, dot)
            point.next_to(cases_obj[-1], DOWN)
            self.play(ReplacementTransform(cases_obj[-1].copy(), point), run_time=2)
            cases_obj.append(point)
        self.think("?")
        self.wait(3)


class Calculation(Scene):
    def construct(self):
        self.mass_doubled()
        self.distance_doubled()
        self.mass_distance_doubled()
        self.mass_doubled_distance_halved()

    def mass_doubled(self):
        title = TextMobject("1. Masses are doubled")
        conditions = [
            r"M_{1} \rightarrow 2 \cdot M_{1}",
            r"M_{2} \rightarrow 2 \cdot M_{2}",
        ]

        self.establish_case(title, conditions)
        cases = [
            r"or, F_{2} = G \frac{2 \times M_{1} \cdot 2 \times M_{2}}{R^2}",
            r"or, F_{2} = 4 \cdot G \frac{M_{1} \cdot M_{2}}{R^2}",
            r"or, F_{2} = 4 \cdot (G \frac{M_{1} \cdot M_{2}}{R^2})",
            r"or, F_{2} = 4 \cdot F",
        ]

        self.show_calculation(cases)

    def distance_doubled(self):
        title = TextMobject("2. Distance between bodies is  doubled")
        conditions = [
            r"R \rightarrow 2 \cdot R",
        ]
        self.establish_case(title, conditions)

        cases = [
            r"or, F_{2} = G \frac{M_{1} \cdot M_{2}}{(2R)^2}",
            r"or, F_{2} = G \frac{M_{1} \cdot M_{2}}{4R^2}",
            r"or, F_{2} = \frac{1}{4} \cdot (G \frac{M_{1} \cdot M_{2}}{R^2})",
            r"or, F_{2} = \frac{1}{4}  \cdot F",
        ]

        self.show_calculation(cases)

    def mass_doubled_distance_halved(self):
        title = TextMobject("4. Masses are doubled but the distance is halved")
        conditions = [
            r"M_{1} \rightarrow 2 \cdot M_{1}",
            r"M_{2} \rightarrow 2 \cdot M_{2}",
            r"R \rightarrow \frac{R}{2}",
        ]

        self.establish_case(title, conditions)
        cases = [
            r"or, F_{2} = G \frac{2 \times M_{1} \cdot 2 \times M_{2}}{(\frac{R}{2})^2}",
            r"or, F_{2} = 4 \cdot G \frac{M_{1} \cdot M_{2}}{\frac{R^2}{4}}",
            r"or, F_{2} = 4 \times 4 \cdot (G \frac{M_{1} \cdot M_{2}}{R^2})",
            r"or, F_{2} = 16 F",
        ]

        self.show_calculation(cases)

    def mass_distance_doubled(self):
        title = TextMobject("3. Both Masses and distance are doubled")
        conditions = [
            r"M_{1} \rightarrow 2 \cdot M_{1}",
            r"M_{2} \rightarrow 2 \cdot M_{2}",
            r"R \rightarrow 2 \cdot R",
        ]

        self.establish_case(title, conditions)
        cases = [
            r"or, F_{2} = G \frac{2 \times M_{1} \cdot 2 \times M_{2}}{(2R)^2}",
            r"or, F_{2} = 4 \cdot G \frac{M_{1} \cdot M_{2}}{4R^2}",
            r"or, F_{2} = 4 \frac{1}{4} \cdot (G \frac{M_{1} \cdot M_{2}}{R^2})",
            r"or, F_{2} = F",
        ]

        self.show_calculation(cases)

    def establish_case(self, title, conditions):
        title.to_edge(UP)
        self.play(Write(title))
        conditions_obj = [title]
        for condition in conditions:
            sentence = TexMobject(condition)
            sentence.next_to(conditions_obj[-1], DOWN, buff=1.0)
            self.play(
                ReplacementTransform(conditions_obj[-1].copy(), sentence), run_time=2
            )
            conditions_obj.append(sentence)
        self.wait(3)
        self.clear()

    def show_calculation(self, steps):
        formula = TexMobject(r"F = G \frac{M_{1} \cdot M_{2}}{R^2}")
        formula.to_edge(UP)
        self.play(Write(formula))
        steps_obj = [formula]
        for step in steps:
            sentence = TexMobject(step)
            sentence.next_to(steps_obj[-1], DOWN, buff=0.5)
            self.play(ReplacementTransform(steps_obj[-1].copy(), sentence), run_time=2)
            steps_obj.append(sentence)
        self.wait(3)
        self.clear()


SCENES_IN_ORDER = [M1M2Setup, SpecialCases, Calculation]
