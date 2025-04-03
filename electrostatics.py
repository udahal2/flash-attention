from manim import *

class PointCharge(ThreeDScene):
    def __init__(self, charge_type, position, radius=0.1, color=BLUE):
        self.charge_type = charge_type
        self.position = position
        self.radius = radius
        self.color = color
        super().__init__()

    def create_charge(self):
        # Create a sphere that represents the charge
        charge = Sphere(radius=self.radius, color=self.color)
        charge.move_to(self.position)
        return charge

class ChargeInteractionScene(ThreeDScene):
    def construct(self):
        # Set up camera and grid to represent 3D space
        self.set_camera_orientation(phi=PI/4, theta=PI/4)
        self.add_axes()

        # Define positions for charges
        positive_charge_position = LEFT * 3 + UP * 2
        negative_charge_position = RIGHT * 3 + DOWN * 2
        
        # Create PointCharge objects
        positive_charge = PointCharge("positive", positive_charge_position, color=YELLOW)
        negative_charge = PointCharge("negative", negative_charge_position, color=RED)
        
        # Create sphere representations
        positive_charge_obj = positive_charge.create_charge()
        negative_charge_obj = negative_charge.create_charge()

        # Add charges to the scene
        self.add(positive_charge_obj, negative_charge_obj)

        # Add electric field vectors representing the electromagnetic field
        self.add_electric_field_vectors(positive_charge_position, negative_charge_position)

        # Animate the movement of the negative charge towards the positive charge
        self.play(
            negative_charge_obj.animate.move_to(positive_charge_position).shift(RIGHT * 0.5),
            run_time=4
        )

        # Add copyright at the end of the video
        self.add_text_copyright()

    def add_axes(self):
        # Create a 3D axis grid to represent 3D space
        axes = ThreeDAxes()
        self.add(axes)

    def add_electric_field_vectors(self, pos_charge, neg_charge):
        # Create electric field vectors from the positive charge to the negative charge
        field_vectors = VGroup()
        num_vectors = 10
        distance = pos_charge - neg_charge
        unit_vector = distance / np.linalg.norm(distance)  # Normalized direction

        for i in range(num_vectors):
            # Create vectors emanating from the positive charge to the negative charge
            start_point = pos_charge + np.array([np.random.uniform(-0.5, 0.5), np.random.uniform(-0.5, 0.5), 0])
            vector = Arrow(start=start_point, end=start_point + unit_vector, buff=0)
            vector.set_color(WHITE).set_opacity(0.8)
            field_vectors.add(vector)

        self.add(field_vectors)

    def add_text_copyright(self):
        # Add your name as a copyright at the bottom right corner
        copyright_text = Text("© Ujwol Dahal", font_size=24).to_corner(DOWN + RIGHT)
        self.add(copyright_text)
