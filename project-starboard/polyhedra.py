# This file animates the rotation of several polyhedras using separate scenes
# Author: Tomáš Sláma
# Date: 2022.01.05

from manim import *

def get_pixel_coordinates(point: np.array):
    x, y, _ = point
    x_ratio = (x + config.frame_x_radius) / (2 * config.frame_x_radius)
    y_ratio = (y + config.frame_y_radius) / (2 * config.frame_y_radius)
    return int(x_ratio * 1920), 1080 - int(y_ratio * 1080)


class PlatonicSolidRotationLayout(Scene):
    def construct(self):
        scale = 0.8
        tetrahedron = VGroup(
            Tex("1. Tetrahedron"),
            FullScreenRectangle().scale(0.3).set_stroke(WHITE, 1),
            # Tetrahedron()[.set_stroke(WHITE,1)0]
        )
        tetrahedron.arrange(DOWN)
        tetrahedron.scale(scale).to_corner(UL)
        print(
            "Tetrahedron pixel coord is {}".format(
                get_pixel_coordinates(tetrahedron[1].get_corner(UL))
            )
        )
        width = tetrahedron[1].width
        height = tetrahedron[1].height
        print(
            "Tetrahedron width is {}".format(
                int(width * 1920 / (2 * config.frame_x_radius))
            )
        )
        print(
            "Tetrahedron height is {}".format(
                int(height * 1080 / (2 * config.frame_y_radius))
            )
        )
        # print(tetrahedron[1].get_center())
        # tetrahedron[2].move_to(tetrahedron[1]).rotate(30*DEGREES, axis=OUT+UR)
        # tetrahedron[2].scale(1.5).set_stroke(BLUE, 1)s
        # tetrahedron[2].add_updater(lambda mob, dt: mob.rotate(dt, axis=UP))

        octahedron = VGroup(Tex("2. Octahedron"), FullScreenRectangle().scale(0.3).set_stroke(WHITE,1))
        octahedron.arrange(DOWN)
        octahedron.scale(scale).to_corner(DL)
        print(
            "Octahedron pixel coord is {}".format(
                get_pixel_coordinates(octahedron[1].get_corner(UL))
            )
        )

        dodecahedron = VGroup(Tex("3. Dodecahedron"), FullScreenRectangle().scale(0.3).set_stroke(WHITE,1))
        dodecahedron.arrange(DOWN)
        dodecahedron.scale(scale).to_corner(UR)
        print(
            "Dodecahedron pixel coord is {}".format(
                get_pixel_coordinates(dodecahedron[1].get_corner(UL))
            )
        )

        icosahedron = VGroup(Tex("4. Icosahedron"), FullScreenRectangle().scale(0.3).set_stroke(WHITE,1))
        icosahedron.arrange(DOWN)
        icosahedron.scale(scale).to_corner(DR)
        print(
            "Icosahedron pixel coord is {}".format(
                get_pixel_coordinates(icosahedron[1].get_corner(UL))
            )
        )

        cube = VGroup(Tex("5. Cube"), FullScreenRectangle().scale(0.3).set_stroke(WHITE,1))
        cube.arrange(DOWN)
        cube.scale(scale).move_to(ORIGIN)
        print(
            "Cube pixel coord is {}".format(get_pixel_coordinates(cube[1].get_corner(UL)))
        )

        self.add(tetrahedron, octahedron, icosahedron, dodecahedron, cube)
        self.wait(10)