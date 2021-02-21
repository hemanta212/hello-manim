from manimlib.imports import*

class set1(Scene):
    def construct(self):
        rec=Rectangle(height=3.5,width=4.5)
        cir1=Circle(radius=1.2).shift(np.array([0.7,0,0]))
        cir2=Circle(radius=1.2).shift(np.array([-0.7,0,0]))

        arr1=Arrow(np.array([0,-2,0]),np.array([0,0,0]),buff=0)
        arr2=Arrow(np.array([3,1,0]),np.array([1.5,0,0]),buff=0)
        arr3=Arrow(np.array([-3,1,0]),np.array([-1.5,0,0]),buff=0)
        arr4=Arrow(np.array([-2.8,-1,0]),np.array([-1.6,-1,0]),buff=0)

        arr1_1=TextMobject("Elements shared by set A and B").scale(0.6).shift(np.array([0,-2.3,0]))
        arr1_2=TextMobject("Elements in set A").scale(0.6).shift(np.array([4.2,1,0]))
        arr1_3=TextMobject("Elements in set B").scale(0.6).shift(np.array([-4.2,1,0]))
        arr1_4=TextMobject("Elements outside A and B").scale(0.6).shift(np.array([-5,-1,0]))
        arr1_5=TextMobject("but inside universal set").scale(0.6).next_to(arr1_4,DOWN,buff=0.2).align_to(arr1_4,LEFT)
        
        a1=TextMobject("2").scale(0.6).shift(np.array([1.1,0,0]))
        b1=TextMobject("1").scale(0.6).shift(np.array([-1.1,0,0]))
        aub1=TextMobject("3").scale(0.6).move_to(np.array([0,0.5,0]))
        aub2=TextMobject("5").scale(0.6).next_to(aub1,DOWN,buff=0.2)
        aub3=TextMobject("7").scale(0.6).next_to(aub2,DOWN,buff=00.2)
        uni=TextMobject("9").scale(0.6).shift(np.array([-1.3,-1.3,0]))
        group=VGroup(a1,b1,aub1,aub2,aub3,uni)

        self.play(ShowCreation(rec))
        self.play(ShowCreation(cir1))
        self.play(ShowCreation(cir2))

        U=TextMobject("U").scale(0.7).move_to(np.array([2,1.5,0]))
        A=TextMobject("A").scale(0.7).move_to(np.array([0.7,1.54,0]))
        B=TextMobject("B").scale(0.7).move_to(np.array([-0.7,1.54,0]))
        C=TextMobject("C").scale(0.7).move_to(np.array([-0.5,-2.5,0]))
        

        self.play(FadeIn(U))
        self.play(FadeIn(A))
        self.play(FadeIn(B))

        self.play(FadeIn(group,run_time=2))
        

        u=TextMobject("Union").shift(np.array([0,3.5,0])).set_color(GREEN_D)
        u1=TextMobject("The union of two sets A and B(A $\\cup$ B) is a set containing all elements that").scale(0.7).shift(np.array([0,3,0]))
        u2=TextMobject(" are in A or in B (possibly both)").scale(0.7).next_to(u1,DOWN,buff=0.2).align_to(u1,LEFT)
        u3=TextMobject("").scale(0.6).next_to(u2,DOWN,buff=0)

        i=TextMobject("Intersection").shift(np.array([0,3.5,0])).set_color(GREEN_D)
        i1=TextMobject("The intersection of two sets A and B(A $\\cap$ B) consists of all elements that").scale(0.7).shift(np.array([0,3,0]))
        i2=TextMobject("are both in A and B").scale(0.7).next_to(i1,DOWN,buff=0.2).align_to(i1,LEFT)
        i3=TextMobject("").scale(0.6).next_to(i2,DOWN,buff=0)

        d=TextMobject("Difference").shift(np.array([0,3.5,0])).set_color(GREEN_D)
        d1=TextMobject("The difference (subtraction) of set B from A(A-B) consists of elements that are").scale(0.7).shift(np.array([0,3,0]))
        d2=TextMobject("in A but not in B").scale(0.7).next_to(d1,DOWN,buff=0.2).align_to(d1,LEFT)
        d3=TextMobject("").scale(0.6).next_to(d2,DOWN,buff=0)

        c=TextMobject("Complement").shift(np.array([0,3.5,0])).set_color(GREEN_D)
        c1=TextMobject("The complement of a set A($\overline{A}$) is the set of all elements that are in the").scale(0.7).shift(np.array([0,3,0]))
        c2=TextMobject("universal set S but are not in A").scale(0.7).next_to(c1,DOWN,buff=0.2).align_to(c1,LEFT)
        c3=TextMobject("").scale(0.6).next_to(c2,DOWN,buff=0)

        self.play(FadeIn(u),FadeIn(u1),FadeIn(u2))
        self.play(Indicate(VGroup(a1,b1,aub1,aub2,aub3)),Indicate(cir1),Indicate(cir2),run_time=3)
        self.wait(2)
        self.play(FadeOut(u1),FadeOut(u2))

        self.play(ReplacementTransform(u,i),FadeIn(i1),FadeIn(i2))
        self.play(Indicate(VGroup(aub1,aub2,aub3),scale_factor=2,color=PURPLE_E),run_time=3)
        self.wait(2)
        self.play(FadeOut(i1),FadeOut(i2))

        self.play(ReplacementTransform(i,d),FadeIn(d1),FadeIn(d2))
        self.play(Indicate(a1,scale_factor=2,color=PURPLE_E),run_time=3)
        self.wait(2)
        self.play(FadeOut(d1),FadeOut(d2))

        self.play(ReplacementTransform(d,c),FadeIn(c1),FadeIn(c2))
        self.play(Indicate(VGroup(b1,aub1,aub2,aub3,uni)),run_time=3)
        self.wait(2)
        self.play(FadeOut(c),FadeOut(c1),FadeOut(c2))

        self.play(FadeOutAndShift(VGroup(rec,cir1,cir2,group,U,A,B),direction=DOWN))

        rec=Rectangle(height=4.5,width=4.5).shift(np.array([0,-0.5,0]))
        cir1=Circle(radius=1.2).shift(np.array([0.7,0,0]))
        cir2=Circle(radius=1.2).shift(np.array([-0.7,0,0]))
        cir3=Circle(radius=1.2).shift(np.array([0,-1,0]))

        
        self.play(ShowCreation(rec))
        self.play(ShowCreation(cir1))
        self.play(ShowCreation(cir2))
        self.play(ShowCreation(cir3))
        self.play(FadeIn(VGroup(U,A,B,C)))
        self.wait(2)
        

        arrA=Arrow(np.array([4,0,0]),np.array([2,0,0]),buff=0,stroke_width=3)
        arrAo=Arrow(np.array([3,0.4,0]),np.array([0.9,0.4,0]),buff=0)
        arranb=Arrow(np.array([3,2,0]),np.array([0,0.5,0]),buff=0)
        arrB=Arrow(np.array([-4,0,0]),np.array([-2,0,0]),buff=0)
        arrBo=Arrow(np.array([-2.8,1,0]),np.array([-1.1,0.2,0]),buff=0)
        arrbnc=Arrow(np.array([-3,-0.5,0]),np.array([-0.7,-0.5,0]),buff=0)
        arrCo=Arrow(np.array([0,-3,0]),np.array([0,-1.6,0]),buff=0)
        arrC=Arrow(np.array([-3,-1.4,0]),np.array([-1.2,-1.4,0]),buff=0)
        arranc=Arrow(np.array([2.5,-0.5,0]),np.array([0.7,-0.5,0]),buff=0)
        arranbnc=Arrow(np.array([2.7,-3,0]),np.array([0,-0.5,0]),buff=0)
        arruni=Arrow(np.array([-3.2,-2.2,0]),np.array([-1.4,-1.8,0]),buff=0)

        A_1=TextMobject("n(A)").scale(0.6).shift(np.array([4.3,0,0]))
        Ao=TextMobject("$n_0(A)$").scale(0.6).shift(np.array([0.9,0.4,0]))
        AnB=TextMobject("n(A $\\cap$ B)").scale(0.6).shift(np.array([3.7,2,0]))
        B_1=TextMobject("n(B)").scale(0.6).shift(np.array([-4.3,0,0]))
        Bo=TextMobject("$n_0(B)$").scale(0.6).shift(np.array([-1.1,0.2,0]))
        BnC=TextMobject("n(B $\\cap$ C)").scale(0.6).shift(np.array([-3.7,-0.5,0]))
        C_1=TextMobject("n(C)").scale(0.6).shift(np.array([-3.3,-1.4,0]))
        Co=TextMobject("$n_0(C)$").scale(0.6).shift(np.array([0,-1.6,0]))
        AnC=TextMobject("n(A $\\cap$ C)").scale(0.6).shift(np.array([3.2,-0.5,0]))
        AnBnC=TextMobject("n(A $\\cap$ B $\\cap$ C)").scale(0.6).shift(np.array([3.3,-3.1,0]))
        uni1=TextMobject("n($\overline{A \\cap B \\cap C}$)").scale(0.6).shift(np.array([-3.9,-2.5,0]))

        #self.play(FadeIn(VGroup(arrA,arranb,arrB,arrbnc,arrC,arranc,arranbnc,arruni)))
        #self.play(FadeIn(VGroup(A_1,Ao,AnB,B_1,Bo,BnC,C_1,Co,AnC,AnBnC,uni1)))

        
        

        topic=TextMobject("Venn Diagram of Three Sets").shift(np.array([0,3.5,0]))
        U1=TextMobject("U=\{1,2,3,4,5,6,7,8\}").scale(0.6).shift(np.array([-2,3,0]))
        A1=TextMobject("A=\{1,2,3,4,5\}").scale(0.6).next_to(U1,DOWN,buff=0.2).align_to(U1,LEFT)
        B1=TextMobject("B=\{4,5,6,7\}").scale(0.6).next_to(A1,DOWN,buff=0.2).align_to(A1,LEFT)
        C1=TextMobject("C=\{3,5,7,9\}").scale(0.6).next_to(U1,RIGHT,buff=0.6)
        

        a1=TextMobject("1").scale(0.6).shift(np.array([0.8,0.4,0]))
        a2=TextMobject("2").scale(0.6).next_to(a1,RIGHT,buff=0.2)
        a3=TextMobject("3").scale(0.6).shift(np.array([1.1,0,0]))
        
        b1=TextMobject("6").scale(0.6).shift(np.array([-1.1,0.2,0]))

        c1=TextMobject("9").scale(0.6).move_to(np.array([0,-1.6,0]))
        
        anb=TextMobject("4").scale(0.6).move_to(np.array([0,0.5,0]))
        anbnc=TextMobject("5").scale(0.6).move_to(np.array([0,-0.5,0]))
        anc=TextMobject("3").scale(0.6).move_to(np.array([0.7,-0.5,0]))
        bnc=TextMobject("7").scale(0.6).move_to(np.array([-0.7,-0.5,0]))
        uni=TextMobject("8").scale(0.6).shift(np.array([-1.3,-1.8,0]))

        self.play(DrawBorderThenFill(topic),run_time=2)
        self.play(FadeInFrom(U1,direction=UP))
        self.play(FadeInFrom(A1,direction=UP))
        self.play(FadeInFrom(B1,direction=UP))
        self.play(FadeInFrom(C1,direction=UP))

        self.play(FadeIn(VGroup(arrA,A_1)))
        self.play(FadeIn(Ao))
        self.play(FadeIn(VGroup(arrB,B_1)))
        self.play(FadeIn(Bo))
        self.play(FadeIn(VGroup(arrC,C_1)))
        self.play(FadeIn(Co))
        self.play(FadeIn(VGroup(arranb,AnB)))
        self.play(FadeIn(VGroup(arrbnc,BnC)))
        self.play(FadeIn(VGroup(arranc,AnC)))
        self.play(FadeIn(VGroup(AnBnC,arranbnc)))
        self.play(FadeIn(VGroup(arruni,uni1)))

        self.play(ReplacementTransform(Ao,a2),ReplacementTransform(Bo,b1),ReplacementTransform(Co,c1),FadeOut(VGroup(arrA,arrB,arrC,B_1,C_1,A_1)))
        self.wait(2)
                  
        self.play(ReplacementTransform(AnB,anb),ReplacementTransform(arranb,anb))        
        self.play(ReplacementTransform(BnC,bnc),ReplacementTransform(arrbnc,bnc))
        self.play(ReplacementTransform(AnC,anc),ReplacementTransform(arranc,anc))
        self.play(ReplacementTransform(AnBnC,anbnc),ReplacementTransform(arranbnc,anbnc))
        self.play(ReplacementTransform(uni1,uni),ReplacementTransform(arruni,uni))
        
        self.wait(2)

        
        
        
