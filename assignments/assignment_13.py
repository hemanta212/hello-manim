from manimlib.imports import *


class CalculusIntro(PiCreatureScene):
    def construct(self):
        self.clear()
        self.topic_anim()
        self.history()
        self.bubble()
        self.ball_throw()

    def topic_anim(self):
        topic = TextMobject("Calculus: Introduction")
        self.play(Write(topic), run_time=3)
        self.wait(1)
        self.play(FadeOutAndShiftDown(topic))

    def history(self):
        topic = TextMobject("Calculus is a mathematical study of continuous change.")
        topic.to_edge(UL)

        etymo = TextMobject("Calculus is a latin word (plural calculi) meaning 'small")
        etymo2 = TextMobject("pebbles' as they were used for calculation.")
        etymo.next_to(topic, 2 * DOWN)
        etymo.to_edge(LEFT)
        etymo2.next_to(etymo, DOWN, buff=0.3)

        history = TextMobject(
            "Calculus was developed independently around 17th century"
        )
        history2 = TextMobject("by Isaac Newton and G.W Leibniz.")
        history.next_to(etymo2, 2 * DOWN)
        history.to_edge(LEFT)
        history2.next_to(history, DOWN, buff=0.3)

        div = TextMobject(
            "It is studied by dividing into several branches diffrential and"
        )
        div2 = TextMobject("integral calculus being the major ones.")
        div.next_to(history2, 2 * DOWN)
        div.to_edge(LEFT)
        div2.next_to(div, DOWN, buff=0.3)

        self.play(Write(topic))
        self.wait()
        self.play(FadeInFromDown(VGroup(etymo, etymo2), run_time=4))
        self.wait()
        self.play(FadeInFromDown(VGroup(history, history2), run_time=4))
        self.wait()
        self.play(FadeInFromDown(VGroup(div, div2), run_time=4))
        self.wait(3)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def bubble(self):
        circle = Circle()
        calculus = TextMobject("Calculus")
        circle.surround(calculus)
        center = VGroup(calculus, circle)
        self.play(Write(center))

        topics = ["Derivatives", "Limits", "Continuity", "Integration"]
        directions = [UL, UR, DR, DL]
        for topic, direction in zip(topics, directions):
            scale_down_factor = 1 - int(len(topic) / 3) / 10
            topic = TextMobject(topic).scale(scale_down_factor)
            topic_circle = Circle()
            topic_circle.surround(topic)
            topic_ball = VGroup(topic, topic_circle)
            topic_ball.next_to(center, direction, buff=0.5)
            self.play(GrowFromCenter(topic_ball))

        self.wait(2)
        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def ball_throw(self):
        text = TextMobject("Lets consider an example.")
        self.play(Write(text), run_time=3)
        self.play(Uncreate(text))

        self.pi_creature_thinks("...")
        ball = Circle().scale(0.5)
        ball.to_edge(DR)

        self.play(ApplyMethod(ball.shift, 4 * UP, rate_func=rush_from), run_time=3)
        self.play(ApplyMethod(ball.shift, 4 * DOWN, rate_func=rush_into), run_time=2)

        self.say("When did the ball reach the highest point?")
        self.wait(2)
        self.say("How many seconds did it take?")
        text = TextMobject(
            "Calculus consists of techniques to get answer to such questions.",
            color=BLUE,
        )
        text.to_edge(UP)
        self.play(Write(text), run_time=4)
        self.wait(2)
