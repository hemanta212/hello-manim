from manimlib.imports import *

# class LimitsAndContinuity(PiCreatureScene, GraphScene, MovingCameraScene):
class Test(GraphScene, MovingCameraScene):
    topic_bubble = None
    CONFIG = {
        "y_max": 7,
        "y_min": 0,
        "x_max": 12,
        "x_min": 0,
        "function_color": RED,
        "axes_color": GREEN,

    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)


    def construct(self):
        self.clear()
        # self.fore_shadow()
        # self.bubble()
        # self.topic_anim()
        # self.intro_example()
        self.setup_axes(animate=False)
        # self.graph_draw()
        # self.limits_intro()
        # self.continuous_function_intro()
        # self.continuous_function_example()
        # self.limit_of_a_linear_func()
        # self.linear_func_graph()
        self.clear()
        self.limit_of_a_quad_func()
        # self.quadratic_func_graph()


    def fore_shadow(self):
        text = TextMobject(
            "There are different topics that go around calculus.", color=BLUE
        )
        text.scale(1.2)
        self.play(Write(text), run_time=3)
        self.wait(1)
        self.play(FadeOut(text))

    def bubble(self):
        circle = Circle()
        calculus = TextMobject("Calculus", color=BLUE).scale(1.5)
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
        topic = TextMobject("Limits and Continuity", color=BLUE).scale(1.5)
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
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def make_row(self, texts, buff=1.0):
        txt_objs = [TextMobject(i) for i in texts]
        first = txt_objs[0]
        if len(txt_objs) == 1:
            return VGroup(first)

        processed = [first]
        for text in txt_objs[1:]:
            text.next_to(processed[-1], buff=buff)
            processed.append(text)
        row = VGroup(*processed)
        return row

    def graph_draw(self):
        func_graph = self.get_graph(
            lambda x: np.divide(1, x), x_min=self.x_min, x_max=self.x_max
        )
        label_coord = self.input_to_graph_point(12, func_graph)
        square = Square().move_to(label_coord)

        text = TextMobject(
            "As the value of x increases,",
            " notice the value of y increases,",
            " but never reaches 0,",
            " no matter how large x gets",
        )
        text.arrange(DOWN, center=False)
        text.to_edge(UR)

        conclusion = TextMobject("Here, the ", "limiting", " value of y is 0.")
        conclusion.set_color_by_tex_to_color_map({"limiting": ORANGE})
        conclusion.next_to(text, DOWN, buff=0.5)

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
        self.play(Write(conclusion), run_time=4)
        self.wait(2)
        self.play(FadeOut(VGroup(*self.mobjects)))

    def limits_intro(self):
        text = TextMobject(
            "Limit deals with values that come very close to",
            " each other but never meet.",
        )
        text.arrange(DOWN)
        text.to_edge(UP)

        text2 = TextMobject(
            "Equation of limit is expressed as",
        )
        text2.next_to(text, DOWN, buff=1.0)

        eqn_lim = TexMobject("lim")
        eqn_tends = TexMobject(r"x \rightarrow a")
        eqn_fx = TexMobject("f(x) = I")
        eqn_lim.next_to(text2, DOWN, buff=1.0).shift(LEFT)
        eqn_tends.next_to(eqn_lim, DOWN, buff=0.4)
        eqn_fx.next_to(eqn_lim)
        eqn = VGroup(eqn_lim, eqn_tends, eqn_fx)

        read_as = TextMobject(
            "Above equation is read as,", "As x approaches a, the limit of f(x) is I."
        )
        read_as.arrange(DOWN)
        read_as.to_edge(DOWN)

        self.play(Write(text), run_time=5)
        self.play(Write(text2), run_time=3)
        self.wait()
        self.play(Write(eqn), run_time=5)
        self.play(Write(read_as), run_time=7)
        self.wait(2)
        self.play(FadeOut(VGroup(*self.mobjects)))

    def continuous_function_intro(self):
        defn = TextMobject(
            "Continuous function is",
            "a function having smooth",
        )
        defn.arrange(DOWN).to_edge(UR)
        defn2 = TextMobject(
            "and unbroken flow in its",
            "graphical representation.",
        )
        defn2.arrange(DOWN).to_edge(UR)
        defn2.next_to(defn, DOWN, buff=0.2)

        self.setup_axes(animate=False)
        func_graph = self.get_graph(lambda x: np.sin(x/2))
        func_graph.shift(3 * UP)

        text = TextMobject(
            "You can draw this without lifting your pen.",
        )
        text.next_to(BOTTOM, UP, buff=0.1)

        self.play(Write(VGroup(defn, defn2)), ShowCreation(func_graph), run_time=10)
        self.wait(2)
        self.play(Write(text), run_time=5)
        self.play(FadeOut(VGroup(func_graph, defn, defn2, text)))

    def continuous_function_example(self):
        sine_func = self.get_graph(lambda x: np.sin(x))
        sine_func_test = TextMobject(
            "Lets see if the sine function is continuous..",
        )
        sine_func_test.next_to(BOTTOM, UP, buff=0.2)

        sine_func_conclusion = TextMobject(
            "Turns out it is!", color=ORANGE
        )
        sine_func_conclusion.to_edge(RIGHT)

        self.play(Write(sine_func_test), run_time=5)
        self.wait(2)
        self.play(ShowCreation(sine_func), run_time=3)
        self.wait(2)
        self.play(Write(sine_func_conclusion))
        self.wait(2)
        self.play(FadeOut(VGroup(*self.mobjects)))

    def limit_of_a_linear_func(self):
        topic = TextMobject("Limit of a function", color=BLUE).scale(1.5)

        intro_text = (
            "Lets suppose a function f(x) = 2x + 3, and take a look at its",
            "domain and range represented by x and f(x) respectively.",
        )
        intro = VGroup(*[TextMobject(i) for i in intro_text])
        intro.arrange(DOWN, center=False).to_edge(UL)

        texts = [
            "(x) 2 1.5 1.25 1.1 1.01 1.001 1.0001".split(" "),
            "f(x) 7 6 5.50 5.20 5.02 5.002 5.0002".split(" "),
        ]
        first_row = self.make_row(texts[0])
        second_row = self.make_row(texts[1])
        first_row.next_to(intro, DOWN, buff=2.0).to_edge(LEFT)
        second_row.next_to(first_row, DOWN, buff=0.5).to_edge(LEFT)

        note_text = (
            "Note that the value of x is closing in towards 1 and",
            "the value of f(x) is approaching 5.",
        )
        note = VGroup(*[TextMobject(i) for i in note_text])
        note.arrange(DOWN, center=False).next_to(second_row, DOWN, buff=1.0)

        self.play(Write(topic), run_time=3)
        self.play(FadeOutAndShiftDown(topic))
        self.play(Write(intro), run_time=8)

        for x_val, fx_val in zip(first_row, second_row):
            self.play(Write(x_val))
            self.play(Write(fx_val))
            self.wait()
        self.wait()
        self.play(Write(note), run_time=8)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def limit_of_a_quad_func(self):
        intro_text = (
            "Lets now look at a another function f(x) = $x^2+2$",
            "and take a look at its domain and range",
            "represented by x and f(x) respectively.",
        )
        intro = VGroup(*[TextMobject(i) for i in intro_text])
        intro.arrange(DOWN, center=False).to_edge(UL)

        texts = [
            "(x) 2 1.50 1.25 1.10 1.01 1.001 1.0001".split(" "),
            "f(x) 6 4.25 3.56 3.21 3.02 3.002 3.0002".split(" "),
        ]
        first_row = self.make_row(texts[0])
        second_row = self.make_row(texts[1])
        first_row.next_to(intro, DOWN, buff=1.5).to_edge(LEFT)
        second_row.next_to(first_row, DOWN, buff=0.5).to_edge(LEFT)

        note_text = (
            "Note that the value of x is closing in towards 1 and",
            "the value of f(x) is approaching 3.",
        )
        note = VGroup(*[TextMobject(i) for i in note_text])
        note.arrange(DOWN, center=False).next_to(second_row, DOWN, buff=1.0)

        self.play(Write(intro), run_time=8)
        for x_val, fx_val in zip(first_row, second_row):
            self.play(Write(x_val))
            self.play(Write(fx_val))
            self.wait()
        self.wait()
        self.play(Write(note), run_time=8)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))


    def linear_func_graph(self):
        func_logic = lambda x: 2 * x + 3
        func_graph = self.get_graph(func_logic)
        graph_label = self.get_graph_label(func_graph, label="2x+3")
        initial_line = self.get_vertical_line_to_graph(2.0, func_graph)
        initial_line.set_color(YELLOW)
        start_dot, end_dot = Dot(color=ORANGE), Dot(color=ORANGE)
        start_dot.add_updater(lambda x: x.move_to(initial_line.get_start()))
        end_dot.add_updater(lambda x: x.move_to(initial_line.get_end()))

        x_value = ValueTracker(2)
        fx = lambda x: 2 * x.get_value() + 3
        fx_value = ValueTracker(fx(x_value))

        def update_decimal_x_tex(tex):
            tex.set_value(x_value.get_value())
            tex.next_to(initial_line.get_start(), DOWN)

        def update_decimal_y_tex(tex):
            tex.set_value(fx(x_value))
            tex.next_to(initial_line.get_end(), UP)

        x_tex = DecimalNumber(x_value.get_value()).add_updater(update_decimal_x_tex)
        fx_tex = DecimalNumber(fx_value.get_value()).add_updater(update_decimal_y_tex)

        def update_line(line: Line):
            new_line = self.get_vertical_line_to_graph(x_value.get_value(), func_graph)
            line.set_height(new_line.get_height())
            line.move_to(new_line)

        initial_line.add_updater(update_line)

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_label))
        self.play(
            ShowCreation(initial_line),
            ShowCreation(VGroup(start_dot, end_dot)),
            ShowCreation(VGroup(x_tex, fx_tex)),
        )
        self.play(x_value.set_value, 1, rate_func=rush_from, run_time=5)
        self.wait(3)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))

        
    def quadratic_func_graph(self):
        func_logic = lambda x: x ** 2 + 2
        func_graph = self.get_graph(func_logic)
        graph_label = self.get_graph_label(func_graph, label="x^2+2")
        initial_line = self.get_vertical_line_to_graph(2.0, func_graph)
        initial_line.set_color(YELLOW)
        start_dot, end_dot = Dot(color=ORANGE), Dot(color=ORANGE)
        start_dot.add_updater(lambda x: x.move_to(initial_line.get_start()))
        end_dot.add_updater(lambda x: x.move_to(initial_line.get_end()))

        x_value = ValueTracker(2)
        fx = lambda x: x.get_value() ** 2 + 2
        fx_value = ValueTracker(fx(x_value))

        def update_decimal_x_tex(tex):
            tex.set_value(x_value.get_value())
            tex.next_to(initial_line.get_start(), DOWN)

        def update_decimal_y_tex(tex):
            tex.set_value(fx(x_value))
            tex.next_to(initial_line.get_end(), UP)

        x_tex = DecimalNumber(x_value.get_value()).add_updater(update_decimal_x_tex)
        fx_tex = DecimalNumber(fx_value.get_value()).add_updater(update_decimal_y_tex)

        def update_line(line: Line):
            new_line = self.get_vertical_line_to_graph(x_value.get_value(), func_graph)
            line.set_height(new_line.get_height())
            line.move_to(new_line)

        initial_line.add_updater(update_line)

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_label))
        self.play(
            ShowCreation(initial_line),
            ShowCreation(VGroup(start_dot, end_dot)),
            ShowCreation(VGroup(x_tex, fx_tex)),
        )
        self.play(x_value.set_value, 1, rate_func=rush_from, run_time=5)
        self.wait(3)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))
