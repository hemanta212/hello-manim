from manimlib.imports import *


class Test(PiCreatureScene):
    def construct(self):
        self.clear()
        # self.topic_anim()
        # self.history()
        #self.demo()
        # self.bubble()
        self.test()

    def test(self):
        topic = TextMobject("Calculus: Introduction")
        dot = Line()
        dot.next_to(topic, RIGHT)

        temp = []
        tester = lambda x: x.set_angle(len(temp))
        dot.add_updater(tester)
        self.add(topic, dot)


    def topic_anim(self):
        topic = TextMobject("Calculus: Introduction")
        self.play(Write(topic), run_time=3)
        self.wait(1)
        self.play(FadeOutAndShiftDown(topic))

    def history(self):
        topic = TextMobject("Calculus is a branch of mathematics that deals with")
        topic2 = TextMobject("non linear change.")
        topic.to_edge(UL)
        topic2.next_to(topic, DOWN).to_edge(LEFT)

        self.play(Write(topic))
        self.play(Write(topic2))
        self.wait()

    def demo(self):
        ball = Circle(color=RED).scale(0.5)
        falling_arc = ArcBetweenPoints(
            ORIGIN + (0, 2, 0),
            (BOTTOM + RIGHT_SIDE) + UP,
            angle=-PI / 2,
            start_angle=TAU / 4,
        )
        self.play(MoveAlongPath(ball, falling_arc), run_time=10)
        self.say("hello")
        self.wait()
 
    def bubble(self):
        circle = Circle()
        calculus = TextMobject("Calculus")
        circle.surround(calculus)
        center = VGroup(calculus, circle)
        self.play(Write(center))

        topics = ["Derivatives", "Limits", "Continuity", "Integration"]
        directions = [UL, UR, DR, DL]
        bubbles = []
        for topic, direction in zip(topics, directions):
            scale_down_factor = 1 - int( len(topic) / 3) / 10 
            topic = TextMobject(topic).scale(scale_down_factor)
            topic_circle = Circle()
            topic_circle.surround(topic)
            topic_ball = VGroup(topic, topic_circle)
            topic_ball.next_to(center, direction, buff=0.5)
            bubbles.append(topic_ball)
            self.play(GrowFromCenter(topic_ball))

        bubble_g = VGroup(*bubbles)
        rotations = (Rotate(bubble, rate_fun=linear) for bubble in bubble_g)
        self.play(Rotate(bubble_g, rate_func=linear), *rotations, run_time=5)
        self.wait(2)
