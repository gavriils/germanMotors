import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

class EmblemCreator():
    def __init__(self, font_path='MercedesFont.ttf'):
        self.font_path = font_path
        self.fig, self.ax = plt.subplots(figsize=(6, 6))

    def draw_circle(self, center, radius, color, fill, linewidth):
        circle = plt.Circle(center, radius, color=color, fill=fill, linewidth=linewidth)
        self.ax.add_artist(circle)

    def draw_outermost_circle(self):
        self.draw_circle((0.5, 0.5), 0.49, color='black', fill=False, linewidth=2)

    def draw_second_outer_circle(self):
        self.draw_circle((0.5, 0.5), 0.475, color='black', fill=True, linewidth=2)

    def draw_first_inner_circle(self):
        self.draw_circle((0.5, 0.5), 0.38, color='black', fill=True, linewidth=2)

    def draw_second_inner_circle(self):
        self.draw_circle((0.5, 0.5), 0.38, color='white', fill=False, linewidth=2)

    def draw_tristar(self):
        center = np.array([0.5, 0.5])
        radius = 0.37  # Adjust as needed to fit the emblem
        angles = np.linspace(0, 2 * np.pi, 4)[:-1] + np.pi / 6 + np.pi # 120-degree intervals, starting from 30 degrees
        end_points = []

        for angle in angles:
            x_end = center[0] + radius * np.cos(angle)
            y_end = center[1] + radius * np.sin(angle)
            self.ax.plot([center[0], x_end], [center[1], y_end], color='white', linewidth=2)
            end_points.append((x_end, y_end, angle))

        inner_radius = radius - 0.02  # Adjust as necessary to ensure lines don't overlap
        spread_angle = 6
        for x_end, y_end, angle in end_points:
            for delta in [-np.pi * spread_angle/180, np.pi * spread_angle/180]:  # ±5 degrees
                x_meet = x_end - inner_radius * np.cos(angle + delta)
                y_meet = y_end - inner_radius * np.sin(angle + delta)
                self.ax.plot([x_end, x_meet], [y_end, y_meet], color='white', linewidth=2)

    def draw_inverted_tristar(self):
        center = np.array([0.5, 0.5])
        radius = 0.04  # Adjust as needed to fit the emblem
        angles = np.linspace(0, 2 * np.pi, 4)[:-1] + np.pi / 6 # 120-degree intervals, starting from 30 degrees
        end_points = []

        for angle in angles:
            x_end = center[0] + radius * np.cos(angle)
            y_end = center[1] + radius * np.sin(angle)
            self.ax.plot([center[0], x_end], [center[1], y_end], color='white', linewidth=2)
            end_points.append((x_end, y_end, angle))

    def add_top_text(self, text='German Motors', startAngle=3/4*(np.pi) + np.pi/128):
        mercedes_font = FontProperties(fname=self.font_path, size=20)
        radius = 0.42
        center = (0.5, 0.5)
        angle_step = (2 * np.pi) / len(text) * 1/4
        for i, char in enumerate(text):
            angle = startAngle - np.pi/32 - angle_step * i   # Start angle at 45 degrees
            x = center[0] + radius * np.cos(angle)
            y = center[1] + radius * np.sin(angle)

            # Calculate the rotation angle for tilting
            rotation_angle = np.degrees(np.arctan2(y - center[1], x - center[0])) - 90

            self.ax.text(x, y, char, ha='center', va='center', fontproperties=mercedes_font, color='white', rotation=rotation_angle)

    def add_bottom_text(self, text='Lakewood, CO', startAngle=5/4*(np.pi)):
        mercedes_font = FontProperties(fname=self.font_path, size=20)
        radius = 0.435
        center = (0.5, 0.5)
        angle_step = (2 * np.pi) / len(text)
        for i, char in enumerate(text):
            angle = startAngle + angle_step * i * 0.25  # Start angle at 45 degrees
            x = center[0] + radius * np.cos(angle)
            y = center[1] + radius * np.sin(angle)

            # Calculate the rotation angle for tilting
            rotation_angle = np.degrees(np.arctan2(y - center[1], x - center[0])) + 90

            self.ax.text(x, y, char, ha='center', va='center', fontproperties=mercedes_font, color='white', rotation=rotation_angle)

    def add_center_text(self, first_line = "Mercedes-Benz Service", second_line = "since 1968"):
        location = 0.2
        mercedes_font = FontProperties(fname=self.font_path, size=15)
        self.ax.text(0.5, location + 0.05, first_line, ha='center', va='center', fontproperties=mercedes_font, color='white')
        self.ax.text(0.5, location, second_line, ha='center', va='center', fontproperties=mercedes_font, color='white')

    def set_limits_and_remove_axes(self):
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.axis('off')

    def create_emblem(self, logo_name='emblem.png'):
        self.draw_outermost_circle()
        self.draw_second_outer_circle()
        self.draw_first_inner_circle()
        self.draw_second_inner_circle()
        self.draw_tristar()  # Draw the tristar
        self.draw_inverted_tristar()
        self.add_top_text(text='German Motors')
        self.add_bottom_text(text='The Best Or Nothing')
        self.add_center_text(first_line = "Mercedes-Benz Service", second_line = "since 1968")
        self.set_limits_and_remove_axes()
        plt.savefig(logo_name, bbox_inches='tight', pad_inches=0.1)
        plt.show()

# Usage
emblem_creator = EmblemCreator()
emblem_creator.create_emblem("germanMotors.pdf")
