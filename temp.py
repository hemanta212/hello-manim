from manimlib.imports import *


class Test(Scene):
    # placeholder for leaving gap between Mobjects
    GAP = "{{GAP}}"
    alkene_topic = None
    general_formula = None

    def construct(self):
        self.unsaturated_hydrocarbon_intro()
        self.alkene_intro()
        self.alkene_mol_formulas()
        self.alkene_examples()
        self.alkyne_intro()
        self.alkyne_mol_formulas()
        self.alkyne_examples()

    def unsaturated_hydrocarbon_intro(self):
        intro = (
            "Unsaturated Hydrocarbons",
            "Those hydrocarbons where all carbon to carbon bonds are",
            "double or triple covalent bonds are unsaturated hydrocarbons",
            "Types of unsaturated hydrocarbons:",
            "1. Alkenes",
            "2. Alkynes",
        )

        color_map = {
            2: {
                "double": ORANGE,
                "or": ORANGE,
                "triple": ORANGE,
                "covalent": ORANGE,
                "bond": ORANGE,
            },
            4: {"Alkenes": BLUE},
            5: {"Alkynes": BLUE},
        }

        self.alkene_topic = self.display_simple_info(
            *intro,
            color_map=color_map,
            skip_exit_anim_and_return=[4],
        )[0]

        new_alkene_title = TextMobject("Alkenes", color=BLUE).scale(1.5)
        new_alkene_title.to_edge(UP)
        self.play(Transform(self.alkene_topic, new_alkene_title))
        self.wait()

    def alkene_intro(self):
        intro = (
            self.alkene_topic,
            "Those hydrocarbons in which at least one carbon to carbon",
            "bond is double covalent bond while the rest maybe double",
            "or single covalent bonds are called alkenes.",
            "Its general formula is $C_{n}H_{2n}$ where n>1",
        )

        color_map = {
            1: {"at": ORANGE, "least": ORANGE, "one": ORANGE},
            2: {"double": ORANGE, "covalent": ORANGE},
            4: {"C": BLUE, "n>1": ORANGE},
        }

        self.general_formula = self.display_simple_info(
            *intro,
            color_map=color_map,
            skip_title_anim=True,
            center=True,
            skip_exit_anim_and_return=[i for i in range(len(intro))],
        )[-1]

    def alkene_mol_formulas(self):
        self.molecular_formula = TextMobject("Molecular formulas;")
        self.molecular_formula.next_to(self.general_formula, DOWN, buff=0.6).to_edge(
            LEFT
        )
        self.play(Write(self.molecular_formula))
        gen_formula = (
            "C_n",
            "H_{2n}",
        )
        ethene = [
            "ethene",
            "take n = 2",
            gen_formula,
            ("C_2", "H_{2 \\times 2}"),
            ("C_2", "H_{4},"),
        ]
        propene = [
            "propene",
            "take n = 3",
            gen_formula,
            ("C_3", "H_{2 \\times 3}"),
            ("C_3", "H_{6},"),
        ]
        butene = [
            "butene",
            "take n = 4",
            gen_formula,
            ("C_4", "H_{2 \\times 4}"),
            ("C_4", "H_{8},"),
        ]

        processed = []
        for molecule in (ethene, propene, butene):
            last_molecule = processed[-1] if processed else None
            formula = self.show_molecular_animations(molecule, last_molecule)
            processed.append(formula)

        self.wait()
        all_contents = Group(*self.mobjects)
        self.play(FadeOutAndShiftDown(all_contents))

    def alkene_examples(self):
        title = TextMobject("Some basic alkenes")

        ethene = (
            TextMobject("1. Ethene"),
            TextMobject("2"),
            TexMobject("C_2H_4"),
            TexMobject("CH_2=CH_2"),
            # ChemObject("C(-[2]H)(-[4]H)(-[6]H)-C(-[2]H)(-[6]H)(-[8]H)"),
            TexMobject(r"\chemfig{C(-[2]H)(-[6]H)=C(-[2]H)(-[6]H)}"),
        )
        propene = (
            TextMobject("2. Propene"),
            TextMobject("3"),
            TexMobject("C_3H_6"),
            TexMobject("CH_2=CH_2-CH_3"),
            # ChemObject("C(-[2]H)(-[4]H)(-[6]H)-C(-[2]H)(-[6]H)-C(-[2]H)(-[6]H)(-[8]H)"),
            TexMobject(r"\chemfig{C(-[2]H)(-[6]H)=C(-[2]H)-C(-[2]H)(-[6]H)(-[8]H)}"),
        )
        butene = (
            TextMobject("3. Butene"),
            TextMobject("4"),
            TexMobject("C_4H_8"),
            TexMobject("CH_3-CH=CH-CH_3"),
            TexMobject(
                "\chemfig{C(-[2]H)(-[4]H)(-[6]H)-C(-[2]H)=C(-[2]H)-C(-[2]H)(-[6]H)(-[8]H)}"
            ),
        )
        title.set_color(BLUE).scale(1.5)
        title.to_edge(UP)
        self.play(Write(title))
        [
            self.display_properties(i, relative_to=title)
            for i in (ethene, propene, butene)
        ]
        self.play(FadeOut(title))

    def alkyne_intro(self):
        intro = (
            "Alkynes",
            "Those hydrocarbons in which at least one carbon to carbon",
            "bond is triple covalent bond while the rest maybe triple,",
            "double or single covalent bonds are called alkynes.",
            "Its general formula is $C_{n}H_{2n-2}$ where n>1",
        )

        color_map = {
            1: {"at": ORANGE, "least": ORANGE, "one": ORANGE},
            2: {"triple": ORANGE, "covalent": ORANGE},
            4: {"C": BLUE, "n>1": ORANGE},
        }

        self.general_formula = self.display_simple_info(
            *intro,
            color_map=color_map,
            center=True,
            skip_exit_anim_and_return=[i for i in range(len(intro))],
        )[-1]

    def alkyne_mol_formulas(self):
        self.molecular_formula = TextMobject("Molecular formulas;")
        self.molecular_formula.next_to(self.general_formula, DOWN, buff=0.6).to_edge(
            LEFT
        )
        self.play(Write(self.molecular_formula))
        gen_formula = (
            "C_n",
            "H_{2n-2}",
        )
        ethyne = [
            "ethyne",
            "take n = 2",
            gen_formula,
            ("C_2", "H_{2 \\times 2 - 2}"),
            ("C_2", "H_{2},"),
        ]
        propyne = [
            "propyne",
            "take n = 3",
            gen_formula,
            ("C_3", "H_{2 \\times 3 - 2}"),
            ("C_3", "H_{4},"),
        ]
        butyne = [
            "butyne",
            "take n = 4",
            gen_formula,
            ("C_4", "H_{2 \\times 4 - 2}"),
            ("C_4", "H_{6},"),
        ]

        processed = []
        for molecule in (ethyne, propyne, butyne):
            last_molecule = processed[-1] if processed else None
            formula = self.show_molecular_animations(molecule, last_molecule)
            processed.append(formula)

        self.wait()
        all_contents = Group(*self.mobjects)
        self.play(FadeOutAndShiftDown(all_contents))

    def alkyne_examples(self):
        title = TextMobject("Some basic alkynes")

        ethyne = (
            TextMobject("1. Ethyne"),
            TextMobject("2"),
            TexMobject("C_2H_2"),
            # ChemObject("CH~CH"),
            TexMobject("CH~CH"),
            # ChemObject("C(-[2]H)~C(-[2]H)"),
            TexMobject(r"\chemfig{C(-[2]H)~C(-[2]H)}"),
        )
        propyne = (
            TextMobject("2. Propyne"),
            TextMobject("3"),
            TexMobject("C_3H_4"),
            # ChemObject("CH_2=CH_2-CH_3"),
            TexMobject("CH~C-CH_3"),
            # ChemObject("C(-[2]H)~C-C(-[2]H)(-[6]H)(-[8]H)"),
            TexMobject(r"\chemfig{C(-[2]H)~C-C(-[2]H)(-[6]H)(-[8]H)}"),
        )
        butyne = (
            TextMobject("3. Butyne"),
            TextMobject("4"),
            TexMobject("C_4H_6"),
            # ChemObject("CH_3-C~C-CH_3"),
            TexMobject("CH_3-C~C-CH_3"),
            # ChemObject("C(-[2]H)(-[4]H)(-[6]H)-C~C-C(-[2]H)(-[6]H)(-[8]H)"),
            TexMobject(r"\chemfig{C(-[2]H)(-[4]H)(-[6]H)-C~C-C(-[2]H)(-[6]H)(-[8]H)}"),
        )
        title.set_color(BLUE).scale(1.5)
        title.to_edge(UP)
        self.play(Write(title))
        [
            self.display_properties(i, relative_to=title)
            for i in (ethyne, propyne, butyne)
        ]
        self.play(FadeOut(title))

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
            self.molecular_formula, DOWN, buff=0.6
        )
        target = (
            target.next_to(last_molecule, buff=1.5)
            if last_molecule
            else target.to_edge(LEFT)
        )
        self.play(MoveToTarget(formula), FadeOut(let_part))
        formula_label.next_to(formula, DOWN, buff=0.3)
        self.play(Write(formula_label))
        return formula

    def display_properties(self, properties, relative_to=None):
        name, c_atoms, mol_formula, cond_formula, structure = properties
        name.next_to(relative_to, DOWN, buff=1.0)
        name.to_edge(LEFT).set_color(ORANGE)
        self.play(Write(name))

        text_map = {
            "$\circ$ Carbon atoms:": c_atoms,
            "$\circ$ Molecular formula:": mol_formula,
            "$\circ$ Condensed formula:": cond_formula,
        }

        property_groups = [name]
        for text, prop in text_map.items():
            label = (
                TextMobject(text)
                .next_to(property_groups[-1], DOWN, buff=0.6)
                .to_edge(LEFT)
            )
            arrow = Arrow(color=YELLOW_C).scale(0.5)
            arrow.next_to(label, DOWN).to_edge(LEFT)
            prop.next_to(arrow)
            property_ = VGroup(arrow, prop)
            self.play(Write(label))
            self.play(Write(property_))
            property_groups.append(VGroup(label, property_))

        structure.next_to(name, DOWN).move_to(RIGHT_SIDE / 3)
        self.play(Write(structure))
        contents = [*property_groups, structure]
        contents_group = VGroup(*contents)
        self.wait(3)
        self.play(FadeOutAndShiftDown(contents_group))

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
