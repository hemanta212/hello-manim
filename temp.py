from manimlib.imports import *


class Test(Scene):
    # placeholder for leaving gap between Mobjects
    GAP = "{{GAP}}"
    last_sentence = None
    general_formula = None

    def construct(self):
        # self.homologous_defn()
        # self.homologous_expln()
        self.alkyl_radical_intro()
        self.alkyl_radical_anim()

    def alkyl_radical_anim(self):
        gen_formula = self.general_formula

        methane = TexMobject("\chemfig{C(-[2]H)(-[4]H)(-[6]H)(-[8]H)}")
        methane.next_to(gen_formula, DOWN).to_edge(LEFT).scale(0.80)
        label = TextMobject("$CH_4$ (alkane)")
        label.next_to(methane, DOWN, buff=0.5)
        self.play(Write(methane))
        self.play(Write(label))

        methane_radical = TexMobject("\chemfig{C(-[2]H)(-[4]H)(-[6]H)}")
        methane_radical.next_to(methane, buff=3.0).scale(0.80)
        label = TextMobject("$CH_3^+$ (alkyl radical)")
        label.next_to(methane_radical, DOWN, buff=0.5)

        bond = Line().scale(0.5)
        h_label = TexMobject("H")
        h_label.next_to(bond, buff=0.1)
        h_bond_g = VGroup(bond, h_label)
        h_bond_g.next_to(methane_radical, buff=0.1)

        ion_circle = Circle()
        ion = TexMobject("+")
        ion_circle.surround(ion)
        positive_ion = VGroup(ion_circle, ion)
        positive_ion.next_to(methane_radical, buff=0.5)

        methane_radical_g = VGroup(methane_radical, h_bond_g)
        self.play(ReplacementTransform(methane.copy(), methane_radical_g))
        self.play(
            FadeOutAndShiftDown(h_bond_g),
            FadeInFrom(positive_ion, UP),
            run_time=3,
        )
        self.play(Write(label))
        self.wait(2)

        self.play(FadeOutAndShiftDown(VGroup(*self.mobjects)))

    def alkyl_radical_intro(self):
        intro = (
            "Alkyl Radicals",
            "The group of atoms obtained after removing single H atom",
            "from alkanes are called alkyl radicals. It is commonly denoted",
            "by R. Its general formula is $C_nH_{2n+1}$.",
        )

        color_map = {
            1: {
                "group": ORANGE,
                "of": ORANGE,
                "atoms": ORANGE,
            },
            2: {
                "from": ORANGE,
                "alkanes": ORANGE,
            },
            3: {
                "R": ORANGE,
                "C": ORANGE,
            },
        }

        self.general_formula = self.display_simple_info(
            *intro,
            color_map=color_map,
            spacing=0.3,
            skip_exit_anim_and_return=[i for i in range(len(intro))],
        )[-1]
        self.wait()

    def homologous_expln(self):
        last_sentence = self.last_sentence

        methane = TexMobject("CH_4")
        label = TextMobject("Methane")
        label.next_to(methane, DOWN)
        methane_g = VGroup(methane, label)
        methane_g.next_to(last_sentence, DOWN, buff=1.5).to_edge(LEFT)
        self.play(Write(methane))
        self.play(Write(label))

        new_methane = methane.copy().next_to(methane, buff=2.0).shift(UP)
        ch2_part = TexMobject("+ CH_2", color=ORANGE).next_to(new_methane, DOWN)
        line = Line().scale(0.5)
        line.next_to(ch2_part, DOWN)
        self.play(ReplacementTransform(methane.copy(), new_methane))
        self.play(Write(ch2_part), FadeIn(line))

        ethane = TexMobject("C_2H_6")
        ethane.next_to(line, DOWN)
        label = TextMobject("Ethane")
        label.next_to(ethane, DOWN)
        self.play(Write(ethane))
        self.play(Write(label))

        new_ethane = ethane.copy().next_to(new_methane, buff=2.0)
        ch2_part = TexMobject("+ CH_2", color=ORANGE).next_to(new_ethane, DOWN)
        line = Line().scale(0.5)
        line.next_to(ch2_part, DOWN)
        self.play(ReplacementTransform(ethane.copy(), new_ethane))
        self.play(Write(ch2_part), FadeIn(line))

        propane = TexMobject("C_3H_8")
        propane.next_to(line, DOWN)
        label = TextMobject("Propane")
        label.next_to(propane, DOWN)
        self.play(Write(propane))
        self.play(Write(label))

        new_propane = propane.copy().next_to(new_ethane, buff=2.0)
        ch2_part = TexMobject("+ CH_2", color=ORANGE).next_to(new_propane, DOWN)
        line = Line().scale(0.5)
        line.next_to(ch2_part, DOWN)
        self.play(ReplacementTransform(propane.copy(), new_propane))
        self.play(Write(ch2_part), FadeIn(line))

        butane = TexMobject("C_4H_{10}")
        butane.next_to(line, DOWN)
        label = TextMobject("Butane")
        label.next_to(butane, DOWN)
        self.play(Write(butane))
        self.play(Write(label))

        comment = TextMobject(
            "Notice how above elements have same general formula i.e. ",
            " $C_nH_{2n+2}$",
        ).set_color_by_tex("C", ORANGE)
        comment.scale(0.90).next_to(label, DOWN, buff=0.2).to_edge(LEFT)

        self.play(Write(comment), run_time=3)
        self.wait(2)

    def homologous_defn(self):
        intro = (
            "Homologous series",
            "A series of organic compounds that can be represented by",
            "same general formula is called homologous series.",
            "Succesive elements in this series differ by a $CH_2$ group.",
        )

        color_map = {
            2: {
                "same": ORANGE,
                "general": ORANGE,
                "formula": ORANGE,
            },
            3: {
                "CH": ORANGE,
            },
        }

        self.last_sentence = self.display_simple_info(
            *intro,
            color_map=color_map,
            skip_exit_anim_and_return=[i for i in range(len(intro))],
        )[-1]
        self.wait()

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
