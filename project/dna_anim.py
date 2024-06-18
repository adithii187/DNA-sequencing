from manim import *
from random import *
import numpy

class genome:
    def __init__(self,arg_seq):
        self.obj_genome = VGroup()
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
                    

    def run_anim(self,scene,v_shift,l_shift,no_shift):
        for (x,y) in zip(range(len(self.arg_seq)),self.arg_seq):

            # if(x>=7 & flag!):
            #     self.obj_genome.scale(0.5)

            box = self.makebox(x,y,v_shift)
            text = self.maketext(x,y,v_shift)

            dna_obj = VGroup(box,text)

            self.obj_genome += dna_obj
            scene.play(Create(box),Write(text),run_time=0.2)
            # scene.play(self.obj_genome.animate.shift(x*LEFT))
            # scene.play(dna_obj.animate.shift(2*LEFT),run_time=0.5)
            scene.play(dna_obj.animate.shift((l_shift)*LEFT+v_shift*UP),run_time=0.2)
        if(not no_shift):
            scene.play(self.obj_genome.animate.shift(2*DOWN))
        scene.wait(0.5)
            # scene.play(Write(text))

    def make_subseq(self, scene):
        for a in range(3):  # make this number 5 or 7
            self.subseq = VGroup()
            for x in range(5):
                gene = VGroup()
                pos = randint(0,21-5)
                for idx in range(6):
                    y= self.arg_seq[pos+idx]
                    col = self.get_color(y)


                    self.square = Square(1,stroke_color=col).shift(2*DOWN + (x+1)*0.75 * UP + (0.5*(pos+idx)-3 -3.5)*RIGHT  ).scale(0.5)
                    self.square.set_fill(col,opacity=0.3)
                    self.V_txt = Text(y,font_size=50,color=col).shift(2*DOWN + (x+1)*0.75 * UP + (0.5*(pos+idx)-3 -3.5)*RIGHT).scale(0.5)
                    gene += VGroup(self.square,self.V_txt)
                    scene.play(Create(self.square), Write(self.V_txt), run_time =0.2 )

                if(a==2 and x==2):
                    self.flagged = gene
                else:
                    self.subseq+=gene

                    # self.subseq -= gene

            scene.wait(0.4)
            # if(a!=2):
            #     scene.play(FadeOut(self.subseq),run_time=0.5)
            # else:
            #     scene.wait(1)
            scene.play(FadeOut(self.subseq),run_time=0.5)



    def l_crit(self,scene):
        scene.play(FadeOut(self.obj_genome),run_time=0.5)
        scene.play(ApplyMethod(self.flagged.scale, 2), ApplyMethod(self.flagged.move_to, ORIGIN), run_time=0.5)
        scene.play(self.flagged.animate.scale(2))


            
class move(Scene):
    def construct(self):
        V_genome = "ATGGCTAACCTTTGGCTGAAATGCC"
        self.scene = super()
        self.seq = genome(V_genome)

        self.seq.run_anim(self.scene,0,3.5,1)
        # self.play(seq.Box_grp.animate.shift(2*UP))
        self.seq.make_subseq(self.scene)

        self.seq.l_crit(self.scene)
        # for x in range(5):
            # pos = randint(0,21)
            # self.shotgunned = genome(V_genome[pos:pos+5])
            # self.shotgunned.run_anim(super(),0.5*x+1,pos/5)

# class shotgunning(Scene):
#     def construct(self):
