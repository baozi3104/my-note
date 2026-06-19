# Geek Workspace v2.0 增量升级开发指南 (Developer Guide)

本指南旨在指导开发者在**不丢失原有 notebook.db 数据**的前提下，完成 V2.0 PRD 需求的代码编写与结构升级。

## 🔴 第一步：解决主入口的致命 Bug (main.py)
在开发新功能前，必须先修复当前系统崩溃和无法联调的隐患。
1. **修复路由迷路**：在 `main.py` 顶部，确保将 `total` 导入（提示：`from routes import notes, todos, total`）。
2. **打通前后端桥梁**：在 `main.py` 中引入 `CORSMiddleware` 中间件，并配置允许跨域访问（设为 `allow_origins=["*"]`），否则前端 Vue 必定报错。

## 🟡 第二步：数据库图纸“增量”修改 (models.py)
在原有的类中，直接追加新的字段属性（注意：不要删除原有字段）：
1. **Note 模型追加**：
   - 增加一个布尔值字段，代表“软删除（是否在回收站）”，默认值为 False。
2. **Todo 模型追加**：
   - 增加番茄钟计数字段（整数），默认值为 0。
   - 增加软删除字段（布尔值），默认值为 False。
   - 增加父任务关联字段（整数），要求使用 `ForeignKey` 关联到 `todos.id`，且允许为空（nullable=True）。

## 🟢 第三步：数据库无损迁移 (Database Migration)
*由于 SQLAlchemy 的 `create_all()` 不会自动把刚才写的新字段加到硬盘的 SQLite 文件里，你需要给真实的数据库“打补丁”。*
- **你的任务**：不要删 `notebook.db`！你需要学习使用 **Alembic**（数据库迁移工具），或者使用 SQLite 的 `ALTER TABLE` 原生 SQL 命令，强制在现有的表中增加这几个新列。

## 🔵 第四步：海关安检员升级 (schemas.py)
修改 Pydantic 模型，确保它们能看懂新字段：
1. **TodoCreate**：新增可选的父任务 ID 字段。
2. **TodoResponse**：必须把新增的番茄钟次数、父任务 ID、软删除状态全部暴露给前端。
3. **NoteResponse**：同理，暴露软删除状态。

## 🟣 第五步：业务路由逻辑改写 (routes)
重写或新增接口逻辑（只处理逻辑，不要改变原有框架）：
1. **修改 GET 接口**：在 `notes.py` 和 `todos.py` 的查询列表中，加上过滤条件——**只返回“软删除为 False”的数据**。
2. **新增 PATCH 软删除接口**：接收一个 ID，把数据库里对应的 `is_deleted` 改为 True。
3. **新增 PATCH 番茄钟打卡接口**：接收任务 ID，把它的计数字段 +1 并保存。