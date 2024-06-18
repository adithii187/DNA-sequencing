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

# class final(ThreeDScene):
#     def construct(self):
#         # move.construct(self,super())
#         welcome.construct(self)
#         introductions.construct(self)
#         move_scene = move()
#         move_scene.construct(self)
        # erasures_scene = erasures()
        # erasures_scene.construct(self)

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
                    

    def run_anim(self,scene,v_shift,l_shift,no_shitf):
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
        if(not no_shitf):
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


                    self.square = Square(1,stroke_color=col).shift(2*DOWN + (x+1)*0.75 * UP + (0.5*(pos+idx)-3 -3.5)*RIGHT).scale(0.5)
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
        arrowR = Arrow(start=[1, 0, 0], end=[3, 0, 0]).shift(DOWN*1)
        arrowL = Arrow(start=[-1, 0, 0], end=[-3, 0, 0]).shift(DOWN*1)
        L = Text("L").shift(DOWN*1)
        crit = Tex("$ >\ \hspace{4mm} l_{crit}$").shift(RIGHT*1)
        scene.play(Write(arrowL), Write(arrowR), Write(L))
        scene.play(FadeOut(self.flagged), FadeOut(arrowL), FadeOut(arrowR))
        scene.play(ApplyMethod(L.scale, 3), ApplyMethod(L.move_to, ORIGIN+LEFT*1))
        scene.play(Write(crit))
        

        scene.play(FadeOut(crit),FadeOut(L))


class move(Scene):
    def construct(self):
        V_genome = "ATGGCTAACCTTTGGCTGAAATGCCCGT"
        self.scene = super()
        self.seq = genome(V_genome)

        self.seq.run_anim(self.scene,0,3.5,False)
        # self.play(seq.Box_grp.animate.shift(2*UP))
        self.seq.make_subseq(self.scene)

        self.seq.l_crit(self.scene)
        # for x in range(5):
            # pos = randint(0,21)
            # self.shotgunned = genome(V_genome[pos:pos+5])
            # self.shotgunned.run_anim(super(),0.5*x+1,pos/5)


class mainResult(MovingCameraScene):

    def makerect(self,hshift,vshift):
        rect = Rectangle(height=0.2,width=2,stroke_color=LIGHT_GRAY).shift(UP*vshift+RIGHT*hshift+DOWN*2).set_fill(color=LIGHTER_GRAY,opacity=0.5)
        return rect

    def makeArrrow(self,startpos,endpos,col,buffer):
        arw = Arrow(start=startpos,end=endpos,buff=buffer,color=col)
        return arw
    
    # @ray.remote
    def run_anim(self):
        self.Sk = Tex(r"$\hat{S}_k$").shift(UP*2)
        self.sirkle = Circle(0.8,color=BLUE_A,fill_opacity=0.3,stroke_color=BLUE_B).shift(UP*2)
        self.vgrp1 = VGroup(self.Sk,self.sirkle)
        self.play(Create(self.Sk),GrowFromCenter(self.sirkle))

        self.wait(1)
        
        self.reads = VGroup()
        ap=[[-10,0],[10,0],[0,0],[5,0],[-5,0],[3,-2],[-3,-2],[6,-2],[9,-2],[-6,-2],[-0,-2]]
        for i in ap:
            if(i[1]==0):
                rect = self.makerect(0.5*i[0],0.2*i[1])
                self.reads.add(rect)
            elif(i[1]==-2):
                rect = self.makerect(0.8*i[0]-1.3,0.2*i[1])
                self.reads.add(rect)
            self.play(Create(rect),run_time=0.1)
        self.wait(2)

        center = self.sirkle.get_center()

        # self.play(Create(self.makeArrrow(center,)))

        for (x,y) in zip(self.reads.submobjects,range(len(self.reads.submobjects))):
            if(y%3==0):
                arw = self.makeArrrow(center,x.get_center(),GREEN,1)
                self.play(x.animate.set_fill(GREEN,opacity=0.5),Write(arw),run_time=0.7)
                self.wait(0.5)
                self.play(FadeOut(arw),run_time=0.7)
                # x.set_fill(color = LIGHTER_GREY, opacity =0.5)
            else:
                arw = self.makeArrrow(center,x.get_center(),RED,1)
                self.play(x.animate.set_fill(RED,opacity=0.5),Write(arw),run_time=0.7)
                self.wait(0.5)
                self.play(FadeOut(arw),run_time=0.7)
                # x.set_fill(color = LIGHTER_GREY, opacity =0.5)


        self.wait(1)

        self.play(Uncreate(self.reads))

        center = self.sirkle.get_center()

        self.camera.frame.save_state()

        self.play(self.camera.frame.animate.scale(1.5))
        self.play(self.camera.frame.animate.shift(RIGHT*3))



        radius_eqn,setu_eqn = self.maketext()

        self.reads = VGroup()
        ap=[[-10,0],[10,0],[0,0],[5,0],[-5,0],[3,-2],[-3,-2],[6,-2],[9,-2],[-6,-2],[-0,-2]]
        for i in ap:
            if(i[1]==0):
                rect = self.makerect(0.5*i[0],0.2*i[1])
                self.reads.add(rect)
            elif(i[1]==-2):
                rect = self.makerect(0.8*i[0]-1.3,0.2*i[1])
                self.reads.add(rect)
            self.play(Create(rect),run_time=0.1)
        self.wait(2)

        center = self.sirkle.get_center()

        # self.play(Create(self.makeArrrow(center,)))

        for (x,y) in zip(self.reads.submobjects,range(len(self.reads.submobjects))):
            if(y%3==0):
                arw = self.makeArrrow(center,x.get_center(),GREEN,1)
                self.play(x.animate.set_fill(GREEN,opacity=0.5),Write(arw),run_time=0.7)
                self.wait(0.5)
                self.play(FadeOut(arw),run_time=0.7)
                # x.set_fill(color = LIGHTER_GREY, opacity =0.5)
            else:
                arw = self.makeArrrow(center,x.get_center(),RED,1)
                self.play(x.animate.set_fill(RED,opacity=0.5),Write(arw),run_time=0.7)
                self.wait(0.5)
                self.play(FadeOut(arw),run_time=0.7)

        self.anim = VGroup(self.vgrp1,self.reads)

        self.play(FadeOut(self.anim))

        self.play(self.camera.frame.animate.shift(RIGHT*3))

        self.play(Uncreate(radius_eqn),Uncreate(setu_eqn))
        self.wait(1)

        Restore(self.camera.frame)
        self.Vs = Tex(r"$\mathbb(V_s)(r,l)\ :=\ max \{|\mathcal{U}|\ :\ \mathcal{U}\ \subset\ S_l(\mathbb{S}),\ \rho(\mathcal{U})\} \le\ r $",font_size=79).shift(RIGHT*5.5)
        self.play(FadeIn(self.Vs, run_time=0.5))
        self. wait(3)
        self.play(FadeOut(self.Vs, run_time=0.5))


    def maketext(self):
        text = Text("I wanna curl up into \n a ball and die :D").shift(RIGHT*6)
        self.play(Write(text))
        self.play(Uncreate(text))

        setu = Tex(r"$\mathcal{U} \subset \Sigma^l $",font_size=96).shift(RIGHT*7)
        self.play(GrowFromEdge(setu,LEFT))
        self.play(setu.animate.shift(UP*1.5))
        radius = Tex(r"$\rho (\mathcal{U}) = min_{\textbf{x}\in \Sigma^l} max_{\textbf{y} \subset \mathcal{U}} d_H(\textbf{x},\textbf{y})$",font_size=70).shift(RIGHT*7)
        self.play(Create(radius))

        return radius,setu

    def construct(self):
        self.run_anim()

    
        
class VS(ThreeDScene):
    def scatterplot(self):

        coords = [[-1.5, 0.5, 1.8],
                [-2.1, -1.2, 0.7],
                [-0.7, -2.4, -2.3],
                [2.0, 1.3, -0.5],
                [0.4, -1.8, 1.9],
                [2.2, 1.9, 0.2],
                [0.6, -0.3, -2.1],
                [-1.8, 2.1, -0.9],
                [1.3, 0.1, -2.4],
                [-2.3, 1.4, 1.0],
                [-1.3, 0.4, 1.7],
                [-1.6, 0.8, 2.0],
                [-1.4, 0.6, 1.9],
                [-1.5, 0.3, 1.7],
                [-1.7, 0.5, 1.5]]

        slplot = VGroup()
        for x in coords:
            # datapoint = Dot3D(point=self.axes.coords_to_point(x),color=RED)
            datapoint = Dot3D(point=x,color=RED)

            self.play(Create(datapoint),run_time=0.1)
            slplot+=datapoint
        self.wait(1)
        return slplot
        # self.play(Uncreate(self.slplot))

    def isinside(self,datapoint):
        if(
            (self.spier.get_center()[0]-datapoint.get_center()[0])**2 + (self.spier.get_center()[1]-datapoint.get_center()[1])**2 
            + (self.spier.get_center()[2]-datapoint.get_center()[2])**2 < 1
        ):
            return True
        else:
            return False
    
    def construct(self):
        self.axes = ThreeDAxes(fill_color=BLUE)


        self.move_camera(phi = 75*DEGREES,theta = 45*DEGREES)
        
        self.play(Create(self.axes))
        self.points = self.scatterplot()
        self.wait(1)
        random_dot = randint(0,10)
        self.spier = Sphere(radius = 1,fill_opacity=0.1,center=[-1.5, 0.5, 1.8])
        self.play(Create(self.spier))
        self.begin_ambient_camera_rotation(rate=1,about="theta")

        for datapoint in self.points.submobjects:
            if(self.isinside(datapoint)):
                self.play(datapoint.animate.set_color(GREEN))
                print(np.array(datapoint.get_center()))
        
        self.wait(1)
        self.stop_ambient_camera_rotation()
        self.wait(2)
        self.play(FadeOut(self.points),Uncreate(self.axes),FadeOut(self.spier))

        self.eqn = Tex(
            r"""\begin{eqnarray*}
            \mathcal{G}(p,L,W) :=
            \{s : V_s(pL,L-W+1) \} 
              \end{eqnarray*}"""
        )

        # self.set_to_default_angled_camera_orientation()
        self.set_camera_orientation(phi=0,theta=-PI/2)

        self.play(Create(self.eqn))
        self.wait(4)
        self.play(self.eqn.animate.shift(DOWN*2))
        table = ImageMobject("table1.png").move_to(ORIGIN).scale(1.5)
        self.add(table)
        eqn2 = Tex(
            r"""\begin{eqnarray*}
            V_s(pL,L-W+1) \le 4 \} 
              \end{eqnarray*}"""
        ).shift(DOWN*2)
        self.wait(2)
        self.play(Transform(self.eqn,eqn2))
        eqn3 = Tex(
            r"""\begin{eqnarray*}
            s \in \mathcal{G}(p,L,W) \implies p<\frac{1}{4} 
              \end{eqnarray*}"""
        ).shift(DOWN*2)
        self.play(Transform(self.eqn,eqn3))
        self.wait(1)

class erasures(Scene):
    def get_color(self,y):
        if y == "A":
            return GREEN
        elif y == "T":
            return RED
        elif y == "C":
            return ORANGE
        elif y == "G":
            return BLUE
        elif y == "$\epsilon$":
            return RED

    def makebox(self,x,y,v_shift):
        col = self.get_color(y)
        self.square = Square(1,stroke_color=col).shift((0.5*x-3)*RIGHT+v_shift*UP).scale(0.5)
        self.square.set_fill(col,opacity=0.2)
            
        return self.square

    def maketext(self,x,y,v_shift,):
        col = self.get_color(y)
        self.V_txt = Text(y,font_size=50,color=col).shift((0.5*x-3)*RIGHT+v_shift*UP).scale(0.5)

        return self.V_txt
    
    def makeTex(self,x,y,v_shift):
        col = self.get_color(y)
        self.V_tex = Tex(y,font_size=96,color=col).shift((0.5*x-3)*RIGHT+v_shift*UP).scale(0.5)
        return self.V_tex

    def construct(self):

        self.seq = "CCTAAGGTCCCTGA"
        self.v_shift = 0
        self.l_shift = 0
        self.obj_genome = VGroup()

        list_of_genes = []  
        list_of_erasures = []  


        for (x,y) in zip(range(len(self.seq)),self.seq):

            box = self.makebox(x,y,self.v_shift)
            text = self.maketext(x,y,self.v_shift)
            dna_obj = VGroup(box,text)
            list_of_genes.append(dna_obj)   

            box = self.makebox(x,"$\epsilons$",self.v_shift)
            tex = self.makeTex(x,"$\epsilon$",self.v_shift)
            dna_obj_erased = VGroup(box,tex)
            list_of_erasures.append(dna_obj_erased)

            self.obj_genome += dna_obj
            self.obj_genome += dna_obj_erased

            # self.obj_genome += dna_obj
            self.play(Create(box),Write(text),run_time=0.2)
            # scene.play(self.obj_genome.animate.shift(x*LEFT))
            # scene.play(dna_obj.animate.shift(2*LEFT),run_time=0.5)
            self.play(dna_obj.animate.shift((self.l_shift)*LEFT+self.v_shift*UP),run_time=0.2)
        
        

        self.play(ReplacementTransform(list_of_genes[2],list_of_erasures[2]))
        self.play(ReplacementTransform(list_of_genes[6],list_of_erasures[6]))
        self.play(ReplacementTransform(list_of_genes[7],list_of_erasures[7]))
        self.play(ReplacementTransform(list_of_genes[9],list_of_erasures[9]))
        self.play(FadeOut(self.obj_genome))
        self.wait(1)


class Kspectrum(Scene):
    def construct(self):
        self.rect = Rectangle(height=0.5,width=13,stroke_color=RED).shift(DOWN*2.5).set_fill(RED,opacity=0.4)
        self.play(Create(self.rect))
        # for (x,y) in zip(range(len(sequence)),sequence):
        startpos1 = LEFT*5
        # startpos2 = LEFT*2
        for i in range(5):
            if(i==0):
                continue
            rect = Rectangle(height=0.5,width=(0.5*i)-0.05,stroke_color=LIGHT_GRAY).shift(DOWN*2+startpos1+UP*(0.6*i+0.5)+RIGHT*(0.25*i)+LEFT*(1.55)).set_fill(LIGHTER_GRAY,opacity=0.4)
            self.play(GrowFromEdge(rect,LEFT),run_time=0.3)
        for i in range(5):
            rect = Rectangle(height=0.5,width=2.5,stroke_color=LIGHT_GRAY).shift(DOWN*2+startpos1+UP*(0.6*i+0.5)+RIGHT*0.5*i+LEFT*(0.25)).set_fill(LIGHTER_GRAY,opacity=0.4)
            self.play(GrowFromEdge(rect,LEFT),run_time=0.3)
        for i in range(5):
            rect = Rectangle(height=0.5,width=2.5,stroke_color=LIGHT_GRAY).shift(DOWN*2+startpos1+(RIGHT*2.6)+UP*(0.6*i+0.5)+RIGHT*0.5*i+LEFT*(0.25)).set_fill(LIGHTER_GRAY,opacity=0.4)
            self.play(GrowFromEdge(rect,LEFT),run_time=0.3)
        for i in range(5):
            rect = Rectangle(height=0.5,width=2.5,stroke_color=LIGHT_GRAY).shift(DOWN*2+startpos1+(RIGHT*5.2)+UP*(0.6*i+0.5)+RIGHT*0.5*i+LEFT*(0.25)).set_fill(LIGHTER_GRAY,opacity=0.4)
            self.play(GrowFromEdge(rect,LEFT),run_time=0.3)
        for i in range(5):
            rect = Rectangle(height=0.5,width=2.5,stroke_color=LIGHT_GRAY).shift(DOWN*2+startpos1+(RIGHT*7.8)+UP*(0.6*i+0.5)+RIGHT*0.5*i+LEFT*(0.25)).set_fill(LIGHTER_GRAY,opacity=0.4)
            self.play(GrowFromEdge(rect,LEFT),run_time=0.3)
        for i in range(5):
            rect = Rectangle(height=0.5,width=0.5*(5-i),stroke_color=LIGHT_GRAY).shift(DOWN*2+startpos1+(RIGHT*10.4)+UP*(0.6*i+0.5)+RIGHT*(0.25*i)+LEFT*(0.25)).set_fill(LIGHTER_GRAY,opacity=0.4)
            self.play(GrowFromEdge(rect,LEFT),run_time=0.3)
            

class AEM(Scene):
    def construct(self):
        text1 = Tex(r"\(\Sigma ' := \{A,G,T,C,\epsilon \} \)",font_size=50)
        self.play(Create(text1))
        self.wait(3)
        self.play(text1.animate.shift(UP*2))
        text2 = Tex(r"r$_i$ = (r$_i$[0], . . . , r$_i$[L-1]) \\ where either r$_i$[j] = s[i+j] or r$_i$[j] = $\epsilon$,\\ for 1 $\le$ i $\le$ G and 0 $\le$  j $\le$ L - 1.")
        self.play(Create(text2))
        self.wait(3)
        self.play(text1.animate.shift(UP*3),text2.animate.shift(UP*2))
        text3 = Tex(r"let $R^W_{\tau}$  be the set of reads with starting positions in\\ s[$\tau$], s[$\tau$ + 1], . . . , s[$\tau$ + W - 1] \\($R^W_{\tau}$ is not known by the assembler)\\ we have $|R^W_{\tau}| \ge 1$ for $\tau$ = 1,2,3...G ",font_size=50).shift(DOWN*1)
        self.play(Create(text3))
        self.wait(7)
        text4 = Tex(r"$\cdot$ There are at most $pL$ erasures per read").move_to(text3.get_center())
        text5 = Tex(r"$\cdot$ Each base s[t] is erased at most a fraction p\\ of the total reads in $R^W_{\tau}$ times for $t-L < \tau \le t-W+1$").move_to(text3.get_center())

        textgrp1 = VGroup(text4,text5)
        self.play(Uncreate(text3))
        self.play(Create(text4))
        self.wait(1)
        self.play(text4.animate.shift(UP*1))
        self.play(Create(text5))
        self.wait(7)

        image = ImageMobject("aemmodel.png").scale(2).move_to(text2.get_center())
        self.play(FadeIn(image),FadeOut(text2))
        self.wait(2)
        self.play(textgrp1.animate.shift(DOWN*7),image.animate.shift(DOWN*2))
        self.play(image.animate.scale(1.2))
        self.wait(1)
        

class MRS(MovingCameraScene):
    def makerect(self,hshift,vshift,erasures):
        # rect = Rectangle(height=0.2,width=2,stroke_color=LIGHT_GRAY).shift(UP*vshift+RIGHT*hshift+DOWN*2).set_fill(color=LIGHTER_GRAY,opacity=0.5)
        rect = Rectangle(height=0.2,width=2,stroke_color=LIGHT_GRAY).move_to([hshift,vshift,0]).set_fill(color=LIGHTER_GRAY,opacity=0.5).shift(DOWN*2)
        erasure = Square(0.2,stroke_color=LIGHT_GRAY).move_to(rect.get_center()).shift(LEFT*(erasures/1.9)).set_fill(color=RED,opacity=0.7)
        read = VGroup(rect,erasure)
        return read

    def construct(self):
        self.Sk = Tex(r"$\mathbb{R}(s,p,W)$").shift(UP*2).scale(0.9)
        self.sirkle = Circle(1.1,color=BLUE_A,fill_opacity=0.3,stroke_color=BLUE_B).shift(UP*2)
        self.vgrp1 = VGroup(self.Sk,self.sirkle)
        self.play(Create(self.Sk),GrowFromCenter(self.sirkle))

        self.wait(1)
        
        self.rspw = VGroup()
        poslist=[[[-10,0,2],[10,0,0],[0,0,1],[5,0,0],[-5,0,-1],[3,-2,1],[-3,-2,0],[6,-2,1],[9,-2,-2],[-6,-2,-2],[-0,-2,-2]],
                 [[-10,-2,2],[10,0,0],[0,-4,1],[5,0,0],[-5,-4,-1],[3,-2,1],[-3,-0,0],[6,-4,1],[9,-2,-2],[-6,-2,-2],[-0,-2,-2]],
                 [[-10,-4,2],[10,-4,0],[0,-4,1],[5,0,0],[-5,0,-1],[3,-2,1],[-3,-4,0],[6,-2,1],[9,-2,-2],[-6,-2,-2],[-0,-2,-2]],
                 [[-10,0,0],[10,0,-2],[0,0,-2],[5,0,-1],[-5,0,-1],[3,-2,2],[-3,-2,0],[6,-2,-2],[9,-2,-2],[-6,-2,-1],[-0,-2,0]],
                 [[-10,-2,-1],[10,0,1],[0,-4,1],[5,0,0],[-5,-4,-1],[3,-2,-2],[-3,-0,0],[6,-4,0],[9,-2,-2],[-6,-2,0],[-0,-2,-2]],
                 [[-10,-4,2],[10,-4,2],[0,-4,0],[5,0,2],[-5,0,-1],[3,-2,0],[-3,-4,1],[6,-2,1],[9,-2,-2],[-6,-2,-2],[-0,-2,-2]],]

        for x in poslist:
            self.read1 = VGroup()
            ap=x
            for i in ap:
                print(i)
                if(i[1]==0):
                    rect = self.makerect(0.5*i[0],0.2*i[1],i[2])
                    self.read1.add(rect)
                elif(i[1]==-2):
                    rect = self.makerect(0.8*i[0]-1.3,0.2*i[1],i[2])
                    self.read1.add(rect)
                elif(i[1]==-4):
                    rect = self.makerect(-0.8*i[0]-2.3,0.2*i[1],i[2])
                    self.read1.add(rect)
                self.play(Create(rect),run_time=0.05)
            self.wait(1)
            self.read1.generate_target()
            self.read1.target.scale(0).move_to(self.sirkle.get_center())

            self.read1.save_state()
            self.play(MoveToTarget(self.read1),run_time=0.5)
            self.play(FadeOut(self.read1))
            self.rspw.add(self.read1)

        # self.play(FadeIn(self.read1))
        # self.play(Restore(self.read1))
        self.play(self.vgrp1.animate.shift(LEFT*4+DOWN*2))
        self.rspw.shift(LEFT*4+DOWN*2)


        kstar = Tex(
            r"$K^*(p,W) =$\\$ min_{s,\mathcal{R}\subset \mathbb{R}(s,p,W)}max\{k: \mathcal{R} \implies supp(\mathcal{S}_k)\}$",
            font_size=45
            ).shift(RIGHT*2.5)
        self.play(Create(kstar))
        self.wait(5)
        kstar2 = Tex(
            r"$K^*(p,W)$",font_size=96
        ).move_to(ORIGIN)

        eqn = Tex(r"$min(L-W+1,\lceil \frac{1}{p} \rceil ) \le K^*(p,W) \le L-W+1 $",font_size=70)


        self.play(Restore(self.rspw.submobjects[3]))            
        bracket = Brace(self.rspw.submobjects[3],UP,stroke_width=2,buff=0.5)
        self.wait(1)
        self.play(Uncreate(self.vgrp1))
        self.play(self.camera.frame.animate.scale(1.5))
        self.play(Transform(kstar,kstar2),Create(bracket))
        self.wait(3)

        self.play(Uncreate(bracket),Uncreate(self.rspw.submobjects[3]))
        self.play(Transform(kstar,eqn))
        # self.play(Uncreate(eqn))
        self.wait(1)

class worstcase(MovingCameraScene):
    def makegenome(self):
        sequence = Tex(r"A T T T $\epsilon$ G C A A C C")
        rect = Rectangle(height=0.5,width=6,stroke_color=LIGHT_GRAY).set_fill(LIGHTER_GRAY,opacity = 0.5)
        square = Square(0.5,stroke_color=LIGHT_GRAY).move_to(rect.get_center()).set_fill(RED,opacity=0.5).shift(LEFT*0.55)
        self.genome = VGroup(rect,square,sequence)
        return self.genome
    
    def makenoisygenome(self):
        sequence = Tex(r"A $\epsilon$ T T $\epsilon$ G C $\epsilon$ A C C")
        rect = Rectangle(height=0.5,width=5.5,stroke_color=LIGHT_GRAY).set_fill(LIGHTER_GRAY,opacity = 0.5)
        square1 = Square(0.5,stroke_color=LIGHT_GRAY).move_to(rect.get_center()).set_fill(RED,opacity=0.5).shift(LEFT*0.55)
        square2 = Square(0.5,stroke_color=LIGHT_GRAY).move_to(rect.get_center()).set_fill(RED,opacity=0.5).shift(LEFT*1.95)
        square3 = Square(0.5,stroke_color=LIGHT_GRAY).move_to(rect.get_center()).set_fill(RED,opacity=0.5).shift(RIGHT*0.95)

        self.genome = VGroup(rect,square1,square2,square3,sequence)
        return self.genome
        
    def makearrow(self,position):
        arrow = Arrow(end=[position,0,0],start=[position,-3,0],buff=1)
        return arrow

    def construct(self):
        genome = self.makegenome()
        genome2 = self.makenoisygenome()
        self.play(GrowFromCenter(genome))
        self.wait(1)

        self.condition = Tex(
            r"""consistency:
            \begin{gather*}
            x_i[t] \in \Sigma '\\
            \Sigma ' = \{A,T,G,C,\epsilon \}
            \end{gather*}
            """
        ).shift(UP*2)

        self.play(Create(self.condition))
        
        position = genome.get_edge_center(LEFT)[0] + 0.4
        for x in range(11):
            arr = self.makearrow(position+x*0.525)
            self.play(Write(arr),run_time=0.1)
            self.wait(0.1)
            self.play(Uncreate(arr),run_time=0.1)

        condition2 = Tex(
            r"""
            horizontal constraint:\\
            $|t:x_i[t] = \epsilon| \le D_h $\\
            for $1 \le i \le m$
            """
        ).shift(UP*2)

        count = Text("Count: ").shift(DOWN*3+LEFT*3)
        self.countval = Text(str(0)).next_to(count)
        self.countval.save_state()
        dh = Tex(r"$\le D_h$").next_to(self.countval)
        self.play(Transform(self.condition,condition2),Transform(genome,genome2),Write(count),Write(self.countval),Create(dh))
        self.wait(1)




        position = genome.get_edge_center(LEFT)[0] + 0.4
        y=1;
        for x in range(11):
            arr = self.makearrow(position+x*0.525)
            self.play(Write(arr),run_time=0.1)
            countval = Text(str(y)).next_to(count)
            if(x==1 or x==4 or x==7):
                self.play(Transform(self.countval,countval),run_time=0.1)
                y+=1
            self.wait(0.1)
            self.play(Uncreate(arr),run_time=0.1)


        condition3 = Tex(
            r"""
            Vertical constraint:\\
            $|i:x_i[t] = \epsilon| \le D_v $\\
            for $1 \le t \le k$
            """
        ).shift(UP*2)

        g1 = self.makenoisygenome().shift(RIGHT*1)
        g2 = self.makenoisygenome().shift(LEFT*1+UP*0.5)
        g3 = self.makenoisygenome().shift(RIGHT*2+UP*1)
        g4 = self.makenoisygenome().shift(LEFT*2+DOWN*0.5)

        genome3 = VGroup(g1,g2,g3,g4).shift(DOWN*0.5)

        
        self.play(Restore(self.countval))

        dv = Tex(r"$\le D_v$").next_to(self.countval)
        self.play(Transform(self.condition,condition3),Transform(genome,genome3),Transform(dh,dv))
        self.wait(1)
        
        position2 = genome3.get_edge_center(LEFT)[0]+0.4

        countlist=[1,2,1]
        z=0
        for x in range(18):
            arr = self.makearrow(position2+x*0.525).shift(DOWN*0.5)
            self.play(Write(arr),run_time=0.1)
            if(x==1 or x==6 or x==9):
                countval = Text(str(countlist[z])).next_to(count)
                self.play(Transform(self.countval,countval),run_time=0.1)
                z+=1
            self.wait(0.1)
            self.play(Uncreate(arr),run_time=0.1)
        self.wait(1)
        


        
