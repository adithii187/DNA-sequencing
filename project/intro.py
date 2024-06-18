from manim import *

class welcome(Scene):
    def construct(self):
        text = Text("Welcome",stroke_width=0.5)
        self.play(Write(text),run_time=0.7)
        self.wait()
        self.play(FadeOut(text),run_time=0.7)

class introductions(Scene):
    def construct(self):
        paper = Text("Fundamental limits of Genome Assembly Under an Adversarial Model")
        by = Text("")
        autrio = Text("Autrio",stroke_width=0.2).to_edge(DR)
        adithi = Text("Adithi",stroke_width=0.2).to_edge(DR).shift(1*UP)
        self.play(Write(autrio),run_time=0.7)
        self.play(Write(adithi),run_time=0.7)
        self.wait()
        # self.play(autrio.animate.fade_out(),adithi.animate.fade_out())
        self.play(FadeOut(autrio),FadeOut(adithi),run_time=0.7)
        # self.play(FadeOut(adithi))


class project(Scene):
    def construct(self):
        welcome.construct(self)
        introductions.construct(self)
