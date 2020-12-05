from manimlib.imports import *


class Test(Scene):
    def construct(self):
        #        img = SVGMobject("thermometer.svg")
        #        self.play(DrawBorderThenFill(img, rate_func=linear))
        self.thermometric_liquids()

    def thermometric_liquids(self):
        intro = (
            "Thermometric Liquids",
            "Liquids that are used inside thermometer are called",
            "thermometeric liquids",
        )
        color_map = {1: {"inside": ORANGE, "thermometer": ORANGE}}
        self.display_simple_info(*intro, color_map=color_map)

    def display_simple_info(
        self,
        *args,
        scale=1.0,
        color_map={},
        exit_animation=FadeOutAndShiftDown,
        spacing=0.5,
        run_time=3,
        wait_at_last=1.0,
    ):
        singlify = lambda x: [f"{i} " for i in x.split(" ")]
        texts = [TextMobject(*singlify(i)) for i in args]
        get_color_map = lambda i: color_map.get(i) if color_map.get(i) else {}

        def get_styled_title(title):
            title.scale(1.5)
            title.to_edge(UP)
            title.set_color(BLUE)
            return title

        processed = []
        for index, text in enumerate(texts):
            if not index == 0:
                text.next_to(processed[-1], DOWN, buff=spacing)
                text.to_edge(LEFT)
            text.scale(scale)
            text = get_styled_title(text) if index == 0 else text
            text.set_color_by_tex_to_color_map(get_color_map(index))
            self.play(Write(text), run_time=run_time)
            processed.append(text)

        self.wait(wait_at_last)
        all_texts = Group(*processed)
        self.play(exit_animation(all_texts))


SCENES_IN_ORDER = [Test]
