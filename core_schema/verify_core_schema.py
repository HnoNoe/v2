"""core_schema 高强度回归：字段白名单 / 规范词映射 / 关键字段 / 值域 / 薪资可核对。

运行：python verify_core_schema.py（本模块被改动后必跑）。
"""
import sys
sys.path.insert(0, "..")

from core_schema import (
    JOB_FIELDS, JOB_KEY_FIELDS, ENTRY_TYPES,
    EDU_VOCAB, EXP_VOCAB,
    canonical_value, validate_job_fields,
)

ok = True


def check(name, cond, detail=""):
    global ok
    status = "PASS" if cond else "FAIL"
    if not cond:
        ok = False
    print("  %s  %s%s" % (status, name, (" | " + str(detail)) if (detail and not cond) else ""))


GOOD = {"岗位名称": "测试岗", "单位名称": "测试公司", "薪资": "10-15K",
        "学历": "本科", "经验": "应届", "已沟通": "否", "投递入口类型": "API"}

print("=== 字段白名单 ===")
check("岗位字段集非空且关键字段在内", all(k in JOB_FIELDS for k in JOB_KEY_FIELDS))
check("投递入口类型词表完整", ENTRY_TYPES == ["Web表单", "邮件", "API", "半自动"])

print("=== 规范词映射 ===")
check("学历别名映射（高中→大专以下）", canonical_value("学历", "高中") == "大专以下")
check("学历别名映射（中专/中技→大专以下）", canonical_value("学历", "中专/中技") == "大专以下")
check("学历空值补全（→学历不限）", canonical_value("学历", "") == "学历不限")
check("学历规范词原样保留（硕士）", canonical_value("学历", "硕士") == "硕士")
check("经验别名映射（在校/应届→应届）", canonical_value("经验", "在校/应届") == "应届")
check("经验空值补全（→经验不限）", canonical_value("经验", "") == "经验不限")
check("已沟通布尔归一（True→是）", canonical_value("已沟通", "True") == "是")
check("已沟通布尔归一（0→否）", canonical_value("已沟通", "0") == "否")

print("=== 高强度校验 ===")
viol, cleaned = validate_job_fields(dict(GOOD))
check("合法记录零违规放行", viol == [], viol)
check("校验不污染原记录（cleaned 独立副本）",
      cleaned is not GOOD and "补全字段" not in GOOD)

viol, _ = validate_job_fields(dict(GOOD, **{"乱写字段": "x"}))
check("未知字段被识别", any("乱写字段" in v for v in viol), viol)
viol, _ = validate_job_fields(dict(GOOD, **{"岗位名称": ""}))
check("关键字段为空被拒", any("岗位名称" in v for v in viol), viol)
viol, _ = validate_job_fields(dict(GOOD, **{"学历": "博士后"}))
check("学历取值越界被识别", any("学历" in v for v in viol), viol)
viol, _ = validate_job_fields(dict(GOOD, **{"经验": "几十年"}))
check("经验取值越界被识别", any("经验" in v for v in viol), viol)
viol, _ = validate_job_fields(dict(GOOD, **{"投递入口类型": "脑电波"}))
check("投递入口类型越界被识别", any("投递入口类型" in v for v in viol), viol)
viol, _ = validate_job_fields(dict(GOOD, **{"薪资": "待遇很好"}))
check("薪资不可核对被识别", any("薪资" in v for v in viol), viol)
viol, cleaned2 = validate_job_fields(dict(GOOD, **{"经验": "在校/应届"}))
check("应届别名规范化入库", (not viol) and cleaned2["经验"] == "应届", viol)
viol, _ = validate_job_fields(dict(GOOD, **{"薪资": "面议"}))
check("薪资面议放行", viol == [], viol)

print()
print("=== core_schema 高强度校验", "通过 ===" if ok else "存在 FAIL ===")
sys.exit(0 if ok else 1)
