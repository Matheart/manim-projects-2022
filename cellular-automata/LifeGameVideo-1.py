from manim import *
from LifeGame import CellTable
from manim.animation.composition import AnimationGroup

# Not used
class IntroCellularAutomatonScene(Scene):
    def construct(self):
        LifeGameLabel = GDHText("生命游戏").shift(2 * DOWN)
        CelAutoLabel = GDHText("元胞自动机").shift(2 * UP)
        arr = Arrow(np.array([0,-2,0]), np.array([0,2,0]), buff = 0.5)
        source = GDHText('起源于').next_to(arr, RIGHT)

        self.play(Write(LifeGameLabel))
        self.wait(1)
        self.play(Write(arr), Write(source), run_time = 0.2)
        self.play(Write(CelAutoLabel))
        self.play(FadeOut(VGroup(arr, source, LifeGameLabel), direction = DOWN))
        self.play(CelAutoLabel.animate.to_edge(UP))
        TitleLine = Line(np.array([-10,0,0]), np.array([10,0,0])).next_to(CelAutoLabel, DOWN)
        self.play(Create(TitleLine), run_time = 0.2)

        VonNeumann_Image = ImageMobject("./assets/VonNeumann.png").to_edge(LEFT)
        VonNeumann_nick = GDHText("冯·诺依曼").next_to(VonNeumann_Image, DOWN)
        self.play(FadeIn(VonNeumann_Image, direction = LEFT), FadeIn(VonNeumann_nick, direction = LEFT))
        self.wait(2)

        QuestionMark = Tex("?", color = RED).scale(2.5).next_to(VonNeumann_Image, RIGHT).shift(UP)
        self.play(GrowFromCenter(QuestionMark))
        self.play(Indicate(QuestionMark))
        self.wait(1)

        robot = SVGMobject("./assets/robot.svg").set_stroke(width = 0.3)
        self.play(FadeIn(robot))
        self.wait(2)
        robot1 = robot.copy().shift(2 * RIGHT + 1.5 * UP)
        robot2 = robot.copy().shift(2 * RIGHT + 1.5 * DOWN)
        robot3 = robot.copy().shift(2 * DOWN)
        robot4 = robot.copy().shift(4 * RIGHT + 1.5 * UP)
        robot5 = robot.copy().shift(4 * RIGHT + 1.5 * DOWN)
        
        self.play(ReplacementTransform(robot.copy(), robot1),
                ReplacementTransform(robot.copy(), robot2))
        self.wait(1)
        self.play(ReplacementTransform(robot.copy(), robot3),
                ReplacementTransform(robot1.copy(), robot4),
                ReplacementTransform(robot2.copy(), robot5),)
        self.wait(3.5)

        Cross_Line1 = Line(2.25 * UP, 3.5 * RIGHT + 2.25 * DOWN, color = "#FF3333")
        Cross_Line2 = Line(3.5 * RIGHT + 2.25 * UP, 3 * DOWN, color = "#FF3333")
        self.play(Write(Cross_Line1), run_time = 0.5)
        self.play(Write(Cross_Line2), run_time = 0.5)
        self.wait(2)

        self.play(
                FadeOut(VGroup(Cross_Line1, Cross_Line2, QuestionMark), direction = DOWN),
                FadeOut(robot, direction = DOWN),
                FadeOut(robot1, direction = DOWN),
                FadeOut(robot2, direction = DOWN),
                FadeOut(robot3, direction = DOWN),
                FadeOut(robot4, direction = DOWN),
                FadeOut(robot5, direction = DOWN),
                FadeOut(VonNeumann_Image, direction = DOWN),
                FadeOut(VonNeumann_nick, direction = DOWN),
        )

        Ulam_Image = ImageMobject("./assets/Ulam.jpg").scale(0.6).next_to(TitleLine, DOWN).to_edge(LEFT)
        Ulam_nick = GDHText("乌拉姆").next_to(Ulam_Image, DOWN)
        self.play(FadeIn(Ulam_Image, direction = LEFT), FadeIn(Ulam_nick, direction = LEFT))

        my_shape = (18, 18)
        stage_set = np.zeros(my_shape)
        stage_set[6][9] = 1
        stage_set[7][8] = stage_set[7][10] = 1
        stage_set[8][8] = stage_set[8][9] = stage_set[8][10] = 1  
        stage_set[9][9] = 1    

        cells = CellTable(
            shape = my_shape,
            original_stage_set = stage_set,
        ).scale(0.8 * 10.0 / 18.0).shift(DOWN + RIGHT)
        self.play(Create(cells))
        self.wait(3.5)
        for i in range(20):
            cells.step()
            self.wait(0.2)
        self.wait(1.5)
        self.play(
            FadeOut(Ulam_Image), FadeOut(Ulam_nick)
        )
        self.play(cells.animate.to_edge(RIGHT), Transform(CelAutoLabel, LifeGameLabel.to_edge(UP)))
        self.wait(2)

        ConwayImage = ImageMobject("./assets/Conway.jpg").scale(0.8).to_edge(LEFT)
        ConwayImage.align_to(cells, direction = UP)
        ConwayImage_BL = ImageMobject("./assets/Conway-BlackAndWhite.jpg").scale(0.8).to_edge(LEFT)
        ConwayImage_BL.align_to(cells, direction = UP)
        ConwayNick = GDHText("约翰·康威").next_to(ConwayImage, DOWN)

        self.play(FadeIn(ConwayImage), FadeIn(ConwayNick))
        self.wait(4.5)
        self.play(FadeOut(ConwayImage, direction = LEFT), FadeIn(ConwayImage_BL, direction = RIGHT))
        self.wait(2)

class GDHText(Text):
    def __init__(self, text: str, font: str = "zcool-gdh", **kwargs):
        super().__init__(text = text, font = font, **kwargs)

class HappyText(Text):
    def __init__(self, text: str, font: str = "HappyZcool-2016", **kwargs):
        super().__init__(text = text, font = font, **kwargs)    
        
class IntroductionGliderScene(Scene):
    def construct(self):
        my_shape = (15, 15)
        stage_set = np.zeros(my_shape)
        stage_set[0][2] = 1
        stage_set[1][0] = stage_set[1][2] = 1
        stage_set[2][1] = stage_set[2][2] = 1

        cells = CellTable(
            shape = my_shape,
            original_stage_set = stage_set,
            shape_sets = {'block_width': 0.35, 'width_buff_ratio': 6.0, 'buff': 0.1,},
        ).shift(0.5*DOWN)
        text = Text('生命游戏', font = "zcool-gdh", color = "#00FFFF").scale(4)

        self.add(cells)
        for i in range(40):
            cells.step()
            if i == 0:
                self.play(FadeIn(text, direction = LEFT), run_time = 0.4)
            else:
                self.wait(0.1)
    # PR后期FadeOut

class IntroScene(Scene):
    def construct(self):
        def sq_no_buff(sq):
            sq_new = Rectangle(
                height = sq.get_height(), 
                width = sq.get_width(), 
                fill_opacity = 1
            ).move_to(sq.get_center())
            return sq_new
        nm_to_ch = "零 一 二 三 四 五 六 七 八 九 十 十一 十二 十三 十四 十五 十六 十七 十八 十九 二十".split()
        # Center (4, 4)
        my_shape = (18, 18)
        stage_set = np.zeros(my_shape)
        stage_set[6][9] = 1
        stage_set[7][8] = stage_set[7][10] = 1
        stage_set[8][8] = stage_set[8][9] = stage_set[8][10] = 1  
        stage_set[9][9] = 1    

        LifeGameLabel = GDHText("生命游戏").scale(1.5).to_edge(UP)
        TitleLine = Line([-10,0,0],[10,0,0]).next_to(LifeGameLabel, DOWN)

        cells = CellTable(
            shape = my_shape,
            original_stage_set = stage_set,
        ).scale(0.8 * 10.0 / 18.0).shift(DOWN)

        self.play(Write(LifeGameLabel), Create(TitleLine))
        self.wait(3)

        ConwayImage_BL = ImageMobject("./assets/Conway-BlackAndWhite.jpg").scale(0.75).next_to(TitleLine, DOWN).shift(0.3 * DOWN).to_edge(LEFT)
        ConwayNick = GDHText("约翰·康威").next_to(ConwayImage_BL, DOWN)
        #Scientific_American_Cover = ImageMobject("./assets/ScientificAmericanCover.jpg").scale(1.78).next_to(TitleLine, DOWN)
        Scientific_American = ImageMobject("./assets/ScientificAmerican.jpg").scale(0.75).next_to(TitleLine, DOWN).shift(2 * RIGHT)

        self.play(FadeIn(ConwayImage_BL), FadeIn(ConwayNick))
        self.wait(1.5)
        self.play(FadeIn(Scientific_American, direction = DOWN)) 
        self.wait(3)
        self.play(FadeOut(ConwayImage_BL), FadeOut(ConwayNick), FadeOut(Scientific_American))
        self.play(Create(cells))
        self.wait(1)
        indicate_acti = AnimationGroup(
            *[ShowPassingFlashAround(sq_no_buff(mob)) for mob in cells.get_activated_vgroup()]
        )
        indicate_term = AnimationGroup(
            *[ShowPassingFlashAround(sq_no_buff(mob)) for mob in cells.get_terminated_vgroup()]
        )
        self.play(indicate_acti)
        self.wait(1.5)
        self.play(indicate_term)
        self.wait(1.5)

        huihe = GDHText("第一代").to_edge(UP).shift(0.5 * LEFT)
        nm = 1
        huihe.add_updater(lambda obj: obj.become(GDHText("第" + nm_to_ch[nm] + "代").to_edge(UP).shift(0.5 * LEFT)))
        
        self.play(FadeOut(LifeGameLabel, direction = DOWN), FadeIn(huihe, direction = UP))
        self.wait(2.5)

        Ruler = ImageMobject("./assets/Tri_Ruler.png").scale(1.5).rotate(10 * DEGREES).next_to(LifeGameLabel, LEFT)
        Computer = ImageMobject("./assets/Computer.png").scale(1.5).rotate(-10 * DEGREES).next_to(LifeGameLabel, RIGHT)
        
        for i in range(15):
            cells.step()
            nm = i + 2
            if i != 12:
                self.wait(0.6)
            else:
                self.play(FadeIn(Ruler, direction = DOWN), FadeIn(Computer, direction = DOWN))
        self.wait(1)
        self.play(FadeIn(FullScreenRectangle(color = BLACK, fill_opacity = 1)))

class RulesDetailScene(Scene):
    def construct(self):
        def sq_no_buff(sq, buff):
            sq_new = Rectangle(
                height = sq.get_height(), 
                width = sq.get_width(), 
                fill_opacity = 1
            ).move_to(sq.get_center())
            return sq_new
        Rule1Stageset = np.zeros((3, 3))
        Rule1Stageset[1][1] = 1
        Rule1Cell = CellTable(
            shape = (3, 3),
            original_stage_set = Rule1Stageset
        )
        Rule1Text = GDHText("周围细胞数小于二 ：孤独而死").scale(1.5).to_edge(UP)
        Rule1Now = GDHText("此时周围细胞数：0").next_to(Rule1Cell, DOWN)

        self.play(FadeIn(Rule1Cell))
        self.wait(1.5)
        Surr_rec = SurroundingRectangle(sq_no_buff(Rule1Cell.get_square([1, 1]), Rule1Cell.shape_sets['buff']))
        self.play(Create(Surr_rec))
        self.wait(2)

        #surround_vg = Rule1Cell.get_surrounded_vgroup([1, 1])
        #Surr_rec_vg = VGroup(*[sq_no_buff(mob, Rule1Cell.shape_sets['buff']).set_color(BLUE).set_opacity(0.3) for mob in surround_vg])
        self.play(Write(Rule1Now))
        self.play(FadeIn(Rule1Text, direction = DOWN))
        self.wait(1)
        self.play(Rule1Cell[1, 1].animate.set_color(GREY))

        Rule2Stageset = np.ones((3, 3))
        Rule2Cell = CellTable(
            shape = (3, 3),
            original_stage_set = Rule2Stageset
        )
        Rule2Text = GDHText("周围细胞数大于三 ：拥挤而死").scale(1.5).to_edge(UP)
        Rule2Now = GDHText("此时周围细胞数：8").next_to(Rule2Cell, DOWN)
        
        self.remove(Surr_rec)
        self.play(
            FadeOut(Rule1Cell, direction = LEFT), 
            FadeIn(Rule2Cell, direction = RIGHT),
            FadeOut(Rule1Text, direction = LEFT), 
            FadeIn(Rule2Text, direction = RIGHT),
            FadeOut(Rule1Now, direction = LEFT), 
            FadeIn(Rule2Now, direction = RIGHT),
        )
        Surr_rec = SurroundingRectangle(sq_no_buff(Rule2Cell.get_square([1, 1]), Rule2Cell.shape_sets['buff']))
        self.play(Create(Surr_rec))

        surround_vg = Rule2Cell.get_surrounded_vgroup([1, 1])

        self.play(AnimationGroup(
            *[Flash(mob) for mob in surround_vg]
        ))
        self.wait(1)
        self.play(Rule2Cell[1, 1].animate.set_color(GREY), run_time = 0.5)
        
        Rule3Stageset = np.zeros((3, 3))
        Rule3Stageset[0][1] = Rule3Stageset[1][0] = Rule3Stageset[1][1] = Rule3Stageset[1][2] = 1
        Rule3Cell = CellTable(
            shape = (3, 3),
            original_stage_set = Rule3Stageset
        )       
        Rule3Text = GDHText("周围细胞数为二或三 ：维持不变").scale(1.5).to_edge(UP)
        Rule3Now = GDHText("此时周围细胞数：3").next_to(Rule3Cell, DOWN)

        self.remove(Surr_rec)
        self.play(
            FadeOut(Rule2Cell, direction = LEFT), 
            FadeIn(Rule3Cell, direction = RIGHT),
            FadeOut(Rule2Text, direction = LEFT), 
            FadeIn(Rule3Text, direction = RIGHT),
            FadeOut(Rule2Now, direction = LEFT), 
            FadeIn(Rule3Now, direction = RIGHT),
        )
        Surr_rec = SurroundingRectangle(sq_no_buff(Rule3Cell.get_square([1, 1]), Rule3Cell.shape_sets['buff']))
        self.play(Create(Surr_rec))

        surround_vg = Rule3Cell.get_surrounded_vgroup([1, 1])

        self.play(
            Flash(Rule3Cell.get_square([0, 1])),
            Flash(Rule3Cell.get_square([1, 0])),
            Flash(Rule3Cell.get_square([1, 2])),
        )
        self.wait(2.5)
        self.remove(Surr_rec)

        Rule4Stageset = np.zeros((3, 3))
        Rule4Stageset[0][1] = Rule4Stageset[1][0] = Rule4Stageset[1][2] = 1
        Rule4Cell = CellTable(
            shape = (3, 3),
            original_stage_set = Rule4Stageset
        )       
        Rule4Text = GDHText("灰格周围细胞数为三 ：生成细胞").scale(1.5).to_edge(UP)
        Rule4Now = GDHText("此时周围细胞数：3").next_to(Rule4Cell, DOWN)

        self.play(
            FadeOut(Rule3Cell, direction = LEFT), 
            FadeIn(Rule4Cell, direction = RIGHT),
            FadeOut(Rule3Text, direction = LEFT), 
            FadeIn(Rule4Text, direction = RIGHT),
            FadeOut(Rule3Now, direction = LEFT), 
            FadeIn(Rule4Now, direction = RIGHT),
        )
        self.wait(2.5)
        Surr_rec = SurroundingRectangle(sq_no_buff(Rule4Cell.get_square([1, 1]), Rule4Cell.shape_sets['buff']))
        self.play(Create(Surr_rec))

        surround_vg = Rule4Cell.get_surrounded_vgroup([1, 1])

        self.wait(1.5)
        self.play(AnimationGroup(
            *[Flash(mob) for mob in Rule4Cell.get_activated_vgroup()]
        ))
        self.wait(2)
        self.play(Rule4Cell[1, 1].animate.set_color(WHITE), run_time = 0.5)
        self.wait(4)

class RulesExampleScene(Scene):
    def construct(self):
        stage_set = np.zeros((9, 9))
        stage_set[4][3:6] = stage_set[5][4] = stage_set[6][4] = 1
        Cell = CellTable(
            shape = (9, 9),
            original_stage_set = stage_set
        ).scale(0.9).shift(0.8 * DOWN)
        huiheOne = GDHText("第一代").scale(1.5).to_edge(UP).shift(0.3 * LEFT)
        huiheTwo = GDHText("第二代").scale(1.5).to_edge(UP).shift(0.3 * LEFT)
        huiheThree = GDHText("第三代").scale(1.5).to_edge(UP).shift(0.3 * LEFT)
        huiheFour = GDHText("第四代").scale(1.5).to_edge(UP).shift(0.3 * LEFT)

        self.play(Create(Cell), run_time = 1.5)
        self.wait(2.5)

        def recal(row, col):
            cnt = Cell.count_neighbor(col, row)
            tmp = Text(str(cnt), font = 'LCD_Tony')
            tmp.scale(0.95).move_to(Cell[col, row].get_center())
            if Cell.stage[col][row]:
                if cnt < 2 or cnt > 3:
                    tmp.set_color("#FF0000") # Red
                else:
                    tmp.set_color(BLACK)
            else:
                if cnt == 3:
                    tmp.set_color("#00FF00") # Green
                else:
                    tmp.set_color(WHITE)
            return tmp

        dn_group = [[0 for i in range(9)] for j in range(9)]
        #print(dn_group)
        for row in range(9):
            for col in range(9):
                cnt = Cell.count_neighbor(col, row)
                dn = Text(str(cnt), font = 'LCD_Tony')
                dn.scale(0.95).move_to(Cell[col, row].get_center())
                if Cell.stage[col][row]:
                    if cnt < 2 or cnt > 3:
                        dn.set_color("#FF0000") # Red
                    else:
                        dn.set_color(BLACK)
                else:
                    if cnt == 3:
                        dn.set_color("#00FF00") # Green
                    else:
                        dn.set_color(WHITE)
                dn_group[row][col] = dn

        self.play(
            AnimationGroup(
                *[Write(dn_group[row][col]) for row in range(9) for col in range(9)]
            ),
            Write(huiheOne)
        )
        self.wait(5.5)
        self.play(ShowPassingFlashAround(Cell.get_square([3, 4])))
        self.wait(2)
        self.play(ShowPassingFlashAround(Cell.get_square([5, 4])),
                ShowPassingFlashAround(Cell.get_square([6, 4])))
        self.wait(1.5)
        Cell.stage[4, 3] = 1
        Cell.stage[4, 5] = Cell.stage[4, 6] = 0
        self.play(
            ReplacementTransform(huiheOne, huiheTwo),
            Cell[4, 3].animate.set_color(WHITE),
            Cell[4, 5].animate.set_color(GREY),
            Cell[4, 6].animate.set_color(GREY), 
            Transform(dn_group[2][3], recal(2, 3)),
            Transform(dn_group[2][4], recal(2, 4)),
            Transform(dn_group[2][5], recal(2, 5)),
            Transform(dn_group[3][3], recal(3, 3)),
            Transform(dn_group[3][5], recal(3, 5)),
            Transform(dn_group[4][3], recal(4, 3)),
            Transform(dn_group[4][4], recal(4, 4)),
            Transform(dn_group[4][5], recal(4, 5)),

            Transform(dn_group[5][3], recal(5, 3)),
            Transform(dn_group[5][4], recal(5, 4)),
            Transform(dn_group[5][5], recal(5, 5)),

            Transform(dn_group[6][3], recal(6, 3)),
            Transform(dn_group[6][4], recal(6, 4)),
            Transform(dn_group[6][5], recal(6, 5)),

            Transform(dn_group[7][3], recal(7, 3)),
            Transform(dn_group[7][4], recal(7, 4)),
            Transform(dn_group[7][5], recal(7, 5)),
        )
        self.wait(0.75)
        Cell.stage[3][3] = Cell.stage[4][3] = Cell.stage[5][3] = Cell.stage[4][5] = 1
        self.play(
            ReplacementTransform(huiheTwo, huiheThree),
            Cell[3, 3].animate.set_color(WHITE),
            Cell[4, 3].animate.set_color(WHITE),
            Cell[5, 3].animate.set_color(WHITE),
            Cell[4, 5].animate.set_color(WHITE),
            AnimationGroup(*[
                Transform(dn_group[row][column], recal(row, column))
                for row in range(2, 6) for column in range(2, 7)
            ]), 
            Transform(dn_group[6][3], recal(6, 3)),
            Transform(dn_group[6][4], recal(6, 4)),
            Transform(dn_group[6][5], recal(6, 5)),
        )
        self.wait(1)
        rec = FullScreenRectangle(color = BLACK, fill_opacity = 1)
        self.play(FadeIn(rec))

class MessScene(Scene):
    def construct(self):
        stage_set = np.zeros((70, 70))
        stage_set[23][23] = stage_set[23][24] = stage_set[23][26] = 1 
        stage_set[24][24] = stage_set[24][25] = 1
        stage_set[25][24] = stage_set[25][25] = 1
        stage_set[26][24] = stage_set[26][25] = 1
        stage_set[27][24] = stage_set[27][26] = 1
        stage_set[28][24] = 1

        nolaw = CellTable(
            shape = (65, 65),
            original_stage_set = stage_set,
            shape_sets = {'block_width': 0.06 * 1.3, 'width_buff_ratio': 6.0, 'buff': None,},
        )
        self.play(FadeIn(nolaw))

        for i in range(150):
            nolaw.step()
            self.wait(0.055)

class StableScene(Scene):
    def construct(self):
        # Block 方块
        Block_set = np.zeros((4, 4))
        Block_set[1][1] = Block_set[1][2] = 1
        Block_set[2][1] = Block_set[2][2] = 1
        BlockCell = CellTable(
            shape = (4, 4),
            original_stage_set = Block_set
        )

        # Boat 小船
        Boat_set = np.zeros((5, 5))
        Boat_set[1][2] = Boat_set[2][1] = Boat_set[2][3] = 1
        Boat_set[3][2] = Boat_set[3][3] = 1

        BoatCell = CellTable(
            shape = (5, 5),
            original_stage_set = Boat_set
        ).shift(0.5 * DOWN)

        # Long Boat 长船

        # Very Long Boat 超长船

        # Dead spark coil 熄灭的火花线圈
        Coil_set = np.zeros((9, 9))
        Coil_set[2][1] = Coil_set[2][2] = Coil_set[2][6] = Coil_set[2][7] = 1
        Coil_set[3][1] = Coil_set[3][3] = Coil_set[3][5] = Coil_set[3][7] = 1
        Coil_set[4][3] = Coil_set[4][5] = 1
        Coil_set[5][1] = Coil_set[5][3] = Coil_set[5][5] = Coil_set[5][7] = 1
        Coil_set[6][1] = Coil_set[6][2] = Coil_set[6][6] = Coil_set[6][7] = 1

        CoilCell = CellTable(
            shape = (9, 9),
            original_stage_set = Coil_set
        ).scale(0.8).shift(0.5 * DOWN)

        # Cis-mirrored worm (触角)
        Worm_set = np.zeros((9, 9))
        Worm_set[0][2:4] = 1
        Worm_set[1][1] = Worm_set[1][3] = 1
        Worm_set[2][1] = Worm_set[2][6] = 1
        Worm_set[3][2:7] = Worm_set[5][2:7] = 1
        Worm_set[6][1] = Worm_set[6][6] = 1
        Worm_set[7][1] = Worm_set[7][3] = 1
        Worm_set[8][2:4] = 1

        WormCell = CellTable(
            shape = (9, 9),
            original_stage_set = Worm_set
        ).scale(0.8).shift(0.5 * DOWN)

        # Inflected clips (弯曲的回形针)
        Clip_set = np.zeros((9, 9))
        Clip_set[0][2] = Clip_set[0][6] = 1
        Clip_set[1][1] = Clip_set[1][3] = Clip_set[1][5] = Clip_set[1][7] = 1
        Clip_set[2][0] = Clip_set[2][3] = Clip_set[2][5] = Clip_set[2][8] = 1
        Clip_set[3][0] = Clip_set[3][1] = Clip_set[3][3] = Clip_set[3][5] = Clip_set[3][7] = Clip_set[3][8] = 1
        Clip_set[4][3] = Clip_set[4][5] = 1
        Clip_set[5][0] = Clip_set[5][1] = Clip_set[5][3] = Clip_set[5][5] = Clip_set[5][7] = Clip_set[5][8] = 1
        Clip_set[6][0] = Clip_set[6][3] = Clip_set[6][5] = Clip_set[6][8] = 1
        Clip_set[7][1] = Clip_set[7][2] = Clip_set[7][6] = Clip_set[7][7] = 1

        ClipCell = CellTable(
            shape = (9, 9),
            original_stage_set = Clip_set
        ).scale(0.8).shift(0.5 * DOWN)

        BlockName = GDHText("方块").next_to(BlockCell, DOWN)
        self.play(Create(BlockCell), FadeIn(BlockName))
        self.wait(1.5)

        dn_group = [[0 for i in range(4)] for j in range(4)]
        for row in range(4):
            for col in range(4):
                cnt = BlockCell.count_neighbor(col, row)
                dn = Text(str(cnt), font = 'LCD_Tony')
                dn.scale(0.95).move_to(BlockCell[col, row].get_center())
                if BlockCell.stage[col][row]:
                    if cnt < 2 or cnt > 3:
                        dn.set_color("#FF0000") # Red
                    else:
                        dn.set_color(BLACK)
                else:
                    if cnt == 3:
                        dn.set_color("#00FF00") # Green
                    else:
                        dn.set_color(WHITE)
                dn_group[row][col] = dn
        self.play(
            AnimationGroup(
                *[Write(dn_group[row][col]) for row in range(4) for col in range(4)]
            )
        )
        self.wait(4.5)
        huihe = GDHText("第一代").scale(1.5).to_edge(UP).shift(0.5 * LEFT)
        stable = GDHText("稳定结构").scale(1.5).to_edge(UP).shift(0.2 * LEFT)
        nm = 1
        nm_to_ch = "零 一 二 三 四 五 六 七 八 九 十 十一 十二 十三 十四 十五 十六 十七 十八 十九 二十".split()
        huihe.add_updater(lambda obj: obj.become(GDHText("第" + nm_to_ch[nm] + "代").scale(1.5).to_edge(UP).shift(0.5 * LEFT)))

        self.play(FadeIn(huihe))

        for i in range(4):
            nm = i + 2
            self.wait(0.3)
        
        self.wait(1.5)
        self.play(ReplacementTransform(huihe, stable))
        self.wait(7)

        self.remove(
            BlockCell, 
            BlockName,
            *[dn_group[row][col] for row in range(4) for col in range(4)]
        )

        BoatName = GDHText("小船").next_to(BoatCell, DOWN)
        CoilName = GDHText("熄灭的火花线圈").next_to(CoilCell, DOWN)
        
        #这个英文名比较难翻译所以我自己给它取了一个名字
        WormName = GDHText("触角").next_to(WormCell, DOWN)    
        ClipName = GDHText("弯曲的回形针").next_to(ClipCell, DOWN)
        
        self.add(BoatCell, BoatName)
        self.wait(1.2)
        self.remove(BoatCell, BoatName)
        self.add(CoilCell, CoilName)
        self.wait(1.8)
        self.remove(CoilCell, CoilName)
        self.add(WormCell, WormName)
        self.wait(1.2)
        self.remove(WormCell, WormName)
        self.add(ClipCell, ClipName)
        self.wait(2.5)

class OscillatorScene(Scene):
    def construct(self):
        def sq_no_buff(sq, buff):
            sq_new = Rectangle(
                height = sq.get_height() - buff, 
                width = sq.get_width() - buff, 
                fill_opacity = 1
            ).move_to(sq.get_center())
            return sq_new
        nm_to_ch = "零 一 二 三 四 五 六 七 八 九 十 十一 十二 十三 十四 十五 十六 十七 十八 十九 二十".split()
        huihe = GDHText("第一代", color = ORANGE).shift(4 * RIGHT + 3 * UP) 
        huihe.add_updater(lambda obj: obj.become(GDHText("第" + nm_to_ch[nm] + "代", color = ORANGE).shift(4 * RIGHT + 3 * DOWN)))      
        BlinkerStage = np.zeros((3, 3))
        BlinkerStage[1][0] = BlinkerStage[1][1] = BlinkerStage[1][2] = 1
        BlinkerCell = CellTable(
            shape = (3, 3),
            original_stage_set = BlinkerStage
        )
        BlinkerText = GDHText("闪光灯").next_to(BlinkerCell, DOWN)
        self.add(BlinkerCell)
        BlinkerPeriod = GDHText("周期为2").next_to(BlinkerText, DOWN)
        BlinkerPeriod[0:2].set_color(YELLOW)
        BlinkerPeriod[-1].set_color(BLUE)

        PDStage = np.zeros((16, 16))
        PDStage[7][3] = PDStage[7][4] = PDStage[7][6] = PDStage[7][7] = PDStage[7][8] = PDStage[7][9] = PDStage[7][11] = PDStage[7][12] = 1
        PDStage[6][5] = PDStage[6][10] = 1 
        PDStage[8][5] = PDStage[8][10] = 1 
        PDCell = CellTable(
            shape = (16, 16),
            original_stage_set = PDStage
        ).scale(0.4 * 0.8).shift(0.5 * DOWN)
        PDText = GDHText("十五项全能").next_to(PDCell, DOWN)
        PDPeriod = GDHText("周期为15").next_to(PDText, DOWN)
        PDPeriod[0:2].set_color(YELLOW)
        PDPeriod[3].set_color(BLUE)
        PDPeriod[4].set_color(BLUE)

        TumblerStage = np.zeros((9, 9))
        TumblerStage[1][1] = TumblerStage[1][7] = 1
        TumblerStage[2][0] = TumblerStage[2][2] = TumblerStage[2][6] = TumblerStage[2][8] = 1
        TumblerStage[3][0] = TumblerStage[3][3] = TumblerStage[3][5] = TumblerStage[3][8] = 1
        TumblerStage[4][2] = TumblerStage[4][6] = 1
        TumblerStage[5][2] = TumblerStage[5][3] = TumblerStage[5][5] = TumblerStage[5][6] = 1
        TumblerCell = CellTable(
            shape = (9, 9),
            original_stage_set = TumblerStage
        ).scale(0.4).shift(0.5 * DOWN)
        TumblerText = GDHText("不倒翁").next_to(TumblerCell, DOWN)
        TumblerPeriod = GDHText("周期为14").next_to(TumblerText, DOWN)
        TumblerPeriod[0:2].set_color(YELLOW)
        TumblerPeriod[3].set_color(BLUE)
        TumblerPeriod[4].set_color(BLUE)

        PulsarStage = np.zeros((15, 15))
        for i in [1, 6, 8, 13]:
            PulsarStage[i][3] = PulsarStage[i][4] = PulsarStage[i][5] = 1
            PulsarStage[i][9] = PulsarStage[i][10] = PulsarStage[i][11] = 1
        for i in [3, 4, 5, 9, 10, 11]:
            PulsarStage[i][1] = PulsarStage[i][6] = PulsarStage[i][8] = PulsarStage[i][13] = 1
        PulsarCell = CellTable(
            shape = (15, 15),
            original_stage_set = PulsarStage
        ).scale(0.4 * 0.8).shift(0.5 * DOWN)
        PulsarText = GDHText("脉冲星").next_to(PulsarCell, DOWN)
        PulsarPeriod = GDHText("周期为3").next_to(PulsarText, DOWN)
        PulsarPeriod[0:2].set_color(YELLOW)
        PulsarPeriod[-1].set_color(BLUE)

        GalaxyStage = np.zeros((13, 13))
        
        for i in [4, 7, 9]:
            GalaxyStage[2][i] = 1
        for i in [2, 3, 5, 7, 8, 9]:
            GalaxyStage[3][i] = 1
        for i in [3, 10]:
            GalaxyStage[4][i] = 1
        for i in [2, 3, 9]:
            GalaxyStage[5][i] = 1
        for i in [3, 9, 10]:
            GalaxyStage[7][i] = 1     
        for i in [2, 9]:   
            GalaxyStage[8][i] = 1
        for i in [3, 4, 5, 7, 9, 10]:
            GalaxyStage[9][i] = 1
        for i in [3, 5, 8]:
            GalaxyStage[10][i] = 1
        GalaxyCell = CellTable(
            shape = (13, 13),
            original_stage_set = GalaxyStage
        ).scale(0.4 * 0.8).shift(0.5 * DOWN)
        GalaxyText = GDHText("高克星系").next_to(GalaxyCell, DOWN)
        GalaxyPeriod = GDHText("周期为8").next_to(GalaxyText, DOWN)
        GalaxyPeriod[0:2].set_color(YELLOW)
        GalaxyPeriod[-1].set_color(BLUE)

        OscillatorText = GDHText("振荡器").scale(1.5).shift(0.3 * LEFT).to_edge(UP)

        for i in range(17):
            BlinkerCell.step()
            if i != 12:
                self.wait(0.5)
            else:
                self.play(FadeIn(OscillatorText, direction = DOWN))
        self.wait(1.5)
        self.play(Write(BlinkerText))
        self.wait(1)
        BlinkerCell.step()
        self.wait(2.5)
        BlinkerCell.step()
        self.wait(2.5)
        BlinkerCell.step()
        self.wait(2.5)
        for i in range(12):
            BlinkerCell.step()
            if i != 9:
                self.wait(0.5)  
            else:
                self.play(Write(BlinkerPeriod)) 
        self.wait(1.5)
        self.remove(BlinkerCell, BlinkerPeriod, BlinkerText)

        surround_vgroup = VGroup(*[
            BackgroundRectangle(sq_no_buff(mob,-0.035), fill_opacity = 0.3, fill_color = YELLOW) 
            for mob in PDCell.get_activated_vgroup()
        ])
        self.add(PDCell, PDText, PDPeriod, surround_vgroup)
        nm = 1
        self.play(FadeIn(huihe))
        for i in range(15):
            PDCell.step()
            nm = i + 2
            self.wait(0.15)
        self.wait(1)
        self.remove(PDCell, PDPeriod, PDText, surround_vgroup)
        surround_vgroup = VGroup(*[
            BackgroundRectangle(sq_no_buff(mob,-0.035), fill_opacity = 0.3, fill_color = YELLOW) 
            for mob in TumblerCell.get_activated_vgroup()
        ])
        self.add(TumblerCell, TumblerText, TumblerPeriod, surround_vgroup)
        nm = 1
        self.play(FadeIn(huihe))
        for i in range(14):
            TumblerCell.step()
            nm = i + 2
            self.wait(0.15)
        self.wait(1)
        self.remove(TumblerCell, TumblerPeriod, TumblerText, surround_vgroup)
        surround_vgroup = VGroup(*[
            BackgroundRectangle(sq_no_buff(mob,-0.035), fill_opacity = 0.3, fill_color = YELLOW) 
            for mob in PulsarCell.get_activated_vgroup()
        ])
        self.add(PulsarCell, PulsarText, PulsarPeriod, surround_vgroup)
        nm = 1
        self.play(FadeIn(huihe))
        for i in range(3):
            PulsarCell.step()
            nm = i + 2
            self.wait(0.5)
        self.wait(1)
        self.remove(PulsarCell, PulsarPeriod, PulsarText, surround_vgroup)
        surround_vgroup = VGroup(*[
            BackgroundRectangle(sq_no_buff(mob,-0.035), fill_opacity = 0.3, fill_color = YELLOW) 
            for mob in GalaxyCell.get_activated_vgroup()
        ])
        self.add(GalaxyCell, GalaxyText, GalaxyPeriod, surround_vgroup)
        nm = 1
        self.play(FadeIn(huihe))
        for i in range(8):
            GalaxyCell.step()
            nm = i + 2
            self.wait(0.15)
        self.wait(2)

class SpaceshipScene(Scene):
    def construct(self):
        def sq_no_buff(sq, buff):
            sq_new = Rectangle(
                height = sq.get_height() - buff, 
                width = sq.get_width() - buff, 
                fill_opacity = 1
            ).move_to(sq.get_center())
            return sq_new

        LightShipStage = np.zeros((18, 18))
        for i in [-1, -4]:
            LightShipStage[6][i] = 1
        LightShipStage[7][-5] = 1
        for i in [-1, -5]:
            LightShipStage[8][i] = 1     
        for i in [-2, -3, -4, -5]:
            LightShipStage[9][i] = 1  

        SpaceshipTitle = GDHText("飞船").scale(1.5).to_edge(UP).shift(0.5 * LEFT)
        LightShipCell = CellTable(
            shape = (18, 18),
            original_stage_set = LightShipStage
        ).scale(0.45).next_to(SpaceshipTitle, DOWN)

        LightShipText = GDHText("轻型飞船").next_to(LightShipCell, RIGHT)

        self.add(LightShipCell)
        surround_vgroup = VGroup(*[
            BackgroundRectangle(sq_no_buff(mob,-0.035), fill_opacity = 0.7, color = PURPLE) 
            for mob in LightShipCell.get_activated_vgroup()
        ])
        trash = []
        self.wait(0.25)
        self.add(surround_vgroup)
        trash.append(surround_vgroup)
        for i in range(20):
            LightShipCell.step()
            if (i + 1) % 4 == 0:
                surround_vgroup = VGroup(*[
                    BackgroundRectangle(sq_no_buff(mob,-0.035), fill_opacity = 0.7) 
                    for mob in LightShipCell.get_activated_vgroup()
                ])

                if i == 3:
                    for mob in surround_vgroup:
                        mob.set_color(BLUE)
                elif i == 7:
                    for mob in surround_vgroup:
                        mob.set_color(GREEN)
                elif i == 11:
                    for mob in surround_vgroup:
                        mob.set_color(ORANGE)
                elif i == 15:
                    for mob in surround_vgroup:
                        mob.set_color(YELLOW)
                elif i == 19:
                    for mob in surround_vgroup:
                        mob.set_color(PINK)                        
                
                self.add(surround_vgroup)
                trash.append(surround_vgroup)

                if i > 3:
                    self.add(arr)
                    trash.append(arr)
            if i <= 3:
                self.wait(0.75)
            else:
                self.wait(0.16)
            if i == 3:
                self.wait(4)
                arr = Arrow(LightShipCell.get_square([7, -1]).get_center(), 
                            LightShipCell.get_square([7,  3]).get_center(), 
                            buff = 0.3, color = RED)

                self.play(GrowArrow(arr), run_time = 0.4)
                trash.append(arr)

        self.wait(1)
        self.play(Write(SpaceshipTitle))
        self.wait(2.5)
        self.play(Write(LightShipText))
        self.wait(1.5)

        self.remove(
            LightShipCell, LightShipText, 
            *[mob for mob in trash]
        )

        GliderStage = np.zeros((10, 10))
        GliderStage[0][1] = GliderStage[1][2] = 1
        GliderStage[2][0] = GliderStage[2][1] = GliderStage[2][2] = 1

        GliderCell = CellTable(
            shape = (10, 10),
            original_stage_set = GliderStage
        ).scale(0.8 * 0.8).next_to(SpaceshipTitle, DOWN)

        GliderText = GDHText("滑翔机").next_to(GliderCell, DOWN)

        self.add(GliderCell, GliderText, SpaceshipTitle)
        self.wait(6)

        for i in range(20):
            GliderCell.step()
            self.wait(0.1)

class GosperSliderGun(Scene):
    def construct(self):
        text = GDHText("高斯帕滑翔机枪", size = 5, color = WHITE)
        self.add(text)

class KaitiText(Text):
    def __init__(self, text: str, font: str = "KaiTi", **kwargs):
        super().__init__(text = text, font = font, **kwargs)

class Reference(Scene):
    def construct(self):
        title = KaitiText("参考资料:").to_edge(UL)
        title.to_edge(UP)
        vg = VGroup(
            title, 
            KaitiText("1. 生命游戏 https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life").scale(0.4),
            KaitiText("2. 【分形与混沌8】生命的源代码？康威生命游戏与复杂性探索 https://www.bilibili.com/video/BV1rJ411n7ri").scale(0.4),
            KaitiText("3. 【混乱博物馆】生命游戏：另一种计算机 https://www.bilibili.com/video/BV1zx41187v3").scale(0.4),
            KaitiText("4. 在生命游戏中建造计算机 https://www.nicolasloizeau.com/gol-computer").scale(0.4),
            KaitiText("5. 一起在康威生命游戏中建造计算机 https://www.youtube.com/watch?v=Kk2MH9O4pXY").scale(0.4),
            KaitiText("6. 康威生命游戏百科 https://www.conwaylife.com/").scale(0.4),
        )
        title.to_edge(UP)
        vg.arrange(DOWN / 2)
        for mob in vg:
            mob.to_edge(LEFT)
    
        self.add(vg)

