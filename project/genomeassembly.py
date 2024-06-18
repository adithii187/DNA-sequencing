from manim import *


class MySquare:
    def __init__(self, i):
        self.data = Square(1,stroke_color=GREEN).shift(i*RIGHT)

    def create(self,scene):
        scene.play(Create(self.data))

 
    def move(self,scene):
        scene.play(self.data.animate.shift(2*LEFT))

class genome:
    def __init__(self,arg_seq):
        self.genome = VGroup()
        self.arg_seq = arg_seq

    def makebox(self,x,y):

        global col
        if y == "A":
            col = GREEN
        elif y == "T":
            col = RED
        elif y == "C":
            col = ORANGE
        elif y == "G":
            col = BLUE

        self.square = Square(1,stroke_color=col).shift(x*RIGHT)
        self.square.set_fill(col,opacity=0.3)
            
        return self.square

    def maketext(self,x,y):

        global col
        if y == "A":
            col = GREEN
        elif y == "T":
            col = RED
        elif y == "C":
            col = ORANGE
        elif y == "G":
            col = BLUE        
        
        self.V_txt = Text(y,font_size=50,color=col).shift(x*RIGHT)

        return self.V_txt
                     

    def run_anim(self,scene):
        for (x,y) in zip(range(len(self.arg_seq)),self.arg_seq):
            box = self.makebox(x,y)
            text = self.maketext(x,y)

            dna_obj = VGroup(box,text)

            self.genome += dna_obj

            scene.play(Create(box),Write(text))
            scene.play(dna_obj.animate.shift(2*LEFT))
            # scene.play(Write(text))
             



# class makegenome(Scene):

#     def __init__(self,arg_seq):
#         self.text_grp = VGroup()
#         self.Box_grp = VGroup()
#         self.construct()

#     def construct(self,arg_seq):

        
#         V_genome = ["A","T","G","C"]
#         # V_genome = arg_seq

        

#         for (x,y) in zip(range(4),V_genome):

#                 global col
#                 if y == "A":
#                     col = GREEN
#                 elif y == "T":
#                     col = RED
#                 elif y == "C":
#                     col = ORANGE
#                 elif y == "G":
#                     col = BLUE

#                 square = Square(1,stroke_color=col).shift(x*RIGHT)
#                 square.set_fill(col,opacity=0.3)
                
#                 self.play(Create(square))

#                 self.play(square.animate.shift(2*LEFT))
#                 self.Box_grp.add(square)

#                 V_txt = Text(y,font_size=50,color=col).shift((x-2)*RIGHT)
#                 self.text_grp.add(V_txt)
#                 self.Box_grp+=self.text_grp

#                 self.play(Write(V_txt))

    

#         return self.Box_grp

class move(Scene):
    def construct(self):
        V_genome = ["A","T"]
        self.seq = genome(V_genome)

        # self.vg = VGroup() 

        # for (x,y) in zip(range(4),V_genome):
        #     self.seq.append(MySquare(x))
        #     self.seq[x].create(super())
        #     self.vg.add( self.seq[x].data)
        
        # self.play(self.vg.animate.shift(2*UP))

        self.seq.run_anim(super())
    

        # self.play(seq.Box_grp.animate.shift(2*UP))