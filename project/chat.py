from manim import *

class MainResult(Scene):

    def makerect(self, hshift, vshift):
        rect = Rectangle(height=0.2, width=2, stroke_color=LIGHT_GRAY).shift(UP * vshift + RIGHT * hshift + DOWN * 2).set_fill(color=LIGHTER_GRAY, opacity=0.5)
        return rect

    def makeArrow(self, startpos, endpos, col, buffer):
        arw = Arrow(start=startpos, end=endpos, buff=buffer, color=col)
        return arw

    def run_anim(self):
        self.Sk = Tex(r"$\hat{S}_k$").shift(UP * 2)
        self.sirkle = Circle(0.8, color=BLUE_A, fill_opacity=0.3, stroke_color=BLUE_B).shift(UP * 2)
        self.vgrp1 = VGroup(self.Sk, self.sirkle)
        self.play(Create(self.Sk), GrowFromCenter(self.sirkle))

        self.wait(1)

        self.reads = VGroup()
        ap = [[-10, 0], [10, 0], [0, 0], [5, 0], [-5, 0], [3, -2], [-3, -2], [6, -2], [9, -2], [-6, -2], [-0, -2]]
        for i in ap:
            if i[1] == 0:
                rect = self.makerect(0.5 * i[0], 0.2 * i[1])
                self.reads.add(rect)
            elif i[1] == -2:
                rect = self.makerect(0.8 * i[0] - 1.3, 0.2 * i[1])
                self.reads.add(rect)
            self.play(Create(rect), run_time=0.1)
        self.wait(2)

        center = self.sirkle.get_center()

        for (x, y) in zip(self.reads.submobjects, range(len(self.reads.submobjects))):
            if y % 3 == 0:
                arw = self.makeArrow(center, x.get_center(), GREEN, 1)
                self.play(x.animate.set_fill(GREEN, opacity=0.5), Create(arw), run_time=0.7)
                self.wait(0.5)
                self.play(FadeOut(arw), run_time=0.7)
            else:
                arw = self.makeArrow(center, x.get_center(), RED, 1)
                self.play(x.animate.set_fill(RED, opacity=0.5), Create(arw), run_time=0.7)
                self.wait(0.5)
                self.play(FadeOut(arw), run_time=0.7)

        self.wait(1)

        self.play(ScaleInPlace(self.vgrp1, 0.5), self.reads.animate.scale(0.5), self.vgrp1.animate.shift(LEFT * 2), self.reads.animate.shift(LEFT * 2), run_time=0.5)
        self.wait(1)

        self.reads2 = self.reads.copy()
        self.play(Uncreate(self.reads2))

        center = self.sirkle.get_center()

        for i in self.reads2.submobjects:
            i.set_fill(color=LIGHTER_GRAY, opacity=0.5)

        for (x, y) in zip(self.reads2.submobjects, range(len(self.reads2.submobjects))):
            if y % 2 == 0:
                arw = self.makeArrow(center, x.get_center(), GREEN, 0.5)
                self.play(x.animate.set_fill(GREEN, opacity=0.5), Create(arw), run_time=0.7)
                self.wait(0.5)
                self.play(FadeOut(arw))
            else:
                arw = self.makeArrow(center, x.get_center(), RED, 0.5)
                self.play(x.animate.set_fill(RED, opacity=0.5), Create(arw), run_time=0.7)
                self.wait(0.5)
                self.play(FadeOut(arw))

        self.play(FadeOut(self.vgrp1), FadeOut(self.reads2))

    def make_text(self):
        text = Text("I wanna curl up into \n a ball and die :D")
        self.play(Write(text))

    def construct(self):
        self.run_anim()
        self.make_text()
