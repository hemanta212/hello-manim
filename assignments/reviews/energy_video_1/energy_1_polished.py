from manimlib.imports import *


class Energy(Scene):
    def construct(self):

        # Sun --> Renewable source of energy

        Renewtxt = TextMobject("Renewable source of energy").scale(0.8)
        Renewtxt.set_color(YELLOW_C)
        Sun = ImageMobject("sun_image.png")
        asksun = (
            TextMobject("Why is the Sun the largest source of energy for us?")
            .set_color(YELLOW_A)
            .scale(0.8)
        )
        answersun = (
            TextMobject("It is because many energy sources are derived from the Sun.")
            .scale(0.7)
            .set_color(YELLOW_D)
        )
        questionsun = VGroup(asksun, answersun)
        questionsun.arrange(DOWN, buff=0.3)
        Sun.move_to(4 * LEFT)
        Renewtxt.move_to(4 * RIGHT)
        sunarrow = Arrow(
            Sun.get_center(), Renewtxt.get_center() + LEFT * 1.5, buff=1
        ).set_color(RED_C)
        movesun = VGroup(sunarrow, Renewtxt)
        movesun.generate_target()
        movesun.target.shift(3 * UP)
        Sun.generate_target()
        Sun.target.shift(3 * UP)
        self.play(GrowFromCenter(Sun), ShowCreation(sunarrow), run_time=3)
        self.play(Write(Renewtxt), run_time=3)
        self.wait()
        self.play(MoveToTarget(movesun), MoveToTarget(Sun), run_time=3)
        self.wait()
        self.play(ShowCreation(asksun), run_time=3)
        self.play(ShowCreation(answersun), run_time=4)
        self.wait(3)
        self.remove(asksun, answersun, sunarrow, Renewtxt)
        Sun.generate_target()
        Sun.target.shift(3.75 * RIGHT)
        self.play(MoveToTarget(Sun), run_time=3)

        # Pointers to sun

        fossil = TextMobject("Fossil Fuel")
        bio = TextMobject("Bio Gas")
        thermal = TextMobject("Thermal Energy")
        tidal = TextMobject("Tidal Energy")
        types = VGroup(fossil, bio, thermal, tidal)
        types.arrange(RIGHT, buff=0.5)
        types.to_edge(DOWN, buff=2)
        types.set_color_by_gradient(YELLOW_A, GOLD_A, GREEN_A, RED_A)
        for x in types:
            arrowtosun = Arrow(
                x.get_center(), Sun.get_center() + DOWN * 0.7, buff=0.5
            ).set_color(MAROON_C)
            self.play(FadeInFromDown(x))
            self.play(ShowCreation(arrowtosun))
            self.wait(2)
            self.remove(x, arrowtosun)

        # Photosynthesis --> Food

        why_sun = (
            TextMobject("Why is the Sun so important?")
            .scale(1.3)
            .set_color(GREEN_E)
        )
        self.play(GrowFromCenter(why_sun), run_time=3)
        self.wait(2)
        self.remove(why_sun)
        self.wait()
        phototxt = TextMobject("Photosynthesis")
        phototxt.to_edge(LEFT, buff=0.5)
        food = TextMobject("Food")
        food.to_edge(RIGHT, buff=0.5)
        photoarrow = Arrow(
            Sun.get_center() + DOWN * 0.7, phototxt.get_center(), buff=0.8
        ).set_color(ORANGE)
        foodarrow = Arrow(
            phototxt.get_center() + 1.5 * RIGHT, food.get_center() + LEFT * 1, buff=0.6
        ).set_color(ORANGE)
        self.play(FadeIn(phototxt), ShowCreation(photoarrow), run_time=3)
        self.play(Indicate(phototxt))
        self.wait()
        self.play(FadeIn(food), ShowCreation(foodarrow), run_time=3)
        self.play(Indicate(food))
        self.wait()
        self.remove(phototxt, photoarrow, food, foodarrow)
        Sun.generate_target()
        Sun.target.shift(LEFT * 5)
        self.play(MoveToTarget(Sun))
        self.wait()

        what_tidal = (
            TextMobject("What is tidal energy?")
            .scale(1.3)
            .set_color(GREEN_E)
        )
        self.play(GrowFromCenter(what_tidal), run_time=3)
        self.wait(2)
        self.remove(what_tidal)
        self.wait()

        heat = Arrow(DOWN * 3, DOWN * 0.5, direction=UP).set_color(RED_D)
        heattxt = TextMobject("Hot air")
        moveheat = VGroup(heat, heattxt)
        moveheat.arrange(RIGHT, buff=0.5)
        moveheat.generate_target()
        moveheat.target.shift(UP * 3)
        self.play(ShowCreation(heat), MoveToTarget(moveheat), run_time=3)
        exphot = (
            TextMobject(
                "Due to the heat of the Sun, the hot air goes up creating a vaccum."
            )
            .scale(0.8)
            .set_color(PURPLE_C)
        )
        self.play(Write(exphot), run_time=3)
        self.wait(3)
        self.remove(exphot)
        coldtxt = TextMobject("Cold air")
        cold = Arrow(LEFT * 3, LEFT * 0.5, direction=RIGHT).set_color(TEAL_C)
        movecold = VGroup(cold, coldtxt)
        movecold.arrange(DOWN, buff=0.5)
        movecold.generate_target()
        movecold.target.shift(RIGHT * 5)
        self.play(ShowCreation(cold), MoveToTarget(movecold), run_time=3)
        self.wait()
        expcold = (
            TextMobject("Cold air comes in to fill in the vaccum.")
            .scale(0.8)
            .set_color(PURPLE_C)
        )
        self.play(Write(expcold), run_time=3)
        self.wait(3)
        self.play(FadeOut(expcold))
        self.wait(2)
        self.remove(movecold, moveheat)
        Sun.generate_target()
        Sun.target.shift(RIGHT * 5)
        finexp = TextMobject(
            "This provides us with tidal energy (dervied from tides). This helps completing the water cycle, resulting in rainfall, which helps us produce hydropower. Hence, the Sun is the largest source of energy because it gives us energy in different forms like the one we saw in form of tidal energy."
        ).scale(0.8)
        finexp.set_color_by_gradient(PURPLE_A, PURPLE_B, PURPLE_C, PURPLE_D, PURPLE_E)
        self.play(MoveToTarget(Sun), Write(finexp), run_time=25)
        self.wait(5)
