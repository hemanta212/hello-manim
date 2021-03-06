# coding: utf-8

a = IntegerMatrix(matrix, include_background_rectangle=True)
matrix = [[1, 1], [0, 1]]
a = IntegerMatrix(matrix, include_background_rectangle=True)
play(Write(a))

grid = NumberPlane((-10, 10), (-5, 5))
add(grid)
a = Arrow()
add(a)
a.rotate(PI/4)
a.shift(UR)
a.scale(2)
b = a.copy()
b.rotate(-PI/4)
add(b)
b.shift(DOWN)
b.shift(RIGHT/2)
d = Dot()
add(d)
d.move_to(a.get_start())
d.move_to(a.get_end())

va = Vector()
add(va)
va.scale(2)
va.move_to(a)
va.rotate(a.get_angle())
va.scale()
va.set_length(a.get_length())
remove(a)

va_p = va.get_projection()
d
d.move_to(va.get_end())
d.move_to(va.get_start())
d.move_to(va.get_end())
va_p = va.get_projection(va.get_end())
add(va_p)
va_p

proj_dash = DashedLine(va.get_end(), va_p)
add(proj_dash)
proj_dash.set_color(ORANGE)
Rotate(proj_dash)
va_p
t_d = add(Dot(va_p))

proj_dash = DashedLine(va.get_end(), 2*DOWN)
add(proj_dash)
remove(proj_dash)
proj_dash = DashedLine(va.get_end(), va.get_end() + 2 * DOWN)
add(proj_dash)
proj_dash.set_color(ORANGE)
proj_dash.set_color(GREEN)
proj_dash.set_color(YELLOW)
proj_dash.set_color(WHITE)

vp = Vector(ORIGIN, va_proj.get_end())
vp = Vector(ORIGIN, proj_dash.get_end())
vp = Vector()
add(vp)

vp.set_length(Line(ORIGIN, proj_dash.get_end()).get_length())
vp.shift(RIGHT/2)
vp.set_color(RED)
vp.set_color(RED_A)

def get_projection(vector_to_project, stable_vector):
    v1, v2 = stable_vector, vector_to_project
    return v1*np.dot(v1, v2)/(get_norm(v1)**2)

def get_vect_mob_projection(vector_to_project, stable_vector):
    return Vector(
        get_projection(
            vector_to_project.get_end(),            
            stable_vector.get_end()
        ),
        color = vector_to_project.get_color()
    ).fade()

