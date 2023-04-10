from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 7
    V_LINES_SPACING = 0.1
    vertical_lines = []

    H_NB_LINES = 7
    H_LINES_SPACING = 0.1
    horizontal_lines = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_vertical_lines()
        self.init_horizontal_lines()
    def on_parent(self, widget, parent):
        pass
    def on_size(self, *args):
        self.update_vertical_lines()
        self.update_horizontal_lines()
        print("Init W: " + str(self.width) + " H: " + str(self.height))

    def on_perspective_point_x(self, widget, value):
        pass
    def on_perspective_point_y(self, widget, value):
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            # self.line = Line(points=[100,0,100,100])
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())


    def update_vertical_lines(self):
        # self.line.points = [self.perspective_point_x, 0, self.perspective_point_x, 100]

        spacing = self.V_LINES_SPACING * self.width
        central_line_x = (self.width / 2)
        offset = -int(self.V_NB_LINES/2) + 0.5
        for i in range(0, self.V_NB_LINES):
            x1, y1 = self.transform(int(central_line_x+offset*spacing),0)
            x2, y2 = self.transform(int(central_line_x+offset*spacing),self.height)

            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset+=1


    def init_horizontal_lines(self):
        with self.canvas:
            Color(1,1,1)
            # self.line = Line(points=[100,0,100,100])
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())


    def update_horizontal_lines(self):
        central_line_x = (self.width / 2)
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2) + 0.5

        xmin = central_line_x+offset*spacing
        xmax = central_line_x-offset*spacing
        spacing_y = self.H_LINES_SPACING * self.height
        for i in range(0, self.H_NB_LINES):
            line_y = 0 + i*spacing_y
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]

            self.horizontal_lines[i].points = [x1, y1, x2, y2]
            offset+=1




    def transform(self, x, y):
        # return self.transform_2D(x,y)
        return self.transform_perspective(x, y)

    def transform_2D(self, x,y):
        return int(x),int(y)
    def transform_perspective(self, x, y):
        line_y = y * self.perspective_point_y / self.height
        if line_y>self.perspective_point_y:
            line_y = self.perspective_point_y
        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - line_y
        factor_y = diff_y / self.perspective_point_y
        factor_y = pow(factor_y, 4)
        offset_x = diff_x * factor_y

        tr_x = self.perspective_point_x + offset_x
        tr_y = self.perspective_point_y - factor_y * self.perspective_point_y
        return int(tr_x),int(tr_y)

class GalaxyApp(App):
    pass

GalaxyApp().run()