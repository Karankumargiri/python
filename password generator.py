from tkinter import *
import tkinter.messagebox as msg
import random
import string


class PasswordGenerator(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.resizable(False, False)

        # Centering window
        app_width, app_height = 500, 280
        x = (self.winfo_screenwidth() - app_width) // 2
        y = (self.winfo_screenheight() - app_height) // 2
        self.geometry(f"{app_width}x{app_height}+{x}+{y}")

        self.choice = StringVar(value="high")

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # Heading
        heading = Frame(self, bg="#2b2e30")
        heading.pack(fill=X)
        Label(heading, text="Password Generator", font=("Helvetica", 23, "bold"), fg="#b1ccea", bg="#2b2e30").pack()

        # Length Input
        length_frame = Frame(self, bg="#e5e7ea", pady=10, padx=20)
        length_frame.pack(fill=X)
        Label(length_frame, text="Set password length", font=("Helvetica", 16), bg="#e5e7ea", fg="#1a0944").pack(side=LEFT)
        self.length_entry = Entry(length_frame, width=5, font=("Helvetica", 13))
        self.length_entry.pack(side=LEFT, padx=(10, 0))

        # Strength Selection
        strength_frame = Frame(self, bg="#e5e7ea", pady=10, padx=20)
        strength_frame.pack(fill=X)
        Label(strength_frame, text="Set password strength", font=("Helvetica", 16), bg="#e5e7ea", fg="#1a0944").pack(anchor=W)
        for val in ["low", "medium", "high"]:
            Radiobutton(strength_frame, text=val, value=val, variable=self.choice, font=("Helvetica", 13), bg="#e5e7ea").pack(side=LEFT, padx=20)

        # Generate Button
        button_frame = Frame(self, bg="#e5e7ea", pady=10)
        button_frame.pack(fill=X)
        Button(button_frame, text="GENERATE", bg="#235d48", fg="#e1e6e4", font=("Helvetica", 13, "bold"),
               padx=20, pady=5, bd=0, cursor="hand2", command=self.handle_generate).pack()

    def handle_generate(self):
        try:
            length = int(self.length_entry.get().strip())
            if not 4 <= length <= 80:
                raise ValueError("Length must be between 4 and 80.")
            strength = self.choice.get()
            password = self.generate_password(length, strength)
            self.show_password(length, strength, password)
        except ValueError:
            msg.showwarning("Invalid Input", "Please enter a valid length between 4 and 80.")

    def generate_password(self, length, strength):
        if strength == "low":
            chars = string.ascii_letters
        elif strength == "medium":
            chars = string.ascii_letters + string.digits
        else:  # high
            chars = string.ascii_letters + string.digits + "!@#$%^&*"

        while True:
            password = ''.join(random.choice(chars) for _ in range(length))
            if strength == "medium" and not any(c.isdigit() for c in password):
                continue
            if strength == "high" and (not any(c.isdigit() for c in password) or not any(c in "!@#$%^&*" for c in password)):
                continue
            return password

    def show_password(self, length, strength, password):
        win = Toplevel(self)
        win.geometry("700x215")
        win.title("Generated Password")
        Label(win, text=f"Generated Password\nLength: {length}  Strength: {strength}",
              font=("Helvetica", 16), fg="#1d3b64").pack(pady=10)
        textbox = Text(win, height=3, width=70, font=("Helvetica", 13), fg="#1d3b64", bg="#e5e7ea")
        textbox.insert(END, password)
        textbox.config(state=DISABLED)
        textbox.pack()
        Button(win, text="Close", font=("Helvetica", 13, "bold"), bg="#3c8bdf", fg="#fff",
               width=13, bd=0, command=win.destroy).pack(side=RIGHT, padx=20, pady=10)

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    PasswordGenerator().run()