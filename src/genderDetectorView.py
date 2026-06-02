"""性别鉴定器界面模块 - 鉴定用户性别"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class GenderDetectorView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("性别鉴定器")
        self.window.geometry("450x420")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        # 窗口居中
        centerWindow(self.window)
        
        self.selectedGender = tk.StringVar(value="")
        self.创建界面()
    
    def 创建界面(self):
        """创建性别鉴定界面"""
        # 标题
        tk.Label(
            self.window,
            text="👤 性别鉴定器",
            font=("微软雅黑", 18, "bold"),
            fg="#00BCD4"
        ).pack(pady=30)
        
        # 说明文字
        tk.Label(
            self.window,
            text="请选择您的性别，AI将为您鉴定",
            font=("微软雅黑", 11),
            fg="#666666"
        ).pack(pady=10)
        
        # 选择按钮容器
        buttonFrame = tk.Frame(self.window)
        buttonFrame.pack(pady=20)
        
        # 男性按钮
        maleButton = tk.Radiobutton(
            buttonFrame,
            text="我是男的",
            font=("微软雅黑", 14),
            variable=self.selectedGender,
            value="男性",
            indicatoron=0,
            width=12,
            height=2,
            bg="#2196F3",
            fg="white",
            selectcolor="#1976D2",
            cursor="hand2"
        )
        maleButton.pack(side=tk.LEFT, padx=10)
        
        # 女性按钮
        femaleButton = tk.Radiobutton(
            buttonFrame,
            text="我是女的",
            font=("微软雅黑", 14),
            variable=self.selectedGender,
            value="女性",
            indicatoron=0,
            width=12,
            height=2,
            bg="#E91E63",
            fg="white",
            selectcolor="#C2185B",
            cursor="hand2"
        )
        femaleButton.pack(side=tk.LEFT, padx=10)
        
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
        
        # 鉴定按钮
        self.detectButton = tk.Button(
            self.window,
            text="开始鉴定",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#00BCD4",
            fg="white",
            command=self.开始鉴定,
            cursor="hand2"
        )
        self.detectButton.pack(pady=10)
    
    def 开始鉴定(self):
        """开始鉴定性别"""
        if not self.selectedGender.get():
            messagebox.showwarning("提示", "请先选择性别")
            return
        
        self.detectButton.config(state='disabled')
        self.progressBar['value'] = 0
        self.progressBar.pack()
        self.statusLabel.pack(pady=10)
        
        thread = threading.Thread(target=self.执行鉴定)
        thread.daemon = True
        thread.start()
    
    def 执行鉴定(self):
        """执行鉴定过程"""
        statusMessages = [
            "正在扫描染色体...",
            "分析生物特征...",
            "读取DNA信息...",
            "鉴定完成..."
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
        """显示鉴定结果"""
        gender = self.selectedGender.get()
        self.statusLabel.config(text="鉴定完成！", fg="#4CAF50")
        messagebox.showinfo(
            "鉴定结果",
            f"检测结果：您是{gender}！\n\n检测准确率：99.99%！"
        )
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
