#!/usr/bin/env python3

from manimlib.imports import *


class Main(Scene):
    def construct(self):
        self.intro()
        self.function_basic()
        self.composite_functions_intro()
        self.composite_functions_demo()
        self.composite_functions_extra()

    def intro(self):
        text = TextMobject("Composite Functions")
        text.set_color_by_gradient(PURPLE, BLUE, GREEN, ORANGE, RED)
        self.play(Write(text), run_time=3)
        self.wait(3)
        self.play(FadeOut(text))

    def composite_functions_demo(self):
        description = TextMobject("Let's take a function")
        description2 = TextMobject("which multiplies its input with 2")
        description.to_edge(UP)
        description2.next_to(description, DOWN)

        machine_text = TextMobject("2 x X")
        machine_text.set_color(BLUE)
        machine_box = Square()
        machine_box.surround(machine_text)
        machine_box.scale(2)
        machine = VGroup(machine_text, machine_box)

        self.play(Write(description), run_time=3)
        self.play(Write(description2), run_time=3)

        self.add(machine)
        self.play(ApplyMethod(machine_text.next_to, machine_box, UP), run_time=3)
        self.play(FadeOut(description), FadeOut(description2))

        description = TextMobject("Let us pass our previous adder function")
        description2 = TextMobject("As a input to this function")
        description.to_edge(UP)
        description2.next_to(description, DOWN)

        self.play(Write(description), run_time=3)
        self.play(Write(description2), run_time=3)

        input_text = TextMobject("x + 2")
        input_box = Rectangle(color=RED)
        input_box.surround(input_text)
        input = VGroup(input_text, input_box)
        input.to_edge(LEFT)

        process_text = TextMobject("(x + 2) x 2")
        process_box = Square(color=BLUE)
        process_box.surround(process_text)
        process = VGroup(process_text, process_box)
        process.move_to(machine_box)

        output_text = TextMobject("2x + 4")
        output_box = Rectangle(color=BLUE)
        output_box.surround(output_text)
        output = VGroup(output_text, output_box)
        output.move_to(machine_box)

        self.play(ApplyMethod(input.move_to, machine_box), run_time=4)
        self.play(Transform(input, process), run_time=3)
        self.play(Transform(input, output), run_time=3)
        self.play(ApplyMethod(input.to_edge, RIGHT), run_time=4)

        description = TextMobject("Well, naturally when we pass function as input")
        description2 = TextMobject("We get function as output")
        description.next_to(machine_box, DOWN)
        description2.next_to(description, 2 * DOWN)

        self.play(Write(description), run_time=3)
        self.play(Write(description2), run_time=3)
        self.play(FadeOut(description), FadeOut(description2), FadeOut(input))

    def composite_functions_intro(self):
        description = TextMobject("So what qualifies as valid input to a function?")
        description2 = TextMobject("To understand this,")
        description3 = TextMobject(
            "let's explain, at a higher level what a function does"
        )
        description.to_edge(UP)
        description2.next_to(description, 2 * DOWN)
        description3.next_to(description, 6 * DOWN)

        self.play(Write(description), run_time=3)
        self.play(Write(description2), run_time=3)
        self.play(Write(description3), run_time=3)
        self.play(FadeOut(description), FadeOut(description2), FadeOut(description3))

        description = TextMobject(
            "A function takes an input and modifies it to produce output."
        )
        description2 = TextMobject(
            "By modifying, here we mean any valid mathematical operation"
        )
        description.to_edge(UP)
        description2.next_to(description, 2 * DOWN)

        self.play(Write(description), run_time=3)
        self.play(Write(description2), run_time=3)
        self.play(FadeOut(description), FadeOut(description2))

        description = TextMobject("This revelation opens up whole new sorts of doors")
        description2 = TextMobject(
            "For example, lets try giving a function another function as input"
        )
        description.to_edge(UP)
        description2.next_to(description, 2 * DOWN)

        self.play(Write(description), run_time=3)
        self.play(Write(description2), run_time=3)
        self.play(FadeOut(description), FadeOut(description2))

    def function_basic(self):
        description = TextMobject("A function is a machine")
        description2 = TextMobject("It takes input and returns output")
        description.to_edge(UP)
        description2.next_to(description, DOWN)

        machine_text = TextMobject("Machine")
        machine_text.set_color(BLUE)
        machine_box = Square()
        machine_box.surround(machine_text)
        machine = VGroup(machine_text, machine_box)

        input_text = TextMobject("input")
        input_box = Rectangle(color=RED)
        input_box.surround(input_text)
        input = VGroup(input_text, input_box)
        input.to_edge(LEFT)

        output_text = TextMobject("output")
        output_box = Rectangle(color=BLUE)
        output_box.surround(output_text)
        output = VGroup(output_text, output_box)
        output.move_to(machine_box)

        self.play(Write(description), run_time=3)
        self.play(Write(description2), run_time=3)

        self.add(machine)
        self.play(ApplyMethod(machine_text.next_to, machine_box, UP), run_time=3)

        self.play(ApplyMethod(input.move_to, machine_box), run_time=4)
        self.play(Transform(input, output), run_time=3)
        self.play(ApplyMethod(input.to_edge, RIGHT), run_time=4)

        self.play(FadeOut(description), FadeOut(description2), FadeOut(input))

        formula_text = TextMobject("X + 2")
        formula_text.move_to(machine_text)
        description = TextMobject("Lets look at a adder function")
        description2 = TextMobject("It adds every input with 2 and outputs the result")
        description.to_edge(UP)
        description2.to_edge(DOWN)
        self.play(
            Write(description),
            Transform(machine_text, formula_text),
            run_time=3,
        )

        input_text = TextMobject("5")
        input_box = Circle(color=RED)
        input_box.surround(input_text)
        input = VGroup(input_text, input_box)
        input.to_edge(LEFT)

        process_text = TextMobject("5 + 2")
        process_box = Square(color=BLUE)
        process_box.surround(process_text)
        process = VGroup(process_text, process_box)
        process.move_to(machine_box)

        output_text = TextMobject("7")
        output_box = Circle(color=BLUE)
        output_box.surround(output_text)
        output = VGroup(output_text, output_box)
        output.move_to(machine_box)

        self.play(ApplyMethod(input.move_to, machine_box), run_time=4)
        self.play(Transform(input, process), run_time=3)
        self.play(Transform(input, output), run_time=3)
        self.play(Write(description2), run_time=3)
        self.play(ApplyMethod(input.to_edge, RIGHT), run_time=4)
        self.play(FadeOut(description), FadeOut(description2), FadeOut(input))

        formula_text = TextMobject("5")
        formula_text.move_to(machine_text)
        description = TextMobject(
            "There are some functions which always give same output"
        )
        description2 = TextMobject("This function always outputs 1 no matter the input")
        description3 = TextMobject("Such functions are called constant functions")
        description.to_edge(UP)
        description2.to_edge(DOWN)
        description3.to_edge(DOWN)
        self.play(
            Write(description),
            Transform(machine_text, formula_text),
            run_time=3,
        )

        input_text = TextMobject("5")
        input_box = Circle(color=RED)
        input_box.surround(input_text)
        input = VGroup(input_text, input_box)
        input.to_edge(LEFT)

        process_text = TextMobject("1")
        process_box = Square(color=BLUE)
        process_box.surround(process_text)
        process = VGroup(process_text, process_box)
        process.move_to(machine_box)

        output_text = TextMobject("1")
        output_box = Circle(color=BLUE)
        output_box.surround(output_text)
        output = VGroup(output_text, output_box)
        output.move_to(machine_box)

        self.play(ApplyMethod(input.move_to, machine_box), run_time=4)
        self.play(Transform(input, process), run_time=3)
        self.play(Transform(input, output), run_time=3)
        self.play(Write(description2), run_time=3)
        self.play(ApplyMethod(input.to_edge, RIGHT), run_time=4)
        self.play(Transform(description2, description3), run_time=3)

        self.wait(2)

    def composite_functions_extra(self):

        description = TextMobject("Lets experiment with this new function")
        description2 = TextMobject("We will pass a input 10 and observe its output")
        description.to_edge(UP)
        description2.next_to(description, DOWN)

        machine_text = TextMobject("2 x X + 4")
        machine_text.set_color(BLUE)
        machine_box = Square()
        machine_box.surround(machine_text)
        machine = VGroup(machine_text, machine_box)

        self.play(
            Write(description),
            run_time=3,
        )
        self.add(machine)
        self.play(ApplyMethod(machine_text.next_to, machine_box, UP), run_time=3)
        self.play(Write(description2), run_time=3)

        input_text = TextMobject("10")
        input_box = Circle(color=RED)
        input_box.surround(input_text)
        input = VGroup(input_text, input_box)
        input.to_edge(LEFT)

        process_text = TextMobject("2 x 10 + 4")
        process_box = Square(color=BLUE)
        process_box.surround(process_text)
        process = VGroup(process_text, process_box)
        process.move_to(machine_box)

        output_text = TextMobject("24")
        output_box = Circle(color=BLUE)
        output_box.surround(output_text)
        output = VGroup(output_text, output_box)
        output.move_to(machine_box)

        self.play(ApplyMethod(input.move_to, machine_box), run_time=4)
        self.play(Transform(input, process), run_time=3)
        self.play(Transform(input, output), run_time=3)
        self.play(ApplyMethod(input.to_edge, RIGHT), run_time=4)
        self.clear()

        description = TextMobject("What's interesting about this output is")
        description2 = TextMobject("Passing 10 to adder function and piping its output")
        description3 = TextMobject(
            "to multiplier function generates the same output 24"
        )
        description.to_edge(UP)
        description2.next_to(description, DOWN)
        description3.next_to(description2, DOWN)
        self.play(
            Write(description),
            run_time=3,
        )
        self.play(
            Write(description2),
            run_time=3,
        )
        self.play(
            Write(description3),
            run_time=3,
        )
        self.wait(2)
        self.clear()

        machine_text = TextMobject("X + 2")
        machine_text.set_color(BLUE)
        machine_box = Square()
        machine_box.surround(machine_text)
        machine = VGroup(machine_text, machine_box)

        self.add(machine)
        self.play(ApplyMethod(machine_text.next_to, machine_box, UP), run_time=3)

        input_text = TextMobject("10")
        input_box = Circle(color=RED)
        input_box.surround(input_text)
        input = VGroup(input_text, input_box)
        input.to_edge(LEFT)

        process_text = TextMobject("10 + 2")
        process_box = Square(color=BLUE)
        process_box.surround(process_text)
        process = VGroup(process_text, process_box)
        process.move_to(machine_box)

        output_text = TextMobject("12")
        output_box = Circle(color=BLUE)
        output_box.surround(output_text)
        output = VGroup(output_text, output_box)
        output.move_to(machine_box)

        self.play(ApplyMethod(input.move_to, machine_box), run_time=4)
        self.play(Transform(input, process), run_time=3)
        self.play(Transform(input, output), run_time=3)
        self.play(ApplyMethod(input.to_edge, RIGHT), run_time=4)

        machine_text2 = TextMobject("2 x X")
        machine_text2.set_color(BLUE)
        machine_box2 = Square()
        machine_box2.surround(machine_text2)
        machine2 = VGroup(machine_text2, machine_box2)
        machine2.to_edge(DOWN)

        self.add(machine2)
        self.play(ApplyMethod(machine_text2.next_to, machine_box2, UP), run_time=3)

        input_text2 = TextMobject("12")
        input_box2 = Circle(color=RED)
        input_box2.surround(input_text2)
        input2 = VGroup(input_text2, input_box2)
        input2.next_to(machine2, LEFT_SIDE)

        self.add(input2)

        process_text2 = TextMobject("2 x 12")
        process_box2 = Square(color=BLUE)
        process_box2.surround(process_text2)
        process2 = VGroup(process_text2, process_box2)
        process2.move_to(machine_box2)

        output_text = TextMobject("24")
        output_box = Circle(color=BLUE)
        output_box.surround(output_text)
        output = VGroup(output_text, output_box)
        output.move_to(machine_box2)

        self.play(ApplyMethod(input2.move_to, machine_box2), run_time=4)
        self.play(Transform(input2, process2), run_time=3)
        self.play(Transform(input2, output), run_time=3)
        self.play(ApplyMethod(input2.to_edge, RIGHT), run_time=4)
        self.clear()

        description = TextMobject("What we just saw was example of composite function")
        description2 = TextMobject("Passing a function to another function as input")
        description3 = TextMobject(
            "And generating a mixed function equivalent to given two function"
        )
        description.to_edge(UP)
        description2.next_to(description, DOWN)
        description3.scale(0.75)
        description3.next_to(description2, DOWN)
        self.play(
            Write(description),
            run_time=3,
        )
        self.play(
            Write(description2),
            run_time=3,
        )
        self.play(
            Write(description3),
            run_time=3,
        )
        self.wait(3)
        self.clear()
