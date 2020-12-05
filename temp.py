from manimlib.imports import *


class Test(Scene):
    def construct(self):
        #        img = SVGMobject("thermometer.svg")
        #        self.play(DrawBorderThenFill(img, rate_func=linear))
        self.thermometric_liquids()

    def thermometric_liquids(self):
        intro = (
            "Thermometric Liquid",
            "Liquid that are use inside thermometer are called",
            "thermometeric liquid",
        )
        self.display_simple_info(*intro)

    def display_simple_info(
        self,
        *args,
        scale=1.0,
        exit_animation=FadeOutAndShiftDown,
        spacing=0.5,
        run_time=3,
        wait_at_last=1.0
    ):
        texts = [TextMobject(i) for i in args]
        title = texts[0]
        title.to_edge(UP)
        title.set_color(BLUE)
        self.play(Write(title), run_time=3)
        self.wait()

        processed = [title]
        for text in texts[1:]:
            text.next_to(processed[-1], DOWN, buff=spacing)
            text.scale(scale)
            self.play(Write(text), run_time=run_time)
            processed.append(text)

        self.wait(wait_at_last)
        all_texts = Group(*processed)
        self.play(exit_animation(all_texts))


SCENES_IN_ORDER = [Test]
