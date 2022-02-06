from manim import *
from LifeGame import CellTable
import rleDecode

class Math_and_CS(Scene):
    def construct(self):
        math = Circle(radius = 2.5, color ="#3333FF", fill_opacity = 0).shift(3 * LEFT)
        cs   = Circle(radius = 2.5, color = RED , fill_opacity = 0).shift(3 * RIGHT)

        math_label = Text("数学", color = "#3333FF", font = 'Source Han Serif SC VF').scale(0.8).next_to(math, UP).shift(0.05 * UP)
        cs_label = Text("计算机科学", color = RED, font = 'Source Han Serif SC VF').scale(0.8).next_to(cs, UP).shift(0.05 * UP)

        analysis  = Text("分析", color = "#3333FF", font = 'Source Han Serif SC VF').scale(0.72).shift(3.6 * LEFT + 1.9 * UP)
        algebra   = Text("代数", color = "#3333FF", font = 'Source Han Serif SC VF').scale(0.72).shift(4.1 * LEFT + 1.1 * UP)
        geometry  = Text("几何", color = "#3333FF", font = 'Source Han Serif SC VF').scale(0.72).shift(4.6 * LEFT + 0.3 * UP)
        topology  = Text("拓扑", color = "#3333FF", font = 'Source Han Serif SC VF').scale(0.72).shift(4.1 * LEFT + -0.5 * UP)
        stat      = Text("概率", color = "#3333FF", font = 'Source Han Serif SC VF').scale(0.72).shift(3.6 * LEFT + -1.3 * UP)
        math_dots = Text("...", color = "#3333FF", font = 'Source Han Serif SC VF').scale(0.72).shift(3.1 * LEFT + -2.1 * UP)

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

        machine_learning = Text("机器学习", color = "#9933FF", font = 'Source Han Serif SC VF').scale(0.6).shift(0.85 * UP)
        info_theory     = Text("信息论", color = "#9933FF", font = 'Source Han Serif SC VF').scale(0.6).shift(0.45 * DOWN)
        automata_theory = Text("自动机理论", color = "#9933FF", font = 'Source Han Serif SC VF').scale(0.6).shift(0.2 * UP)
        inter_dots    = Text("...",     color = "#9933FF", font = 'Source Han Serif SC VF').scale(0.6).shift(1.1 * DOWN)

        self.play(LaggedStart(
            *[
                FadeIn(machine_learning, shift = 0.2 * DOWN),
                FadeIn(info_theory, shift = 0.2 * DOWN),
                FadeIn(automata_theory, shift = 0.2 * DOWN),
                FadeIn(inter_dots, shift = 0.2 * DOWN)
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

        ca = Text("元胞自动机",color = "#3333FF", font = 'Source Han Serif SC VF').scale(1.2).to_edge(UL)
        self.play(ReplacementTransform(automata_theory, ca))

        ca_line = Line(15 * LEFT, 15 * RIGHT, color = "#3333FF").next_to(ca, DOWN)
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


class Intro_to_CA(MovingCameraScene):
    def construct(self):
        ca = Text("元胞自动机",color = "#3333FF", font = 'Source Han Serif SC VF').scale(1.2).to_edge(UL)
        ca_line = Line(7 * LEFT, 7 * RIGHT, color = "#3333FF").to_edge(UP).shift(DOWN)

        self.add(ca, ca_line)

        gol = Text("- 生命游戏",color = "#FF007F", font = 'Source Han Serif SC VF').scale(1.2).next_to(ca, RIGHT)

        surviv_shape = (3, 3)
        surviv_stage = np.zeros(surviv_shape)
        surviv_stage[0][0] = surviv_stage[1][0] = surviv_stage[2][2] =  1

        surviv_cells = CellTable(
            shape = surviv_shape,
            original_stage_set = surviv_stage,
        ).scale(0.9).shift(4.5 * LEFT + 0.6 * UP)

        # pifont
        # \ding{}
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{pifont}")

        tick = Tex(r"\ding{51}", color = GREEN, tex_template = myTemplate).move_to(surviv_cells.get_square([1, 1])) # svg

        death_shape = (3, 3)
        death_stage = np.zeros(death_shape)
        death_stage[0][0] = death_stage[1][1] = 1
        
        death_cells = CellTable(
            shape = death_shape,
            original_stage_set = death_stage,
        ).scale(0.9).shift(4.5 * LEFT + 2 * DOWN)

        cross = Tex(r"\ding{55}", color = RED, tex_template = myTemplate).move_to(death_cells.get_square([1, 1])) # svg

        self.add(surviv_cells, tick, death_cells, cross)

        self.play(LaggedStart(
            *[FadeIn(i, shift = DOWN) for i in gol]
        ))

        self.wait(2)

        arrow = Arrow(3 * LEFT, 2 * RIGHT, color = YELLOW)
        self.play(GrowArrow(arrow))

        star_stage = rleDecode.expand_rle('star-board')
        
        star_board = CellTable(
            shape = (47, 47),
            original_stage_set = star_stage
        ).scale(0.1).shift(4.5 * RIGHT  + 0.5 * DOWN)
        self.add(star_board)

        """
        for i in range(40):
            star_board.step()
            self.wait(0.1)
        """
        self.wait(1)

        screen_rec = FullScreenRectangle(color = YELLOW)
        self.add(screen_rec)
        screen_rec = screen_rec.copy().set_color("#FFD700")
        self.play(self.camera.frame.animate.scale(2))
        for time_width in [0.2, 0.5, 1, 2]:
            self.play(
                ShowPassingFlash(
                    screen_rec.copy().set_color("#FFD700"),
                    run_time = 1,
                    time_width = time_width
                )
            )
        self.wait(2)


class TestStarStage(Scene):
    def construct(self):
        star_stage = rleDecode.expand_rle('star-board')
        
        star_board = CellTable(
            shape = (47, 47),
            original_stage_set = star_stage
        ).scale(0.05)
        self.add(star_board)

        for i in range(60):
            star_board.step()
            self.wait(0.1)
    
class TestFont(Scene):
    def construct(self):
        text1 = Text("数学分析 高等代数", font = "Source Han Serif SC VF").shift(2 * UP)
        text2 = Text("数学分析 高等代数", font = "Source Han Serif SC VF")
        text3 = Text("数学分析 高等代数").shift(2 * DOWN)
        self.add(text1, text2, text3)