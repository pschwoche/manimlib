from manim import *

class LittleCharacter(VGroup):
    def __init__(self, color=BLUE, **kwargs):
        super().__init__(**kwargs)

        head_circle = Circle(radius=0.4).set_fill(color, opacity=1).set_stroke(WHITE, 2)
        left_eye = Dot(point=LEFT*0.15 + UP*0.1, radius=0.05)
        right_eye = Dot(point=RIGHT*0.15 + UP*0.1, radius=0.05)
        mouth_smile = Arc(radius=0.15, start_angle=0, angle=PI).shift(DOWN*0.1)
        mouth_sad = Arc(radius=0.15, start_angle=PI, angle=-PI).shift(DOWN*0.1)
        mouth_sad.set_opacity(0)

        face = VGroup(left_eye, right_eye, mouth_smile, mouth_sad)
        head = VGroup(head_circle, face).shift(UP*1.5)

        body = Line(start=head_circle.get_bottom(), end=DOWN*0.5)
        arm_left = Line(start=body.get_start(), end=LEFT*0.6 + UP*0.4)
        arm_right = Line(start=body.get_start(), end=RIGHT*0.6 + UP*0.4)
        leg_left = Line(start=body.get_end(), end=LEFT*0.3 + DOWN)
        leg_right = Line(start=body.get_end(), end=RIGHT*0.3 + DOWN)

        self.head = head
        self.mouth_smile = mouth_smile
        self.mouth_sad = mouth_sad
        self.arm_right = arm_right

        self.add(head, body, arm_left, arm_right, leg_left, leg_right)

class AnimateCharacter(Scene):
    def construct(self):
        char = LittleCharacter().scale(1.2)
        self.play(FadeIn(char))
        self.play(char.arm_right.animate.rotate(PI/6, about_point=char.arm_right.get_start()))
        self.play(
            char.mouth_smile.animate.set_opacity(0),
            char.mouth_sad.animate.set_opacity(1)
        )
        self.play(char.animate.shift(UP*0.5), run_time=0.5)
        self.play(char.animate.shift(DOWN*0.5), run_time=0.5)
        self.wait()
