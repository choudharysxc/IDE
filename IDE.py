from tkinter import *
from tkinter.filedialog import asksaveasfilename ,askopenfilename
import subprocess

compiler=Tk()
compiler.title("IDE MAx")
file_path=''


def run():
    global file_path
    if file_path == '':
        save_promt = Toplevel()
        text=Label(save_promt,text="Please save your code")
        text.pack
        return
    if file_path:
        command = f"python3 {file_path}"
        process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        output,error =process.communicate()
        code_output.insert('1.0', output.decode('utf-8'))
        code_output.insert('1.0', error)
    else:
        code_output.insert('1.0',"No file selected to run")


def set_file_path(path):
    global file_path
    file_path=path



def openfile():
    path=askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path, 'r') as file:
        code=file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_file_path(path)


def saveas():
    if file_path == '':
        
        path=asksaveasfilename(filetypes=[('Python files','*.py')])
    else:
        path=file_path

    with open(path,'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(path)






menu_bar=Menu(compiler)
file_bar=Menu(menu_bar,tearoff=0)
file_bar.add_command(label='open',command=openfile)
file_bar.add_command(label="Exit",command=exit)
file_bar.add_command(label="Save As",command=saveas)
file_bar.add_command(label="save",command=saveas)
menu_bar.add_cascade(label='File',menu=file_bar)
compiler.config(menu=menu_bar)




run_bar=Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run',command=run)
menu_bar.add_cascade(label='Run',menu=run_bar)
compiler.config(menu=menu_bar)

editor=Text()
editor.pack()
code_output=Text(height=10)
code_output.pack()
compiler.mainloop()

