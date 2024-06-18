# import manimlib
from manim import *

class makeCircle(Scene):
    def construct(self):
        circ = Circle()

        sqr = Square(1)

        sqr.set_fill(PINK,opacity = 0.3)

        circ.set_fill(BLUE, opacity=0.3)
        # self.play(Create(circ))
        # self.wait(1)
        self.play(Create(sqr))
        self.play(Rotate(sqr,PI/4))
        self.play(Transform(sqr,circ))
        self.wait(1)

def create_textbox(color, string):
    result = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        height=2, width=3, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    text = Text(string).move_to(box.get_center()) # create text
    result.add(box, text) # add both objects to the VGroup
    return result


class TextBox(Scene):  
    def construct(self):

        # create text box
        textbox = create_textbox(color=BLUE, string="Hello world")
        self.add(textbox)

        # move text box around
        self.play(textbox.animate.shift(2*RIGHT), run_time=3)
        self.play(textbox.animate.shift(2*UP), run_time=3)
        self.wait()


