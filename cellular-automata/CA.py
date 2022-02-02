from manim import *

class Math_and_CS(Scene):
    def construct(self):
        #math = RoundedRectangle(width = 3.5, height = 6, color = BLUE).shift(2 * LEFT)
        #cs = RoundedRectangle(width = 3.5, height = 6, color = RED).shift(2 * RIGHT)

        math = Circle(radius = 2.5, color = BLUE, fill_opacity = 0).shift(3 * LEFT)
        cs   = Circle(radius = 2.5, color = RED , fill_opacity = 0).shift(3 * RIGHT)

        math_label = Text("数学", color = BLUE, font = 'LXGWWenKai-Regular').scale(0.8).next_to(math, UP).shift(0.05 * UP)
        cs_label = Text("计算机科学", color = RED, font = 'LXGWWenKai-Regular').scale(0.8).next_to(cs, UP).shift(0.05 * UP)

        analysis  = Text("分析", color = BLUE, font = 'LXGWWenKai-Regular').scale(0.72).shift(3.6 * LEFT + 1.9 * UP)
        algebra   = Text("代数", color = BLUE, font = 'LXGWWenKai-Regular').scale(0.72).shift(4.1 * LEFT + 1.1 * UP)
        geometry  = Text("几何", color = BLUE, font = 'LXGWWenKai-Regular').scale(0.72).shift(4.6 * LEFT + 0.3 * UP)
        topology  = Text("拓扑", color = BLUE, font = 'LXGWWenKai-Regular').scale(0.72).shift(4.1 * LEFT + -0.5 * UP)
        stat      = Text("概率", color = BLUE, font = 'LXGWWenKai-Regular').scale(0.72).shift(3.6 * LEFT + -1.3 * UP)
        math_dots = Text("...", color = BLUE, font = 'LXGWWenKai-Regular').scale(0.72).shift(3.1 * LEFT + -2.1 * UP)

        software   = Text("软件工程", color = "#FF6666", font = 'LXGWWenKai-Regular').scale(0.7).shift(3.5 * RIGHT + 1.8 * UP)
        vr         = Text("虚拟现实", color = "#FF6666", font = 'LXGWWenKai-Regular').scale(0.7).shift(4.0 * RIGHT + 1.0 * UP)
        architect  = Text("体系结构", color = "#FF6666", font = 'LXGWWenKai-Regular').scale(0.7).shift(4.5 * RIGHT + 0.2 * UP)
        interact   = Text("人机交互", color = "#FF6666", font = 'LXGWWenKai-Regular').scale(0.7).shift(4.0 * RIGHT + -0.6 * UP)
        visual     = Text("可视化",   color = "#FF6666", font = 'LXGWWenKai-Regular').scale(0.7).shift(3.5 * RIGHT + -1.4 * UP)
        cs_dots    = Text("...",     color = "#FF6666", font = 'LXGWWenKai-Regular').scale(0.7).shift(3.0 * RIGHT + -2.2 * UP)

        self.add(math, cs, math_label, cs_label)
        self.add(analysis, algebra, geometry, topology, stat, math_dots)
        self.add(software, vr, architect, interact, visual, cs_dots)

        math_group = VGroup(math, math_label, analysis, algebra, geometry, topology, stat, math_dots)
        cs_group   = VGroup(cs, cs_label, software, vr, architect, interact, visual, cs_dots)

        self.play(math_group.animate.shift(1.7 * RIGHT), cs_group.animate.shift(1.7 * LEFT))

        machine_learning = Text("机器学习", color = PURPLE, font = 'LXGWWenKai-Regular').scale(0.6).shift(0.85 * UP)
        info_theory     = Text("信息论", color = PURPLE, font = 'LXGWWenKai-Regular').scale(0.6).shift(0.45 * DOWN)
        automata_theory = Text("自动机理论", color = PURPLE, font = 'LXGWWenKai-Regular').scale(0.6).shift(0.2 * UP)
        inter_dots    = Text("...",     color = PURPLE, font = 'LXGWWenKai-Regular').scale(0.6).shift(1.1 * DOWN)

        self.play(LaggedStart(
            *[
                FadeIn(machine_learning, direction = DOWN),
                FadeIn(info_theory, direction = DOWN),
                FadeIn(automata_theory, direction = DOWN),
                FadeIn(inter_dots, direction = DOWN)
            ]
        ))
        
        self.wait(1.5)

        self.play(
            VGroup(math_group, cs_group).animate.set_opacity(0.2),
            automata_theory.animate.set_opacity(1.8)
        )

        self.wait(1.5)

        self.play(
            Unwrite(
                VGroup(
                    analysis, algebra, geometry, topology, stat, math_dots,
                    software, vr, architect, interact, visual, cs_dots,
                    machine_learning, info_theory, inter_dots
                )
            ),
            Uncreate(VGroup(math, cs))
        )