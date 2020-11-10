# Selection
# [[output.gif]]


#!/usr/bin/env python3

from manimlib.imports import *

class ShapesPlay(Scene):
    TEXT_SIZE_F = 1.5
    TOP_LEFT = (LEFT_SIDE + TOP) / TEXT_SIZE_F
    TOP_RIGHT = (RIGHT_SIDE + TOP) / TEXT_SIZE_F
    BOTTOM_LEFT = (LEFT_SIDE + BOTTOM) / TEXT_SIZE_F
    BOTTOM_RIGHT = (RIGHT_SIDE + BOTTOM) / TEXT_SIZE_F

    shapes_info = {
        'circle': (GOLD, ORIGIN),
        'square': (RED_E, TOP_LEFT),
        'triangle': (BLUE_E, TOP_RIGHT),
        'ellipse': (GREY, BOTTOM_RIGHT),
        'rectangle': (MAROON, BOTTOM_LEFT),
    }

    SHAPE_NAMES = shapes_info.keys()

    def gen_shape_text(self, name):
        color, pos = self.shapes_info[name]
        shape_text = TextMobject(name)
        shape_text.set_color(color)
        shape_text.shift(pos)
        return shape_text

    def construct(self):
        texts = [self.gen_shape_text(name) for name in self.SHAPE_NAMES]
        shapes = [self.gen_shape_obj(name) for name in self.SHAPE_NAMES]
        formulas = [self.gen_shape_formula(name) for name in self.SHAPE_NAMES]
        text_animations = [Write(text_obj, run_time=3) for text_obj in texts]

        self.play(*text_animations)
        for text, shape, formula in zip(texts, shapes, formulas):
            self.play(Transform(text, shape, run_time=2))
            formula.next_to(shape, DOWN)
            self.play(Write(formula, run_time=2))

    def gen_shape_obj(self, name):
        circle = Circle(radius=1.0, color=PURPLE_A)
        triangle = Polygon(np.array([0,0,0]), np.array([1,-1,0]),np.array([-1,-1,0]))
        square = Square(side_length=1.0, color=GOLD_A)
        ellipse = Ellipse(width=2, height=1, color=RED)
        rectangle = Rectangle(height=1, width=1.5)

        shapes_map = {
            'circle': circle,
            'triangle': triangle,
            'square': square,
            'rectangle': rectangle,
            'ellipse': ellipse,
            }

        for shape_name, shape_obj in shapes_map.items():
            color, pos = self.shapes_info[shape_name]
            shape_obj.move_to(pos)

        return shapes_map[name]

    def gen_shape_formula(self, name):
        circle = TexMobject(r'\pi r^2')
        triangle = TexMobject(r'\frac{1}{2} base \times height')
        square = TexMobject(r'length^2')
        ellipse = TexMobject(r'\pi a b')
        rectangle = TexMobject(r'length \times breadth')

        formula_map = {
            'circle': circle,
            'triangle': triangle,
            'square': square,
            'rectangle': rectangle,
            'ellipse': ellipse,
            }

        return formula_map[name]
