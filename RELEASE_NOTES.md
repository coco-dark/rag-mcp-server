# 发布说明

## 版本 0.1.10 (2025-08-19)

### 🚀 新功能
- 支持 SSE (Server-Sent Events) 传输协议
- 支持 stdio 传输协议
- 完整的 MCP 服务器实现，包括工具、资源和提示管理

### 🔧 技术改进
- 使用 uv 进行包管理和构建
- 优化的依赖管理
- 改进的错误处理和日志记录

### 📦 包信息
- **包名**: `rag-mcp-server-lizhibing`
- **版本**: 0.1.10
- **Python 版本要求**: >= 3.11
- **许可证**: MIT

### 📋 依赖项
- `httpx>=0.28.1` - HTTP 客户端
- `mcp[cli]>=1.13.0` - MCP 协议支持
- `fastapi>=0.104.0` - Web 框架
- `uvicorn>=0.24.0` - ASGI 服务器
- `pydantic>=2.0.0` - 数据验证
- `python-dotenv>=1.0.0` - 环境变量管理

### 🛠️ 安装方法
```bash
# 使用 uv
uv pip install rag-mcp-server-lizhibing==0.1.10

# 使用 pip
pip install rag-mcp-server-lizhibing==0.1.10
```

### 🚀 使用方法
```bash
# 启动 SSE 服务器
python run_server.py --transport sse --port 8080 --host 0.0.0.0 --mount-path /mcp

# 启动 stdio 服务器
python run_server.py --transport stdio
```

### 🔗 相关链接
- **PyPI**: https://pypi.org/project/rag-mcp-server-lizhibing/0.1.10/
- **GitHub**: https://github.com/yourusername/rag-mcp-server

### 📝 更新日志
- 初始版本发布
- 支持 MCP 协议
- 实现 RAG 搜索功能
- 支持多种传输协议

---

## 构建和发布

### 使用 uv 构建
```bash
# 构建包
uv build

# 发布到 PyPI
uv publish --username __token__ --password YOUR_API_TOKEN
```

### 构建产物
- `rag_mcp_server_lizhibing-0.1.10-py3-none-any.whl` - Wheel 包
- `rag_mcp_server_lizhibing-0.1.10.tar.gz` - 源码分发包 