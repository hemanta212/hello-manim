from manimlib.imports import *


class Test(TeacherStudentsScene, Scene):
    def construct(self):
        self.wait(2)
        Text1 = TextMobject("What will we study today, Teacher?")
        Text1.scale(1.8).set_color(RED)
        self.student_says(Text1)
        self.wait(2)

        Text2 = TextMobject("Today we will study about Probability and its Principles")
        Text2.scale(1.8).set_color(MAROON)
        self.teacher_says(Text2)
        self.wait(2)
        self.clear()
        self.wait(2)

        topic = TextMobject("Probability")
        topic.scale(1.5).set_color_by_gradient(RED, BLUE, GREEN)
        self.play(GrowFromCenter(topic), run_time=3, rate_func=rush_into)
        self.play(ApplyMethod(topic.shift, 3.5 * UP))
        self.wait(2)

        text3 = TextMobject(
            "Probability is a branch of mathematics which deals with the likelihood of an event or circumstance through numbers."
        )
        text3.scale(0.8).set_color(PURPLE).align_to(LEFT)

        self.play(Write(text3), run_time=3)
        self.play(ApplyMethod(text3.shift, 2 * UP))
        self.wait(2)

        text4 = TextMobject("Probability ranges its value from 0 to 1. 0")
        text4.scale(1.2).set_color(GREEN).align_to(LEFT).move_to(DOWN * 0.5)
        self.play(FadeIn(text4), run_time=3)
        self.wait(2)
        self.play(Uncreate(text3), run_time=2)
        self.wait()

        self.play(ApplyMethod(text4.shift, 2 * UP), run_time=2)
        self.wait(2)
        self.teacher_says("0 indicates impossibility ")
        self.wait(2)
        self.student_says(" What does 1 indicate teacher?")
        self.wait(2)
        self.teacher_says("1 indicates full possibility/certainty")
        self.wait(2)
        self.play(FadeOut(text4), run_time=2)
        self.wait(2)

        self.teacher_says("Now let's learn Principles of Probability")
        self.wait(2)
        self.clear()
        self.wait(2)

        topic1 = TextMobject("Principles of Probability")
        topic1.scale(1.5).set_color_by_gradient(RED, BLUE, GREEN)
        self.play(GrowFromCenter(topic1), run_time=3, rate_func=rush_into)
        self.play(ApplyMethod(topic1.shift, 3.5 * UP))
        self.wait(2)

        text5 = TextMobject(
            "We use addition, multiplication, and complement rules to calculate probability of an event(s) or an outcome(s). "
        )
        text5.scale(0.8).set_color(BLUE).align_to(LEFT).move_to(UP * 2)
        self.play(Write(text5), run_time=4)
        self.wait(2)
        self.clear()
        self.wait(2)

        topic2 = TextMobject("Mutually Exclusive Events")
        topic2.scale(1.5).set_color_by_gradient(RED, YELLOW, GREEN)
        self.play(GrowFromCenter(topic2), run_time=3, rate_func=rush_into)
        self.play(ApplyMethod(topic2.shift, 3.5 * UP))
        self.wait(2)

        text6 = TextMobject(
            "If two events cannot occur at a same time, they are said to be mutually exclusive. "
        )
        text6.scale(0.8).set_color(GREEN).align_to(LEFT).move_to(UP * 2)
        self.play(Write(text6), run_time=4)
        self.wait(2)
        self.play(Uncreate(text6), run_time=2)
        self.wait(2)

        text7 = TextMobject(
            "Let A and B be two mutually exclusive events. As stated earlier, their probability of occurrence at the same time is 0."
        )
        text7.scale(0.8).set_color(GREEN).align_to(LEFT).move_to(UP * 2)
        self.play(Write(text7), run_time=4)
        self.wait(2)

        """
        probimg = ImageMobject("prob1")
        probimg.move_to(DOWN * 0.5).scale(1.2)
        self.play(FadeIn(probimg), run_time=2)
        self.wait(2)
        self.play(Uncreate(text7), run_time=2)
        self.wait(2)
        self.play(FadeOut(probimg), run_time=2)
        self.wait(2)
        self.clear()

        text8 = TextMobject(" Example of Mutually Exclusive Events ")
        text8.scale(1.5).set_color_by_gradient(RED, YELLOW, BLUE)
        self.play(GrowFromCenter(text8), run_time=3, rate_func=rush_into)
        self.play(ApplyMethod(text8.shift, 3.5 * UP))
        self.wait(2)

        text9 = TextMobject(
            " 1. Getting multiple(s) of 2 and multiple(s) of 5 after rolling an unbiased dice 2 times respectively. "
        )
        text9.scale(0.8).set_color(GREEN).align_to(LEFT).move_to(UP * 2)
        self.play(Write(text9), run_time=2)
        self.wait(2)

        Given2 = TexMobject(
            r" Here,\ Possible\ of\ outcomes/sample\ space\  = \left \{1, 2, 3, 4, 5, 6   \right \} ",
            r" Event\ A: Multiples\ of\ 2 = \left \{ 2, 4, 6 \right \}",
            r" Event\ B: Multiple\ of\ 5 = \left \{ 5 \right \}",
            r" Since\ both\ the\ events\ don't\ have\ any\ common\ outcome,\ they\ are\ mutually\ exclusive",
        )

        Given2.arrange(DOWN)
        Given2.scale(0.7)
        Given2.set_color(BLUE)
        for x in range(0, len(Given2)):

            self.play(Write(Given2[x]), run_time=3)
            self.wait(2)
        self.wait(2)
        self.clear()
        self.wait()
        """
