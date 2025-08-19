# 🚀 RAG MCP服务器快速启动指南

## 5分钟快速上手

### 1. 环境准备
```bash
# 确保Python 3.11+已安装
python --version

# 克隆项目（如果还没有）
git clone <repository-url>
cd rag-mcp-server
```

### 2. 安装依赖
```bash
# 使用uv（推荐）
uv sync

# 或使用pip
pip install -r requirements.txt
```

### 3. 快速测试
```bash
# 运行测试确保一切正常
make test

# 或直接运行
python test_rag_server.py
```

### 4. 功能演示
```bash
# 查看所有功能演示
make demo

# 或直接运行
python demo.py
```

### 5. 启动MCP服务器
```bash
# 使用启动脚本（推荐）
python start_server.py

# 或直接启动
python rag_server.py

# 或使用Makefile
make run
```

## 🎯 常用命令

### 开发命令
```bash
make help          # 查看所有可用命令
make install       # 安装依赖
make test          # 运行测试
make demo          # 运行演示
make run           # 启动服务器
make clean         # 清理临时文件
```

### 启动选项
```bash
# 基本启动
python start_server.py

# 启用调试日志
python start_server.py --log-level DEBUG

# 保存日志到文件
python start_server.py --log-file server.log

# 启动前运行测试
python start_server.py --test
```

## 🔧 MCP工具使用

### 可用的MCP工具
1. **search_docs** - 搜索相关文档
2. **add_document** - 添加新文档
3. **get_document** - 获取特定文档
4. **delete_document** - 删除文档
5. **list_documents** - 列出所有文档
6. **get_server_info** - 获取服务器信息

### 示例调用
```python
# 搜索文档
search_docs("Python编程", 5)

# 添加文档
add_document("新文档内容", '{"category": "demo"}')

# 获取文档
get_document("doc_0")
```

## 📁 项目结构
```
rag-mcp-server/
├── rag_server.py          # 主服务器文件
├── start_server.py        # 启动脚本
├── test_rag_server.py     # 测试套件
├── demo.py               # 功能演示
├── config.json           # 配置文件
├── requirements.txt       # Python依赖
├── Makefile              # 开发工具
├── README.md             # 详细文档
└── QUICKSTART.md         # 快速启动指南
```

## ⚡ 快速验证

### 1. 检查依赖
```bash
python -c "import mcp; print('✅ MCP包已安装')"
```

### 2. 运行测试
```bash
python test_rag_server.py
```

### 3. 启动服务器
```bash
python rag_server.py
# 按Ctrl+C停止
```

## 🐛 常见问题

### 问题1: 导入错误
```bash
# 确保在虚拟环境中
source .venv/bin/activate

# 检查依赖是否安装
uv sync
```

### 问题2: 权限错误
```bash
# 确保文件有执行权限
chmod +x *.py
```

### 问题3: 端口被占用
```bash
# 检查端口使用情况
lsof -i :8000

# 或使用不同端口
python start_server.py --port 8001
```

## 🎉 下一步

1. **阅读完整文档**: 查看 `README.md` 了解详细功能
2. **自定义配置**: 编辑 `config.json` 调整服务器参数
3. **集成客户端**: 配置MCP客户端连接到服务器
4. **扩展功能**: 添加更多文档格式支持和向量模型

## 📞 获取帮助

- 查看 `README.md` 获取详细文档
- 运行 `make help` 查看所有可用命令
- 运行 `python start_server.py --help` 查看启动选项
- 提交GitHub Issue报告问题

---

**提示**: 首次使用建议按顺序执行：`make install` → `make test` → `make demo` → `make run` 