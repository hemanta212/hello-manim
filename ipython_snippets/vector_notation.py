# coding: utf-8

grid = NumberPlane((-10, 10), (-5, 5))
add(grid)

va_coor_tex = TexText("(2, 2)")
vb_coor_tex = TexText("(2, 0)")
va_tex, vb_tex = TexText("2i+2j"), TexText("2i+0j")

va = Vector(direction=UR, color=GREEN).scale(2).shift(UR/2)
vb = Vector(color=BLUE).scale(3, about_edge=LEFT)
add(va, vb)

add(va_coor_tex)

va_coor_tex.next_to(va.get_end(), UR)
add(va_coor_tex)

add(vb.coor_tex.next_to(vb))
add(vb_coor_tex.next_to(vb.get_end()))

arrow = TexText("$\\rightarrow$")
va_arrow, vb_arrow = arrow.copy(), arrow.copy()
add(va_arrow.next_to(va_coor_tex))
add(vb_arrow.next_to(vb_coor_tex))
add(va_tex.next_to(va_arrow))
va_tex.set_color(GREEN)
add(vb_tex.next_to(vb_arrow).set_color(BLUE))
