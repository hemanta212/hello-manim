# coding: utf-8

self.wait(10)
self.wait(5)
clear()
x_axis = Axes()
add(_)
axes = Axes(
    # x-axis ranges from -1 to 10, with a default step size of 1
    x_range=(-1, 10),
    # y-axis ranges from -2 to 10 with a step size of 0.5
    y_range=(-2, 2, 0.5),
    # The axes will be stretched so as to match the specified
    # height and width
    height=6,
    width=10,
    # Axes is made of two NumberLine mobjects.  You can specify
    # their configuration with axis_config
    axis_config={
        "stroke_color": GREY_A,
        "stroke_width": 2,
    },
    # Alternatively, you can specify configuration for just one
    # of them, like this.
    y_axis_config={
        "include_tip": False,
    }
)
# Keyword arguments of add_coordinate_labels can be used to
# configure the DecimalNumber mobjects which it creates and
# adds to the axes
axes.add_coordinate_labels(
    font_size=20,
    num_decimal_places=1,
)
self.add(axes)
remove(axes)
axes_ = Axes()
add(axes_)
remove(axes_)
axes_ = Axes(x_axis_config={'include_tip':False}) 
add(axes_)
va = Vector(direction=UR, color=GREEN).scale(2).shift(UR/2)
vb = Vector(color=BLUE).scale(3, about_edge=LEFT)
add(va, vb)
vb.rotate(20 * DEGREE)
vb.rotate(20 * DEGREES)
remove(vb)
vb = Vector(color=BLUE).scale(3, about_edge=LEFT)
add(vb)
vb.rotate_in_place(20 * DEGREES, about_edge=LEFT)
vb.rotate(20 * DEGREES, about_edge=LEFT)
va_perp = Line(va.get_end(), va.get_end()+2*DOWN, color=BLUE)
add(va_perp)
va.set_color(ORANGE_A)
va.set_color(ORANGE)
play(FadeOut(vb))
base_line = Line(va.get_start(), va_perp.get_end())
add(base_line)
theta_tex = TexText("$\\theta$").scale(0.5)
theta_tex.next_to(va.get_start(), UR)
add(theta_tex)
theta_tex.next_to(va.get_start())
theta_tex.next_to(va.get_start(), buff=0.5)
theta_tex.next_to(va.get_start(), buff=0.5).shift(UP/4)
theta_tex.scale(2)
theta_tex.scale(0.8)
