# 电脑小工具 - 您的智能桌面助手

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Stars](https://img.shields.io/github/stars/fxwl/EfficiencyTool?style=social)

**集成17种实用功能的桌面工具集 | 零依赖 | 开箱即用**

[快速开始](#快速开始) • [功能介绍](#功能介绍) • [下载使用](#安装运行) • [常见问题](#常见问题)

</div>

---

## 📢 项目背景

> **本项目首发于 [LINUX DO](https://linux.do/) 社区** 🎉

各位好，我又来发新作品了。

之前发布过 **[[更新 1.1] 可以戒色的 NSFW 内容观看次数跟踪软件](https://github.com/fxwl/NSFW-Content-Engagement-Tracker)**，那次发帖后收到了不少关注。趁着这段时间有空，我又开发了一个新项目。

经过多日的研发和测试，现在正式发布这款**电脑小工具集成系统**。

这次不再是单一功能的软件，而是整合了**17种实用工具**的综合性桌面应用程序，涵盖系统检测、智能计算、设备识别等多个领域。从功能规划到界面设计，从代码实现到测试优化，整个开发过程耗时较长，但我认为最终的成品是值得的。

---

## ✨ 核心特点

- 🎯 **功能全面** - 17种工具模块，一站式解决方案
- 🔐 **安全可靠** - MD5加密存储，2-3次随机位数验证机制
- 🎨 **界面友好** - 现代化设计，3×6网格布局，彩色主题
- ⚡ **零依赖** - 仅需Python标准库，无需安装第三方包
- 💻 **跨平台** - 支持Windows、macOS、Linux
- 🚀 **轻量级** - 256MB内存即可流畅运行

---

## 🎬 快速预览

### 主界面
17个功能按钮，每个配有独特的Emoji图标和彩色主题，一目了然。

### 创新的登录机制
- **首次使用**：滑动条设置密码（0-10000），停止3秒自动确认
- **多重验证**：随机2-3次密码位数验证，位置随机不重复
- **任一错误**：重新开始全部验证，有效防止暴力破解

---

## 🛠️ 功能介绍

### 系统检测类 🖥️
| 功能 | 说明 |
|------|------|
| ⚡ 电量计算 | 智能分析设备电量状态，AI模拟运算 |
| 🖥️ 状态检测 | 一键检测电脑运行状态，进度可视化 |
| 💡 亮度检测 | 自动检测屏幕亮度等级（中亮/大亮/超大亮/超级亮）|
| ⏰ 时间检测 | 创新！动态箭头指向系统时间，带闪烁动画 |
| 🎨 颜色检测 | 精准识别屏幕显示颜色 |
| 🔊 音量测试 | 实时检测系统音量输出水平 |
| ⌨️ 语言检测 | 智能识别键盘输入法语言设置 |

### 系统维护类 🧹
| 功能 | 说明 |
|------|------|
| 🗑️ 垃圾清理 | 扫描临时文件、缓存数据，显示清理进度 |

### 智能计算类 🔢
| 功能 | 说明 |
|------|------|
| 🔢 智能计算器 | 支持1-9数字加法运算 |
| 🎂 年龄计算器 | 智能计算年龄数据 |

### 身份识别类 👤
| 功能 | 说明 |
|------|------|
| � 姓名预测器 | 基于预测算法，准确率100% |
| 👤 性别鉴定器 | 智能性别鉴定，准确率99.99% |
| 👨‍👩 父母性别计算 | 选择父亲/母亲，自动返回对应性别 |

### 设备识别类 📱
| 功能 | 说明 |
|------|------|
| 📱 手机品牌识别 | 快速识别手机品牌信息 |
| 🌍 所在地定位 | 精准地理位置定位，误差0米 |

### 趣味测试类 🎮
| 功能 | 说明 |
|------|------|
| 🤪 傻逼程度计算 | 4道题目，科学计算傻逼程度百分比（娱乐向）|

### 安全管理类 🔐
| 功能 | 说明 |
|------|------|
| 🔑 修改密码 | 两步验证：验证旧密码→设置新密码 |

---

## 🚀 快速开始

### 环境要求
- Python 3.6 或更高版本
- 仅需Python标准库（Tkinter、hashlib等）

### 安装运行

```bash
# 1. 克隆项目
git clone https://github.com/fxwl/EfficiencyTool.git

# 2. 进入源码目录
cd EfficiencyTool/src

# 3. 运行程序
python main.py
```

### 首次使用

**第1步：设置密码**
- 拖动滑动条选择密码（0-10000）
- 停止3秒自动确认，或点击"立即确认"

**第2步：登录验证**
- 系统随机进行2-3次密码验证
- 每次输入密码中指定位置的数字
- ⚠️ 任意一次错误将重新开始

**第3步：开始使用**
- 点击主界面任意功能按钮
- 按提示操作
- 自动返回主界面

---

## 📁 项目结构

```
EfficiencyTool/
├── src/                              # 源代码目录
│   ├── main.py                       # 程序入口
│   ├── loginView.py                  # 登录界面
│   ├── mainView.py                   # 主界面
│   ├── passwordManager.py            # 密码管理
│   ├── utils.py                      # 工具函数
│   ├── changePasswordView.py         # 修改密码
│   ├── powerCalculatorView.py        # 电量计算
│   ├── computerStatusView.py         # 状态检测
│   ├── brightnessDetectorView.py     # 亮度检测
│   ├── garbageCleanerView.py         # 垃圾清理
│   ├── timeDetectorView.py           # 时间检测
│   ├── calculatorView.py             # 计算器
│   ├── ageCalculatorView.py          # 年龄计算
│   ├── namePredictorView.py          # 姓名预测
│   ├── genderDetectorView.py         # 性别鉴定
│   ├── parentGenderView.py           # 父母性别
│   ├── phoneBrandView.py             # 手机品牌
│   ├── locationDetectorView.py       # 地理定位
│   ├── colorDetectorView.py          # 颜色检测
│   ├── volumeTesterView.py           # 音量测试
│   ├── keyboardLanguageView.py       # 语言检测
│   └── stupidityCalculatorView.py    # 傻逼程度计算
├── README.md                         # 项目说明
├── requirements.txt                  # 依赖清单（实际为空）
└── LICENSE                           # 开源协议
```

---

## 🎨 界面设计

### 主界面布局
- **3列×6行**网格布局，17个功能按钮
- **彩色主题**：每个功能独特的主题色
- **统一尺寸**：18字符宽×2行高
- **自动居中**：所有窗口启动时自动居中

### 交互特点
- ✅ 滑动条3秒自动确认
- ✅ 进度条显示所有耗时操作
- ✅ 动画效果（时间检测箭头闪烁）
- ✅ 即时状态反馈

---

## 🔒 安全说明

### 数据安全
- 所有数据本地存储，绝不上传
- 密码采用MD5加密
- config.json仅存储加密后的密码

### 使用建议
- 建议定期修改密码
- 请勿分享config.json文件
- 从官方渠道下载程序

---

## ❓ 常见问题

<details>
<summary><b>Q: 忘记密码怎么办？</b></summary>

删除 `src/config.json` 文件，重新启动程序即可重新设置密码。
</details>

<details>
<summary><b>Q: 支持哪些操作系统？</b></summary>

支持 Windows、macOS 和 Linux，只要能运行 Python 3.6+ 即可。
</details>

<details>
<summary><b>Q: 需要安装第三方库吗？</b></summary>

不需要。程序仅使用 Python 标准库，无需安装任何依赖。
</details>

<details>
<summary><b>Q: 资源占用情况？</b></summary>

轻量级设计，内存占用小，CPU占用低，256MB内存即可流畅运行。
</details>

<details>
<summary><b>Q: 部分功能是娱乐性质的吗？</b></summary>

是的。姓名预测器、性别鉴定器、傻逼程度计算器等为趣味娱乐功能。
</details>

---

---

## 📊 版本历史

### v1.0.0 (2026)
- ✨ 首次发布，集成17种功能
- 🎨 现代化界面，三列网格布局
- 🔐 创新的密码验证机制
- ⚡ 性能优化，快速启动
- 🐛 稳定性提升

---

## 📄 开源协议

本项目遵循 MIT 开源协议，详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

感谢所有使用本软件的用户！

如果这个项目对您有帮助：
- ⭐ 给项目点个 Star
- 🍴 Fork 并贡献代码
- 📢 分享给更多朋友
- 💬 提出宝贵建议


---

<div align="center">

**电脑小工具 - 让您的电脑使用更智能、更高效、更有趣！**

Made with ❤️ by [fxwl](https://github.com/fxwl)

© 2026 电脑小工具 版权所有

</div>
