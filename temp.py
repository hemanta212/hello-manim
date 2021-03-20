from manimlib.imports import *


class LimitsAndContinuity(PiCreatureScene):
    # class Test(PiCreatureScene):

    topic_bubble = None

    def construct(self):
        self.clear()
        self.fore_shadow()
        self.bubble()
        self.topic_anim()
        self.intro_example()

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

    def intro_example(self):
        text1 = TextMobject("Consider an equation y=1/x and look")
        text2 = TextMobject("how y behaves as x increases")
        text1.to_edge(UP)
        text2.next_to(text1, DOWN, buff=0.5)

        self.play(Write(text1), run_time=3)
        self.play(Write(text2), run_time=3)
        # self.play(FadeOutAndShiftDown(VGroup(text1, text2)))

        texts = [
            ("x", "y"),
            ("1", "1"),
            ("2", "1/2"),
            ("3", "1/3"),
        ]
        ellipsis = TextMobject("...")
        first_row = self.make_row(texts[0])
        first_row.next_to(text2, DOWN, buff=2.0)  # .to_edge(LEFT)
        proof_lines = [first_row]
        for text in texts[1:]:
            row = self.make_row(text)
            row.next_to(proof_lines[-1], DOWN, buff=0.5)  # .to_edge(LEFT)
            proof_lines.append(row)

        for line in proof_lines:
            self.play(Write(line), run_time=3)

        ellipsis.next_to(proof_lines[-1])
        self.play(FadeIn(ellipsis))
        self.wait(3)

    def make_row(self, texts):
        txt_objs = [TextMobject(i) for i in texts]
        first = txt_objs[0]
        if len(txt_objs) == 1:
            return VGroup(first)

        processed = [first]
        for text in txt_objs[1:]:
            text.next_to(processed[-1], buff=1.0)
            processed.append(text)
        row = VGroup(*processed)
        return row


class Test(GraphScene, MovingCameraScene):
    CONFIG = {
        "graph_origin": ORIGIN,
        "y_max": 50,
        "y_min": 0,
        "x_max": 5,
        "x_min": 0,
        "y_tick_frequency": 5,
        "x_tick_frequency": 0.5,
        "function_color": RED,
        "axes_color": GREEN,
    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.graph_draw()

    def graph_draw(self):
        self.setup_axes(animate=False)
        func_graph = self.get_graph(
            lambda x: np.divide(1, x), x_min=self.x_min, x_max=self.x_max
        )
        # vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
        graph_label = self.get_graph_label(func_graph, label="1/x")
        label_coord = self.input_to_graph_point(2.8, func_graph)
        square = Square().move_to(label_coord)

        text = TextMobject(
            "As the value of x increases,",
            " notice the value of y increases,",
            " but never reaches 0,",
            " no matter how large x gets",
        )
        text.arrange(DOWN, center=False)
        text.to_edge(DL)

        self.play(ShowCreation(func_graph), Write(text), run_time=10)
        
        # Save the state of camera
        self.camera_frame.save_state()
        self.play(
            self.camera_frame.set_height,
            square.get_width() * 1.2,
            self.camera_frame.move_to,
            square,
            run_time=5,
        )
        self.wait(2)
        # Restore the state saved
        self.play(Restore(self.camera_frame))

        self.wait(2)
