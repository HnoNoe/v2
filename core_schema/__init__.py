"""core_schema —— 统一字段数据库的唯一事实源。

专利核心：字段名全局唯一、字段值可核对。所有模块以本包定义的字段名为基准。
字段表（docs/统一字段数据库-完整字段表.xlsx）的人读版与本文件机器版一一对应，
改字段先改这里，再同步 xlsx。

高强度校验目标：入库即合法，不合法就拒绝并留痕，绝不留脏数据。
"""
from .fields import (  # noqa: F401
    L0_FIELDS, L0_REQUIRED, L1_TYPES, L2_FIELDS,
    RESUME_ALLOWED_FIELDS, RESUME_ALLOWED_L2,
    L3_FIELDS, L3_REQUIRED,
    JOB_FIELDS, JOB_KEY_FIELDS, TASK_FIELDS, TASK_STATUS, TASK_LOCKED,
    ENTRY_TYPES,
    EDU_VOCAB, EDU_ALIASES, EXP_VOCAB, EXP_ALIASES, FLAG_FIELDS,
    canonical_value, validate_job_fields,
)
