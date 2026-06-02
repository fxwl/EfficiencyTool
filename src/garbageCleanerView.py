"""垃圾清理界面模块 - 清理电脑垃圾文件"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class GarbageCleanerView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("电脑垃圾清理")
        self.window.geometry("450x350")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        # 窗口居中
        centerWindow(self.window)
        
        self.创建界面()
    
    def 创建界面(self):
        """创建垃圾清理界面"""
        # 标题
        tk.Label(
            self.window,
            text="电脑垃圾清理",
            font=("微软雅黑", 18, "bold"),
            fg="#4CAF50"
        ).pack(pady=30)
        
        # 说明文字
        tk.Label(
            self.window,
            text="点击下方按钮清理电脑垃圾文件",
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
            fg="#4CAF50"
        )
        self.statusLabel.pack(pady=10)
        
        # 清理按钮
        self.cleanButton = tk.Button(
            self.window,
            text="开始清理",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#4CAF50",
            fg="white",
            command=self.开始清理,
            cursor="hand2"
        )
        self.cleanButton.pack(pady=20)
    
    def 开始清理(self):
        """开始垃圾清理"""
        self.cleanButton.config(state='disabled')
        self.progressBar['value'] = 0
        
        # 在新线程中执行清理
        thread = threading.Thread(target=self.执行清理)
        thread.daemon = True
        thread.start()
    
    def 执行清理(self):
        """执行清理过程（后台线程）"""
        statusMessages = [
            "正在扫描垃圾文件...",
            "分析临时文件...",
            "检测系统缓存...",
            "评估清理方案...",
            "尝试清理中...",
            "生成清理报告..."
        ]
        
        for i in range(101):
            time.sleep(0.03)
            
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
        
        # 清理完成
        self.window.after(0, self.显示结果)
    
    def 显示结果(self):
        """显示清理结果"""
        self.statusLabel.config(text="清理流程完成", fg="#FF5722")
        messagebox.showwarning("清理结果", "电脑垃圾过多无法清理")
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
