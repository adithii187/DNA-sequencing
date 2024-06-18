from manim import *
from random import *
import numpy

class welcome(Scene):
    def construct(self):
        text = Text("Welcome",stroke_width=0.5)
        self.play(Write(text),run_time=0.7)
        self.wait()
        self.play(FadeOut(text),run_time=0.7)

class introductions(Scene):
    def construct(self):
        paper1 = Text("Fundamental limits of Genome Assembly", stroke_width = 0.3,).shift(2.5*UP) 
        paper1.set_color_by_gradient(BLUE, RED)
        
        paper2 = Text("Under an Adversarial Model", stroke_width= 0.3).next_to(paper1, DOWN)
        paper2.set_color_by_gradient(BLUE, RED)

        by = Text("by").to_edge(DR).shift(1*UP).scale(0.5)
        autrio = Text("Autrio",stroke_width=0.2).to_edge(DR).shift(0.5*UP).scale(0.5)
        adithi = Text("Adithi",stroke_width=0.2).to_edge(DR).scale(0.5).shift(0.25*DOWN)
        # self.add(paper1, paper2)
        # self.play(Write(paper1), run_time = 0.7)
        # self.play(Write(paper2), run_time = 0.7)
        self.play(Write(paper1), Write(paper2))
        self.play(Write(by), run_time=0.7)
        self.play(Write(autrio),run_time=0.7)
        self.play(Write(adithi),run_time=0.7)
        self.wait()
        # self.play(autrio.animate.fade_out(),adithi.animate.fade_out())
        self.play(FadeOut(by), FadeOut(autrio),FadeOut(adithi), FadeOut(paper2), FadeOut(paper1),run_time=0.7)
        # self.play(FadeOut(adithi))
        
class genome:
    def __init__(self,arg_seq):
        self.genome_obj = VGroup()
        self.arg_seq = arg_seq
    def get_color(self,y):
        if y == "A":
            return GREEN
        elif y == "T":
            return RED
        elif y == "C":
            return ORANGE
        elif y == "G":
            return BLUE

    def makebox(self,x,y,v_shift):
        col = self.get_color(y)
        self.square = Square(1,stroke_color=col).shift((0.5*x-3)*RIGHT+v_shift*UP).scale(0.5)
        self.square.set_fill(col,opacity=0.3)
            
        return self.square

    def maketext(self,x,y,v_shift,):

        col = self.get_color(y)
        self.V_txt = Text(y,font_size=50,color=col).shift((0.5*x-3)*RIGHT+v_shift*UP).scale(0.5)

        return self.V_txt
                     
    def run_anim(self,scene,v_shift,l_shift):
        for (x,y) in zip(range(len(self.arg_seq)),self.arg_seq):

            box = self.makebox(x,y,v_shift)
            text = self.maketext(x,y,v_shift)

            dna_obj = VGroup(box,text)

            self.genome_obj += dna_obj
            scene.play(Create(box),Write(text),run_time=0.2)
            # scene.play(self.genome_obj.animate.shift(x*LEFT))
            # scene.play(dna_obj.animate.shift(2*LEFT),run_time=0.5)
            scene.play(dna_obj.animate.shift((l_shift)*LEFT+v_shift*UP),run_time=0.2)
        scene.play(self.genome_obj.animate.shift(2*DOWN))
        scene.wait(0.5)
            # scene.play(Write(text))

    # from manim import *

# class MyScene(Scene):
    # class MyScene(Scene):
    def make_subseq(self, scene):
        subseq = VGroup()  # Create a VGroup to hold all genes
        highlighted_gene = None  # Initialize the variable to hold the highlighted gene
        for a in range(3):  # make this number 5 or 7
            for x in range(5):
                gene = VGroup()
                pos = randint(0, 19)
                for idx in range(6):
                    y = self.arg_seq[pos + idx]
                    col = self.get_color(y)

                    square = Square(1, stroke_color=col).shift(2 * DOWN + (x + 1) * 0.75 * UP + (0.5 * (pos + idx) - 3 - 3.5) * RIGHT).scale(0.5)
                    square.set_fill(col, opacity=0.3)
                    V_txt = Text(y, font_size=50, color=col).shift(2 * DOWN + (x + 1) * 0.75 * UP + (0.5 * (pos + idx) - 3 - 3.5) * RIGHT).scale(0.5)
                    gene += VGroup(square, V_txt)
                    if a == 1 and x == 2:  # Customize the condition for the gene you want to highlight
                        highlighted_gene = gene
                    scene.play(Create(square), Write(V_txt), run_time=0.2)
                subseq += gene
            scene.wait(0.4)
            if(a != 2):
                scene.play(FadeOut(subseq),run_time=0.5)
            elif highlighted_gene is not None:
                subseq-=highlighted_gene
                # scene.play(ApplyMethod(subseq.fade, 1), run_time=0.5) 
                scene.play(FadeOut(subseq),run_time=0.5)
                scene.play(ApplyMethod(highlighted_gene.scale, 2), ApplyMethod(highlighted_gene.move_to, ORIGIN), run_time=0.5)  # Zoom in on the highlighted gene

    # def construct(self):
    #     self.make_subseq(self)

    
    # def l_crit(self):


class move(Scene):
    def construct(self):
        welcome.construct(self)
        introductions.construct(self)

        V_genome = "ATGGCTAACCTTTGGCTGAAATGCC"
        self.scene = super()
        self.seq = genome(V_genome)

        self.seq.run_anim(self.scene,0,3.5)
        # self.play(seq.Box_grp.animate.shift(2*UP))
        self.seq.make_subseq(self.scene)
        # self.seq.
        # for x in range(5):
            # pos = randint(0,21)
            # self.shotgunned = genome(V_genome[pos:pos+5])
            # self.shotgunned.run_anim(super(),0.5*x+1,pos/5)

# class shotgunning(Scene):
#     def construct(self):

# class l_crit(Scene):
#     def construct(self):



# class project(Scene):
#     def construct(self):
#         welcome.construct(self)
#         introductions.construct(self)