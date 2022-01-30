# This file animates the fibonacci sequence scene by making use of zooming in / out
# Author: Tomáš Sláma
# Date: 2022.01.05

from manim import *
from random import *

class FibonacciSequence(MovingCameraScene):
    def create_square(self, size):
        return VGroup(Square(side_length=size), Tex(f"${size}^2$").scale(size))

    def get_camera_centering_animation(self, squares):
        h = squares.height * 1.5
        return self.camera.frame.animate.set_height(h).move_to(squares)

    def construct(self):
        squares = VGroup(self.create_square(1))

        self.camera.frame.move_to(squares).set_height(squares.height * 1.5)
        self.camera.frame.save_state()

        self.play(Write(squares[0]))

        n = 7

        a = 1
        b = 1
        directions = [RIGHT, UP, LEFT, DOWN]
        for i in range(n):
            b = b + a
            a = b - a
            # b' = a + b
            # a' = b

            direction = directions[i % 4]

            new_square = self.create_square(a).next_to(squares, direction, buff=0)
            squares.add(new_square)

            self.play(
                FadeIn(new_square, shift=direction * a / 3),
                self.get_camera_centering_animation(squares),
            )

        dot = Dot().move_to(squares[0].get_corner(LEFT + UP)).scale(0.5)

        path = TracedPath(dot.get_center)

        def update_camera_position(camera):
            camera.move_to(dot.get_center())

        self.wait(1)

        self.play(
            squares.animate.set_color(DARK_GRAY),
            AnimationGroup(
                self.camera.frame.animate.restore().move_to(dot),
                Write(dot),
                lag_ratio=0.5,
            ),
        )

        self.add(path)

        self.add(self.camera.frame)
        
        self.camera.frame.add_updater(update_camera_position)

        center_dot = dot.copy()
        self.add(center_dot)

        a = 0
        b = 1
        for i in range(n + 1):
            direction = directions[i % 4] + directions[(i + 1) % 4]
            b = b + a
            a = b - a

            phi = (1 + 5 ** (1 / 2)) / 2
            zoom_coefficient = phi * 0.9
            
            self.play(
                Rotate(
                    dot,
                    about_point=squares[i].get_corner(direction),
                    angle=PI / 2,
                ),
                self.camera.frame.animate.scale(zoom_coefficient),
                rate_func=linear,
            )

        self.camera.frame.clear_updaters()
        path.clear_updaters()

        self.play(self.get_camera_centering_animation(squares))
        
        self.wait(1)

        self.play(
            FadeOut(squares),
            FadeOut(dot),
            AnimationGroup(
                Unwrite(path, run_time=2),
                AnimationGroup(Flash(center_dot, color=WHITE), FadeOut(center_dot)),
                lag_ratio=0.9,
            ),
        )