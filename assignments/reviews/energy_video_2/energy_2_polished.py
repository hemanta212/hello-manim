from manimlib.imports import *


class Energy(GraphScene):
    CONFIG = {
        "y_max": 100,
        "y_min": 0,
        "x_max": 100,
        "x_min": 0,
        "y_tick_frequency": 10,
        "x_tick_frequency": 10,
        "y_axis_label": "Energy Consumption",
        "x_axis_label": "Population",
        "axes_color": BLUE,
        "include_tip": True,
    }

    def construct(self):
        self.energy_intro_pop()
        self.energy_population_graph()
        self.explain()

    def energy_intro_pop(self):
        askpop = TextMobject(
            "Do you know what population growth leads to?",
            "You guessed it! Industrialization. But what does it lead to?",
            "As population increases, so does the energy consumption.",
        )
        askpop.arrange(DOWN, buff=1)
        askpop[0].set_color(TEAL_E)
        askpop[1].set_color(YELLOW_D).scale(0.9)
        askpop[2].set_color(BLUE)
        self.play(Write(askpop[0]), run_time=3)
        self.wait(2)
        for i in range(1, len(askpop)):
            self.play(ReplacementTransform(askpop[i - 1].copy(), askpop[i]), run_time=3)
            self.wait(2)
        self.play(Indicate(askpop[2]))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def energy_population_graph(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x: x, color=RED_D, x_min=0, x_max=90)
        self.play(ShowCreation(graph), run_time=4)
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def explain(self):
        evidence = TexMobject(
            r"Research \ shows \ 75 \ percentage \ of \ energy \ consumption \ is \ non-renewable \ energy.",
            r"This \ is \ leading \ to \ energy \ crisis.",
            r"Non-renewable \ sources \ of \ energy \ might \ be \ extinct \ in \ 25-31 \ years.",
            r"What \ can \ be \ done?",
        )
        evidence.scale(0.7)
        evidence.arrange(DOWN, buff=1)
        evidence[0].set_color(PURPLE_A)
        self.play(Write(evidence[0]), run_time=3)
        self.wait(2)
        for i in range(1, len(evidence)):
            arrow = Arrow(
                evidence[i - 1].get_center() + DOWN * 0.1,
                evidence[i].get_center() + UP * 0.1,
                color=ORANGE,
            )
            evidence[i].set_color(PURPLE_A)
            self.play(ShowCreation(arrow))
            self.wait()
            self.play(
                ReplacementTransform(evidence[i - 1], evidence[i]), FadeOut(arrow)
            )
            self.wait(4)
        self.remove(evidence[3])
        self.wait()
        sun = ImageMobject("sun_image.png")
        sun.scale(0.8)
        header = TextMobject(
            "Use renewable sources of energy which are generally derived from sources found in nature. One example is the energy produced by the Sun."
        ).scale(0.8)
        footer = (
            TextMobject(
                "Use other alternative sources of energy like Biogas, Hydropower, Electrical energy, etc."
            )
            .scale(0.8)
            .set_color(GOLD_D)
        )
        footer2 = TextMobject("SAVE ENERGY!").scale(0.8).set_color(BLUE_E)
        footers = VGroup(footer, footer2)
        footers.arrange(DOWN, buff=0.5)
        header.set_color_by_gradient(BLUE_A, YELLOW_C, RED_C, PINK)
        header.to_edge(UP)
        self.play(Write(header), run_time=5)
        self.wait()
        self.play(GrowFromCenter(sun))
        self.play(Rotating(sun), run_time=3)
        self.remove(sun)
        self.play(FadeInFromDown(footer), run_time=3)
        self.wait(5)
        self.play(Write(footer2))
        self.play(Indicate(footer2))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))
