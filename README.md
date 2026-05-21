# Python 工程实践笔记

> 一个面向 Python 语言基础、面向对象编程、数据库操作与后端开发基础的结构化代码实践仓库。

<p>
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-Active-3b3430?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Notes-Blog%20Synced-b98b5f?style=flat-square" alt="Blog Synced">
</p>

## 项目简介

本仓库用于整理和沉淀我的 Python 编程实践代码，内容覆盖 Python 基础语法、数据结构、函数、文件操作、异常处理、面向对象编程以及数据库操作等方向。

与零散代码片段不同，本仓库采用 **阶段化学习路径 + 主题化代码目录 + 可运行示例脚本** 的组织方式，方便持续复习、扩展和工程化整理。

本仓库的主要特点：

- **阶段化组织**：按照 Python 基础、面向对象、数据库编程等方向逐步展开；
- **主题化拆分**：每个目录聚焦一个核心知识点或实践场景；
- **代码可运行**：示例代码以可执行、可修改、可复现实验为目标；
- **博客同步**：对应的理论总结、图文笔记和实践过程同步发布在个人技术博客中。

个人博客：[Yunfei’s Blog](https://NimbusFan.github.io)

## 仓库结构

```text
.
├── Stage1_Core_Basics/
│   ├── 01_Data_Types/
│   ├── 02_Condition_Statements/
│   ├── 03_Loop_Statements/
│   ├── 04_Functions/
│   ├── 05_Data_Containers/
│   ├── 06_Advanced_Functions/
│   ├── 07_File_Operations/
│   ├── 08_Exception_Module_Package/
│   └── 09_Basic_Comprehensive_Case/
│
├── Stage2_OOP/
│   └── 01_Object-Oriented/
│
├── Stage2_Database/
│   └── 02_SQL_MySQL/
│
└── README.md
````

> 仓库结构会随着后续学习和项目实践持续调整。

## 模块说明

### Stage 1 · Python 基础语法与数据结构

该阶段主要整理 Python 的基础语法、控制结构、函数、数据容器、文件操作和异常处理等内容。

| 模块                            | 内容                       |
| ----------------------------- | ------------------------ |
| `01_Data_Types`               | 字面量、变量、数据类型转换、字符串格式化     |
| `02_Condition_Statements`     | 布尔逻辑、比较运算符、条件分支          |
| `03_Loop_Statements`          | `while` 循环、`for` 循环、迭代逻辑 |
| `04_Functions`                | 函数定义、参数传递、返回值            |
| `05_Data_Containers`          | 列表、元组、字典、集合、字符串操作        |
| `06_Advanced_Functions`       | 作用域、匿名函数、函数进阶用法          |
| `07_File_Operations`          | 文件读取、写入与数据持久化            |
| `08_Exception_Module_Package` | 异常处理、模块与包管理              |
| `09_Basic_Comprehensive_Case` | 基础综合案例与数据可视化实践           |

### Stage 2 · 面向对象程序设计

该阶段主要整理 Python 面向对象编程相关内容，帮助建立更系统的程序设计思维。

主要内容包括：

* 类与对象建模；
* 实例属性与实例方法；
* 封装、继承与多态；
* 面向对象思想在小型示例中的应用。

### Stage 2 · 数据库编程

该阶段主要整理 SQL 基础语法、MySQL 使用方式以及 Python 操作数据库的实践内容。

主要内容包括：

* SQL 基础语法；
* DDL / DML / DQL 基础操作；
* MySQL 命令行使用；
* Python 通过 `pymysql` 连接数据库；
* 数据插入、查询、事务提交与自动提交。

## 开发环境

| 项目    | 工具 / 版本           |
| ----- | ----------------- |
| 编程语言  | Python 3.13       |
| 数据库   | MySQL             |
| 数据库驱动 | PyMySQL           |
| 编辑器   | VS Code / PyCharm |
| 笔记工具  | Obsidian          |
| 图床工具  | PicGo             |

## 使用方式

克隆仓库：

```bash
git clone https://github.com/NimbusFan/Python-Zero-to-Hero.git
cd Python-Zero-to-Hero
```

运行指定示例：

```bash
python path/to/example.py
```

如果运行数据库相关示例，请先确保本地已经安装并启动 MySQL，同时正确配置数据库连接信息。

## 组织原则

本仓库遵循以下整理原则：

1. **小示例优先**
   每个脚本尽量聚焦一个知识点或一个明确的实践场景。

2. **可读性优先**
   代码以便于理解、复习和长期维护为目标，而不是追求复杂写法。

3. **概念先行，代码验证**
   先明确知识点的使用场景，再通过代码进行验证。

4. **面向复习与扩展**
   仓库结构尽量保持清晰，方便后续补充项目案例和工程实践内容。

## 作者

**Yunfei Fan**

* 本科：河海大学 地理信息科学
* 研究生：华东师范大学 测绘工程
* 关注方向：GIS、空间智能、多模态检索、后端工程与 AI 工程化实践

## 说明

本仓库主要用于个人学习记录、代码实践和技术复盘。
如果其中的目录结构或示例代码对你有帮助，欢迎参考、交流或 Star。

---

如果这个仓库对你有帮助，欢迎点一个 Star。

```
```
