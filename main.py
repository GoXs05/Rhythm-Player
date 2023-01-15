import time
import tkinter as tk

root = tk.Tk()
root.title("Rhythm Player")

time_sig_label = tk.Label(root, text="\t              Enter Time Signature here. \n\t             (4/4, 3/4, 12/8, etc.)")
time_sig_label.grid(row=0, column=0, sticky="W")
time_sig_entry = tk.Entry(root)
time_sig_entry.grid(row=0, column=1)

rhythm_label = tk.Label(root, text="Enter Rhythm here. \nEnter each value in a different line or separated with a space, \nwith no punctuation in between. (e.g. 0.25 0.25 0.5)\n  The rhythm may be more than 1 measure long. \n\nQuick Value Guide: \nWhole Note: 1 \nHalf Note: 0.5 \nQuarter Note: 0.25 \nEighth Note: 0.125 \nSixteenth Note: 0.0625 \nEtc.")
rhythm_label.grid(row=1, column=0, sticky="W")
rhythm_text = tk.Text(root, width=40, height=10)
rhythm_text.grid(row=1, column=1)

def generate_rhythm():
    time_signature = time_sig_entry.get()

    num, den = time_signature.split("/")

    num = int(num)
    den = int(den)

    beat_duration = 60 / 60  # Tempo in BPM
    # Idea for future functionality implementation - add user input for BPM

    rhythm = rhythm_text.get("1.0", tk.END)

    rhythm = rhythm.split()

    rhythm = [float(x) for x in rhythm]

    for note in rhythm:
        print("Playing a note for", note, "beats")
        time.sleep(note * beat_duration)

generate_button = tk.Button(root, text="Generate Rhythm", command=generate_rhythm)
generate_button.grid(row=2, column=1, pady=10)

root.mainloop()
