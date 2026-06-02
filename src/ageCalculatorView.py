"""年龄计算器界面模块 - 计算用户年龄"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class AgeCalculatorView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("年龄计算器")
        self.window.geometry("450x450")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        centerWindow(self.window)
        
        self.age = tk.IntVar(value=25)
        self.创建界面()
    
    def 创建界面(self):
        """创建年龄计算界面"""
        tk.Label(
            self.window,
            text="🎂 年龄计算器",
            font=("微软雅黑", 18, "bold"),
            fg="#FF9800"
        ).pack(pady=30)
        
        tk.Label(
            self.window,
            text="请选择您的年龄，AI将为您计算",
            font=("微软雅黑", 11),
            fg="#666666"
        ).pack(pady=10)
        
        # 年龄显示
        self.ageLabel = tk.Label(
            self.window,
            text="25 岁",
            font=("微软雅黑", 24, "bold"),
            fg="#FF9800"
        )
        self.ageLabel.pack(pady=15)
        
        # 滑动条
        scale = tk.Scale(
            self.window,
            from_=1,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.age,
            command=self.更新年龄显示,
            length=350,
            font=("微软雅黑", 10)
        )
        scale.pack(pady=10)
        
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
            fg="#FF9800"
        )
        
        # 计算按钮
        self.calcButton = tk.Button(
            self.window,
            text="开始计算",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#FF9800",
            fg="white",
            command=self.开始计算,
            cursor="hand2"
        )
        self.calcButton.pack(pady=20)
    
    def 更新年龄显示(self, value):
        """更新年龄显示"""
        self.ageLabel.config(text=f"{value} 岁")
    
    def 开始计算(self):
        """开始计算年龄"""
        self.calcButton.config(state='disabled')
        self.progressBar['value'] = 0
        self.progressBar.pack()
        self.statusLabel.pack(pady=10)
        
        thread = threading.Thread(target=self.执行计算)
        thread.daemon = True
        thread.start()
    
    def 执行计算(self):
        """执行计算过程"""
        statusMessages = [
            "正在分析细胞活力...",
            "计算生命长度...",
            "读取年龄信息...",
            "计算完成..."
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
        """显示计算结果"""
        userAge = self.age.get()
        self.statusLabel.config(text="计算完成！", fg="#4CAF50")
        messagebox.showinfo(
            "计算结果",
            f"根据AI分析\n\n您今年 {userAge} 岁！\n\n是否准确？[非常准确]"
        )
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
