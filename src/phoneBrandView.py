"""手机品牌识别器界面模块"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class PhoneBrandView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("手机品牌识别")
        self.window.geometry("450x420")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        centerWindow(self.window)
        
        self.selectedBrand = tk.StringVar(value="")
        self.创建界面()
    
    def 创建界面(self):
        """创建界面"""
        tk.Label(
            self.window,
            text="📱 手机品牌识别",
            font=("微软雅黑", 18, "bold"),
            fg="#9C27B0"
        ).pack(pady=30)
        
        tk.Label(
            self.window,
            text="请选择您的手机品牌",
            font=("微软雅黑", 11),
            fg="#666666"
        ).pack(pady=10)
        
        # 下拉菜单
        brands = ["请选择", "苹果", "华为", "小米", "OPPO", "vivo", "三星", "其他"]
        
        combobox = ttk.Combobox(
            self.window,
            textvariable=self.selectedBrand,
            values=brands,
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
            fg="#9C27B0"
        )
        
        # 识别按钮
        self.detectButton = tk.Button(
            self.window,
            text="开始识别",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#9C27B0",
            fg="white",
            command=self.开始识别,
            cursor="hand2"
        )
        self.detectButton.pack(pady=20)
    
    def 开始识别(self):
        """开始识别"""
        brand = self.selectedBrand.get()
        if not brand or brand == "请选择":
            messagebox.showwarning("提示", "请先选择手机品牌")
            return
        
        self.detectButton.config(state='disabled')
        self.progressBar['value'] = 0
        self.progressBar.pack()
        self.statusLabel.pack(pady=10)
        
        thread = threading.Thread(target=self.执行识别)
        thread.daemon = True
        thread.start()
    
    def 执行识别(self):
        """执行识别"""
        statusMessages = [
            "正在连接设备...",
            "读取型号信息...",
            "分析品牌特征...",
            "识别完成..."
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
        brand = self.selectedBrand.get()
        self.statusLabel.config(text="识别完成！", fg="#4CAF50")
        messagebox.showinfo(
            "识别结果",
            f"检测完成！\n\n您使用的是：{brand}\n\n识别成功！"
        )
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
