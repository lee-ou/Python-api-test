# Python API 自动化测试框架

## 📋 项目简介

这是一个基于 Python + pytest + allure 的 API 自动化测试框架，支持数据驱动测试、测试报告生成、邮件通知、钉钉通知等功能。

## 🏗️ 项目结构

```
Python-api-test/
├── commons/               # 公共模块
│   ├── all_requests.py   # HTTP请求封装
│   ├── assert_cases.py   # 断言处理
│   ├── cases.py          # 用例执行逻辑
│   ├── hot_loads.py      # 热加载功能
│   ├── module.py         # 模块管理
│   ├── replace_template.py # 模板替换
│   └── save_extract.py   # 数据提取保存
├── config/               # 配置文件
│   ├── config.yaml       # 主配置文件
│   └── email_template.html # 邮件模板
├── datas/                # 测试数据
│   └── Auth/            # 认证相关数据
├── outputs/              # 输出文件
│   ├── log/             # 日志文件
│   ├── reports/         # 测试报告
│   └── temps/           # 临时文件
├── testcases/           # 测试用例
│   └── test_api_funcs.py # API功能测试
├── utils/               # 工具函数
│   ├── clear_old_files.py # 文件清理
│   ├── copy_data.py      # 数据复制
│   ├── generate_report.py # 报告生成
│   ├── mock_api.py       # Mock API
│   ├── notification_utils.py # 通知工具
│   ├── send_email_utils.py # 邮件发送
│   ├── user_auth.py      # 用户认证
│   └── yaml_handle.py    # YAML处理
├── conftest.py          # pytest配置
├── pytest.ini           # pytest设置
├── requirements.txt     # 依赖管理
└── run.py              # 启动入口
```

## 🚀 快速开始

### 环境准备

1. **Python环境**：确保安装了 Python 3.7+
2. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

### 配置设置

1. **修改配置文件**：编辑 `config/config.yaml`
   - 设置测试环境URL
   - 配置邮件通知（可选）
   - 配置钉钉通知（可选）
   - 配置数据库连接（如需要）

2. **准备测试数据**：在 `datas/` 目录下准备测试用例的 YAML 文件

### 运行测试

1. **执行所有测试**：
   ```bash
   python run.py
   ```

2. **执行特定测试**：
   ```bash
   pytest testcases/test_api_funcs.py -v
   ```

3. **生成 Allure 报告**：
   ```bash
   allure serve outputs/temps/allure_results
   ```

## 📊 功能特性

- ✅ **数据驱动测试**：支持 YAML 格式的测试数据
- ✅ **自动化报告**：集成 Allure 测试报告
- ✅ **多种通知方式**：支持邮件和钉钉通知
- ✅ **日志记录**：详细的测试执行日志
- ✅ **数据提取**：支持响应数据提取和参数化
- ✅ **断言验证**：多种断言方式
- ✅ **环境管理**：支持多环境配置

## 🔧 配置说明

### config.yaml 主要配置项

```yaml
# 基础配置
BaseConfig:
  test_email: '测试邮箱'

# 测试报告
REPORT:
  title: '接口自动化测试报告'

# 项目环境
ENV:
  test_url: '测试环境URL'

# 邮箱配置
SMTP:
  switch: False  # 是否开启邮件通知
  smtp_server: smtp.qq.com
  # ... 其他邮件配置

# 钉钉通知配置
DingTalk_RobotNotice:
  switch: False  # 是否开启钉钉通知
  # ... 其他钉钉配置
```

## 📝 测试用例编写

测试用例使用 YAML 格式编写，示例：

```yaml
- case_info:
    case_name: "获取用户信息"
    url: "/api/user/info"
    method: "GET"
    headers:
      Authorization: "Bearer ${auth_token}"
    expected:
      status_code: 200
      json_path:
        $.code: 0
        $.message: "success"
```

## 🤝 贡献指南

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目使用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

如有问题或建议，请联系项目维护者。 