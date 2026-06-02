"""计算器界面模块 - 可能出错的加法计算器"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import random
from utils import centerWindow


class CalculatorView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("智能计算器")
        self.window.geometry("450x450")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        # 窗口居中
        centerWindow(self.window)
        
        self.number1 = tk.IntVar(value=1)
        self.number2 = tk.IntVar(value=1)
        self.创建界面()
    
    def 创建界面(self):
        """创建计算器界面"""
        # 标题
        tk.Label(
            self.window,
            text="智能计算器",
            font=("微软雅黑", 18, "bold"),
            fg="#00BCD4"
        ).pack(pady=30)
        
        # 说明文字
        tk.Label(
            self.window,
            text="选择两个数字进行加法运算",
            font=("微软雅黑", 11),
            fg="#666666"
        ).pack(pady=10)
        
        # 数字选择区域
        selectFrame = tk.Frame(self.window)
        selectFrame.pack(pady=20)
        
        # 第一个数字
        tk.Label(
            selectFrame,
            text="数字1:",
            font=("微软雅黑", 12)
        ).grid(row=0, column=0, padx=10, pady=10)
        
        scale1 = tk.Scale(
            selectFrame,
            from_=1,
            to=9,
            orient=tk.HORIZONTAL,
            variable=self.number1,
            length=200,
            font=("微软雅黑", 12)
        )
        scale1.grid(row=0, column=1, padx=10, pady=10)
        
        # 第二个数字
        tk.Label(
            selectFrame,
            text="数字2:",
            font=("微软雅黑", 12)
        ).grid(row=1, column=0, padx=10, pady=10)
        
        scale2 = tk.Scale(
            selectFrame,
            from_=1,
            to=9,
            orient=tk.HORIZONTAL,
            variable=self.number2,
            length=200,
            font=("微软雅黑", 12)
        )
        scale2.grid(row=1, column=1, padx=10, pady=10)
        
        # 进度条容器
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
            fg="#00BCD4"
        )
        
        # 计算按钮
        self.calculateButton = tk.Button(
            self.window,
            text="开始计算",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#00BCD4",
            fg="white",
            command=self.开始计算,
            cursor="hand2"
        )
        self.calculateButton.pack(pady=20)
    
    def 开始计算(self):
        """开始计算"""
        self.calculateButton.config(state='disabled')
        self.progressBar['value'] = 0
        self.progressBar.pack()
        self.statusLabel.pack(pady=10)
        
        # 在新线程中执行计算
        thread = threading.Thread(target=self.执行计算)
        thread.daemon = True
        thread.start()
    
    def 执行计算(self):
        """执行计算过程（后台线程）"""
        statusMessages = [
            "正在初始化计算引擎...",
            "加载数学模型...",
            "执行加法运算...",
            "验证计算结果...",
            "生成最终答案..."
        ]
        
        for i in range(101):
            time.sleep(0.025)
            
            # 更新进度条
            self.window.after(0, lambda v=i: self.progressBar.config(value=v))
            
            # 更新状态文字
            if i % 20 == 0 and i < len(statusMessages) * 20:
                msgIndex = min(i // 20, len(statusMessages) - 1)
                self.window.after(
                    0,
                    lambda msg=statusMessages[msgIndex]: 
                        self.statusLabel.config(text=msg)
                )
        
        # 计算完成
        self.window.after(0, self.显示结果)
    
    def 显示结果(self):
        """显示计算结果（有概率出错）"""
        num1 = self.number1.get()
        num2 = self.number2.get()
        correctAnswer = num1 + num2
        
        # 30% 概率计算错误
        if random.random() < 0.3:
            # 随机错误：±1 或 ±2
            error = random.choice([-2, -1, 1, 2])
            result = correctAnswer + error
            resultMessage = f"{num1} + {num2} = {result}"
        else:
            result = correctAnswer
            resultMessage = f"{num1} + {num2} = {result}"
        
        self.statusLabel.config(text="计算完成！", fg="#4CAF50")
        messagebox.showinfo("计算结果", resultMessage)
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
