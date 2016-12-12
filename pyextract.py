import csv
import os
from Tkinter import *
import tkFileDialog


def multiscan(reader, f):
    next(reader)
    next(reader)
    for row in reader:
        if row != [] and row[0] != '':
            if row[0][0] == ' ' or row[0][0] == 'R':
                f.write('\n')
                f.write('\n')
            elif row[0][0] == 'K':
                break
            elif len(row[1:-1]) > 2:
                f.write('+' + '\t+'.join(row[1:]) + '\n')
    f.write('\n')
    f.write('\n')
    f.close()


def biotek(reader, f):
    for row in reader:
        if row != [] and row[0] != '':
            if row[0][0] == 'r' or row[0][0] == 'K':
                f.write('\n')
            if len(row[1:-1]) > 2:
                f.write('+' + '\t+'.join(row[1:-1]) + '\n')

    f.write('\n')
    f.write('')
    f.close()


def finishedpopup():
        toplevel = Toplevel()
        toplevel.geometry('300x100')
        label1 = Label(toplevel, text='Conversion Finished!').pack()
        toplevel.focus_force()


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('pyextract')
        self.pack(fill=BOTH, expand=1)
        fileopenButton = Button(self, text='Import File', command=self.askopenfilename)
        fileopenButton.place(x=300, y=10)
        filesaveasButton = Button(self, text='Export File', command=self.asksaveasfilename)
        filesaveasButton.place(x=300, y=60)
        convertButton = Button(self, text='Convert', command=self.convert)
        convertButton.place(x=300, y=110)
        self.filetext = Entry(self, width=35)
        self.filetext.place(x=0, y=10)
        self.savefiletext = Entry(self, width=35)
        self.savefiletext.place(x=0, y=60)

        self.file_opt = options = {}
        options['filetypes'] = [('BioTek/Multiscan Files', '*.txt;*.exp'), ('All files', '*.*')]
        options['title'] = 'Import File'
        options['initialdir'] = os.getcwd()

        self.savefile_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('Text Files', '*.txt')]
        options['title'] = 'Export File'
        options['initialdir'] = os.getcwd()

    def askopenfilename(self):
        if len(self.filetext.get()) != 0:
            self.filetext.delete('0', END)
        self.filetext.insert(END, tkFileDialog.askopenfilename(**self.file_opt))

    def asksaveasfilename(self):
        if len(self.savefiletext.get()) != 0:
            self.savefiletext.delete('0', END)
        self.savefiletext.insert(END, tkFileDialog.asksaveasfilename(**self.savefile_opt))

    def convert(self):
        self.filename = self.filetext.get()
        self.savefilename = self.savefiletext.get()
        if self.filename and self.savefilename:
            with open(self.savefilename, 'w') as f:
                with open(self.filename, 'r') as csvfile:
                    reader = csv.reader(csvfile, delimiter='\t')
                    row1 = next(reader)
                    if row1[0][0] == 'P':
                        multiscan(reader, f)
                        finishedpopup()
                    else:
                        biotek(reader, f)
                        finishedpopup()

if __name__ == '__main__':
    gui = Tk()
    gui.geometry('400x150')
    gui.resizable(width=False, height=False)
    app = Window(gui)
    gui.mainloop()
