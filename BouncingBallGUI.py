import tkinter as tk
import time
import random

class BouncingBallGUI(tk.Frame):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.balls = []

        # add widgets to the frame
        self.canvas = tk.Canvas(self,width=400,height=400)
        self.canvas.grid(row=0,columnspan=4)

        x_label = tk.Label(self,text='x:')
        x_label.grid(row=1)

        self.x_value = tk.StringVar()
        self.x_value.set('0')
        
        x_entry = tk.Entry(self,textvariable=self.x_value)
        x_entry.grid(row=1,column=1)

        y_label = tk.Label(self,text='y:')
        y_label.grid(row=1,column=2)

        self.y_value = tk.StringVar()
        self.y_value.set('0')
        
        y_entry = tk.Entry(self,textvariable=self.y_value)
        y_entry.grid(row=1,column=3)

        add_button = tk.Button(self,text='Add Ball',command=self.add_ball)
        add_button.grid(row=2,column=1,columnspan=2)

        self.parent.after(0,self.move_balls)

    def add_ball(self):
        SIZE_OF_BALL = 30
        x_coord = int(self.x_value.get())
        y_coord = int(self.y_value.get())
        
        ball = self.canvas.create_oval(x_coord,y_coord,x_coord + SIZE_OF_BALL,
                                       y_coord + SIZE_OF_BALL,fill='blue')

        self.balls.append([ball,random.uniform(-2,2),random.uniform(-2,2)])

    def move_balls(self):

        for ball_data in self.balls:
            ball = ball_data[0]
            x_dir = ball_data[1]
            y_dir = ball_data[2]
            
            left_x, top_y, right_x, bottom_y = self.canvas.coords(ball)
            if x_dir > 0 and right_x >= self.canvas.winfo_width():
                x_dir *= -1
            if x_dir < 0 and left_x <= 0:
                x_dir *= -1
            if y_dir > 0 and bottom_y >= self.canvas.winfo_height():
                y_dir *= -1
            if y_dir < 0 and top_y <= 0:
                y_dir *= -1
            ball_data[1] = x_dir
            ball_data[2] = y_dir
            self.canvas.move(ball,x_dir,y_dir)

        self.parent.after(20,self.move_balls)
        


if __name__ == '__main__':
    app = tk.Tk()
    frame = BouncingBallGUI(app)
    frame.pack()
    app.mainloop()
