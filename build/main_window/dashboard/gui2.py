from pathlib import Path
from tkinter import Frame, Tk, Canvas, Entry, Text, Button, PhotoImage
import controller as db_controller
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def dashboard():
    Dashboard()
    

class Dashboard(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 470,
            width = 1001,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1001.0,
            470.0,
            fill="#1E2431",
            outline="")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            485.0,
            223.0,
            image=self.image_image_1
        )

        self.total_sale = self.canvas.create_text(
            738.0,
            126.0,
            anchor="nw",
            text="30,000",
            fill="#FFFFFF",
            font=("Lato Bold", 30 * -1)
        )

        self.total_order = self.canvas.create_text(
            784.0,
            335.0,
            anchor="nw",
            text="20,000",
            fill="#FFFFFF",
            font=("Lato Bold", 30 * -1)
        )
    
     
        
        


        self.figure = Figure(figsize=(5, 3), facecolor='#2A2F3A')
        self.ax = self.figure.add_subplot()
        self.canvas_graph = FigureCanvasTkAgg(self.figure, self)
        self.canvas_graph.get_tk_widget().place(x=23, y=85, width=589, height=333)
        
        self.auto_refresh_interval = 2000
        self.auto_refresh()
    def update_text(self):
        total_sales = db_controller.get_total_price()
        total_orders = db_controller.get_total_order()
        self.canvas.itemconfigure(self.total_sale, text=f"₱{total_sales}")
        self.canvas.itemconfigure(self.total_order, text=total_orders)
        self.update_graph(total_sales, total_orders)
        
    def update_graph(self, total_sales, total_orders):
        self.ax.clear()
        categories = ['Sales', 'Order']
        values = [total_sales, total_orders]
        colors = ['#2B70A1', '#FB3968']
        x_pos = np.arange(len(categories))
        
        bars = self.ax.bar(x_pos, values, color=colors)
        self.ax.set_xticks(x_pos)
        self.ax.set_xticklabels(categories, color='white')  # Change text color
        self.ax.set_ylabel('Amount', color='white')  # Change text color
        self.ax.set_title('Sales Performance and No. of Order', color='white')  # Change text color
        self.ax.set_facecolor('#2A2F3A')  # Change background color
        
        # Change bar color
        for bar, color in zip(bars, colors):
            bar.set_color(color)
        
        self.canvas_graph.draw()
        
    def auto_refresh(self):
        self.update_text()
        self.after(self.auto_refresh_interval, self.auto_refresh)
