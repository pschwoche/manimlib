from manim import *

class LittleCharacter(VGroup):
    def __init__(self, color=BLUE, **kwargs):
        super().__init__(**kwargs)

        # Kopf und Gesicht
        head_circle = Circle(radius=0.4).set_fill(color, opacity=1).set_stroke(WHITE, 2)
        left_eye = Dot(point=LEFT*0.15 + UP*0.1, radius=0.05)
        right_eye = Dot(point=RIGHT*0.15 + UP*0.1, radius=0.05)
        mouth_smile = Arc(radius=0.15, start_angle=0, angle=PI).shift(DOWN*0.1)
        mouth_sad = Arc(radius=0.15, start_angle=PI, angle=-PI).shift(DOWN*0.1)
        mouth_sad.set_opacity(0)  # initial hidden

        face = VGroup(left_eye, right_eye, mouth_smile, mouth_sad)
        head = VGroup(head_circle, face).shift(UP*1.5)

        # Körper
        body = Line(start=head_circle.get_bottom(), end=DOWN*0.5)

        # Gliedmaßen
        arm_left = Line(start=body.get_start(), end=LEFT*0.6 + UP*0.4)
        arm_right = Line(start=body.get_start(), end=RIGHT*0.6 + UP*0.4)
        leg_left = Line(start=body.get_end(), end=LEFT*0.3 + DOWN)
        leg_right = Line(start=body.get_end(), end=RIGHT*0.3 + DOWN)

        # Alles zusammen
        self.head = head
        self.mouth_smile = mouth_smile
        self.mouth_sad = mouth_sad
        self.body = body
        self.arm_left = arm_left
        self.arm_right = arm_right
        self.leg_left = leg_left
        self.leg_right = leg_right

        self.add(head, body, arm_left, arm_right, leg_left, leg_right)
