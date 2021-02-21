from manimlib.imports import *
 


class Math1(TeacherStudentsScene, Scene):
  def construct(self):
     self.wait(2)
     Text1 = TextMobject("What will we study today, Teacher?")
     Text1.scale(1.8).set_color(RED)
     self.student_says(Text1)
     self.wait(2)
     
     Text2 = TextMobject(" We will continue on principles of probability and Tree Diagram")
     Text2.scale(1.8).set_color(MAROON)
     self.teacher_says(Text2)
     self.wait(2)
     self.clear()     
     self.wait(2)
	 
     topic = TextMobject("Addition rule of probability")
     topic.scale(1.2).set_color_by_gradient(RED, BLUE, PURPLE) 
     self.play(GrowFromCenter(topic) , run_time = 3, rate_func = rush_into)
     self.play(ApplyMethod(topic.shift,3.5*UP))
     self.wait(2)
     
     text3 = TextMobject("The addition rule states that if two events are mutually exclusive, the probability of that A or B will occur is the sum of the probability of each event.")
     text3.scale(0.7).set_color(RED).align_to(LEFT)
     self.play(Write(text3), run_time = 3)
     self.play(ApplyMethod(text3.shift,2*UP))
     self.wait(2)
     self.play(Uncreate(text3), run_time = 2)
     
     
     
     Given1 = TexMobject(
            r" P \left ( A\ or\ B \right ) = P\left ( A \right ) + P\left ( B \right ) ",
            r" or ",
            r" n \left ( A\ or\ B \right ) = n\left ( A \right ) + n\left ( B \right )",          
     
           
  
        )

     Given1.arrange(DOWN) 
     Given1.scale(0.7)
     Given1.set_color(BLUE)
     for x in range(0, len(Given1)):
    
        self.play(Write(Given1[x]), run_time = 3)
        self.wait(2)
     self.wait(2)
     self.clear()
     
     self.teacher_says("Lets solve a question on addition rule")
     self.wait(2)   
     self.student_says("Ok Teacher ")
     self.wait()
     self.clear()
     self.wait(2)
     
     topic1 = TextMobject("1. Find the probability of getting either a Heart or a Black card from a well shuffled pack of 52 cards. ")
     topic1.scale(0.7).set_color_by_gradient(RED, BLUE, PURPLE) 
     self.play(GrowFromCenter(topic1) , run_time = 3, rate_func = rush_into)
     self.play(ApplyMethod(topic1.shift,3.2*UP))
     self.wait(2)
  
     Given2 = TexMobject(
            r" Solution,",
            r" Sample\ space\ n\left ( s \right ) = 52 ",
            r" Event\  1:",
            r" No.\ of\ Hearts\ n\left ( H \right ) = 13",
            r" Probability\ of\ getting\ Hearts\ P\left ( H \right ) = \frac{n\left ( H \right )}{n\left ( s \right )} = \frac{13}{52}",
            r" Event\  2:",
            r" No.\ of\ Blacks\ n\left ( B \right ) = 26",
            r" Probability\ of\ getting\ Black\ Cards\  P\left ( B \right ) = \frac{n\left ( B \right )}{n\left ( s \right )} = \frac{26}{52}",
            r" Since\ the\ events\ are\ mutually\ exclusive\ we\ follow\ the\ additive\ rule",
            r" P\left ( H\ or\ B \right ) = P\left ( H \right ) + P\left ( B \right ) = \frac{13}{52} + \frac{26}{52} = \frac{3}{4}",
           
  
        )

     Given2.arrange(DOWN) 
     Given2.scale(0.6)
     Given2.set_color(BLUE)
     for x in range(0, len(Given2)):
    
        self.play(Write(Given2[x]), run_time = 2)
        self.wait(2)
     self.wait(2)
     self.clear()
     self.wait()
     
     topic2 = TextMobject("Multiplication rule of probability")
     topic2.scale(1.2).set_color_by_gradient(RED, BLUE, PURPLE) 
     self.play(GrowFromCenter(topic2) , run_time = 3, rate_func = rush_into)
     self.play(ApplyMethod(topic2.shift,3.5*UP))
     self.wait(2)
     
     text4 = TextMobject("For multiplicative rule of probability, let's understand dependent and independent events first. By definition, two events are said to be independent if the outcome/occurrence of one of the events is not dependent on another event. For instance, if you toss a coin and a dice at the same time, the probability of getting Head on the coin and 1 on the dice have no relation at all. So, they are independent events.  ")
     text4.scale(0.7).set_color(RED).align_to(LEFT)
     self.play(Write(text4), run_time = 5)
     self.play(ApplyMethod(text4.shift,1.5*UP))
     self.wait(2)
     self.play(Uncreate(text4),run_time = 2)
     
     self.clear()
     text4 = TextMobject("For multiplicative rule of probability, let's understand dependent and independent events first. By definition, two events are said to be independent if the outcome/occurrence of one of the events is not dependent on another event. For instance, if you toss a coin and a dice at the same time, the probability of getting Head on the coin and 1 on the dice have no relation at all. So, they are independent events.  ")
     text4.scale(0.7).set_color(RED).align_to(LEFT)
     self.play(Write(text4), run_time = 5)
     self.play(ApplyMethod(text4.shift,1.5*UP))
     self.wait(2)
     self.play(Uncreate(text4),run_time = 2)
     
     Given3 = TexMobject(
            r" the\ probability\ of\ occurrence\ of\ two\ independent\ events\ is\ equal\ to\ product\ of\ the\ probability\ of\ occurrence\ of\ each\ individual\ event.  ",
            r" P\left ( A\cap B \right ) = P\left ( A \right ) * P\left ( B \right ) ",
            r" This\ is\ the\ multiplicative\ rule\ of\ probability.  ",               
     
           
  
        )

     Given3.arrange(DOWN) 
     Given3[0].scale(0.45)
     Given3[1].scale(0.5)
     Given3[2].scale(0.5)
     
     Given3.set_color(BLUE)
     for x in range(0, len(Given3)):
    
        self.play(Write(Given3[x]), run_time = 2)
        self.wait(2)
     self.wait(2)
     self.clear()
     
     self.teacher_says("Lets solve a question on multiplication rule")
     self.wait(2)   
     self.student_says("Ok Teacher ")
     self.wait()
     self.clear()
     self.wait(2)
     
     topic3 = TextMobject("2. Two cards are drawn from a well shuffled deck of 52 cards one after another with replacement before the second draw. Find the probability that both of them are red cards. ")
     topic3.scale(0.7).set_color_by_gradient(RED, BLUE, ORANGE) 
     self.play(GrowFromCenter(topic3) , run_time = 3, rate_func = rush_into)
     self.play(ApplyMethod(topic3.shift,3.2*UP))
     self.wait(2)
  
     Given4 = TexMobject(
            r" Solution,",
            r" Numbers\ of\ cards/sample\ space\ n\left ( s \right ) = 52 ",
            r" No.\ of\ red\ cards\ n\left ( R \right ) = 26",
            r" Event\ 1\ P\left ( X \right ): The\ First\ Card\ is\ drawn",
            r" Probability\ of\ getting\ a\ Red\ Card\ P\left ( R\right ) = \frac{n\left ( R\right )}{n\left ( s \right )} = \frac{26}{52}",
            r" Event\ 2\ P\left ( Y\right ): The\ Second\ Card\ is\ drawn\ after\ replacement",
            r" Probability\ of\ getting\ a\ Red\ Card\ P\left ( R\right ) = \frac{n\left ( R\right )}{n\left ( s \right )} = \frac{26}{52}",
            
            r" Probability\ that\ both\ of\ them\ are\ red\ cards: ",
            r" P\left ( X\cap Y \right ) = P\left ( X \right ) * P\left ( Y \right ) = \frac{26}{52} * \frac{26}{52} = \frac{1}{4} ",
           
  
        )

     Given4.arrange(DOWN) 
     Given4.scale(0.5)
     Given4.set_color(BLUE)
     for x in range(0, len(Given4)):
    
        self.play(Write(Given4[x]), run_time = 2)
        self.wait(2)
     self.wait(2)
     self.clear()
     self.wait()
     
     topic4 = TextMobject("Tree Diiagram")
     topic4.scale(1.2).set_color_by_gradient(RED, BLUE, PURPLE) 
     self.play(GrowFromCenter(topic4) , run_time = 3, rate_func = rush_into)
     self.play(ApplyMethod(topic4.shift,3.5*UP))
     self.wait(2)
     
     self.student_says("Sir, What is Tree Diagram?")
     self.wait(2)
     self.teacher_says("A probability tree diagram is a schematic representation of all events and their outcomes")
     self.wait(2)
     self.teacher_says("It uses lines and boxes to represent probability and events respectively. ")
     self.wait(2)
     self.teacher_says("This can be further explained by an example")
     self.wait(2)
     self.clear()
     self.wait()
     
     
     text5 = TextMobject("3. A fair coin is tossed three times. Make a tree diagram and find the probability of obtaining Three Tails  ")
     text5.scale(0.7).set_color(RED).align_to(LEFT)
     self.play(Write(text5), run_time = 3)
     self.play(ApplyMethod(text5.shift,3.3*UP))
     self.wait(2)
     
     treeimg = ImageMobject("treed")
     treeimg.scale(1.5).move_to(UP*1)
     self.play(FadeIn(treeimg), run_time = 3)
     self.wait(2)
     
     Given5 = TexMobject(
            r" Solution,",
            r" We\ have\ only\ one\ possible\ case\ for\ three\ tails\ \left \{ TTT \right \} ",
            r" Probability;",
            r" P\left ( TTT \right ) = P\left ( T1\cap T2\cap T3 \right ) = \frac{1}{2} * \frac{1}{2} * \frac{1}{2} = \frac{1}{8}",
            
            
           
  
        )

     Given5.arrange(DOWN) 
     Given5.scale(0.5).move_to(DOWN*2.2)
     Given5.set_color(BLUE)
     for x in range(0, len(Given5)):
    
        self.play(Write(Given5[x]), run_time = 3)
        self.wait(2)
     self.wait(2)
     
     