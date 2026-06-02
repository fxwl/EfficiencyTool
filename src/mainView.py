"""主界面模块 - 电脑小工具主页面"""
import tkinter as tk
from tkinter import messagebox
from powerCalculatorView import PowerCalculatorView
from computerStatusView import ComputerStatusView
from garbageCleanerView import GarbageCleanerView
from timeDetectorView import TimeDetectorView
from parentGenderView import ParentGenderView
from stupidityCalculatorView import StupidityCalculatorView
from calculatorView import CalculatorView
from brightnessDetectorView import BrightnessDetectorView
from changePasswordView import ChangePasswordView
from namePredictorView import NamePredictorView
from genderDetectorView import GenderDetectorView
from ageCalculatorView import AgeCalculatorView
from phoneBrandView import PhoneBrandView
from locationDetectorView import LocationDetectorView
from colorDetectorView import ColorDetectorView
from volumeTesterView import VolumeTesterView
from keyboardLanguageView import KeyboardLanguageView
from utils import centerWindow


class MainView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("电脑小工具")
        self.root.geometry("750x750")
        self.root.resizable(False, False)
        
        # 窗口居中
        centerWindow(self.root)
        
        self.创建界面()
    
    def 创建界面(self):
        """创建主界面布局"""
        # 标题
        titleLabel = tk.Label(
            self.root,
            text="电脑小工具",
            font=("微软雅黑", 24, "bold"),
            fg="#333333"
        )
        titleLabel.pack(pady=30)
        
        # 工具按钮容器 - 使用Grid布局实现三列
        buttonFrame = tk.Frame(self.root)
        buttonFrame.pack(expand=True, pady=10)
        
        # 按钮配置
        buttonConfigs = [
            ("⚡ 电量计算", "#FF9800", self.打开电量计算),
            ("🖥 电脑状态检测", "#2196F3", self.打开电脑状态检测),
            ("🗑 电脑垃圾清理", "#4CAF50", self.打开垃圾清理),
            ("⏰ 本机时间检测", "#9C27B0", self.打开时间检测),
            ("👨‍👩 父母性别计算", "#E91E63", self.打开父母性别计算),
            ("🤪 傻逼程度计算", "#F44336", self.打开傻逼程度计算),
            ("🔢 智能计算器", "#00BCD4", self.打开计算器),
            ("💡 屏幕亮度检测", "#FFC107", self.打开亮度检测),
            ("🔑 修改密码", "#607D8B", self.打开修改密码),
            ("🔮 姓名预测器", "#E91E63", self.打开姓名预测),
            ("👤 性别鉴定器", "#00BCD4", self.打开性别鉴定),
            ("🎂 年龄计算器", "#FF9800", self.打开年龄计算),
            ("📱 手机品牌识别", "#9C27B0", self.打开手机品牌),
            ("🌍 所在地定位", "#4CAF50", self.打开所在地定位),
            ("🎨 屏幕颜色检测", "#FF5722", self.打开屏幕颜色),
            ("🔊 音量测试器", "#03A9F4", self.打开音量测试),
            ("⌨️ 键盘语言检测", "#795548", self.打开键盘语言),
        ]
        
        # 创建按钮 - 三列布局
        for index, (text, color, command) in enumerate(buttonConfigs):
            row = index // 3
            col = index % 3
            
            button = tk.Button(
                buttonFrame,
                text=text,
                font=("微软雅黑", 12),
                width=18,
                height=2,
                bg=color,
                fg="white",
                command=command,
                cursor="hand2"
            )
            button.grid(row=row, column=col, padx=8, pady=8)
        
        # 版权信息
        tk.Label(
            self.root,
            text="© 2026 电脑小工具",
            font=("微软雅黑", 9),
            fg="#999999"
        ).pack(side=tk.BOTTOM, pady=10)
    
    def 打开电量计算(self):
        """打开电量计算界面"""
        self.root.withdraw()  # 隐藏主窗口
        PowerCalculatorView(self.root, self.返回主界面)
    
    def 打开电脑状态检测(self):
        """打开电脑状态检测界面"""
        self.root.withdraw()
        ComputerStatusView(self.root, self.返回主界面)
    
    def 打开垃圾清理(self):
        """打开垃圾清理界面"""
        self.root.withdraw()
        GarbageCleanerView(self.root, self.返回主界面)
    
    def 打开时间检测(self):
        """打开时间检测界面"""
        self.root.withdraw()
        TimeDetectorView(self.root, self.返回主界面)
    
    def 打开父母性别计算(self):
        """打开父母性别计算界面"""
        self.root.withdraw()
        ParentGenderView(self.root, self.返回主界面)
    
    def 打开傻逼程度计算(self):
        """打开傻逼程度计算界面"""
        self.root.withdraw()
        StupidityCalculatorView(self.root, self.返回主界面)
    
    def 打开计算器(self):
        """打开计算器界面"""
        self.root.withdraw()
        CalculatorView(self.root, self.返回主界面)
    
    def 打开亮度检测(self):
        """打开屏幕亮度检测界面"""
        self.root.withdraw()
        BrightnessDetectorView(self.root, self.返回主界面)
    
    def 打开修改密码(self):
        """打开修改密码界面"""
        self.root.withdraw()
        ChangePasswordView(self.root, self.返回主界面)
    
    def 打开姓名预测(self):
        """打开姓名预测器"""
        self.root.withdraw()
        NamePredictorView(self.root, self.返回主界面)
    
    def 打开性别鉴定(self):
        """打开性别鉴定器"""
        self.root.withdraw()
        GenderDetectorView(self.root, self.返回主界面)
    
    def 打开年龄计算(self):
        """打开年龄计算器"""
        self.root.withdraw()
        AgeCalculatorView(self.root, self.返回主界面)
    
    def 打开手机品牌(self):
        """打开手机品牌识别"""
        self.root.withdraw()
        PhoneBrandView(self.root, self.返回主界面)
    
    def 打开所在地定位(self):
        """打开所在地定位"""
        self.root.withdraw()
        LocationDetectorView(self.root, self.返回主界面)
    
    def 打开屏幕颜色(self):
        """打开屏幕颜色检测"""
        self.root.withdraw()
        ColorDetectorView(self.root, self.返回主界面)
    
    def 打开音量测试(self):
        """打开音量测试器"""
        self.root.withdraw()
        VolumeTesterView(self.root, self.返回主界面)
    
    def 打开键盘语言(self):
        """打开键盘语言检测"""
        self.root.withdraw()
        KeyboardLanguageView(self.root, self.返回主界面)
    
    def 返回主界面(self):
        """从子页面返回主界面"""
        self.root.deiconify()  # 显示主窗口
    
    def 运行(self):
        """启动主界面"""
        self.root.mainloop()
