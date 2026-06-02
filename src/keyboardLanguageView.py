"""键盘语言检测器界面模块"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class KeyboardLanguageView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("键盘语言检测")
        self.window.geometry("450x420")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        centerWindow(self.window)
        
        self.selectedLang = tk.StringVar(value="")
        self.创建界面()
    
    def 创建界面(self):
        """创建界面"""
        tk.Label(
            self.window,
            text="⌨️ 键盘语言检测",
            font=("微软雅黑", 18, "bold"),
            fg="#795548"
        ).pack(pady=30)
        
        tk.Label(
            self.window,
            text="请选择您正在使用的输入法",
            font=("微软雅黑", 11),
            fg="#666666"
        ).pack(pady=10)
        
        # 下拉菜单
        languages = ["请选择", "中文", "英文", "日文", "韩文"]
        
        combobox = ttk.Combobox(
            self.window,
            textvariable=self.selectedLang,
            values=languages,
            state='readonly',
            font=("微软雅黑", 12),
            width=18
        )
        combobox.current(0)
        combobox.pack(pady=15)
        
        # 进度条
        self.progressFrame = tk.Frame(self.window)
        self.progressFrame.pack(pady=20, padx=40, fill='x')
        
        self.progressBar = ttk.Progressbar(
            self.progressFrame,
            length=350,
            mode='determinate',
            maximum=100
        )
        
        self.statusLabel = tk.Label(
            self.progressFrame,
            text="",
            font=("微软雅黑", 10),
            fg="#795548"
        )
        
        # 检测按钮
        self.detectButton = tk.Button(
            self.window,
            text="开始检测",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#795548",
            fg="white",
            command=self.开始检测,
            cursor="hand2"
        )
        self.detectButton.pack(pady=20)
    
    def 开始检测(self):
        """开始检测"""
        lang = self.selectedLang.get()
        if not lang or lang == "请选择":
            messagebox.showwarning("提示", "请先选择语言")
            return
        
        self.detectButton.config(state='disabled')
        self.progressBar['value'] = 0
        self.progressBar.pack()
        self.statusLabel.pack(pady=10)
        
        thread = threading.Thread(target=self.执行检测)
        thread.daemon = True
        thread.start()
    
    def 执行检测(self):
        """执行检测"""
        statusMessages = [
            "正在扫描键盘...",
            "分析输入法...",
            "识别语言类型...",
            "检测完成..."
        ]
        
        for i in range(101):
            time.sleep(0.02)
            self.window.after(0, lambda v=i: self.progressBar.config(value=v))
            
            if i % 25 == 0 and i < len(statusMessages) * 25:
                msgIndex = min(i // 25, len(statusMessages) - 1)
                self.window.after(0, lambda msg=statusMessages[msgIndex]: 
                    self.statusLabel.config(text=msg))
        
        self.window.after(0, self.显示结果)
    
    def 显示结果(self):
        """显示结果"""
        lang = self.selectedLang.get()
        self.statusLabel.config(text="检测完成！", fg="#4CAF50")
        messagebox.showinfo(
            "检测结果",
            f"检测完成！\n\n您正在使用：{lang}输入法\n\n识别成功！"
        )
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
