# coding: utf-8
a_b
a_b.to_edge(UL)
add(a_b)
proj_line = DashedLine(va.get_end(), va.get_end()+2*DOWN)
play(ShowCreation(proj_line))
vb.set_color(YELLOW)
remove(proj_line)
proj_line.set_color(BLUE)
play(ShowCreation(proj_line))
proj_line.set_color(BLUE)
remove(proj_line)
proj_line = Line(va.get_end(), va.get_end()+2*DOWN, color=BLUE)
play(ShowCreation(proj_line))
va_proj = Vector().scale(2, about_edge=LEFT).set_color(GREEN_D)
add(va_proj)
GREEN_E
GREEN_F
remove(va_proj)
va_proj = Vector().scale(2, about_edge=LEFT).set_color(GREEN_E)
add(va_proj)
help(Braces)
help(Brace)
va_proj_brace = Brace(va_proj, DOWN, tex_string="Length of projected $\\vec{A}$")
va_proj_brace = Brace(va_proj, DOWN)
play(ShowCreationThenDistroy(va_proj_brace))
play(ShowCreationThenDestroy(va_proj_brace))
play(ShowCreationThenDestruction(va_proj_brace))
def blip(obj, timer=2, wait=2):
    play(ShowCreationThenDestruction(obj), run_time=timer)
    self.wait(wait)
    
blip(va_proj_brace)
def blip(obj, timer=2, wait=2):
    self.play(ShowCreationThenDestruction(obj), run_time=timer)
    self.wait(wait)
    
blip(va_proj_brace)
va_proj_brace.tex_string = 'raju'
add(va_proj_brace)
add(TexText("$\\vec{a}$"))
remove(self.mobjects[-1])
def blip(self, obj, timer=2, wait=2):
    self.play(ShowCreationThenDestruction(obj), run_time=timer)
    self.wait(wait)
    
blip(self, va_proj_brace)
blip(self, va_proj_brace, 1, 2)
def blip(self, obj, timer=2, wait=2):
    self.play(ShowCreationThenDestruction(obj), run_time=timer)
    
help(ShowCreationThenDestruction)
def blip(self, obj, timer=2, wait=2):
    self.play(ShowCreationThenDestruction(obj, time_width=wait), run_time=timer)
    
    
blip(self, va_proj_brace, 1, 2)
def blip(self, obj, timer=2, wait=2):
    self.play(ShowCreationThenDestruction(obj, time_width=wait), run_time=timer)
    
blip(self, va_proj_brace, 1, 2)
blip(self, va_proj_brace, 1, 5)
va_proj_tex = va_proj_brace.get_text("Length of proj. of $\\vec{A}$")
vb_brace = Brace(vb, DOWN)
vb_brace_tex = vb.get_text("Length of $\\vec{B}$")
vb_brace_tex = vb_brace.get_text("Length of $\\vec{B}$")
play(ShowCreation(va_proj_brace), ShowCreation(va_proj_tex))
play(FadeOut(VGroup(*self.mobjects[-2:])))
play(ShowCreation(vb_brace),ShowCreation(vb_brace_tex))
play(FadeOut(VGroup(*self.mobjects[-2:])))
play(ShowCreation(va_proj_brace), ShowCreation(va_proj_tex))
play(FadeOut(VGroup(*self.mobjects[-2:])))
play(ShowCreation(vb.copy()))
play(ShowCreation(vb_brace),ShowCreation(vb_brace_tex))
play(FadeOut(VGroup(*self.mobjects[-3:])))
play(ShowCreation(va_proj_brace), ShowCreation(va_proj_tex))
play(FadeOut(VGroup(*self.mobjects[-2:])))
add(vb.copy())
play(ShowCreation(vb_brace),ShowCreation(vb_brace_tex))
play(FadeOut(VGroup(*self.mobjects[-3:])))
remove(proj_line, va_proj)
va_extend_line = Line(va.get_start(), va.get_end()).scale(5)
add(_)
add(va_extend_line)
