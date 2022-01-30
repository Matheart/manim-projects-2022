# About root of unity: a unit circle and a graph
# Author: Apostolos
# Date: 2021.12.14

from manim import *
import math
import numpy as np

# no. Roots
n = 6
# Size of graph on left
r = 1.5
# Find average of \zeta_{n}^t
def avgSum(x):
	return np.average([np.exp(complex(0, TAU * x * k / n)) for k in range(n)])

# Make dot have path after it
def updatePath(path, dot):
	path.add_line_to(dot.get_center())

class RootOfUnityFilter(Scene):
	def construct(self):
		# Set up ValueTracker and vtDisplay to show t
		vt = ValueTracker(0)
		vtDisplay = DecimalNumber(font_size=36).set_color(WHITE)
		vtDisplay.add_updater(lambda d: d.set_value(vt.get_value()))
		
		tex1 = Tex('Graph of $z^t$', font_size=40)
		tex2 = Tex(r'For all roots of $z^{'+str(n)+'}-1$', font_size=36)
		tex3 = MathTex(r't=', font_size=36)
		tex4 = Tex(r'Average of all $z^t$', color=RED)
		sublabel = VGroup(tex3, vtDisplay).arrange(RIGHT)
		label = VGroup(tex1, tex2, sublabel).arrange(DOWN)

		#Square around complex plane
		square = Square(side_length=3*r).shift(4.5 * LEFT)
		# Plane showing roots of unity
		plane = ComplexPlane(x_range=(-1.5,1.5,1), y_range=(-1.5,1.5,1), 
			x_length=3*r, y_length=3*r, faded_line_ratio=5
		).add_coordinates().shift(4.5 * LEFT)
		# Plane showing graph of real and imaginary parts of avgDot wrt t
		graph = Axes(x_range=(0,13,1), y_range=(-1,1.5,0.5),
			x_length=6, y_length=2.5*r,
			axis_config={"include_numbers": True, "tip_length": 0.25},
			x_axis_config={"numbers_with_elongated_ticks": [3*i for i in range(5)], 
				"numbers_to_include": [3*i for i in range(5)],
				"line_to_number_buff": 0.35
			}
		).shift(3*RIGHT+0.25*r*UP)

		# Caption of graph
		caption1 = Tex(r'Real part of average', color=YELLOW, font_size=36).shift(3*RIGHT)
		caption2 = Tex(r'Imaginary part of average', color=BLUE, font_size=36).shift(3*RIGHT)
		caption = VGroup(caption1, caption2).arrange(DOWN).shift(3*RIGHT+2*DOWN)

		# Keep labels next to the square
		always(label.next_to, square, UP)
		always(tex4.next_to, square, DOWN)
		self.add(plane)
		self.play(Create(plane), Create(square), Create(graph))

		# Unit circle
		circle = Circle(radius=r, color=DARK_GREY, arc_center=4.5*LEFT)
		# Dots representing roots of unity
		dots = [Dot(radius=0.05, color=LIGHT_GREY, point = 4.5 * LEFT) for i in range(n)]
		lines = [Line(start=4.5*LEFT, end=4.5*LEFT+r*RIGHT, color=GREY) for i in range(n)]
		# List of creation of lines
		lineCreate = [Create(line) for line in lines]
		# Shift dots by r
		dotShift = [Transform(dot, dot.copy().shift(r * RIGHT)) for dot in dots]

		# Average dot
		avgDot = Dot(radius=0.08, color=RED, point = 4.5 * LEFT + r * RIGHT)

		# Real and imaginary dots
		realDot = Dot(radius=0.05, color=YELLOW, point = graph.c2p(0, 1))
		imagDot = Dot(radius=0.05, color=BLUE, point = graph.c2p(0, 0))
		# Automatically add extend path to dot location
		realDot.add_updater(lambda dot: dot.move_to(graph.c2p(vt.get_value(), avgSum(vt.get_value()).real)))
		imagDot.add_updater(lambda dot: dot.move_to(graph.c2p(vt.get_value(), avgSum(vt.get_value()).imag)))

		# Real and imaginary paths
		realPath = VMobject(color=YELLOW)
		realPath.set_points_as_corners([realDot.get_center(), realDot.get_center()])
		# Automatically extend path to dot location
		realPath.add_updater(lambda x: updatePath(realPath, realDot))
		imagPath = VMobject(color=BLUE)
		imagPath.set_points_as_corners([imagDot.get_center(), imagDot.get_center()])
		imagPath.add_updater(lambda x: updatePath(imagPath, imagDot))


		self.add(circle, *lines, *dots, imagPath, realPath, imagDot, realDot)
		self.play(*dotShift, *lineCreate, GrowFromCenter(circle),
			Write(label), Write(caption)
		)
		self.wait(0.1)
		self.play(Create(avgDot), Write(tex4))
		# Get average dot to move automatically
		avgDot.add_updater(lambda dot: dot.move_to(plane.n2p(avgSum(vt.get_value()))))
		
		def changeVT(newVT, speed):
			currentVT = vt.get_value()
			deltaVT = newVT - currentVT
			# Rotate dots at variable speed
			dotRotations = [Rotating(dots[k], radians=k*TAU*deltaVT/n, about_point=4.5*LEFT) for k in range(n)]
			# Rotate lines at variable speed
			lineRotations = [Rotating(lines[k], radians = k*TAU*deltaVT/n, about_point=4.5*LEFT) for k in range(n)]
			self.play(*dotRotations, *lineRotations, vt.animate.set_value(newVT), 
				run_time =  deltaVT/speed, rate_func=rate_functions.ease_in_out_cubic
			)
			self.wait(0.1)

		changeVT(1, 0.4)
		changeVT(2, 0.4)
		changeVT(3, 0.4)
		changeVT(6, 1)
		changeVT(12, 1)