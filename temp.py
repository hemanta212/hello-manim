from manimlib.imports import *


class Test(Scene):
    # placeholder for leaving gap between Mobjects
    GAP = "{{GAP}}"
    saturated_topic = None
    general_formula = None
    molecular_formula = None

    def construct(self):
        self.lab()

    def staturated_intro(self):
        self.intro()
        self.saturated_hydrocarbon_intro()
        self.saturated_hydrocarbon_mol_formulas()

    def lab(self):
        title = TextMobject("Word root for saturated hydrocarbons")
        first_row = [
            ("No. of", "C atoms"),
            "Name",
            ("Mol.", "formula"),
            "Structure",
        ]
        carbon_atoms_col = [
            "No. of C atoms",
            "1",
            "2",
        ]

        a = [
            "Symbol"
            "",
            "Methane",
            TexMobject(r"CH_4"),
            TexMobject("\chemfig{C(-[0]H)(-[2]H)(-[4]H)(-[6]H)}")
        ]
        b = [
            "Symbol",
            "$C_1$",
            "$C_2$",
            "$C_3$",
            "$C_4$",
            "$C_5$",
            "$C_6$",
        ]
        c = [
            "Word root",
            "Meth",
            "Eth",
            "Prop",
            "But",
            "Pent",
            "Hex",
        ]
        title.set_color(BLUE)
        title.to_edge(UP)
        first_row_group = self.makeColGroup(first_row)
        first_row_group.next_to(title, DOWN, buff=1.0).to_edge(LEFT).shift(RIGHT)
        b_ = self.makeColGroup(b)
        b_.next_to(first_row_group, buff=1.0)
        self.play(Write(title))
        self.play(Write(first_row_group))
        self.play(Write(b_))

        c_ = self.makeColGroup(c)
        c_.next_to(b_, buff=1.0)
        self.play(Write(c_))

        self.wait(4)



    def labi(self):
        first_row = [
            ("No. of", "C atoms"),
            "Name",
            ]
        a = TextMobject(first_row[1])
        b = TextMobject("Rajukoghar")
        c = TextMobject("Lado chusera bas")
        b.next_to(a, DOWN)
        c.next_to(b, DOWN)
        g = VGroup(a,b,c)
        g.to_edge(UL)

        aq = TextMobject(first_row[1])
        ce = TextMobject("Rajukoghar")
        bw = TextMobject("Lado chusera bas")
        bw.next_to(aq, DOWN)
        ce.next_to(bw, DOWN)
        gg = VGroup(aq,bw,ce)
        gg.next_to(g, buff=0.5)
        self.play(Write(g), Write(gg))

    def word_roots_table(self):
        title = TextMobject("Word root for saturated hydrocarbons")
        carbon_atoms_col = [
            "No. of C atoms",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
        ]
        symbol_col = [
            "Symbol",
            "$C_1$",
            "$C_2$",
            "$C_3$",
            "$C_4$",
            "$C_5$",
            "$C_6$",
        ]
        word_root_col = [
            "Word root",
            "Meth",
            "Eth",
            "Prop",
            "But",
            "Pent",
            "Hex",
        ]

        title.set_color(BLUE)
        title.to_edge(UP)
        carbon_atoms = self.makeColGroup(carbon_atoms_col)
        carbon_atoms.next_to(title, DOWN, buff=1.0).to_edge(LEFT).shift(RIGHT)
        symbols = self.makeColGroup(symbol_col)
        symbols.next_to(first_row_group, buff=1.0)
        word_roots = self.makeColGroup(word_root_col)
        word_roots.next_to(symbols, buff=1.0)

        self.play(Write(title))
        self.play(Write(carbon_atoms))
        self.play(Write(symbols))
        self.play(Write(word_roots))
        self.wait(4)

    def makeColGroup(self, texts, tex_class=TextMobject, spacing=0.5, text_scale=1.0):
        text_objects = []
        for text in texts:
            obj = None
            if isinstance(text, str):
                singlify = lambda x: [f"{i} " for i in x.split(" ")]
                obj = TextMobject(*singlify(text))
            elif isinstance(text, TexMobject):
                obj = text
            elif isinstance(text, tuple):
                objects = [tex_class(i) for i in text]
                processed = [objects[0]]
                for i in objects[1:]:
                    i.next_to(processed[-1], DOWN, buff=0.2)
                    processed.append(i)
                obj = VGroup(*processed)
            else:
                AssertionError(f"Unsupported type of {type(text)}: {text}")

            obj.scale(text_scale)
            text_objects.append(obj)

        first = text_objects[0]
        processed = [first]
        for obj in text_objects[1:]:
            obj.next_to(processed[-1], DOWN, buff=spacing)
            processed.append(obj)

        return VGroup(*processed)

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

        topic = TextMobject("Saturated Hydrocarbons")
        topic.move_to(ORIGIN).to_edge(UP).scale(1.5).set_color(BLUE)
        self.play(Transform(self.saturated_topic, topic))

    def saturated_hydrocarbon_intro(self):
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

        self.general_formula = self.display_simple_info(
            *intro,
            color_map=color_map,
            skip_title_anim=True,
            center=True,
            skip_exit_anim_and_return=[i for i in range(len(intro))],
        )[-1]

    def saturated_hydrocarbon_mol_formulas(self):
        self.molecular_formula = TextMobject("Molecular formulas;")
        self.molecular_formula.next_to(self.general_formula, DOWN, buff=1.0).to_edge(
            LEFT
        )
        self.play(Write(self.molecular_formula))
        gen_formula = (
            "C_n",
            "H_{2n+1}",
        )
        methane = [
            "methane",
            "take n = 1",
            gen_formula,
            ("C_1", "H_{2 \\times 1 + 2}"),
            ("C", "H_{4},"),
        ]

        ethane = [
            "ethane",
            "take n = 2",
            gen_formula,
            ("C_2", "H_{2 \\times 2 + 2}"),
            ("C_2", "H_{6},"),
        ]
        butane = [
            "butane",
            "take n = 4",
            gen_formula,
            ("C_4", "H_{2 \\times 4 + 2}"),
            ("C_4", "H_{10},"),
        ]

        processed = []
        for molecule in (methane, ethane, butane):
            last_molecule = processed[-1] if processed else None
            formula = self.show_molecular_animations(molecule, last_molecule)
            processed.append(formula)

    def show_molecular_animations(self, molecule, last_molecule):
        processed = []
        formula = None

        molecule_name, let, *sequences = molecule
        singlify = lambda x: [f"{i} " for i in x.split(" ")]
        let_part = TextMobject(*singlify(let))
        let_part.set_color_by_tex_to_color_map(
            {"n": ORANGE, "1": ORANGE, "2": ORANGE, "4": ORANGE}
        )
        formula_label = TextMobject(molecule_name)

        for index, formulas in enumerate(sequences):
            C_part, H_part = (TexMobject(i).set_color(BLUE) for i in formulas)
            let_part.next_to(self.molecular_formula, RIGHT)
            C_part.next_to(let_part, RIGHT, buff=1)
            H_part.next_to(C_part, RIGHT, buff=0.0)
            formula = VGroup(C_part, H_part)
            if not index:
                self.play(Write(let_part))
                self.play(ReplacementTransform(self.general_formula.copy(), formula))
            else:
                self.play(
                    ReplacementTransform(processed[index - 1], formula), run_time=2
                )
            processed.append(formula)
            self.wait()

        target = formula.generate_target().next_to(
            self.molecular_formula, DOWN, buff=1.0
        )
        target = (
            target.next_to(last_molecule, buff=1.5)
            if last_molecule
            else target.to_edge(LEFT)
        )
        self.play(MoveToTarget(formula), FadeOut(let_part))
        formula_label.next_to(formula, DOWN, buff=0.5)
        self.play(Write(formula_label))
        return formula

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
