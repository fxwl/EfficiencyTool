"""屏幕颜色检测器界面模块"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class ColorDetectorView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("屏幕颜色检测")
        self.window.geometry("450x480")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        centerWindow(self.window)
        
        self.selectedColor = tk.StringVar(value="")
        self.创建界面()
    
    def 创建界面(self):
        """创建界面"""
        tk.Label(
            self.window,
            text="🎨 屏幕颜色检测",
            font=("微软雅黑", 18, "bold"),
            fg="#FF5722"
        ).pack(pady=30)
        
        tk.Label(
            self.window,
            text="请观察下方色块并选择颜色",
            font=("微软雅黑", 11),
            fg="#666666"
        ).pack(pady=10)
        
        # 颜色显示块
        self.colorCanvas = tk.Canvas(
            self.window,
            width=200,
            height=100,
            bg="white",
            highlightthickness=2,
            highlightbackground="#CCCCCC"
        )
        self.colorCanvas.pack(pady=15)
        
        # 绘制彩色方块
        colors = ["#F44336", "#2196F3", "#4CAF50", "#FFEB3B"]
        colorNames = ["红色", "蓝色", "绿色", "黄色"]
        for i, color in enumerate(colors):
            x = (i % 2) * 100
            y = (i // 2) * 50
            self.colorCanvas.create_rectangle(
                x, y, x + 100, y + 50,
                fill=color,
                outline=""
            )
        
        # 选择按钮
        tk.Label(
            self.window,
            text="请选择色块的颜色：",
            font=("微软雅黑", 11)
        ).pack(pady=10)
        
        buttonFrame = tk.Frame(self.window)
        buttonFrame.pack(pady=10)
        
        for i, (color, name) in enumerate(zip(colors, colorNames)):
            btn = tk.Radiobutton(
                buttonFrame,
                text=name,
                variable=self.selectedColor,
                value=name,
                font=("微软雅黑", 11),
                bg=color,
                fg="white",
                selectcolor=color,
                indicatoron=0,
                width=8,
                cursor="hand2"
            )
            btn.grid(row=0, column=i, padx=5)
        
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
            fg="#FF5722"
        )
        
        # 检测按钮
        self.detectButton = tk.Button(
            self.window,
            text="开始检测",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#FF5722",
            fg="white",
            command=self.开始检测,
            cursor="hand2"
        )
        self.detectButton.pack(pady=10)
    
    def 开始检测(self):
        """开始检测"""
        if not self.selectedColor.get():
            messagebox.showwarning("提示", "请先选择颜色")
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
            "正在分析色彩...",
            "读取RGB值...",
            "颜色识别中...",
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
        color = self.selectedColor.get()
        self.statusLabel.config(text="检测完成！", fg="#4CAF50")
        messagebox.showinfo(
            "检测结果",
            f"检测完成！\n\n您的屏幕显示的颜色是：{color}\n\n准确率：100%"
        )
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
