from manimlib.imports import *
from helper import Grid, ScreenGrid

class example(GraphScene):
    def construct(self):
        self.showq()
        self.solMath()

    def solMath(self):
        fInfo  = VGroup(
                TexMobject("\\text{Birth Rate = } ","8\\%").arrange(RIGHT),
                TexMobject("\\text{Death Rate = } ","2\\%").arrange(RIGHT),
                TexMobject("\\text{Time = 3 years}"),
                TexMobject("\\text{Rate of increase of Population = } 8\\% - 2\\% = ","6\\%").arrange(RIGHT),
                TexMobject("\\text{Present Population } (P_t) = ","6,00,000").arrange(RIGHT)
                ).arrange(DOWN, aligned_edge=LEFT).scale(0.7).shift([-1,1,0])

        for each in fInfo:
            self.play(Write(each))
            self.wait()

        f = TexMobject(
                "P_t",
                "=",
                "P ", 
                "(1 + \\frac{R}{100})^T",
                ).shift([-1, -1.3,0])
        
        f2 = TexMobject(
                "or, 6,00,000",
                "=",
                "P ", 
                "(1 + \\frac{6}{100})^3",
                ).shift([-1,-2.5,0])
        
        f3 = TexMobject(
                "\\text{or, }",
                "6,00,000",
                "=",
                "P ", 
                "(\\frac{53}{50})^3",
                ).shift([-1.3,1.5,0])
        
        
        f4 = TexMobject(
                "\\text{or, }",
                "P ", 
                "=",
                "6,00,000",
                "(\\frac{125000}{148877})",
                ).shift([-1.3,0,0])
        
        f5 = TexMobject(
                "\\text{Therefore, }",
                "P =",
                "503771.569"
                ).shift([-1.3, -1.5, 0])
        
        self.play(Write(f, run_time=3))
        self.play(TransformFromCopy(fInfo[3][1], f2[0])) 
        self.play(TransformFromCopy(f[1], f2[1])) 
        self.play(TransformFromCopy(f[2], f2[2])) 
        self.play(TransformFromCopy(fInfo[3], f2[3])) 
        self.wait()
        self.clear()
        
        self.play(f2.shift, [0,5.5,0])
        self.wait()

        self.play(TransformFromCopy(f2, f3))
        self.wait()
        
        self.play(TransformFromCopy(f3[0], f4[0]))
        self.play(TransformFromCopy(f3[3], f4[1]))
        self.play(TransformFromCopy(f3[2], f4[2]))
        self.play(TransformFromCopy(f3[1], f4[3]))
        self.play(TransformFromCopy(f3[4], f4[4]))
        self.wait() 
        
        self.play(TransformFromCopy(f4, f5))
        self.wait()

        t1 = TextMobject("The population before 3 years was 503772. ","(As Population is discrete. We usually round it off)").shift([-1,-2.5,0]).scale(0.6)
        t1[1].set_color(RED)

        self.play(Write(t1))
        self.wait()

    def showq(self):
        title = TextMobject("Example")
        self.play(Write(title))
        self.wait()

        self.clear()

        question = TexMobject("\\text{The birth rate of the population of a town is } 8 \\% \\text{ every year and death rate is } 2 \\% \\text{ per year.}","\\text{If the population of the town is } 6,00,000 \\text{. Find the population before 3 years.}").scale(0.7).shift([0,2,0]).arrange(DOWN, aligned_edge=LEFT)
        
        self.play(Write(question, run_time=8))
        self.wait()

        self.play(question.shift, [0, 3,0])
        self.wait()

        sol = TextMobject("Solution:").shift([-6,2,0]).set_color(GREEN) 
        self.play(Write(sol))
        self.wait()






