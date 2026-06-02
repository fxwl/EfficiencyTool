"""时间检测界面模块 - 检测本机时间"""
import tkinter as tk
from tkinter import ttk
import threading
import time
from utils import centerWindow


class TimeDetectorView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        
        self.window = tk.Toplevel()
        self.window.title("本机时间检测")
        self.window.geometry("500x400")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        # 窗口居中
        centerWindow(self.window)
        
        self.arrowWindow = None  # 悬浮箭头窗口
        self.animationRunning = False
        self.创建界面()
    
    def 创建界面(self):
        """创建时间检测界面"""
        # 标题
        tk.Label(
            self.window,
            text="本机时间检测",
            font=("微软雅黑", 18, "bold"),
            fg="#9C27B0"
        ).pack(pady=30)
        
        # 说明文字
        tk.Label(
            self.window,
            text="点击下方按钮检测本机当前时间",
            font=("微软雅黑", 11),
            fg="#666666"
        ).pack(pady=10)
        
        # 进度条容器
        self.progressFrame = tk.Frame(self.window)
        self.progressFrame.pack(pady=30, padx=40, fill='x')
        
        self.progressBar = ttk.Progressbar(
            self.progressFrame,
            length=400,
            mode='determinate',
            maximum=100
        )
        self.progressBar.pack()
        
        self.statusLabel = tk.Label(
            self.progressFrame,
            text="",
            font=("微软雅黑", 10),
            fg="#9C27B0"
        )
        self.statusLabel.pack(pady=10)
        
        # 检测按钮
        self.detectButton = tk.Button(
            self.window,
            text="开始检测",
            font=("微软雅黑", 13),
            width=15,
            height=2,
            bg="#9C27B0",
            fg="white",
            command=self.开始检测,
            cursor="hand2"
        )
        self.detectButton.pack(pady=20)
    
    def 开始检测(self):
        """开始时间检测"""
        self.detectButton.config(state='disabled')
        self.progressBar['value'] = 0
        
        # 在新线程中执行检测
        thread = threading.Thread(target=self.执行检测)
        thread.daemon = True
        thread.start()
    
    def 执行检测(self):
        """执行检测过程（后台线程）"""
        statusMessages = [
            "正在同步时间服务器...",
            "读取系统时钟...",
            "校验时间准确性...",
            "定位时间显示区域...",
            "生成指向标记..."
        ]
        
        for i in range(101):
            time.sleep(0.02)
            
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
        """显示检测结果 - 创建悬浮箭头窗口"""
        self.statusLabel.config(text="✓ 检测完成！", fg="#4CAF50")
        
        # 创建悬浮箭头窗口
        self.创建悬浮箭头()
        
        # 隐藏进度条，显示确定按钮
        self.progressBar.pack_forget()
        self.detectButton.pack_forget()
        
        confirmButton = tk.Button(
            self.window,
            text="确定",
            font=("微软雅黑", 12),
            width=10,
            bg="#9C27B0",
            fg="white",
            command=self.关闭并返回,
            cursor="hand2"
        )
        confirmButton.pack(pady=20)
    
    def 创建悬浮箭头(self):
        """创建指向屏幕右下角时间的悬浮箭头窗口"""
        self.arrowWindow = tk.Toplevel(self.window)
        self.arrowWindow.overrideredirect(True)  # 无边框窗口
        self.arrowWindow.attributes('-topmost', True)  # 置顶
        self.arrowWindow.attributes('-alpha', 0.9)  # 半透明
        
        # 获取屏幕尺寸
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()
        
        # Windows 任务栏时间位置通常在右下角
        # 任务栏高度约40px，时间区域宽度约100px
        timeX = screenWidth - 80  # 时间中心位置
        timeY = screenHeight - 20  # 任务栏中心
        
        # 箭头窗口放在时间上方
        arrowWidth = 200
        arrowHeight = 120
        arrowX = timeX - arrowWidth // 2
        arrowY = timeY - arrowHeight - 50  # 在时间上方50px
        
        self.arrowWindow.geometry(f"{arrowWidth}x{arrowHeight}+{arrowX}+{arrowY}")
        
        # 创建画布
        canvas = tk.Canvas(
            self.arrowWindow,
            width=arrowWidth,
            height=arrowHeight,
            bg='white',
            highlightthickness=3,
            highlightbackground='#9C27B0'
        )
        canvas.pack()
        
        # 绘制指向下方的箭头
        self.arrowId = canvas.create_line(
            arrowWidth // 2, 20,  # 起点（上方中心）
            arrowWidth // 2, arrowHeight - 10,  # 终点（下方中心）
            arrow=tk.LAST,
            width=10,
            fill='#9C27B0',
            arrowshape=(25, 30, 10)
        )
        
        # 添加文字
        canvas.create_text(
            arrowWidth // 2, 10,
            text="↓ 时间在这里 ↓",
            font=("微软雅黑", 11, "bold"),
            fill='#9C27B0'
        )
        
        # 开始闪烁动画
        self.animationRunning = True
        self.箭头动画(canvas)
    
    def 箭头动画(self, canvas):
        """箭头闪烁动画"""
        if not self.animationRunning or not self.arrowWindow.winfo_exists():
            return
        
        # 获取当前颜色
        currentColor = canvas.itemcget(self.arrowId, 'fill')
        
        # 切换颜色（闪烁效果）
        if currentColor == '#9C27B0':
            canvas.itemconfig(self.arrowId, fill='#E91E63')
        else:
            canvas.itemconfig(self.arrowId, fill='#9C27B0')
        
        # 继续动画
        self.window.after(500, lambda: self.箭头动画(canvas))
    
    def 关闭窗口(self):
        """关闭窗口"""
        self.animationRunning = False
        if self.arrowWindow and self.arrowWindow.winfo_exists():
            self.arrowWindow.destroy()
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        self.animationRunning = False
        if self.arrowWindow and self.arrowWindow.winfo_exists():
            self.arrowWindow.destroy()
        self.window.destroy()
        self.onClose()
