"""音量测试器界面模块"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class VolumeTesterView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("音量测试器")
        self.window.geometry("450x450")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        centerWindow(self.window)
        
        self.volume = tk.IntVar(value=50)
        self.创建界面()
    
    def 创建界面(self):
        """创建界面"""
        tk.Label(
            self.window,
            text="🔊 音量测试器",
            font=("微软雅黑", 18, "bold"),
            fg="#03A9F4"
        ).pack(pady=30)
        
        tk.Label(
            self.window,
            text="请调节音量滑块",
            font=("微软雅黑", 11),
            fg="#666666"
        ).pack(pady=10)
        
        # 音量显示
        self.volumeLabel = tk.Label(
            self.window,
            text="50%",
            font=("微软雅黑", 24, "bold"),
            fg="#03A9F4"
        )
        self.volumeLabel.pack(pady=15)
        
        # 滑动条
        scale = tk.Scale(
            self.window,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.volume,
            command=self.更新音量显示,
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
            fg="#03A9F4"
        )
        
        # 测试按钮
        self.testButton = tk.Button(
            self.window,
            text="开始测试",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#03A9F4",
            fg="white",
            command=self.开始测试,
            cursor="hand2"
        )
        self.testButton.pack(pady=20)
    
    def 更新音量显示(self, value):
        """更新音量显示"""
        self.volumeLabel.config(text=f"{value}%")
    
    def 开始测试(self):
        """开始测试"""
        self.testButton.config(state='disabled')
        self.progressBar['value'] = 0
        self.progressBar.pack()
        self.statusLabel.pack(pady=10)
        
        thread = threading.Thread(target=self.执行测试)
        thread.daemon = True
        thread.start()
    
    def 执行测试(self):
        """执行测试"""
        statusMessages = [
            "正在检测音量...",
            "分析音频输出...",
            "读取声音大小...",
            "测试完成..."
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
        vol = self.volume.get()
        self.statusLabel.config(text="测试完成！", fg="#4CAF50")
        messagebox.showinfo(
            "测试结果",
            f"检测完成！\n\n您的音量设置为：{vol}%\n\n测试成功！"
        )
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
