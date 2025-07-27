from manim import * 

class KerboCharacter(VGroup):
    def __init__(self, suit_color=GRAY, skin_color=GREEN, **kwargs):
        super().__init__(**kwargs)

        # Kopf mit Jeb-Grinsen
        head = Circle(radius=0.5).set_fill(skin_color, opacity=1).set_stroke(WHITE, 3)
        eye_left = Ellipse(width=0.2, height=0.3).shift(LEFT*0.2 + UP*0.1).set_fill(WHITE).set_stroke(BLACK, 1)
        eye_right = eye_left.copy().shift(RIGHT*0.4)
        pupil_left = Dot(radius=0.05).move_to(eye_left.get_center())
        pupil_right = Dot(radius=0.05).move_to(eye_right.get_center())
        grin = Arc(radius=0.3, start_angle=0, angle=PI).shift(DOWN*0.3)

        face = VGroup(eye_left, eye_right, pupil_left, pupil_right, grin)
        head_group = VGroup(head, face).shift(UP*1.5)

        # Körper (simpler Raumanzug)
        body = Rectangle(width=0.6, height=1.0).set_fill(suit_color, opacity=1).set_stroke(WHITE, 2)

        # Arme und Beine
        arm_left = Line(start=body.get_top() + LEFT*0.3, end=body.get_bottom() + LEFT*0.6)
        arm_right = Line(start=body.get_top() + RIGHT*0.3, end=body.get_bottom() + RIGHT*0.6)
        leg_left = Line(start=body.get_bottom() + LEFT*0.15, end=DOWN*1.5 + LEFT*0.2)
        leg_right = Line(start=body.get_bottom() + RIGHT*0.15, end=DOWN*1.5 + RIGHT*0.2)

        self.add(head_group, body, arm_left, arm_right, leg_left, leg_right)

        # Zugriff für Animationen
        self.head = head_group
        self.grin = grin
        self.arm_left = arm_left
        self.arm_right = arm_right

class AnimateCharacter(Scene):
    def construct(self):
        char = KerboCharacter().scale(1.2)
        self.play(FadeIn(char))

        # Arm heben
        #self.play(char.arm_right.animate.rotate(PI/6, about_point=char.arm_right.get_start()))

        # Mund ändern (z. B. auf traurig)
        #self.play(
         #   char.mouth_smile.animate.set_opacity(0),
        #    char.mouth_sad.animate.set_opacity(1)
        #)

        # Sprung oder Bewegung
        #self.play(char.animate.shift(UP*0.5), run_time=0.5)
        #self.play(char.animate.shift(DOWN*0.5), run_time=0.5)

        self.wait()
