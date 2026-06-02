"""登录界面模块 - 处理首次设置密码和后续登录验证"""
import tkinter as tk
from tkinter import ttk, messagebox
import random
from passwordManager import PasswordManager
from utils import centerWindow


class LoginView:
    def __init__(self, root, onLoginSuccess):
        self.root = root
        self.onLoginSuccess = onLoginSuccess
        self.passwordManager = PasswordManager()
        self.currentFrame = None
        
        # 登录验证相关
        self.totalQuestions = random.randint(2, 3)  # 随机2-3次验证
        self.currentQuestion = 0
        self.askedPositions = []  # 已经问过的位置
        
        # 倒计时相关
        self.countdownTimer = None
        self.countdown = 3
        self.countdownLabel = None
        
        self.root.title("登录")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        # 窗口居中
        centerWindow(self.root)
        
        if self.passwordManager.是否首次使用():
            self.显示首次设置界面()
        else:
            self.显示登录界面()
    
    def 显示首次设置界面(self):
        """首次使用 - 滑动设置密码"""
        if self.currentFrame:
            self.currentFrame.destroy()
        
        self.currentFrame = tk.Frame(self.root)
        self.currentFrame.pack(expand=True, fill='both', padx=20, pady=20)
        
        tk.Label(
            self.currentFrame,
            text="欢迎首次使用",
            font=("微软雅黑", 16)
        ).pack(pady=20)
        
        tk.Label(
            self.currentFrame,
            text="请滑动选择您的密码（0-10000）",
            font=("微软雅黑", 12)
        ).pack(pady=5)
        
        tk.Label(
            self.currentFrame,
            text="停止滑动3秒后自动确认",
            font=("微软雅黑", 9),
            fg="#999999"
        ).pack(pady=2)
        
        self.passwordValue = tk.IntVar(value=5000)
        self.passwordLabel = tk.Label(
            self.currentFrame,
            text="5000",
            font=("微软雅黑", 20, "bold"),
            fg="blue"
        )
        self.passwordLabel.pack(pady=10)
        
        # 倒计时标签
        self.countdownLabel = tk.Label(
            self.currentFrame,
            text="",
            font=("微软雅黑", 10),
            fg="#FF5722"
        )
        self.countdownLabel.pack(pady=5)
        
        scale = tk.Scale(
            self.currentFrame,
            from_=0,
            to=10000,
            orient=tk.HORIZONTAL,
            variable=self.passwordValue,
            command=self.更新密码显示,
            length=300
        )
        scale.pack(pady=15)
        
        tk.Button(
            self.currentFrame,
            text="立即确认",
            font=("微软雅黑", 12),
            command=self.保存初始密码,
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=5
        ).pack(pady=10)
        
        # 启动初始倒计时
        self.重置倒计时()
    
    def 更新密码显示(self, value):
        """更新密码显示标签"""
        self.passwordLabel.config(text=value)
        # 滑动时重置倒计时
        self.重置倒计时()
    
    def 重置倒计时(self):
        """重置倒计时"""
        # 取消之前的倒计时
        if self.countdownTimer:
            self.root.after_cancel(self.countdownTimer)
        
        # 重置倒计时秒数
        self.countdown = 3
        self.更新倒计时显示()
    
    def 更新倒计时显示(self):
        """更新倒计时显示并执行倒计时逻辑"""
        if self.countdown > 0:
            self.countdownLabel.config(text=f"⏱ {self.countdown} 秒后自动确认")
            self.countdown -= 1
            self.countdownTimer = self.root.after(1000, self.更新倒计时显示)
        else:
            self.countdownLabel.config(text="✓ 自动确认中...")
            # 延迟100毫秒后保存，让用户看到提示
            self.root.after(100, self.保存初始密码)
    
    def 保存初始密码(self):
        """保存初始密码"""
        # 取消倒计时
        if self.countdownTimer:
            self.root.after_cancel(self.countdownTimer)
            self.countdownTimer = None
        
        passwordStr = str(self.passwordValue.get())
        self.passwordManager.保存密码(passwordStr)
        messagebox.showinfo("成功", "密码设置成功！")
        self.显示登录界面()
    
    def 显示登录界面(self):
        """显示登录验证界面"""
        if self.currentFrame:
            self.currentFrame.destroy()
        
        self.currentFrame = tk.Frame(self.root)
        self.currentFrame.pack(expand=True, fill='both', padx=20, pady=20)
        
        tk.Label(
            self.currentFrame,
            text="登录验证",
            font=("微软雅黑", 16)
        ).pack(pady=20)
        
        # 显示验证进度
        tk.Label(
            self.currentFrame,
            text=f"第 {self.currentQuestion + 1}/{self.totalQuestions} 次验证",
            font=("微软雅黑", 10),
            fg="#666666"
        ).pack(pady=5)
        
        passwordLength = self.passwordManager.获取密码长度()
        
        # 确保不重复问同一个位置
        availablePositions = [i for i in range(passwordLength) if i not in self.askedPositions]
        self.randomPosition = random.choice(availablePositions)
        self.askedPositions.append(self.randomPosition)
        
        tk.Label(
            self.currentFrame,
            text=f"请输入密码的第 {self.randomPosition + 1} 位数字",
            font=("微软雅黑", 12)
        ).pack(pady=10)
        
        self.digitEntry = tk.Entry(
            self.currentFrame,
            font=("微软雅黑", 14),
            width=10,
            justify='center'
        )
        self.digitEntry.pack(pady=10)
        
        tk.Button(
            self.currentFrame,
            text="登录",
            font=("微软雅黑", 12),
            command=self.验证登录,
            bg="#2196F3",
            fg="white",
            padx=30,
            pady=5
        ).pack(pady=20)
    
    def 验证登录(self):
        """验证登录密码"""
        try:
            inputDigit = int(self.digitEntry.get())
            if self.passwordManager.验证密码位(self.randomPosition, inputDigit):
                self.currentQuestion += 1
                
                # 检查是否完成所有验证
                if self.currentQuestion >= self.totalQuestions:
                    messagebox.showinfo("成功", "登录成功！")
                    self.root.destroy()
                    self.onLoginSuccess()
                else:
                    # 继续下一次验证
                    self.显示登录界面()
            else:
                messagebox.showerror("错误", "密码错误，请重试")
                self.digitEntry.delete(0, tk.END)
                # 密码错误，重置验证流程
                self.currentQuestion = 0
                self.askedPositions = []
                self.显示登录界面()
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")
