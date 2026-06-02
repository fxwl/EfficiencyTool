"""修改密码界面模块 - 处理密码修改"""
import tkinter as tk
from tkinter import messagebox
from passwordManager import PasswordManager
from utils import centerWindow


class ChangePasswordView:
    def __init__(self, parentRoot, onClose):
        self.parentRoot = parentRoot
        self.onClose = onClose
        self.passwordManager = PasswordManager()
        self.passwordManager.加载配置()
        
        self.window = tk.Toplevel()
        self.window.title("修改密码")
        self.window.geometry("400x380")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.关闭窗口)
        
        # 窗口居中
        centerWindow(self.window)
        
        self.currentFrame = None
        self.currentStep = "verify"  # verify: 验证旧密码, set_new: 设置新密码
        
        # 倒计时相关
        self.countdownTimer = None
        self.countdown = 3
        self.countdownLabel = None
        
        self.显示验证旧密码界面()
    
    def 显示验证旧密码界面(self):
        """显示验证旧密码界面"""
        if self.currentFrame:
            self.currentFrame.destroy()
        
        self.currentFrame = tk.Frame(self.window)
        self.currentFrame.pack(expand=True, fill='both', padx=20, pady=20)
        
        tk.Label(
            self.currentFrame,
            text="修改密码",
            font=("微软雅黑", 16)
        ).pack(pady=20)
        
        tk.Label(
            self.currentFrame,
            text="请滑动输入当前密码（0-10000）",
            font=("微软雅黑", 12)
        ).pack(pady=5)
        
        tk.Label(
            self.currentFrame,
            text="停止滑动3秒后自动确认",
            font=("微软雅黑", 9),
            fg="#999999"
        ).pack(pady=2)
        
        self.oldPasswordValue = tk.IntVar(value=5000)
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
            variable=self.oldPasswordValue,
            command=self.更新密码显示,
            length=300
        )
        scale.pack(pady=15)
        
        tk.Button(
            self.currentFrame,
            text="立即确认",
            font=("微软雅黑", 12),
            command=self.验证旧密码,
            bg="#2196F3",
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
            self.window.after_cancel(self.countdownTimer)
        
        # 重置倒计时秒数
        self.countdown = 3
        self.更新倒计时显示()
    
    def 更新倒计时显示(self):
        """更新倒计时显示并执行倒计时逻辑"""
        if self.countdown > 0:
            self.countdownLabel.config(text=f"⏱ {self.countdown} 秒后自动确认")
            self.countdown -= 1
            self.countdownTimer = self.window.after(1000, self.更新倒计时显示)
        else:
            self.countdownLabel.config(text="✓ 自动确认中...")
            # 延迟100毫秒后验证
            if self.currentStep == "verify":
                self.window.after(100, self.验证旧密码)
            else:
                self.window.after(100, self.保存新密码)
    
    def 验证旧密码(self):
        """验证旧密码"""
        # 取消倒计时
        if self.countdownTimer:
            self.window.after_cancel(self.countdownTimer)
            self.countdownTimer = None
        
        oldPasswordStr = str(self.oldPasswordValue.get())
        oldPasswordMd5 = self.passwordManager.passwordData.get('password', '')
        
        import hashlib
        inputMd5 = hashlib.md5(oldPasswordStr.encode()).hexdigest()
        
        if inputMd5 == oldPasswordMd5:
            messagebox.showinfo("验证成功", "旧密码验证通过，请设置新密码")
            self.currentStep = "set_new"
            self.显示设置新密码界面()
        else:
            messagebox.showerror("验证失败", "旧密码错误，请重试")
            self.显示验证旧密码界面()
    
    def 显示设置新密码界面(self):
        """显示设置新密码界面"""
        if self.currentFrame:
            self.currentFrame.destroy()
        
        self.currentFrame = tk.Frame(self.window)
        self.currentFrame.pack(expand=True, fill='both', padx=20, pady=20)
        
        tk.Label(
            self.currentFrame,
            text="设置新密码",
            font=("微软雅黑", 16)
        ).pack(pady=20)
        
        tk.Label(
            self.currentFrame,
            text="请滑动选择新密码（0-10000）",
            font=("微软雅黑", 12)
        ).pack(pady=5)
        
        tk.Label(
            self.currentFrame,
            text="停止滑动3秒后自动确认",
            font=("微软雅黑", 9),
            fg="#999999"
        ).pack(pady=2)
        
        self.newPasswordValue = tk.IntVar(value=5000)
        self.passwordLabel = tk.Label(
            self.currentFrame,
            text="5000",
            font=("微软雅黑", 20, "bold"),
            fg="green"
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
            variable=self.newPasswordValue,
            command=self.更新新密码显示,
            length=300
        )
        scale.pack(pady=15)
        
        tk.Button(
            self.currentFrame,
            text="立即确认",
            font=("微软雅黑", 12),
            command=self.保存新密码,
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=5
        ).pack(pady=10)
        
        # 启动倒计时
        self.重置倒计时()
    
    def 更新新密码显示(self, value):
        """更新新密码显示标签"""
        self.passwordLabel.config(text=value)
        # 滑动时重置倒计时
        self.重置倒计时()
    
    def 保存新密码(self):
        """保存新密码"""
        # 取消倒计时
        if self.countdownTimer:
            self.window.after_cancel(self.countdownTimer)
            self.countdownTimer = None
        
        newPasswordStr = str(self.newPasswordValue.get())
        self.passwordManager.保存密码(newPasswordStr)
        messagebox.showinfo("成功", "密码修改成功！")
        self.关闭并返回()
    
    def 关闭窗口(self):
        """关闭窗口"""
        if self.countdownTimer:
            self.window.after_cancel(self.countdownTimer)
        self.关闭并返回()
    
    def 关闭并返回(self):
        """关闭当前窗口并返回主界面"""
        if self.countdownTimer:
            self.window.after_cancel(self.countdownTimer)
        self.window.destroy()
        self.onClose()
