from manimlib.imports import *


class Test(Scene):
    GAP = "{{GAP}}"

    def construct(self):
        self.intro()

    def lab(self):
        benz = ChemObject("-(-[1]O^{-})=[7]O")
        self.play(Write(benz))
        self.wait(2)

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

        saturated = self.display_simple_info(
            *intro, color_map=color_map, skip_exit_anim_and_return=[3]
        )[0]

        target = saturated.generate_target()
        target.move_to(ORIGIN).to_edge(UP)
        self.play(MoveToTarget(saturated))
        self.play(ScaleInPlace(saturated, 1.5))

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
        # index of text
        skip_exit_anim_and_return=[],
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
