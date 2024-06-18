from manim import *
from random import *
import numpy

class AnimationExample(Scene):
    def construct(self):
        text = Text("Hello, Manim!", font_size=48)
        self.play(Write(text))

        # Define the object you want to animate below the text
        circle = Circle(radius=1, color=RED)

        # Define the final position for the object
        final_position = text.get_center() + DOWN * 2

        # Animate the object to the final position
        self.play(Transform(circle, final_position))

        self.wait(1)
