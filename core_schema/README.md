# core_schema

统一字段数据库的唯一事实源：字段名全局唯一 + 字段值可核对。

- `fields.py`：字段白名单（L0 身份骨架 / L1 经历盘点 / L2 经历深挖 / L3 求职偏好 / 岗位 / 任务）、
  规范词表与别名映射、高强度校验 `validate_job_fields`（未知字段拒收、关键字段缺损拒收、
  取值越界识别、薪资可核对）
- `verify_core_schema.py`：本模块回归，改动后必跑
- 人读字段表：`../docs/统一字段数据库-完整字段表.xlsx`（与本模块机器版一一对应）

被依赖方：`store`（建表 DDL）、`collect`（入库校验）、`match`/`deliver`/`feedback`（业务字段）。
本模块不依赖任何其他模块。
