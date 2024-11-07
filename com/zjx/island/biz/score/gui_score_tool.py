import os
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil

def select_files():
    files = filedialog.askopenfilenames(title="选择多个文件")
    if files:
        selected_files.clear()
        selected_files.extend(files)
        update_file_list_display()
    else:
        messagebox.showwarning("警告", "请至少选择一个文件！")

def update_file_list_display():
    file_list_display.delete(1.0, tk.END)
    for file in selected_files:
        file_list_display.insert(tk.END, file + "\n")

def generate_files():
    if not selected_files:
        messagebox.showwarning("警告", "没有选择文件！")
        return

    template_file = os.path.join(os.getcwd(), 'template.txt')  # 假设模板文件为 template.txt
    if not os.path.exists(template_file):
        messagebox.showerror("错误", "模板文件不存在！")
        return

    output_dir = os.path.join(os.getcwd(), "output_files")
    os.makedirs(output_dir, exist_ok=True)

    for file in selected_files:
        file_name = os.path.basename(file)
        output_file_path = os.path.join(output_dir, f"new_{file_name}")
        shutil.copy(template_file, output_file_path)
        # 根据需要对生成的新文件进行进一步修改...

    messagebox.showinfo("成功", f"生成了 {len(selected_files)} 个新文件，保存在 output_files 目录下")

def main():
    global file_list_display, selected_files

    selected_files = []

    root = tk.Tk()
    root.title("文件生成工具")
    root.geometry("500x400")

    select_button = tk.Button(root, text="选择文件", command=select_files)
    select_button.pack(pady=10)

    generate_button = tk.Button(root, text="生成文件", command=generate_files)
    generate_button.pack(pady=10)

    file_list_display = tk.Text(root, height=15, width=60)
    file_list_display.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
