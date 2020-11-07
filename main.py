# Training
# We are building a simple circle and line and translate them to another cirlce sitting on platform and hit it. The ball will fall off with acceleration and go below. The formula for parabola will appear.


#!/usr/bin/env python3

from manimlib.imports import *

class ProjectileMotion(Scene):
    def construct(self):
        BOTTOM_LEFT = BOTTOM + LEFT_SIDE
        arm_line = Line(
            #np.array([-6, 0, 0]), np.array([-6, 3.5, 0])
            BOTTOM_LEFT, BOTTOM_LEFT + 2 * UP
            )
        fist_circle = Circle(radius=0.5)

        platform_line = Line()
        platform_ball = Circle(radius=0.5)

        #falling_arc = Arc(arc_center=ORIGIN+DOWN, radius=3, angle=-PI/2, start_angle=TAU/4)

        arm_line.set_angle(PI/4)
        fist_circle.next_to(arm_line, UP+RIGHT)

        arm = VGroup(arm_line, fist_circle)

        #platform_line.move_to(1.4 * UP)
        platform_ball.next_to(platform_line, UP)

        falling_arc = ArcBetweenPoints(ORIGIN+(0.5,1.5,0), BOTTOM+RIGHT_SIDE, angle=-PI/2, start_angle=TAU/4)

        self.play(*[ShowCreation(i) for i in [falling_arc, arm_line, fist_circle, platform_line, platform_ball]])

        arm_line.set_length(arm_line.get_length()+16)
        fist_circle.next_to(arm_line, UP+RIGHT)
        self.play(
            GrowFromEdge(arm, arm_line.start),
            #ApplyMethod(arm.set_length, arm_line.get_length()+16) 
            #ApplyMethod(fist_circle.next_to, arm_line)
            run_time = 3
                  )
        self.play(
            MoveAlongPath(platform_ball, falling_arc)
            )
