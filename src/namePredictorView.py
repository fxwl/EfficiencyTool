"""姓名预测器界面模块 - 预测用户姓名"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class NamePredictorView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("姓名预测器")
        self.window.geometry("450x400")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        # 窗口居中
        centerWindow(self.window)
        
        self.userName = ""
        self.创建界面()
    
    def 创建界面(self):
        """创建姓名预测界面"""
        # 标题
        tk.Label(
            self.window,
            text="🔮 姓名预测器",
            font=("微软雅黑", 18, "bold"),
            fg="#E91E63"
        ).pack(pady=30)
        
        # 说明文字
        tk.Label(
            self.window,
            text="请输入您的姓名，AI将为您预测",
            font=("微软雅黑", 11),
            fg="#666666"
        ).pack(pady=10)
        
        # 输入框
        tk.Label(
            self.window,
            text="您的姓名：",
            font=("微软雅黑", 12)
        ).pack(pady=10)
        
        self.nameEntry = tk.Entry(
            self.window,
            font=("微软雅黑", 14),
            width=20,
            justify='center'
        )
        self.nameEntry.pack(pady=10)
        
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
            fg="#E91E63"
        )
        
        # 预测按钮
        self.predictButton = tk.Button(
            self.window,
            text="开始预测",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#E91E63",
            fg="white",
            command=self.开始预测,
            cursor="hand2"
        )
        self.predictButton.pack(pady=20)
    
    def 开始预测(self):
        """开始预测姓名"""
        self.userName = self.nameEntry.get().strip()
        
        if not self.userName:
            messagebox.showwarning("提示", "请输入您的姓名")
            return
        
        self.predictButton.config(state='disabled')
        self.progressBar['value'] = 0
        self.progressBar.pack()
        self.statusLabel.pack(pady=10)
        
        # 在新线程中执行预测
        thread = threading.Thread(target=self.执行预测)
        thread.daemon = True
        thread.start()
    
    def 执行预测(self):
        """执行预测过程（后台线程）"""
        statusMessages = [
            "正在连接宇宙数据库...",
            "读取姓名信息...",
            "AI推理中...",
            "分析完成..."
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
        """显示预测结果"""
        self.statusLabel.config(text="预测完成！", fg="#4CAF50")
        messagebox.showinfo(
            "预测结果",
            f"经过精密计算\n\n您的名字是：{self.userName}\n\n准确率：100%！"
        )
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
