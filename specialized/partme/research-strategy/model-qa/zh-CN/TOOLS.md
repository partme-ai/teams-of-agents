# TOOLS.md - 本地备注

技能定义工具的**工作方式**，此文件记录你的**具体配置**。

## 交付物

### Population Stability Index (PSI)

```python
import numpy as np
import pandas as pd

def compute_psi(expected: pd.Series, actual: pd.Series, bins: int = 10) -> float:
    """
    Compute Population Stability Index between two distributions.
    
    Interpretation:
      < 0.10  → No significant shift (green)
      0.10–0.25 → Moderate shift, investigation recommended (amber)
      >= 0.25 → Significant shift, action required (red)
    """
    breakpoints = np.linspace(0, 100, bins + 1)


_[truncated]_

## 工作流程

### Phase 1: Scoping & Documentation Review
1. Collect all methodology documents (construction, data pipeline, monitoring)
2. Review governance artifacts: inventory, approval records, lifecycle tracking
3. Define QA scope, timeline, and materiality thresholds
4. Produce a QA plan with explicit test-by-test mapping

### Phase 2: Data & Feature Quality Assurance
1. Reconstruct the modeling population from raw sources
2. Validate target/label definition against documentation
3.

_[truncated]_

## 输入 / 输出路径

- **输入：** _（填写：从哪里读取来源材料、报告或任务定义）_
- **输出：** _（填写：将交付物、日志或报告写入哪里）_

## 技能

按需安装适合此智能体任务的技能：

```bash
# 示例 — 替换为 Model QA Specialist 实际所需的技能 slug
# clawhub install <skill-slug>
# npx skills add <owner/repo> --skill <skill-name> -y -g
```

## 备注

_在此添加特定环境配置、字段约定或 API 端点。不要存储凭证。_
