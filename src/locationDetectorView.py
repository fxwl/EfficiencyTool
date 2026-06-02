"""所在地定位器界面模块"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class LocationDetectorView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("所在地定位")
        self.window.geometry("450x400")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        centerWindow(self.window)
        
        self.location = ""
        self.创建界面()
    
    def 创建界面(self):
        """创建界面"""
        tk.Label(
            self.window,
            text="🌍 所在地定位",
            font=("微软雅黑", 18, "bold"),
            fg="#4CAF50"
        ).pack(pady=30)
        
        tk.Label(
            self.window,
            text="请输入您所在的城市",
            font=("微软雅黑", 11),
            fg="#666666"
        ).pack(pady=10)
        
        tk.Label(
            self.window,
            text="城市名称：",
            font=("微软雅黑", 12)
        ).pack(pady=10)
        
        self.locationEntry = tk.Entry(
            self.window,
            font=("微软雅黑", 14),
            width=20,
            justify='center'
        )
        self.locationEntry.pack(pady=10)
        
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
            fg="#4CAF50"
        )
        
        # 定位按钮
        self.locateButton = tk.Button(
            self.window,
            text="开始定位",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#4CAF50",
            fg="white",
            command=self.开始定位,
            cursor="hand2"
        )
        self.locateButton.pack(pady=20)
    
    def 开始定位(self):
        """开始定位"""
        self.location = self.locationEntry.get().strip()
        
        if not self.location:
            messagebox.showwarning("提示", "请输入城市名称")
            return
        
        self.locateButton.config(state='disabled')
        self.progressBar['value'] = 0
        self.progressBar.pack()
        self.statusLabel.pack(pady=10)
        
        thread = threading.Thread(target=self.执行定位)
        thread.daemon = True
        thread.start()
    
    def 执行定位(self):
        """执行定位"""
        statusMessages = [
            "卫星定位中...",
            "分析IP地址...",
            "读取GPS信号...",
            "定位完成..."
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
        self.statusLabel.config(text="定位完成！", fg="#4CAF50")
        messagebox.showinfo(
            "定位结果",
            f"定位成功！\n\n您当前位于：{self.location}\n\n定位误差：0米"
        )
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
