from manimlib.imports import *


class Test(Scene):
    def construct(self):
        self.thermometric_liquids()
        # self.clinical_thermometer()
        # self.intro()

    def intro(self):
        topic = TextMobject("Thermometer")
        image = ImageMobject("thermometer.jpg")
        desc = TextMobject("A device used to measure temperature")
        topic.scale(1.5)
        desc.next_to(image, DOWN)
        self.play(Write(topic))
        self.play(ApplyMethod(topic.next_to, image, 2 * UP))
        self.play(ShowCreation(image))
        self.play(Write(desc))
        self.wait(2)

    def thermometric_liquids(self):
        GAP = "{{GAP}}"
        intro = (
            "Thermometric Liquids",
            GAP,
            "Liquids that are used inside thermometer are called",
            "thermometeric liquids.",
            GAP,
            "Examples of thermometric liquids;",
            "1. Mercury",
            "2. Alcohol",
        )
        color_map = {
            2: {"inside": ORANGE, "thermometer": ORANGE},
            6: {"Mercury": BLUE},
            7: {"Alcohol": ORANGE},
        }
        self.display_simple_info(*intro, color_map=color_map, center=True)

    def laboratory_thermometer(self):
        intro = [
            "Clinical thermometer",
            "Range of temperature.",
            "- Celsius: 35$^{\circ}$C to 42$^{\circ}$C",
            "- Fahrenheit: 94$^{\circ}$F to 108$^{\circ}$F",
            "It is used to measure the temperature",
            "of the human body.",
        ]
        color_map = {
            2: {"35": ORANGE, "42": ORANGE},
            3: {"94": ORANGE, "108": ORANGE},
            5: {"human": BLUE, "body": BLUE},
        }
        self.display_simple_info(
            *intro, image="clinical.jpg", image_scale=2.0, color_map=color_map
        )

    def clinical_thermometer(self):
        GAP = "{{GAP}}"
        intro = [
            "Clinical thermometer",
            GAP,
            "Range of temperature:",
            "- Celsius: 35$^{\circ}$C to 42$^{\circ}$C",
            "- Fahrenheit: 94$^{\circ}$F to 108$^{\circ}$F",
            GAP,
            "It is used to measure the temperature",
            "of the human body.",
        ]
        color_map = {
            3: {"35": ORANGE, "42": ORANGE},
            4: {"94": ORANGE, "108": ORANGE},
            7: {"human": BLUE, "body": BLUE},
        }
        self.display_simple_info(
            *intro, image="clinical.jpg", image_scale=2.0, color_map=color_map
        )

    def display_simple_info(
        self,
        *args,
        scale=1.0,
        color_map={},
        image=None,
        image_scale=1.0,
        exit_animation=FadeOutAndShiftDown,
        spacing=0.5,
        run_time=3,
        center=False,
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

        if image:
            image_ = ImageMobject(image).to_edge(RIGHT)
            image_.scale(image_scale)
            self.add(image_)

        body_texts = texts[1:]
        for index, text in enumerate(texts[1:]):
            index += 1
            is_gap = text.tex_string.strip() == "{{GAP}}"
            text.next_to(processed[-1], DOWN, buff=spacing)
            text = text.to_edge(LEFT) if not center else text
            text.scale(scale)
            text.set_color_by_tex_to_color_map(get_color_map(index))
            text = text.set_color(BLACK) if is_gap else text
            self.play(Write(text), run_time=run_time) if not is_gap else print("")
            processed.append(text)

        self.wait(wait_at_last)
        contents = Group(*self.mobjects, *self.foreground_mobjects)
        self.play(exit_animation(contents))


SCENES_IN_ORDER = [Test]
