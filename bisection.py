from manim import *
import math

class Bisection(Scene):
    def construct(self):
        # Start with method name----
        text = Text("Bisection method", font="Consolas")
        
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))

        # Add axes----
        axes = Axes(
            x_range = (-3, 3), 
            y_range = (-1, 2),
            axis_config = {
                "color": GREY_A
            })
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio = 0.01, run_time = 1))

        # Axes.get_graph will return the graph of a function
        fn_graph = axes.get_graph(
            lambda x: -0.5 if x < -0.5*math.pi else math.sin(x) + 0.5,
            color = BLUE,
            use_smoothing = True
        )
        
        # Axes.get_graph_label takes in either a string or a mobject
        fn_label = axes.get_graph_label(
            fn_graph, "y = f(x)", x_val = -3, direction = UL
        )
        self.play(
            Create(fn_graph),
            FadeIn(fn_label),
        )
        self.wait()

        # Add red dot at lower bound of interval
        # and green dot at upper bound
        dot_lb = Dot(color = RED)
        dot_lb.move_to(axes.i2gp(-3, fn_graph))
        dot_ub = Dot(color = GREEN)
        dot_ub.move_to(axes.i2gp(3, fn_graph))
        self.play(FadeIn(dot_lb, scale = 0.5))
        self.play(FadeIn(dot_ub, scale = 0.5))

        # Add midpoint dot and coordinate----
        dot_mid = Dot()
        dot_mid.move_to(axes.c2p(0, 0))

        value = VGroup(
            Tex("x = "),
            DecimalNumber(
                0,
                show_ellipsis = False,
                num_decimal_places = 4,
                include_sign = True,
            )
        )
        value.arrange(RIGHT)
        value.next_to(fn_label, 2*UP)

        value[1].add_updater(lambda m: m.set_value(axes.point_to_coords(dot_mid.get_center())[0]))

        self.play(FadeIn(dot_mid, value, scale = 0.5))
        # self.add(value)

        # 1st iteration----
        

        dot1 = Dot(axes.i2gp(0, fn_graph), color = GREEN)
        v_line1 = axes.get_vertical_line(axes.input_to_graph_point(0.0, fn_graph))
        self.play(
            Create(v_line1),
            FadeIn(dot1, scale = 0.5)
        )
        self.wait()

        # 2nd iteration----
        self.play(dot_mid.animate.move_to(axes.c2p(-1.5, 0)))
        self.wait()

        dot2 = Dot(axes.i2gp(-1.5, fn_graph), color = RED)
        v_line2 = axes.get_vertical_line(axes.input_to_graph_point(-1.5, fn_graph))
        self.play(
            Create(v_line2),
            FadeIn(dot2, scale = 0.5)
        )
        self.wait()

        # 3rd iteration----
        self.play(dot_mid.animate.move_to(axes.c2p(-0.75, 0)))
        self.wait()

        dot3 = Dot(axes.i2gp(-0.75, fn_graph), color = RED)
        v_line3 = axes.get_vertical_line(axes.input_to_graph_point(-0.75, fn_graph))
        self.play(
            Create(v_line3),
            FadeIn(dot3, scale = 0.5)
        )
        self.wait()

        # 4th iteration----
        self.play(dot_mid.animate.move_to(axes.c2p(-0.375, 0)))
        self.wait()

        dot4 = Dot(axes.i2gp(-0.375, fn_graph), color = GREEN)
        v_line4 = axes.get_vertical_line(axes.input_to_graph_point(-0.375, fn_graph))
        self.play(
            Create(v_line4),
            FadeIn(dot4, scale = 0.5)
        )
        self.wait()

        # 5th iteration----
        self.play(dot_mid.animate.move_to(axes.c2p(-0.5625, 0)))
        self.wait()

        dot5 = Dot(axes.i2gp(-0.5625, fn_graph), color = RED)
        v_line5 = axes.get_vertical_line(axes.input_to_graph_point(-0.5625, fn_graph))
        self.play(
            Create(v_line5),
            FadeIn(dot5, scale = 0.5)
        )
        self.wait()

        # 6th iteration----
        self.play(dot_mid.animate.move_to(axes.c2p(-0.46875, 0)))
        self.wait()

        dot6 = Dot(axes.i2gp(-0.46875, fn_graph), color = GREEN)
        v_line6 = axes.get_vertical_line(axes.input_to_graph_point(-0.46875, fn_graph))
        self.play(
            Create(v_line6),
            FadeIn(dot6, scale = 0.5)
        )
        self.wait()

        # Finally move to true zero
        self.play(dot_mid.animate.move_to(axes.i2gp(math.asin(-0.5), fn_graph)))
        self.wait()
