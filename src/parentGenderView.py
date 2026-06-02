"""父母性别计算器界面模块 - 计算父母性别"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from utils import centerWindow


class ParentGenderView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("父母性别计算器")
        self.window.geometry("450x480")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        # 窗口居中
        centerWindow(self.window)
        
        self.selectedParent = tk.StringVar(value="")
        self.calculateButton = None
        self.创建界面()
    
    def 创建界面(self):
        """创建父母性别计算界面"""
        # 标题
        tk.Label(
            self.window,
            text="父母性别计算器",
            font=("微软雅黑", 18, "bold"),
            fg="#E91E63"
        ).pack(pady=30)
        
        # 说明文字
        tk.Label(
            self.window,
            text="请选择要计算性别的对象",
            font=("微软雅黑", 12),
            fg="#666666"
        ).pack(pady=15)
        
        # 选择按钮容器
        buttonFrame = tk.Frame(self.window)
        buttonFrame.pack(pady=30)
        
        # 父亲按钮
        fatherButton = tk.Radiobutton(
            buttonFrame,
            text="👨 父亲",
            font=("微软雅黑", 16),
            variable=self.selectedParent,
            value="父亲",
            indicatoron=0,
            width=12,
            height=3,
            bg="#2196F3",
            fg="white",
            selectcolor="#1976D2",
            activebackground="#1565C0",
            cursor="hand2"
        )
        fatherButton.pack(side=tk.LEFT, padx=10)
        
        # 母亲按钮
        motherButton = tk.Radiobutton(
            buttonFrame,
            text="👩 母亲",
            font=("微软雅黑", 16),
            variable=self.selectedParent,
            value="母亲",
            indicatoron=0,
            width=12,
            height=3,
            bg="#E91E63",
            fg="white",
            selectcolor="#C2185B",
            activebackground="#AD1457",
            cursor="hand2"
        )
        motherButton.pack(side=tk.LEFT, padx=10)
        
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
        """开始计算性别"""
        selected = self.selectedParent.get()
        
        if not selected:
            messagebox.showwarning("提示", "请先选择父亲或母亲")
            return
        
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
            "正在分析生物特征...",
            "检测染色体信息...",
            "评估性别特征...",
            "生成计算结果..."
        ]
        
        for i in range(101):
            time.sleep(0.02)
            
            # 更新进度条
            self.window.after(0, lambda v=i: self.progressBar.config(value=v))
            
            # 更新状态文字
            if i % 25 == 0 and i < len(statusMessages) * 25:
                msgIndex = min(i // 25, len(statusMessages) - 1)
                self.window.after(
                    0,
                    lambda msg=statusMessages[msgIndex]: 
                        self.statusLabel.config(text=msg)
                )
        
        # 计算完成
        self.window.after(0, self.显示结果)
    
    def 显示结果(self):
        """显示计算结果"""
        selected = self.selectedParent.get()
        
        # 根据选择返回对应性别
        if selected == "父亲":
            result = "男性"
        else:
            result = "女性"
        
        self.statusLabel.config(text="计算完成！", fg="#4CAF50")
        messagebox.showinfo(
            "计算结果",
            f"经过精密计算\n{selected}的性别是：{result}"
        )
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.window.destroy()
        self.onClose()
