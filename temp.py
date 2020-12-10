from manimlib.imports import *


class Test(Scene):
    # placeholder for leaving gap between Mobjects
    GAP = "{{GAP}}"
    saturated_topic = None

    def construct(self):
        self.lab()

    # self.intro()
    # self.saturated_hydrocarbon_intro()

    def lab(self):
        benz = ChemObject("C(-[2]H)(-[4]H)(-[6]H) C(-[2]H)(-[4]H)(-[6]H)")
        benz.to_edge(LEFT)
        self.play(Write(benz))
        self.wait(2)

    def saturated_hydrocarbon_intro(self):
        self.saturated_topic = TextMobject("Saturated hydrocarbons")
        self.saturated_topic.move_to(ORIGIN).to_edge(UP).scale(1.5).set_color(BLUE)
        self.add(self.saturated_topic)

        methane, ethane, butane = "C(-[2]H)(-[4]H)(-[6]H)"

        intro = (
            self.saturated_topic,
            "Those hydrocarbons where all carbon to carbon bonds",
            "are single covalent bond are saturated hydrocarbons",
            "Its general formula is $C_{n}H_{2n+2}$",
        )

        color_map = {
            2: {"single": ORANGE, "covalent": ORANGE, "bond": ORANGE},
            3: {"C": BLUE},
        }

        self.display_simple_info(
            *intro,
            color_map=color_map,
            skip_title_anim=True,
            center=True,
            skip_exit_anim_and_return=[intro[-1]],
        )

    def intro(self):
        intro = (
            "An Introduction to Hydrocarbons",
            self.GAP,
            "Types of hydrocarbons:",
            "$\circ$ Saturated hydrocarbons",
            "$\circ$ Unsaturated hydrocarbons",
        )
        color_map = {
            3: {"Saturated": ORANGE},
            4: {"Unsaturated": ORANGE},
        }

        self.saturated_topic = self.display_simple_info(
            *intro, color_map=color_map, skip_exit_anim_and_return=[3]
        )[0]

        topic = TextMobject("Saturated hydrocarbons")
        topic.move_to(ORIGIN).to_edge(UP).scale(1.5).set_color(BLUE)
        self.play(Transform(self.saturated_topic, topic))

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
        skip_title_anim=False,
        # index of text
        skip_exit_anim_and_return=[],
    ):
        singlify = lambda x: [f"{i} " for i in x.split(" ")]
        texts = []
        for i in args:
            if isinstance(i, str):
                texts.append(TextMobject(*singlify(i)))
            else:
                texts.append(i)
        get_color_map = lambda i: color_map.get(i) if color_map.get(i) else {}

        def get_styled_title(title):
            title = title if skip_title_anim else title.scale(1.5)
            title.to_edge(UP)
            title.set_color(BLUE)
            title.set_color_by_tex_to_color_map(get_color_map(0))
            return title

        title = get_styled_title(texts[0])
        self.play(Write(title), run_time=run_time) if not skip_title_anim else ""

        processed = [title]
        body_texts = texts[1:]
        to_return = [] if not 0 in skip_exit_anim_and_return else [title]

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
            to_return.append(text) if index in skip_exit_anim_and_return else ""
            processed.append(text)

        self.wait(wait_at_last)
        all_objs = [*self.mobjects, *self.foreground_mobjects]
        exitables = set(all_objs) - set(to_return)
        contents = Group(*exitables)
        self.play(exit_animation(contents))
        return to_return
