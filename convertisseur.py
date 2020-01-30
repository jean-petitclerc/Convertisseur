import tkinter as tk
import locale
locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'


UNITS = [("Bytes", 1), ("KB", 1024), ("4K blocks", 4096), ("8K blocks", 8192), ("16K blocks", 16384),
         ("32K blocks", 32768), ("MB", 1024*1024), ("GB", 1024**3), ("TB", 1024**4)]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        frame_entree = tk.LabelFrame(self, text="Entrée")
        frame_result = tk.LabelFrame(self, text="Résultats")
        self.ent_val = tk.Entry(frame_entree)
        self.ent_val.pack(side=tk.TOP, padx=10, pady=7)
        self.unite = tk.IntVar()
        self.unite.set(1)
        btn_afficher = tk.Button(text="Afficher", command=self.afficher_resultat)
        self.lbl_status = tk.Label(text="")
        self.buttons = [self.create_radio(frame_entree, c) for c in UNITS]
        for button in self.buttons:
            button.pack(anchor=tk.W, padx=10, pady=3)

        self.var_virg = tk.IntVar()
        self.chk_virg = tk.Checkbutton(frame_result, text="Mode Hai-Thuy", variable=self.var_virg, command=self.afficher_resultat)
        lbl_bytes = tk.Label(frame_result, text="Bytes:")
        lbl_kb = tk.Label(frame_result, text="Kilobytes:")
        lbl_4k = tk.Label(frame_result, text="4 KB blocks:")
        lbl_8k = tk.Label(frame_result, text="8 KB blocks:")
        lbl_16k = tk.Label(frame_result, text="16 KB blocks:")
        lbl_32k = tk.Label(frame_result, text="32 KB blocks:")
        lbl_1m = tk.Label(frame_result, text="Megabytes:")
        lbl_1g = tk.Label(frame_result, text="Gigabytes:")
        lbl_1t = tk.Label(frame_result, text="Térabytes:")
        self.val_bytes = tk.Entry(frame_result, justify="right", state="readonly")
        self.val_kb = tk.Entry(frame_result, justify="right", state="readonly")
        self.val_4k = tk.Entry(frame_result, justify="right", state="readonly")
        self.val_8k = tk.Entry(frame_result, justify="right", state="readonly")
        self.val_16k = tk.Entry(frame_result, justify="right", state="readonly")
        self.val_32k = tk.Entry(frame_result, justify="right", state="readonly")
        self.val_1m = tk.Entry(frame_result, justify="right", state="readonly")
        self.val_1g = tk.Entry(frame_result, justify="right", state="readonly")
        self.val_1t = tk.Entry(frame_result, justify="right", state="readonly")
        self.chk_virg.grid(row=0, column=0, sticky="e", padx=10, pady=5)
        lbl_bytes.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        lbl_kb.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        lbl_4k.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        lbl_8k.grid(row=4, column=0, sticky="e", padx=10, pady=5)
        lbl_16k.grid(row=5, column=0, sticky="e", padx=10, pady=5)
        lbl_32k.grid(row=6, column=0, sticky="e", padx=10, pady=5)
        lbl_1m.grid(row=7, column=0, sticky="e", padx=10, pady=5)
        lbl_1g.grid(row=8, column=0, sticky="e", padx=10, pady=5)
        lbl_1t.grid(row=9, column=0, sticky="e", padx=10, pady=5)
        self.val_bytes.grid(row=1, column=1, sticky="e", padx=10, pady=5)
        self.val_kb.grid(row=2, column=1, sticky="e", padx=10, pady=5)
        self.val_4k.grid(row=3, column=1, sticky="e", padx=10, pady=5)
        self.val_8k.grid(row=4, column=1, sticky="e", padx=10, pady=5)
        self.val_16k.grid(row=5, column=1, sticky="e", padx=10, pady=5)
        self.val_32k.grid(row=6, column=1, sticky="e", padx=10, pady=5)
        self.val_1m.grid(row=7, column=1, sticky="e", padx=10, pady=5)
        self.val_1g.grid(row=8, column=1, sticky="e", padx=10, pady=5)
        self.val_1t.grid(row=9, column=1, sticky="e", padx=10, pady=5)

        #frame_entree.pack(side=tk.LEFT, padx=10, pady=10)
        #frame_result.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH)
        frame_entree.grid(row=0, column=0, padx=10, pady=10, sticky="n")
        frame_result.grid(row=0, column=1, padx=10, pady=10, sticky="n")
        btn_afficher.grid(row=1, column=0, columnspan=2, padx=10, sticky="ew")
        self.lbl_status.grid(row=2, column=0, columnspan=2, sticky="ew")

    def create_radio(self, parent, option):
        text, value = option
        return tk.Radiobutton(parent, text=text, value=value,
                              command=self.afficher_resultat,
                              variable=self.unite)

    def afficher_resultat(self):
        if self.ent_val.get().isdigit():
            quantite = int(self.ent_val.get())
            unite = self.unite.get()
            virgules = self.var_virg.get()
            resultat = quantite * unite
            self.val_bytes.delete(0, tk.END)
            if virgules:
                self.replace_entry(self.val_bytes, f'{resultat:n}')
                self.replace_entry(self.val_kb, f'{resultat//1024:n}')
                self.replace_entry(self.val_4k, f'{resultat//4096:n}')
                self.replace_entry(self.val_8k, f'{resultat//8192:n}')
                self.replace_entry(self.val_16k, f'{resultat//16384:n}')
                self.replace_entry(self.val_32k, f'{resultat//32768:n}')
            else:
                self.replace_entry(self.val_bytes, str(resultat))
                self.replace_entry(self.val_kb, str(resultat//1024))
                self.replace_entry(self.val_4k, str(resultat//4096))
                self.replace_entry(self.val_8k, str(resultat//8192))
                self.replace_entry(self.val_16k, str(resultat//16384))
                self.replace_entry(self.val_32k, str(resultat//32768))
            self.replace_entry(self.val_1m, f'{resultat/(1024**2):9.3f}')
            self.replace_entry(self.val_1g, f'{resultat/(1024**3):6.6f}')
            self.replace_entry(self.val_1t, f'{resultat/(1024**4):3.9f}')
            self.lbl_status.configure(text=" ")
        else:
            self.lbl_status.configure(text="Nombre invalide.")

    def replace_entry(self, ent, val):
        ent.configure(state="normal")
        ent.delete(0, tk.END)
        ent.insert(0, val)
        ent.configure(state="readonly")

if __name__ == "__main__":
    app = App()
    app.title("Convertisseur d'unités")
    app.mainloop()
