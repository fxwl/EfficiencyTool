"""电脑状态检测界面模块 - 检测电脑开机状态"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class ComputerStatusView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("电脑状态检测")
        self.window.geometry("450x350")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        # 窗口居中
        centerWindow(self.window)
        
        self.创建界面()
    
    def 创建界面(self):
        """创建电脑状态检测界面"""
        # 标题
        tk.Label(
            self.window,
            text="电脑状态检测",
            font=("微软雅黑", 18, "bold"),
            fg="#2196F3"
        ).pack(pady=30)
        
        # 说明文字
        tk.Label(
            self.window,
            text="点击下方按钮检测电脑当前状态",
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
        
        # 检测按钮
        self.detectButton = tk.Button(
            self.window,
            text="开始检测",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#2196F3",
            fg="white",
            command=self.开始检测,
            cursor="hand2"
        )
        self.detectButton.pack(pady=20)
    
    def 开始检测(self):
        """开始电脑状态检测"""
        self.detectButton.config(state='disabled')
        self.progressBar['value'] = 0
        
        # 在新线程中执行检测
        thread = threading.Thread(target=self.执行检测)
        thread.daemon = True
        thread.start()
    
    def 执行检测(self):
        """执行检测过程（后台线程）"""
        statusMessages = [
            "正在初始化检测模块...",
            "读取系统信息中...",
            "检测硬件状态...",
            "分析系统进程...",
            "评估电脑状态...",
            "生成检测报告..."
        ]
        
        for i in range(101):
            time.sleep(0.025)
            
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
        
        # 检测完成
        self.window.after(0, self.显示结果)
    
    def 显示结果(self):
        """显示检测结果"""
        self.statusLabel.config(text="检测完成！", fg="#4CAF50")
        messagebox.showinfo("检测结果", "电脑属于开机状态")
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
