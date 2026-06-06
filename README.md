# Python 编程实践笔记

> 面向 Python 基础语法、面向对象编程、数据库操作、分布式计算与工程化能力训练的结构化代码仓库。

<p>
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=flat-square&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/PySpark-Data%20Processing-E25A1C?style=flat-square&logo=apachespark&logoColor=white" alt="PySpark">
  <img src="https://img.shields.io/badge/Blog-Yunfei's%20Blog-b98b5f?style=flat-square" alt="Blog">
</p>

## 简介

本仓库用于整理 Python 编程学习与工程实践过程中的核心代码，内容覆盖基础语法、数据结构、函数、文件操作、异常处理、面向对象编程、数据库操作、PySpark 分布式计算以及部分进阶编程技术。

仓库采用 **阶段化目录结构** 与 **主题化示例脚本** 进行组织，尽量让每一部分代码都对应一个明确的知识点或实践场景，方便后续复习、查阅和迁移到实际项目中。

相关图文笔记同步发布在个人技术博客：

- Blog: [Yunfei’s Blog](https://nimbusfan.github.io/)
- Repository: [Python-Zero-to-Hero](https://github.com/NimbusFan/Python-Zero-to-Hero)

---

## 目录结构

```text
Python-Zero-to-Hero/
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
├── Stage3_Big_Data/
│   └── 01_PySpark/
│
├── Stage4_Advanced_Techniques/
│   └── 01_Advanced_Techniques/
│
└── README.md
```

---

## 内容概览

### Stage 1 · Python 基础语法与数据结构

这一阶段主要整理 Python 的基础语法、控制结构、函数、数据容器、文件操作、异常处理和基础综合案例。

| 模块 | 内容 |
|---|---|
| `01_Data_Types` | 字面量、变量、数据类型转换、字符串格式化 |
| `02_Condition_Statements` | 布尔逻辑、比较运算符、条件分支 |
| `03_Loop_Statements` | `while` 循环、`for` 循环、迭代逻辑 |
| `04_Functions` | 函数定义、参数传递、返回值 |
| `05_Data_Containers` | 列表、元组、字典、集合、字符串操作 |
| `06_Advanced_Functions` | 函数多返回值、参数传递、匿名函数等 |
| `07_File_Operations` | 文件读取、写入与数据持久化 |
| `08_Exception_Module_Package` | 异常处理、模块与包管理 |
| `09_Basic_Comprehensive_Case` | 基础综合案例与数据可视化实践 |

---

### Stage 2 · 面向对象程序设计

这一阶段主要整理 Python 面向对象编程相关内容，用于建立更系统的程序设计思维。

主要内容包括：

- 类与对象；
- 成员变量与成员方法；
- 构造方法；
- 封装、继承与多态；
- 类型注解；
- 面向对象思想在小型示例中的应用。

---

### Stage 2 · 数据库编程

这一阶段主要整理 SQL 基础语法、MySQL 使用方式以及 Python 操作数据库的实践内容。

主要内容包括：

- SQL 语言分类；
- DDL / DML / DQL 基础操作；
- MySQL 命令行使用；
- 表结构设计与数据操作；
- Python 使用 `pymysql` 连接 MySQL；
- 数据查询、数据插入、事务提交与自动提交。

---

### Stage 3 · 大数据与分布式计算

这一阶段主要整理 PySpark 的基础使用方式，重点理解 SparkContext、RDD 编程模型以及常用算子。

主要内容包括：

- PySpark 运行环境配置；
- SparkContext 与 RDD 基础；
- 数据输入与数据输出；
- `map`、`flatMap`、`reduceByKey`、`filter`、`distinct`、`sortBy` 等常用算子；
- RDD 分区与结果文件输出。

---

### Stage 4 · Python 进阶编程与工程基础

这一阶段主要整理 Python 进阶语法与工程开发中常见的基础能力。

主要内容包括：

- 闭包；
- 装饰器；
- 单例模式与工厂模式；
- 多线程编程；
- Socket 网络通信；
- 正则表达式；
- 递归与文件目录遍历。

---

## 开发环境

| 项目 | 工具 / 版本 |
|---|---|
| 编程语言 | Python 3.13 |
| 数据库 | MySQL |
| 数据库驱动 | PyMySQL |
| 分布式计算 | PySpark |
| 编辑器 | VS Code / PyCharm |
| 笔记工具 | Obsidian |
| 图床工具 | PicGo |

---

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

数据库相关示例需要先安装并启动 MySQL，并根据脚本内容配置数据库连接信息。

PySpark 相关示例需要提前配置 Python 与 PySpark 运行环境。

---

## 组织原则

### 小示例优先

每个脚本尽量聚焦一个知识点或一个明确的实践场景，避免把多个概念混在同一个文件中。

### 可运行优先

示例代码以可执行、可修改、可复现为目标，便于在本地快速验证概念。

### 概念与代码对应

代码内容与博客笔记中的理论说明保持对应，方便从“理解概念”过渡到“动手实现”。

### 面向复习与迁移

目录结构保持清晰，便于后续查阅、复盘，也方便将相关代码片段迁移到实际项目中。

---

## 作者

**Yunfei Fan**

- 本科：河海大学 地理信息科学
- 研究生：华东师范大学 测绘工程
- 关注方向：GIS、空间智能、多模态检索、后端工程与 AI 工程化实践

---

## 说明

本仓库主要用于个人学习记录、代码实践与技术复盘。  
如果其中的目录结构、示例代码或博客笔记对你有帮助，欢迎参考、交流或 Star。