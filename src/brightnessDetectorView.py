"""屏幕亮度检测界面模块 - 检测屏幕亮度"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import random
from utils import centerWindow


class BrightnessDetectorView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("屏幕亮度检测")
        self.window.geometry("450x350")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        # 窗口居中
        centerWindow(self.window)
        
        self.创建界面()
    
    def 创建界面(self):
        """创建屏幕亮度检测界面"""
        # 标题
        tk.Label(
            self.window,
            text="屏幕亮度检测",
            font=("微软雅黑", 18, "bold"),
            fg="#FFC107"
        ).pack(pady=30)
        
        # 说明文字
        tk.Label(
            self.window,
            text="点击下方按钮检测屏幕当前亮度",
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
            fg="#FFC107"
        )
        self.statusLabel.pack(pady=10)
        
        # 检测按钮
        self.detectButton = tk.Button(
            self.window,
            text="开始检测",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#FFC107",
            fg="white",
            command=self.开始检测,
            cursor="hand2"
        )
        self.detectButton.pack(pady=20)
    
    def 开始检测(self):
        """开始亮度检测"""
        self.detectButton.config(state='disabled')
        self.progressBar['value'] = 0
        
        # 在新线程中执行检测
        thread = threading.Thread(target=self.执行检测)
        thread.daemon = True
        thread.start()
    
    def 执行检测(self):
        """执行检测过程（后台线程）"""
        statusMessages = [
            "正在读取显示器信息...",
            "分析光线传感器数据...",
            "测量屏幕亮度值...",
            "评估亮度等级...",
            "生成检测报告..."
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
        
        # 检测完成
        self.window.after(0, self.显示结果)
    
    def 显示结果(self):
        """显示检测结果 - 根据随机值显示亮度等级"""
        # 随机生成亮度等级
        brightnessLevels = [
            ("中亮", "#FF9800"),
            ("大亮", "#FFC107"),
            ("超大亮", "#FFEB3B"),
            ("超级亮", "#FFFF00")
        ]
        
        # 随机选择一个亮度等级
        level, color = random.choice(brightnessLevels)
        
        self.statusLabel.config(text="检测完成！", fg="#4CAF50")
        
        messagebox.showinfo(
            "检测结果",
            f"当前屏幕亮度等级：\n\n{level}"
        )
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
