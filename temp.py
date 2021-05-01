from manimlib.imports import *


class Test(Scene):
    event_text = None

    def construct(self):
        self.intro()
        self.probability_terms()
        self.events_intro()
        self.sample_space_intro()

    def intro(self):
        text = TextMobject("Probability", color=BLUE)
        text.scale(1.5).to_edge(UP)

        intro = (
            "The probability of an event is a measure of the likelihood ",
            "that it will happen."
        )
        intro_text = VGroup(*[TextMobject(i) for i in intro])
        intro_text.arrange(DOWN, center=False).shift(UP)

        self.play(Write(text))
        self.wait(1)
        self.play(Write(intro_text), run_time=8)
        self.wait(3)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))


    def probability_terms(self):
        title = TextMobject("Terms used in Probability", color=BLUE).scale(1.5).to_edge(UP)
        self.play(Write(title), run_time=3)

        types = (
            "Lets understand some of the terms used in calculating",
            "probability.",
            "1. Events",
            "2. Sample Space",
        )
        types_text = VGroup(*[TextMobject(i) for i in types])
        types_text.arrange(DOWN, center=False).shift(UP)

        events, sample_space = types_text[-2], types_text[-1]
        events.to_edge(LEFT)
        sample_space.to_edge(LEFT)

        fadeouts = VGroup(*types_text[:2], sample_space)
        self.event_text = events
        self.play(Write(types_text), run_time=8)
        self.play(FadeOut(title), FadeOut(fadeouts))

    def events_intro(self):
        title = TextMobject("Events", color=BLUE).scale(1.5).to_edge(UP)

        text = (
            "Event is a set of possible outcomes of an experiment.",
            "Some examples of events are toss of coin, roll of a dice, ",
            "and lottery draws.",
        )
        text_g = VGroup(*[TextMobject(i) for i in text])
        text_g.arrange(DOWN, center=False).shift(UP)

        self.play(ReplacementTransform(self.event_text, title))
        self.play(Write(text_g), run_time=10)
        self.wait(3)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))

    def sample_space_intro(self):
        title = TextMobject("Sample Space", color=BLUE).scale(1.5).to_edge(UP)

        text = (
            "Sample space is a set of all possible outcomes of an experiment.",
            "Tossing a coin and getting a head is an event whereas",
            "the sample space will be head and tails (all possile",
            "outcomes of a coin toss).",
        )
        text_g = VGroup(*[TextMobject(i) for i in text])
        text_g.arrange(DOWN, center=False).shift(UP)

        self.play(Write(title))
        self.play(Write(text_g), run_time=10)
        self.wait(3)
        self.play(FadeOutAndShiftDown(Group(*self.mobjects)))
