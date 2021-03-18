from manimlib.imports import *


class Test(GraphScene):

    CONFIG = {
        "x_min": -10,
        "x_max": 10.3,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2),
    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(lambda x: np.cos(x), self.function_color)
        func_graph2 = self.get_graph(lambda x: np.sin(x))
        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
        graph_label = self.get_graph_label(func_graph, label="\\cos(x)")
        graph_label2 = self.get_graph_label(
            func_graph2, label="\\sin(x)", x_val=-10, direction=UP / 2
        )

        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT + UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_label))
        self.play(Write(graph_label2), ShowCreation(two_pi))
        self.wait(3)


class LimitsAndContinuity(PiCreatureScene):
# class Test(PiCreatureScene):

    topic_bubble = None

    def construct(self):
        self.clear()
        self.fore_shadow()
        self.bubble()
        self.topic_anim()

    def fore_shadow(self):
        text = TextMobject("There are different topics that go around calculus.")
        self.play(Write(text), run_time=3)
        self.wait(1)
        self.play(FadeOut(text))

    def bubble(self):
        circle = Circle()
        calculus = TextMobject("Calculus")
        circle.surround(calculus)
        center = VGroup(calculus, circle)
        self.play(FadeIn(center))

        topics = ["Derivatives", "Limits", "Continuity", "Integration"]
        directions = [UL, UR, DR, DL]
        req_bubbles, other_bubbles = [], []
        for topic_text, direction in zip(topics, directions):
            scale_down_factor = 1 - int(len(topic_text) / 3) / 10
            topic = TextMobject(topic_text).scale(scale_down_factor)
            topic_circle = Circle()
            topic_circle.surround(topic)
            topic_ball = VGroup(topic, topic_circle)
            topic_ball.next_to(center, direction, buff=0.5)
            self.play(GrowFromCenter(topic_ball))
            if topic_text == "Limits" or topic_text == "Continuity":
                req_bubbles.append(topic_ball)
            else:
                other_bubbles.append(topic_ball)

        self.topic_bubble = VGroup(*req_bubbles)
        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(center, *other_bubbles)))

    def topic_anim(self):
        topic = TextMobject("Limits and Continuity")
        self.play(ReplacementTransform(self.topic_bubble, topic), run_time=3)
        self.wait(3)
        self.play(FadeOutAndShiftDown(topic))
