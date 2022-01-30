# tupper self referential formula
# Author: kolibril13
# Date: 2021.12.14

from manim import *

formula = r" \frac{1}{2} < \left\lfloor \mathrm{mod}\left(\left\lfloor \frac{y}{17} \right\rfloor 2^{-17 \lfloor x \rfloor - \mathrm{mod}\left(\lfloor y\rfloor, 17\right)},2\right)\right\rfloor "
tex = MathTex(formula)

code= """def tupper(x,y):
    return 0.5 < ((y // 17) // (2**(17 * x + y % 17))) % 2
"""
code = Code(code=code, background_stroke_color= WHITE, tab_width=2, background="window",
                    language="Python", font="Monospace")

def tupper(x,y):
    return 0.5 < ((y // 17) // (2**(17 * x + y % 17))) % 2
N = 4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605266940161251266951421550539554519153785457525756590740540157929001765967965480064427829131488548259914721248506352686630476300
x, y = np.meshgrid(np.arange(107), np.arange(N, N + 17)[::-1])
array= tupper(x, y)

dotgrid = VGroup(*[Dot(radius=0.2, color=BLACK) for d in range(0,array.shape[0]*array.shape[1])]).arrange_in_grid(cols= array.shape[1], buff=0).scale(0.3)
for i, val in enumerate(array.flatten()):
    if val == True:
        dotgrid[i].set_color(WHITE).scale(1.1)
        
class Example(Scene):
    def construct(self):
        VGroup(tex,code,dotgrid).arrange(DOWN)
        self.add(tex,code,dotgrid)