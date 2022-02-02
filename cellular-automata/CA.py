from manim import *

class Math_and_CS(Scene):
    def construct(self):
        math = Circle(radius = 2.5, color = BLUE, fill_opacity = 0).shift(3 * LEFT)
        cs   = Circle(radius = 2.5, color = RED , fill_opacity = 0).shift(3 * RIGHT)

        math_label = Text("数学", color = BLUE, font = 'Source Han Serif SC VF').scale(0.8).next_to(math, UP).shift(0.05 * UP)
        cs_label = Text("计算机科学", color = RED, font = 'Source Han Serif SC VF').scale(0.8).next_to(cs, UP).shift(0.05 * UP)

        analysis  = Text("分析", color = BLUE, font = 'Source Han Serif SC VF').scale(0.72).shift(3.6 * LEFT + 1.9 * UP)
        algebra   = Text("代数", color = BLUE, font = 'Source Han Serif SC VF').scale(0.72).shift(4.1 * LEFT + 1.1 * UP)
        geometry  = Text("几何", color = BLUE, font = 'Source Han Serif SC VF').scale(0.72).shift(4.6 * LEFT + 0.3 * UP)
        topology  = Text("拓扑", color = BLUE, font = 'Source Han Serif SC VF').scale(0.72).shift(4.1 * LEFT + -0.5 * UP)
        stat      = Text("概率", color = BLUE, font = 'Source Han Serif SC VF').scale(0.72).shift(3.6 * LEFT + -1.3 * UP)
        math_dots = Text("...", color = BLUE, font = 'Source Han Serif SC VF').scale(0.72).shift(3.1 * LEFT + -2.1 * UP)

        software   = Text("软件工程", color = "#FF6666", font = 'Source Han Serif SC VF').scale(0.7).shift(3.5 * RIGHT + 1.8 * UP)
        vr         = Text("虚拟现实", color = "#FF6666", font = 'Source Han Serif SC VF').scale(0.7).shift(4.0 * RIGHT + 1.0 * UP)
        architect  = Text("体系结构", color = "#FF6666", font = 'Source Han Serif SC VF').scale(0.7).shift(4.5 * RIGHT + 0.2 * UP)
        interact   = Text("人机交互", color = "#FF6666", font = 'Source Han Serif SC VF').scale(0.7).shift(4.0 * RIGHT + -0.6 * UP)
        visual     = Text("可视化",   color = "#FF6666", font = 'Source Han Serif SC VF').scale(0.7).shift(3.5 * RIGHT + -1.4 * UP)
        cs_dots    = Text("...",     color = "#FF6666", font = 'Source Han Serif SC VF').scale(0.7).shift(3.0 * RIGHT + -2.2 * UP)

        self.add(math, cs, math_label, cs_label)
        self.add(analysis, algebra, geometry, topology, stat, math_dots)
        self.add(software, vr, architect, interact, visual, cs_dots)

        math_group = VGroup(math, math_label, analysis, algebra, geometry, topology, stat, math_dots)
        cs_group   = VGroup(cs, cs_label, software, vr, architect, interact, visual, cs_dots)

        self.play(math_group.animate.shift(1.7 * RIGHT), cs_group.animate.shift(1.7 * LEFT))

        machine_learning = Text("机器学习", color = "#7F00FF", font = 'Source Han Serif SC VF').scale(0.6).shift(0.85 * UP)
        info_theory     = Text("信息论", color = "#7F00FF", font = 'Source Han Serif SC VF').scale(0.6).shift(0.45 * DOWN)
        automata_theory = Text("自动机理论", color = "#7F00FF", font = 'Source Han Serif SC VF').scale(0.6).shift(0.2 * UP)
        inter_dots    = Text("...",     color = "#7F00FF", font = 'Source Han Serif SC VF').scale(0.6).shift(1.1 * DOWN)

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
            VGroup(
                math_label, analysis, algebra, geometry, topology, stat, math_dots,
                cs_label, software, vr, architect, interact, visual, cs_dots,
                machine_learning, info_theory, inter_dots
            ).animate.set_opacity(0.2),
            math.animate.set_color("#000013"), ## 006D85
            cs.animate.set_color("#130000"), ## a70d00
            automata_theory.animate.set_opacity(3)
        )

        unwrite_vg = [analysis, algebra, geometry, topology, stat, math_dots,
                    software, vr, architect, interact, visual, cs_dots,
                    machine_learning, info_theory, inter_dots, math_label, cs_label]
                
        self.play(
            *[Unwrite(obj) for obj in unwrite_vg],
            Uncreate(math), Uncreate(cs)
        )

        self.wait(0.5)

        self.play(automata_theory.animate.scale(2.5))
        self.wait(2)

        ca = Text("元胞自动机",color = "#7F00FF", font = 'Source Han Serif SC VF').scale(1.2).to_edge(UL)
        self.play(ReplacementTransform(automata_theory, ca))

        ca_line = Line(15 * LEFT, 15 * RIGHT, color = "#7F00FF").next_to(ca, DOWN)
        self.play(FadeIn(ca_line))
        self.wait(2)

        phy_text = Text("物理", color = YELLOW)
        phy_dot = Dot(color = YELLOW).next_to(phy_text, LEFT)
        phy = VGroup(phy_text, phy_dot).to_edge(LEFT)
        bio_text = Text("化学", color = YELLOW)
        bio_dot = Dot(color = YELLOW).next_to(bio_text, LEFT)
        bio = VGroup(bio_text, bio_dot).to_edge(LEFT)
        chem_text = Text("理论生物学", color = YELLOW)
        chem_dot = Dot(color = YELLOW).next_to(chem_text, LEFT)
        chem = VGroup(chem_text, chem_dot).to_edge(LEFT)
        crypt_text = Text("密码学", color = YELLOW)
        crypt_dot = Dot(color = YELLOW).next_to(crypt_text, LEFT)
        crypt = VGroup(crypt_text, crypt_dot).to_edge(LEFT)

        subjects = VGroup(phy, bio, chem, crypt).arrange(direction = DOWN)
        phy.to_edge(LEFT)
        bio.to_edge(LEFT)
        chem.to_edge(LEFT)
        crypt.to_edge(LEFT)

        self.play(FadeIn(subjects, direction = RIGHT))
        self.wait(2)

class TestFont(Scene):
    def construct(self):
        text1 = Text("数学分析 高等代数", font = "Source Han Serif SC VF").shift(2 * UP)
        text2 = Text("数学分析 高等代数", font = "Source Han Serif SC VF")
        text3 = Text("数学分析 高等代数").shift(2 * DOWN)
        self.add(text1, text2, text3)