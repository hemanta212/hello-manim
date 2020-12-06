from manimlib.imports import *


class Test(Scene):
    def construct(self):
        #        img = SVGMobject("thermometer.svg")
        #        self.play(DrawBorderThenFill(img, rate_func=linear))
        # self.thermometric_liquids()
        self.clinical_thermometer()

    def thermometric_liquids(self):
        intro = (
            "Thermometric Liquids",
            "Liquids that are used inside thermometer are called",
            "thermometeric liquids.",
            "Examples of thermometric liquids,",
            "1. Mercury",
            "2. Alcohol",
        )
        color_map = {
            1: {"inside": ORANGE, "thermometer": ORANGE},
            5: {"Alcohol": ORANGE},
            4: {"Mercury": BLUE},
        }
        self.display_simple_info(*intro, color_map=color_map)

    def clinical_thermometer(self):
        intro = [
            "Clinical thermometer: (SVG image of the thermometer)",
            "Range of temperature.",
            "Degree Celsius: 35 to 42",
            "Degree Fahrenheit: 94 to 108",
            "It is used to measure the temperature of the human body.",
        ]
        color_map = {}
        self.display_simple_info(*intro, image="test.svg")

    def display_simple_info(
        self,
        *args,
        scale=1.0,
        color_map={},
        image=None,
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
            title.set_color_by_tex_to_color_map(get_color_map(0))
            return title

        title = get_styled_title(texts[0])
        self.play(Write(title), run_time=run_time)

        processed = [title]

        body_texts = texts[1:]
        if image:
            svg_image = SVGMobject(image).to_edge(RIGHT)
            body_texts = [image, body_texts]

        paragraphs = VGroup(*body_texts).arrange(DOWN)
        paragraphs.insert(svg_image, 0)
        for index, text in enumerate(texts[1:]):
            index += 1
            text.next_to(processed[-1], DOWN, buff=spacing)
            text.scale(scale)
            text.set_color_by_tex_to_color_map(get_color_map(index))
            self.play(Write(text), run_time=run_time)
            processed.append(text)

        self.wait(wait_at_last)
        all_texts = Group(*processed)
        self.play(exit_animation(all_texts))


SCENES_IN_ORDER = [Test]
