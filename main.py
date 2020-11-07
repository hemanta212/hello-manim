#!/usr/bin/env python3

from manimlib.imports import *


class ProjectileMotion(Scene):

    luffy_narrator = None
    nami_narrator = None
    luffy_voice = None
    luffy_arm = None
    nami_voice = None

    def construct(self):
        self.intro()
        self.platformAndLuffy()
        self.luffyNamiConversation()
        self.clear()
        self.outro()

    def outro(self):
        text = TextMobject("Manim  X OnePiece")
        text.set_color_by_gradient(PURPLE, BLUE, GREEN, ORANGE, RED)
        self.play(Write(text))
        self.play(ApplyMethod(text.scale, 2))
        self.wait(3)

    def intro(self):
        title = TextMobject("Manim Training Assignment 01")
        title.set_color(RED)
        title.to_edge(UP)

        presentedStr = TextMobject("Presented by")
        presentedStr.set_color(YELLOW)

        author = TextMobject("- Hemanta Sharma")
        author.scale(0.75)
        author.next_to(title.get_corner(DOWN + RIGHT), DOWN)

        self.add(title)
        self.wait(2)

        self.play(
            Transform(title, presentedStr),
            ApplyMethod(
                author.move_to, presentedStr.get_corner(DOWN + RIGHT) + DOWN + 2 * LEFT
            ),
        )
        self.wait(1)

        self.play(ApplyMethod(author.scale, 1.5))
        author.match_color(presentedStr)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(author))

    @staticmethod
    def make_stick_man():
        BOTTOM_LEFT = BOTTOM + LEFT_SIDE
        body_line = Line(
            BOTTOM_LEFT + RIGHT,
            BOTTOM_LEFT + RIGHT + 2 * UP,
        )
        head_circle = Circle(radius=0.5)
        head_circle.move_to(body_line.end)
        stickman = VGroup(body_line, head_circle)
        return stickman

    def luffyEnters(self):
        self.luffy = self.make_stick_man()
        self.add(self.luffy)
        self.play(FadeIn(self.luffy))

        self.luffy_narrator = NarratorBubble(
            next_to=(self.luffy, UP + RIGHT), scale=0.75
        )
        self.luffy_voice = self.luffy_narrator.speak("hi, everyone")

        self.play(FadeIn(self.luffy_voice))

        voice2 = self.luffy_narrator.speak("I am luffy,", "a rubber man")
        self.play(Transform(self.luffy_voice, voice2))
        self.wait(2)

        voice3 = self.luffy_narrator.speak("Don't believe?", "Let me stretch")
        self.play(Transform(self.luffy_voice, voice3))
        self.wait(2)
        self.play(FadeOut(self.luffy_voice))

    def platformAndLuffy(self):
        BOTTOM_LEFT = BOTTOM + LEFT_SIDE
        arm_line = Line(
            BOTTOM_LEFT,
            BOTTOM_LEFT + 2 * UP,
        )
        fist_circle = Circle(radius=0.5)

        platform_line = Line()
        platform_ball = Circle(radius=0.5)

        arm_line.set_angle(PI / 4)
        fist_circle.next_to(arm_line, UP + RIGHT)

        self.luffy_arm = VGroup(arm_line, fist_circle)

        platform_line.move_to(1.4 * UP)
        platform_ball.next_to(platform_line, UP)

        falling_arc = ArcBetweenPoints(
            ORIGIN + (0.5, 2, 0),
            BOTTOM + RIGHT_SIDE,
            angle=-PI / 2,
            start_angle=TAU / 4,
        )
        self.luffyEnters()
        self.play(
            ShowCreation(platform_line),
            ShowCreation(platform_ball),
        )
        arm_line.set_length(arm_line.get_length() + 16)
        fist_circle.next_to(arm_line, UP + RIGHT)

        self.luffy_narrator = NarratorBubble(
            next_to=(self.luffy, UP + RIGHT), scale=0.75
        )
        self.luffy_voice = self.luffy_narrator.speak("Gomu Gomu no", "pistol")
        self.luffy_voice.rotate(PI / 4)
        self.play(
            GrowFromEdge(self.luffy_arm, arm_line.start),
            FadeIn(self.luffy_voice),
            run_time=3,
        )
        self.play(MoveAlongPath(platform_ball, falling_arc))

    def luffyNamiConversation(self):
        self.nami_narrator = NarratorBubble(next_to=(RIGHT_SIDE, LEFT), scale=0.75)

        self.nami_voice = self.nami_narrator.speak("Oe luffy captain,")
        self.play(FadeOut(self.luffy_arm))
        luffy_voice = self.luffy_narrator.speak("oh! oe Nami...")

        self.play(FadeIn(self.nami_voice), run_time=2)
        self.play(
            Transform(self.luffy_voice, luffy_voice),
            run_time=2,
        )

        nami_voice2 = self.nami_narrator.speak(
            "The ball you threw", "was a projectile!"
        )
        luffy_voice2 = self.luffy_narrator.speak("Nani!", "(what!)")
        self.play(
            Transform(self.nami_voice, nami_voice2),
            run_time=4,
        )
        self.play(
            Transform(self.luffy_voice, luffy_voice2),
            run_time=2,
        )

        nami_voice3 = self.nami_narrator.speak(
            "It has trajectory",
            "$ y = x \\tan(\\theta) - \\frac{gx^{2}}{ {2v_{0}}^{2} cos^ {2}\\theta}$",
        )
        nami_voice3.set_color_by_gradient(RED, ORANGE, BLUE, PURPLE)
        luffy_voice3 = self.luffy_narrator.speak("????", "Nanda kurea?")
        self.play(
            Transform(self.nami_voice, nami_voice3),
            run_time=4,
        )
        self.play(
            Transform(self.luffy_voice, luffy_voice3),
            run_time=2,
        )

        nami_voice4 = self.nami_narrator.speak("What is so hard", "about that?")
        luffy_voice4 = self.luffy_narrator.speak("Oh! I got it", "It's a mystery ball")
        self.play(
            Transform(self.nami_voice, nami_voice4),
            run_time=4,
        )
        self.play(
            Transform(self.luffy_voice, luffy_voice4),
            run_time=2,
        )

        nami_voice5 = self.nami_narrator.speak("Aaho sencho", "(Stupid captain)")
        self.play(
            Transform(self.nami_voice, nami_voice5),
            run_time=4,
        )


class NarratorBubble:
    def __init__(self, next_to=(ORIGIN,), scale=1.0):
        self.position = next_to
        self.scale = scale

    def speak(self, *args):
        messages = []
        for text in args:
            msg = TextMobject(text)
            msg.scale(self.scale)
            if messages:
                msg.next_to(messages[-1], DOWN)
            messages.append(msg)

        message = VGroup(*messages)
        bubble = Ellipse()
        bubble.surround(message)
        voice = VGroup(message, bubble)
        voice.next_to(*self.position)
        return voice
