from manimlib.imports import *


class Test(Scene):
    # A palceholder string for denoting to leave gaps in places
    GAP = "{{GAP}}"

    def construct(self):
        self.intro()
        self.parts_of_thermometer()
        self.thermometric_liquids()
        self.clinical_thermometer()
        self.laboratory_thermometer()
        self.min_max_thermometer()

    def intro(self):
        topic = TextMobject("Thermometer")
        image = ImageMobject("thermometer.jpg")
        desc = TextMobject("A device which is designed to measure temperature.")
        image.scale(2.0)
        topic.scale(1.5)
        desc.next_to(image, DOWN)
        self.play(Write(topic))
        self.play(FadeOut(topic), FadeIn(image), run_time=3)
        self.play(Write(desc))
        self.wait(2)
        self.play(FadeOutAndShiftDown(desc), FadeOutAndShiftDown(image))

    def parts_of_thermometer(self):
        intro = ("Parts of thermometer",)
        self.display_simple_info(
            *intro, image="labelled_thermometer.jpg", wait_at_last=3.0
        )

    def thermometric_liquids(self):
        intro = (
            "Thermometric Liquids",
            self.GAP,
            "Liquids used in the thermometer to ",
            "measure the temperature.",
            self.GAP,
            "Examples of thermometric liquids;",
            "1. Mercury",
            "2. Alcohol",
        )
        color_map = {
            2: {"in": ORANGE, "the": ORANGE, "thermometer": ORANGE},
            6: {"Mercury": BLUE},
            7: {"Alcohol": ORANGE},
        }
        self.display_simple_info(*intro, color_map=color_map, center=True)

    def clinical_thermometer(self):
        intro = (
            "Clinical thermometer",
            self.GAP,
            "Range of temperature:",
            "$\circ$ Celsius: 35$^{\circ}$C to 42$^{\circ}$C",
            "$\circ$ Fahrenheit: 94$^{\circ}$F to 108$^{\circ}$F",
            self.GAP,
            "It is used to measure the temperature",
            "of the human body.",
        )
        color_map = {
            3: {"35": ORANGE, "42": ORANGE},
            4: {"94": ORANGE, "108": ORANGE},
            7: {"human": BLUE, "body": BLUE},
        }
        self.display_simple_info(
            *intro, image="clinical.jpg", image_scale=2.0, color_map=color_map
        )

    def laboratory_thermometer(self):
        intro = (
            "Laboratory thermometer",
            self.GAP,
            "Range of temperature:",
            "$\circ$ –10$^{\circ}$C to 100$^{\circ}$C",
            self.GAP,
            "It is used for laboratory purposes.",
        )
        color_map = {
            3: {"10": ORANGE, "100": ORANGE},
        }
        self.display_simple_info(
            *intro, image="laboratory.jpg", image_scale=2.0, color_map=color_map
        )

    def min_max_thermometer(self):
        intro = (
            "Maximum and Minimum thermometer",
            self.GAP,
            "$\circ$ Used by meteorologist to understand",
            "the temperature of the day.",
            "$\circ$ Used to record the extremes of",
            "temperature at a location.",
        )

        self.display_simple_info(
            *intro,
            image="max_min_thermometer.jpg",
            image_scale=2,
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
        body_texts = texts[1:]

        if image:
            image_ = ImageMobject(image).scale(image_scale)
            image_ = image_.to_edge(RIGHT) if body_texts else image_
            self.add(image_)

        for index, text in enumerate(texts[1:]):
            index += 1
            is_gap = text.tex_string.strip() == self.GAP
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
