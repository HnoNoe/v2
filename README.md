# 求职批量投递系统 v2

依据专利技术交底书实现的下一代版本。**模块化拆解重构**：单向依赖、领域层互不横连、
每个模块自带回归。设计全文见 [v2-拆解.md](v2-拆解.md)。

## 结构

```
clients/    CLI / Web / 桌面（薄客户端，待实装）
api/        FastAPI 服务层（待实装）
viz/        可视化统一出口（待实装）
deliver/    投递：任务/渠道/三重护栏/安全模式（待实装）
feedback/   反馈回写：式五闭环 → 再匹配（待实装）
match/      匹配：式一凸组合/式二余弦/式三逻辑斯谛(已修 S 曲线托底)/统一空间（待实装）
profile/    画像：简历解析/L0~L3 分层/权重（待实装）
collect/    采集：平台适配器 + 反爬三件套（自助登录/2.5s 限速/stealth）（待实装）
account/    账号：注册登录/会话/数据行级隔离（待实装）
store/      存储：SQLite 本地 / MySQL 云端抽象（待实装）
core_schema/ ✅ 统一字段数据库唯一事实源（已实装，含高强度回归）
```

## 依赖铁律

1. 依赖只向下；领域层（collect/profile/match/deliver/feedback/viz）禁止互相 import；
2. 改某模块先跑它的 `verify_*.py` + `core_schema/verify_core_schema.py`；
3. `core_schema` 是字段唯一事实源，改字段先改 `core_schema/fields.py` 再同步 xlsx。

## 与既有版本的关系

| 仓库 | 状态 |
|---|---|
| [job-delivery-system](https://github.com/HnoNoe/job-delivery-system) `main` | 精简版（检索+投递），队友交付线，继续维护 |
| [v1](https://github.com/HnoNoe/v1) | 完整版归档，只修致命 bug |
| **本仓库 v2** | 主线开发，按 v2-拆解.md 迁移顺序推进 |
