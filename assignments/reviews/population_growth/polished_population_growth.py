# what is more beautiful than objects moving by my programmatic expression of will
from manimlib.imports import *
import json


class PopGrowth(GraphScene):
    CONFIG = {
        "x_min": 1950,
        "x_max": 1975,
        "x_axis_width": 9,
        "y_min": 0,
        "y_max": 40,
        "graph_origin": [-5, -2.5, 0],
        "function_color": RED,
        "axes_color": GREEN,
        "x_tick_frequency": 10,  # this is literally for showing the tick on the screen
        "y_tick_frequency": 5,
        "area_opacity": 5,
        "x_axis_label": "Year",
        "y_axis_label": "Population",
    }

    def construct(self):
        self.pv = 0
        self.prev = 0
        data1 = {}
        data2 = {}

        with open("data-nepal-pop.json", "r") as f:
            data1 = json.load(f)
        with open("data-nepal-pop-projected.json", "r") as f:
            data2 = json.load(f)

        popData = data1 + data2
        popData = popData[1:]
        self.stats = {}

        years = []

        for index in range(len(popData)):
            each = popData[index]
            self.stats[each["Year"]] = float(each["TotalPopulation"]) / 1000
            years.append(each["Year"])

        years = sorted(years)

        self.fstats = {}

        for index in range(len(popData)):
            each = years[index]
            self.fstats[index] = self.stats[each]

        self.first()
        # self.graphs()
        self.graph2()
        self.formula()
        self.lformula()

    def lformula(self):
        t1 = (
            TexMobject(
                "\\text{However, sometimes, we might encounter problems with separate growth rate for each individual year. ",
                "In that case, if } R(1), R(2), R(3) ... R(t) \\text{ be the rates of growth of } 1^\\text{st}, 2^\\text{nd}, 3^\\text{rd}, ... T^\\text{th} \\text{ different years:}",
            )
            .scale(0.6)
            .arrange(DOWN, aligned_edge=LEFT)
            .shift([0, 2, 0])
        )

        for each in t1:
            self.play(Write(each, run_time=7))
            self.wait()

        eqn = TexMobject(
            "P=",
            "P_0 ",
            "(1 + \\frac{R(1)}{100}) ",
            "(1 + \\frac{R(2)}{100}) ",
            "(1 + \\frac{R(3)}{100}) ",
            "...",
            "(1 + \\frac{R(t)}{100}) ",
        )

        self.play(Write(eqn, run_time=5))
        self.wait()

    def formula(self):
        t1 = (
            TextMobject(
                "Now, what are the formulas that will enable you to calculate the population growth, or population depreciation over the course of time?"
            )
            .scale(0.8)
            .shift([0, 2, 0])
        )
        t2 = VGroup(
            TexMobject(
                "\\text{Suppose a town has a }",
                " \\text{total population } (P_0) ",
                "\\text{ of now and is subjected to have a }",
                " \\text{growth rate of } (R)",
                " \\text{ for years } (T).}",
            ).scale(0.55),
            TexMobject(
                "\\text{The final }",
                "\\text{population } (P)",
                "\\text{ of the town after T years can be represented by the formulae:}",
            ).scale(0.55),
        ).arrange(DOWN, aligned_edge=LEFT)
        t2[0][1].set_color(RED)
        t2[0][3].set_color(YELLOW)
        t2[0][4].set_color(GREEN)
        t2[1][1].set_color(BLUE)

        self.play(Write(t1, run_time=8))
        self.wait()

        for each in t2:
            self.play(Write(each, run_time=8))
            self.wait(2)

        self.wait(2)

        formula = TexMobject("P ", "", "= P_0 ", "(1 + \\frac{R}{100})^T ", "").shift(
            [0, -1.5, 0]
        )
        formula2 = TexMobject(
            "P ", "- P_0", "= P_0 (1 + \\frac{R}{100})^T", "- P_0"
        ).shift([0, -0.5, 0])

        self.play(Write(formula, run_time=3))
        self.wait()
        self.remove(t1)
        for each in t2:
            self.remove(each)

        t3 = (
            TextMobject(
                "If the population is subjected to decrease after T years, the rate must be negative."
            )
            .scale(0.8)
            .shift([0, 2, 0])
        )
        t4 = TextMobject("For the decreased population:").scale(0.8).shift([0, 1, 0])

        self.play(Write(t3, run_time=5))
        self.play(Write(t4))
        self.wait()

        self.play(formula.shift, [0, 1, 0])
        self.play(ReplacementTransform(formula, formula2))
        self.wait()
        self.wait()
        self.clear()

    def graph2(self):
        """
        Attempted to make a graph in manim but failed--will try again in the future.
        For now, using the image from the document
        """

        img = ImageMobject("pop-graph").scale(3.4)
        self.add(img)
        self.wait()
        self.wait()

        # self.play(img.scale, 0.5)
        self.play(img.shift, [0, 2, 0])
        self.wait()

        t1 = TextMobject(
            "The population of Nepal according to World Population Review has been changing from years earlier, and is predicted to change for years to come."
        ).scale(0.8)
        t1.shift([0, -2, 0])
        self.play(Write(t1, run_time=8))
        self.wait(2)
        self.remove(t1)
        self.play(img.shift, [0, -2, 0])
        self.wait()
        self.clear()

        t1 = (
            TextMobject(
                "But did you know that we can actually calculate this change with simple mathematical formulas you have been learning?"
            )
            .scale(0.8)
            .shift([0, 3, 0])
        )
        t2 = TextMobject(
            "Before we dive into formulas, let me introduce you to some basic terms associated with population growth."
        ).scale(0.8)

        self.play(Write(t1, run_time=8))
        self.wait()
        self.play(Write(t2, run_time=8))
        self.wait()
        self.clear()

        terms = VGroup(
            TexMobject("\\text{Initial Population } (P_0)").set_color(RED),
            TexMobject("\\text{Final Population } (P)").set_color(BLUE),
            TexMobject("\\text{Growth Rate } (R)").set_color(GREEN),
            TexMobject("\\text{Time Interval } (T)").set_color(YELLOW),
        ).arrange(DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)

        for each in terms:
            self.play(FadeIn(each, RIGHT))
            self.wait()

        self.wait()
        self.play(FadeOutAndShift(terms))

    def ftg(self, x):
        print(x)
        x = int(x)
        val = 0

        try:
            val = self.stats[x]
            self.pv += val
            self.prev = 5
        except:
            val = self.pv + self.prev
            self.prev += 5

        # print(self.pv, x, val)

        return val

    def graphs(self):
        self.setup_axes(animate=False)

        self.x_axis.shift(
            LEFT * abs(self.y_axis[0].points[0] - self.x_axis[0].points[0])
        )
        self.y_axis.shift(
            DOWN * abs(self.y_axis[0].points[0] - self.x_axis[0].points[0])
        )

        self.x_axis.add_numbers(*range(1950, 1975 + 5, 5))
        fg = self.get_graph(self.ftg)

        self.play(ShowCreation(fg))
        self.wait()

    def first(self):
        title = TextMobject("What is Population?")
        self.play(Write(title))
        self.wait()

        self.play(title.shift, [0, 2, 0])
        desc = TextMobject(
            "The number of people living in an area at a particular time is known as population."
        ).scale(0.8)
        self.play(Write(desc, run_time=6))
        self.wait()
        self.clear()

        title2 = TextMobject("Do you think this number will always remain the same?")
        # self.play(write(title, run_time=3))
        self.play(Transform(title, title2))
        self.wait()
        self.play(title.shift, [0, 2, 0])

        desc = TextMobject(
            "Population changes over a course of period, and in most cases, population grows over a course of period."
        ).scale(0.8)

        self.play(Write(desc, run_time=6))
        self.wait(2)
        self.clear()
