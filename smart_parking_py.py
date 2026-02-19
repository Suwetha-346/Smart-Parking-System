import tkinter as tk
import serial
import threading
import queue
from PIL import Image, ImageTk, ImageDraw, ImageFont 

class SmartParkingSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SMART PARKING SYSTEM")
        self.root.maxsize(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.create_gui()
        self.ser = self.find_serial_port()
        if self.ser:
            self.read_queue = queue.Queue()
            self.read_serial_thread = threading.Thread(target=self.read_serial, daemon=True)
            self.read_serial_thread.start()
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  
        else:
            print("Arduino not found. Check connection and try again.")
        self.root.bind("<Configure>", self.on_configure)
        self.car_image = self.load_car_image()

    def create_gui(self):
        self.root.configure(bg="yellow")
        heading_label = tk.Label(self.root, text="SMART PARKING SYSTEM", font=("Helvetica", 24, "bold"), bg="yellow",fg="BLACK")
        heading_label.pack(pady=20)
        self.parking_frame = tk.Frame(self.root, bg="yellow")
        self.parking_frame.pack(fill=tk.BOTH, expand=True)
        self.create_parking_slots(6, 1)  
        self.create_bottom_labels(6)  

    def create_parking_slots(self, num_columns, num_rows):
        for row in range(num_rows):
            for col in range(num_columns):
                slot_number = row * num_columns + col + 1  
                slot = tk.Canvas(self.parking_frame, width=(self.root.winfo_screenwidth() - 260) // num_columns,
                                 height=(self.root.winfo_screenheight() - 190) // num_rows, bg="white", highlightthickness=12,
                                 highlightbackground="black")
                slot.grid(row=row, column=col, padx=10, pady=(10, 5))
                label = tk.Label(slot, text="searching...", font=("Helvetica", 10, "bold"), bg="white")
                label.place(relx=0.5, rely=0.5, anchor="center")

    def create_bottom_labels(self, num_columns):
        for col in range(num_columns):
            slot_name_label = tk.Label(self.parking_frame, text=f"Slot {col+1}", font=("Helvetica", 12, "bold"), bg="yellow")
            slot_name_label.grid(row=2, column=col, pady=0)

    def find_serial_port(self):
        port_name = 'COM10'
        try:
            return serial.Serial(port_name, 9600, timeout=1)
        except serial.SerialException:
            print(f"Error: Unable to open {port_name}. Check the port and try again.")
            return None

    def read_serial(self):
        try:
            while True:
                serial_data = self.ser.readline().decode('utf-8').strip()
                self.read_queue.put(serial_data)
                self.root.after(10, self.process_serial_data)  
        except Exception as e:
            exit(0)
            print(f"Error reading serial data: {e}")

    def process_serial_data(self):
        while not self.read_queue.empty():
            data = self.read_queue.get()
            slot_index = None

            if "1st parking slot is full" in data:
                slot_index = 0
                content = True  # Indicates the slot is full
            elif "1st parking slot is empty" in data:
                slot_index = 0
                content = False  # Indicates the slot is empty
            elif "2nd parking slot is full" in data:
                slot_index = 1
                content = True
            elif "2nd parking slot is empty" in data:
                slot_index = 1
                content = False
            elif "3rd parking slot is full" in data:
                slot_index = 2
                content = True
            elif "3rd parking slot is empty" in data:
                slot_index = 2
                content = False
            elif "4th parking slot is full" in data:
                slot_index = 3
                content = True
            elif "4th parking slot is empty" in data:
                slot_index = 3
                content = False
            elif "5th parking slot is full" in data:
                slot_index = 4
                content = True
            elif "5th parking slot is empty" in data:
                slot_index = 4
                content = False
            elif "6th parking slot is full" in data:
                slot_index = 5
                content = True
            elif "6th parking slot is empty" in data:
                slot_index = 5
                content = False

            if slot_index is not None:
                self.update_slot_content(slot_index, content)

    def load_car_image(self):
        car_image = Image.open("car_parking.png")  
        car_image = car_image.resize((268, 715)) 
        return ImageTk.PhotoImage(car_image)

    def update_slot_content(self, slot_index, is_full):
        num_columns = 6 
        frame = self.parking_frame
        try:
            slot = frame.grid_slaves(row=slot_index // num_columns, column=slot_index % num_columns)[0]
            slot.destroy()
            new_slot = tk.Canvas(frame, width=(self.root.winfo_screenwidth() - 260) // 6,
                                 height=(self.root.winfo_screenheight() - 190) // 1, bg="white", highlightthickness=12,
                                 highlightbackground="black")
            new_slot.grid(row=slot_index // num_columns, column=slot_index % num_columns, padx=10, pady=(10, 5))  # Added extra padding to the top

            if is_full:
                new_slot.create_image(0, 0, anchor="nw", image=self.car_image)
                new_slot.config(bg="red") 
            else:
                rotated_text_image = self.rotate_text_image("Empty!!!", 90)
                rotated_text_photo = ImageTk.PhotoImage(rotated_text_image)
                new_slot.create_image(0, 0, anchor="nw", image=rotated_text_photo)
                new_slot.config(bg="green") 
                new_slot.image = rotated_text_photo  
        except IndexError:
            pass  

    def rotate_text_image(self, text, angle):
        image = Image.new("RGBA", (500, 500), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()  
        font_size = 40  
        bold_font = ImageFont.truetype("arialbd.ttf", font_size)  
        text_bbox = draw.textbbox((0, 0), text, font=bold_font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        text_position = ((300 - text_width) // 2, (210 - text_height) // 2)  
        draw.text(text_position, text, font=bold_font, fill="white")
        rotated_image = image.rotate(angle, expand=True)
        return rotated_image

    def on_closing(self):
        if self.ser.is_open:
            self.ser.close()  
        self.root.destroy() 

    def on_configure(self, event):
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - 50, self.root.winfo_screenheight() - 50))

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartParkingSystemGUI(root)
    root.mainloop()
