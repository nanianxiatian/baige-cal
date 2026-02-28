# 阴阳师速度计算器

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一款专为《阴阳师》手游设计的速度计算器，支持白葛和白面两种常用阵容的速度计算。

## ✨ 功能特点

- **白葛计算器**：计算葛叶+白藏主阵容的超阎魔速度
- **白面计算器**：计算面灵气+白藏主阵容的超阎魔速度
- **灵活计算**：支持任意输入两个速度，自动计算第三个速度
- **精确计算**：结果保留4位小数，满足精确需求
- **界面友好**：简洁直观的图形界面，操作便捷

## 📥 下载使用

### 方式一：下载可执行文件（推荐）

**GitHub Release**：
- 前往 [Releases](https://github.com/nanianxiatian/baige-cal/releases/tag/v1.0.0) 页面
- 下载最新版本的 `yys_speed_calc_v4.exe`
- 双击运行即可使用，无需安装Python

**Gitee Release**：
- 前往 [发行版](https://gitee.com/nanianxiatianxy/baige-cal/releases/tag/v1.0.0) 页面
- 下载最新版本的exe文件

### 方式二：运行Python源码

```bash
# 克隆仓库
git clone https://gitee.com/nanianxiatianxy/baige-cal.git

# 进入目录
cd 仓库名

# 运行程序
python calculator.py
```

**环境要求**：
- Python 3.7+
- tkinter（通常随Python一起安装）

## 🎮 使用说明

### 基础速度值

| 式神 | 基础速度 |
|------|----------|
| 葛叶 | 117 |
| 面灵气 | 119 |
| 白藏主 | 111 + 60 = 171 |
| 阎魔 | 127 |

### 计算公式

**白葛阵容**：
```
白藏主实际 × (葛叶实际 + 75) / (75 + 白藏主实际) = 阎魔实际
```

**白面阵容**：
```
白藏主实际 × (面灵气实际 + 60) / (60 + 白藏主实际) = 阎魔实际
```

### 计算示例

1. **已知葛叶和白藏主的御魂速度，求阎魔御魂速度**
   - 选择模式："葛叶御魂速度 + 白藏主御魂速度"
   - 输入葛叶御魂速度（如：100）
   - 输入白藏主御魂速度（如：100）
   - 点击"计算"得到阎魔御魂速度

2. **已知白藏主和阎魔的御魂速度，求葛叶御魂速度**
   - 选择模式："白藏主御魂速度 + 阎魔御魂速度"
   - 输入对应速度值
   - 点击"计算"

## 📸 界面预览

![界面预览](screenshots/preview.png)

## 🛠️ 自行打包

如果你想自己打包成exe文件：

```bash
# 安装pyinstaller
pip install pyinstaller

# 打包
pyinstaller --onefile --windowed --name "阴阳师速度计算器" calculator.py

# 打包后的文件在 dist/ 目录下
```

## 📝 更新日志

### v4.0 (2026-02-28)
- 修正白面计算器的面灵气基础速度为119
- 优化窗口大小，支持完整显示所有内容
- 添加计算公式和详细说明

### v3.0 (2026-02-28)
- 修正计算逻辑，使用正确的实际速度公式
- 支持任意输入两个速度计算第三个

### v2.0 (2026-02-28)
- 重构界面，支持三种计算模式选择
- 添加详细的速度信息显示

### v1.0 (2026-02-27)
- 初始版本发布
- 基础的白葛和白面计算功能

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。

## 💬 联系方式

如有问题或建议，欢迎通过以下方式联系：

- GitHub Issues: [提交问题](https://github.com/你的用户名/仓库名/issues)
- Gitee Issues: [提交问题](https://gitee.com/你的用户名/仓库名/issues)

## 🙏 致谢

感谢《阴阳师》玩家社区提供的计算公式和数据支持。

---

**注意**：本工具仅供学习交流使用，与《阴阳师》官方无关。
