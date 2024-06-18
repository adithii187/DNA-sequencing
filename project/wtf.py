from manim import *

class Adversamodel(MovingCameraScene):
    def construct(self):
        FText1 = Tex(r"(1) The genome was assumed to be an i.i.d. sequence\\ of length G, and the asymptotic regime G $\rightarrow \infty$ was considered.").shift(UP)
        FText2 = Tex(r"(2) Errors were assumed to be i.i.d.\\ for some fixed and known probability p.").shift(DOWN)

        self.play(Create(FText1))
        self.play(Create(FText2))
        self.wait(2)
        self.play(FadeOut((FText1)))
        self.play(FadeOut((FText2)))
        
        AdText1 = Tex(r"$({a}')$There are at most D erasures per read.").shift(UP*2)
        AdText2 = Tex(r"$({b}')$Each base s[t] is erased at most D times across all reads").shift(UP*1)

        # AdText3 = Tex(r"(a) There are at most pL erasures per read.")
        # AdText4 = Tex(r"(b) Each base s[t] is erased in at most a fraction p of the reads in ${R}^W_τ$ , for t − L < τ ≤ t − W + 1.")

        self.play(Create(AdText1))
        self.play(Create(AdText2))
        self.wait(2)

        # self.play(FadeOut((AdText1)))
        # self.play(FadeOut((AdText2)))

        # image = ImageMobject("img1.png")
        # self.play(FadeIn(image))
        # self.wait(1)
        # self.play(FadeOut(image))

        # self.play(Create(AdText3))
        # self.play(Create(AdText4))
        # self.wait(2)
        # self.play(FadeOut(Create(AdText3)))
        # self.play(FadeOut(Create(AdText4)))
        self.play(FadeOut(AdText1))
        self.play(FadeOut(AdText2))
        self.wait(2)

        A1 = Tex(r"A1. Reconstruct the entire sequence $\textbf{s}$ from R",font_size=45).shift(UP*2)
        A2 = Tex(r"A2. Reconstruct the k-spectrum\\ of $\textbf{s}, {S}_k(\textbf{s})$, from R, for some $k \le L$",font_size=45)
        A3 = Tex(r"A3. Reconstruct the support of the k-spectrum of\\ $\textbf{s}$, $supp({S}_k(\textbf{s}))$, from R, for some $k \le L$.",font_size=45).shift(DOWN*2)

        self.play(Create(A1))
        self.play(Create(A2))
        self.play(Create(A3))
        self.wait(2)

        self.play(FadeOut((A1)))
        self.play(FadeOut((A2)))
        self.play(FadeOut((A3)))

    
        Labelseq = Tex(r"DNA sequence")
        Labelread = Tex(r"reads")
        arrowdna = Arrow(start=[0, -2, 0], end=[0, 0, 0])
        # arrowread = Arrow(start=[])
        Textcorollary = Tex(r"If we have ${D}_v{V}_s({D}_h, k)$ < m, then the k-spectrum assembler given by $\hat{S}_k({D}_h, {D}_v, m) = {\textbf{x} \in \sum \textbf{x} is : ({D}_h, {D}_v, m)-typical} satisfies \hat{S}_k({D}_h, {D}_v, n) \subset {S}_k$")

class failed(Scene):
    def construct(self):
        Adversamodel.construct(self)