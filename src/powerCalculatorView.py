"""电量计算界面模块 - 模拟电量计算功能"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class PowerCalculatorView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("电量计算")
        self.window.geometry("450x350")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        # 窗口居中
        centerWindow(self.window)
        
        self.创建界面()
    
    def 创建界面(self):
        """创建电量计算界面"""
        # 标题
        tk.Label(
            self.window,
            text="电量计算工具",
            font=("微软雅黑", 18, "bold"),
            fg="#4CAF50"
        ).pack(pady=30)
        
        # 说明文字
        tk.Label(
            self.window,
            text="点击下方按钮开始计算电量",
            font=("微软雅黑", 11),
            fg="#666666"
        ).pack(pady=10)
        
        # 进度条容器
        self.progressFrame = tk.Frame(self.window)
        self.progressFrame.pack(pady=30, padx=40, fill='x')
        
        self.progressBar = ttk.Progressbar(
            self.progressFrame,
            length=350,
            mode='determinate',
            maximum=100
        )
        self.progressBar.pack()
        
        self.statusLabel = tk.Label(
            self.progressFrame,
            text="",
            font=("微软雅黑", 10),
            fg="#2196F3"
        )
        self.statusLabel.pack(pady=10)
        
        # 计算按钮
        self.calculateButton = tk.Button(
            self.window,
            text="开始计算",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#4CAF50",
            fg="white",
            command=self.开始计算,
            cursor="hand2"
        )
        self.calculateButton.pack(pady=20)
    
    def 开始计算(self):
        """开始电量计算（模拟AI运算）"""
        self.calculateButton.config(state='disabled')
        self.progressBar['value'] = 0
        
        # 在新线程中执行计算
        thread = threading.Thread(target=self.执行计算)
        thread.daemon = True
        thread.start()
    
    def 执行计算(self):
        """执行计算过程（后台线程）"""
        statusMessages = [
            "AI 初始化中...",
            "数据采集中...",
            "神经网络计算中...",
            "深度学习分析中...",
            "电量评估中...",
            "结果生成中..."
        ]
        
        for i in range(101):
            time.sleep(0.03)  # 模拟计算耗时
            
            # 更新进度条
            self.window.after(0, lambda v=i: self.progressBar.config(value=v))
            
            # 更新状态文字
            if i % 17 == 0 and i < len(statusMessages) * 17:
                msgIndex = min(i // 17, len(statusMessages) - 1)
                self.window.after(
                    0,
                    lambda msg=statusMessages[msgIndex]: 
                        self.statusLabel.config(text=msg)
                )
        
        # 计算完成
        self.window.after(0, self.显示结果)
    
    def 显示结果(self):
        """显示计算结果"""
        self.statusLabel.config(text="计算完成！", fg="#4CAF50")
        messagebox.showinfo("计算结果", "有电")
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
