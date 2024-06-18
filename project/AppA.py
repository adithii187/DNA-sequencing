from manim import *

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
        self.square = Square(1,stroke_color=col).shift((0.75*x-3)*RIGHT+v_shift*UP).scale(0.75)
        self.square.set_fill(col,opacity=0.3)
            
        return self.square

    def maketext(self,x,y,v_shift,):

        col = self.get_color(y)
        self.V_txt = Text(y,font_size=50,color=col).shift((0.75*x-3)*RIGHT+v_shift*UP).scale(0.75)

        return self.V_txt
                    

    def run_anim(self,scene,v_shift,l_shift,no_shift):
        for (x,y) in zip(range(len(self.arg_seq)),self.arg_seq):

            box = self.makebox(x,y,v_shift)
            text = self.maketext(x,y,v_shift)


            dna_obj = VGroup(box,text)
            # crit = Tex("$ >\ \hspace{4mm} l_{crit}$").shift(RIGHT*1)

            self.obj_genome += dna_obj
            scene.play(Create(box),Write(text),run_time=0.01)
            # scene.play(self.obj_genome.animate.shift(x*LEFT))
            # scene.play(dna_obj.animate.shift(2*LEFT),run_time=0.5)
            scene.play(dna_obj.animate.shift((l_shift)*LEFT+v_shift*UP),run_time=0.01)
            # scene.play(Write(arrowL), Write(arrowR), Write(L))
        return self.obj_genome
   
    def written(self, scene):
        a1 = Tex(r"$a_1$").shift((DOWN*1), LEFT*5)
        a2 = Tex(r"$a_2$").shift(DOWN*1, RIGHT*2.5)
        b1 = Tex(r"$b_1$").shift(DOWN*1, LEFT*2)
        b2 = Tex(r"$b_2$").shift(DOWN*1, RIGHT*6)

        arrowRa1 = Arrow(start=[-5, 0, 0], end=[-4, 0, 0], buff=0.2).shift(DOWN*1)
        arrowLa1 = Arrow(start=[-5, 0, 0], end=[-6.5, 0, 0], buff=0.2).shift(DOWN*1)

        arrowRa2 = Arrow(start=[2.5, 0, 0], end=[3.5, 0, 0], buff=0.2).shift(DOWN*1)
        arrowLa2 = Arrow(start=[2.5, 0, 0], end=[1, 0, 0], buff=0.2).shift(DOWN*1)

        arrowRb1 = Arrow(start=[-2, 0, 0], end=[-3.5, 0, 0], buff=0.2).shift(DOWN*1)
        arrowLb1 = Arrow(start=[-2, 0, 0], end=[-0.5, 0, 0], buff=0.2).shift(DOWN*1)

        arrowRb2 = Arrow(start=[6, 0, 0], end=[7, 0, 0], buff=0.2).shift(DOWN*1)
        arrowLb2 = Arrow(start=[6, 0, 0], end=[4, 0, 0], buff=0.2).shift(DOWN*1)
        # scene.play(Create(arrowL))
        # self.expl2 = Tex(r"are \emph{interleaved} if $a_1 < b_1 < a_2 < b_2$").shift(DOWN*3)
        
        scene.play(Write(arrowLa1), Write(arrowRa1),Write(arrowLa2), Write(arrowRa2), Write(arrowLb1), Write(arrowRb1), Write(arrowLb2), Write(arrowRb2), Create(a1), Create(a2), Create(b1), Create(b2))
        scene.wait(1)
        scene.play(FadeOut(arrowLa1), FadeOut(arrowRa1), FadeOut(arrowLa2), FadeOut(arrowLb1), FadeOut(arrowLb2), FadeOut(arrowRa2), FadeOut(arrowRb1), FadeOut(arrowRb2), FadeOut(a1), FadeOut(a2), FadeOut(b1), FadeOut(b2))
        # scene.wait(2)

    def shitface(self,scene):
        scene.play(scene.camera.frame.animate.shift(DOWN*2))
        
    def bruh(self,scene):
        expl1 = Tex(r"Two pairs of repeats $\textbf{s}^l_{a_1}, \textbf{s}^l_{a_2}$ and $\textbf{s}^k_{b_1}, \textbf{s}^k_{b_2}$").shift(DOWN*2)
        expl2 = Tex(r"are \emph{interleaved} if $a_1 < b_1 < a_2 < b_2$").shift(DOWN*3)
        anim = [
            # Write(expl[0]),
            # Write(expl[1]),
            # Wait(0.5),
            FadeOut(expl1[0]),
            FadeOut(expl2[0]),
            # length
        ]
        scene.play(Create(expl1), Create(expl2))
        scene.wait(4)
        scene.play(AnimationGroup(*anim, run_time=1))
        # scene.wait(2)
        length = Tex(r"length = min(l,k)").shift(DOWN*3)
        scene.play(Create(length), run_time=1)
        scene.wait(3)
        scene.play(FadeOut(length))
        tot_length = Tex(r"${l}_{inter}$ $(\textbf{s})$ = max(min(l,k))").shift(DOWN*3)
        scene.play(Create(tot_length))
        scene.wait(3)
        scene.play(FadeOut(tot_length))

        
    def triple(self, scene):
        # scene.play(Write(arrowLa1), Write(arrowRa1),Write(arrowLa2), Write(arrowRa2), Write(arrowLb1), Write(arrowRb1), Write(arrowLb2), Write(arrowRb2), Create(a1), Create(a2), Create(b1), Create(b2))
        arrT1 = Arrow(start=[-3, -2, 0], end=[-3, 0, 0])
        t1 = Tex(r"${t_1}$").shift(DOWN*2).shift(LEFT*3)
        arrT2 = Arrow(start=[2, -2, 0], end=[2, 0, 0])
        t2 = Tex(r"${t_2}$").shift(DOWN*2).shift(RIGHT*2)
        arrT3 = Arrow(start=[4, -2, 0], end=[4, 0, 0])
        t3 = Tex(r"${t_3}$").shift(DOWN*2).shift(RIGHT*4)
        scene.play(Create(arrT1), Create(arrT2), Create(arrT3), Create(t1), Create(t2), Create(t3),run_time=1)
        scene.wait(2)
        scene.play(FadeOut(arrT1), FadeOut(arrT2), FadeOut(arrT3), FadeOut(t1), FadeOut(t2), FadeOut(t3))
        # //transpose invarient
        # lcrit = Tex

    def pic(self,scene):
        img = ImageMobject("image.png").move_to(ORIGIN).scale(3)
        scene.add(img)
        scene.wait(2)
        scene.remove(img)
        

class appa(MovingCameraScene):
    def construct(self):
        V_genome = "ATGGCGGAACGTGGTGGAA"
        self.seq = genome(V_genome)
        to_fade = self.seq.run_anim(self,0,3.75,False)
        self.wait(2)
        self.seq.written(self)
        self.seq.shitface(self)
        self.seq.bruh(self)
        self.seq.triple(self)
        self.play(FadeOut(to_fade))
        self.seq.pic(self)
        
        
        theorem1 = Tex(r"If $k > l_{crit}(\textbf{s})$, then $\textbf{s}$ is the unique sequence with k-spectrum $\mathcal{S}_k$(s). Conversely, if $k \le l_{crit}(\textbf{s})$,, there existssequence $\textbf{s = s'}$ for which $\mathcal{S}_k$(s) = $\mathcal{S}_k$(s').",font_size=40).shift(DOWN*4)
        theorem2 = Tex(r"If $k > l_{crit}^{~}(\textbf{s})$, the Multibridging algorithm correctly assembles s from supp($\mathcal{S}_k$).",font_size=40).shift(DOWN*2)

        self.play(Create(theorem1))
        self.wait(3)
        self.play(Create(theorem2))
        self.wait(3)
