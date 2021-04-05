# coding: utf-8

self.wait(30)
clear()
add(TexText("$A \\cdot B =$").to_edge(UP).shift(DOWN))
self.mobjects[-1].to_edge(LEFT)
tex_parts = [TexText(i) for i in ["2i", "+", '2j', r'$\cdot$', '2i', '+', '0j']]
self.wait(10)
tex_parts = [TexText(i) for i in ["(2i", "+", '2j)', '$\\cdot$', '(2i', '+', '0j']]
self.wait(4)
self.mobjects
for i in tex_parts:
    i.next_to(self.mobjects[-1])
    add(i)
    
tex_parts = [TexText(i) for i in ["(2i", "+", '2j)', '$\\cdot$', '(2i', '+', '0j)']]
remove(self.mobjects[1:])
remove(*self.mobjects[1:])
for i in tex_parts:
    i.next_to(self.mobjects[-1])
    add(i)
    
text_parts[0].set_color(BLUE)
tex_parts[0].set_color(BLUE)
tex_parts[1].set_color(BLUE)
tex_parts[1].set_color(WHITE)
tex_parts[2].set_color(WHITE)
tex_parts[2].set_color(BLUE)
tex_parts[4].set_color(BLUE)
tex_parts[4].set_color(ORANGE)
tex_parts[6].set_color(ORANGE)
tex_parts[4].set_color(BLUE)
tex_parts[2].set_color(ORANGE)
move_parts = [i for n,i in enumerate(tex_parts) if n%2==0]
play(*[Indicate(i) for i in move_parts])
play(*[Indicate(i) for i in move_parts])
i_parts = VGroup(move_parts[0], move_parts[2])
j_parts = VGroupo(move_parts[1], move_parts[-1])
j_parts = VGroup(move_parts[1], move_parts[-1])
i_dest = TexText("($2i \\cdot 2i$)")
i_dest = TexText("($2i \\cdot 2i$) + ")
i_dest = TexText("($2i \\cdot 2i$) \ + \ ")
j_dest = TexText("($2j \\cdot 0j$)")
a_b = self.mobjects[0].copy().shift(DOWN)
add(a_b)
i_dest.next_to(a_b)
j_dest.next_to(i_dest)
play(ReplacementTransform(i_parts.copy(), i_dest))
play(ReplacementTransform(j_parts.copy(), j_dest))
two_row = VGroup(a_b, i_dest, j_dest)
new_row = VGroup(a_b.copy.shift(DOWN), TexText("4"))
new_row = VGroup(a_b.copy().shift(DOWN), TexText("4"))
new_row = VGroup(a_b.copy().shift(DOWN), TexText("4").next_to(a_b.copy().shift(DOWN)))
play(ReplacementTransform(two_row.copy(), new_row))
