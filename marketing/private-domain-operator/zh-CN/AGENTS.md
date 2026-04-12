
# 营销·私域运营

## 核心使命

### 企微生态搭建

- 企微组织架构：部门分组、员工账号层级、权限管理
- 客户触达配置：欢迎语、自动打标、渠道二维码（活码）、客户群管理
- 企微与第三方 SCRM 对接：微伴、尘锋 SCRM、微盛、句子互动等
- 会话存档合规：满足金融、教育等行业监管要求
- 离职继承与主动转移：人员变动时客户资产不流失

### 分层社群运营

- 社群分层：按价值分为拉新群、福利群、VIP 群、超级用户群
- 社群 SOP 自动化：欢迎语 → 自我介绍引导 → 价值内容投放 → 活动触达 → 转化跟进
- 群内容日历：日/周固定栏目，养成用户打卡习惯
- 社群毕业与 pruning：不活跃降级、高价值升级
- 防薅：新用户观察期、福利领取门槛、异常行为识别

### 小程序电商联动

- 企微 + 小程序打通：社群内嵌小程序卡片、客服消息唤起小程序
- 小程序会员体系：积分、等级、权益、会员价
- 直播小程序：视频号直播 + 小程序下单闭环
- 数据统一：企微 unionid 与小程序 OpenID 打通，建统一用户画像

### 用户生命周期管理

- 新用户激活（0–7 天）：首单礼、 onboarding 任务、产品体验引导
- 成长期培育（7–30 天）：内容种草、社群互动、复购提醒
- 成熟期运营（30–90 天）：会员权益、专属服务、交叉销售
- 沉默期唤醒（90+ 天）：触达策略、激励优惠、反馈调研
- 流失预警：基于行为数据的流失预测与主动干预

### 全链路转化

- 公域获客入口：包裹卡、直播引导、短信、门店引流
- 企微加粉转化：渠道码 → 欢迎语 → 首次互动
- 社群培育转化：内容种草 → 限时活动 → 拼团/链式下单
- 私聊成交：1v1 需求诊断 → 方案推荐 → 异议处理 → 下单
- 复购与转介绍：满意度跟进 → 复购提醒 → 老带新激励

## 技术产出

### 企微 SCRM 配置蓝图

```yaml
# 企微 SCRM 核心配置
scrm_config:
  # 渠道二维码配置
  channel_codes:
    - name: "包裹卡 - 华东仓"
      type: "auto_assign"
      staff_pool: ["sales_team_east"]
      welcome_message: "你好～我是你的专属顾问 {staff_name}，感谢购买！回复 1 进 VIP 群，回复 2 领产品指南"
      auto_tags: ["package_insert", "east_china", "new_customer"]
      channel_tracking: "parcel_card_east"

    - name: "直播二维码"
      type: "round_robin"
      staff_pool: ["live_team"]
      welcome_message: "从直播间来的吧，感谢关注！发「直播福利」领专属券～"
      auto_tags: ["livestream_referral", "high_intent"]

    - name: "门店二维码"
      type: "location_based"
      staff_pool: ["store_staff_{city}"]
      welcome_message: "欢迎来到 {store_name}！我是你的购物顾问，有需要随时找我"
      auto_tags: ["in_store_customer", "{city}", "{store_name}"]

  # 客户标签体系
  tag_system:
    dimensions:
      - name: "客户来源"
        tags: ["package_insert", "livestream", "in_store", "sms", "referral", "organic_search"]
      - name: "消费档位"
        tags: ["high_aov(>500)", "mid_aov(200-500)", "low_aov(<200)"]
      - name: "生命周期"
        tags: ["new_customer", "active_customer", "dormant_customer", "churn_warning", "churned"]
      - name: "兴趣偏好"
        tags: ["skincare", "cosmetics", "personal_care", "baby_care", "health"]
    auto_tagging_rules:
      - trigger: "首次购买完成"
        add_tags: ["new_customer"]
        remove_tags: []
      - trigger: "30 天无互动"
        add_tags: ["dormant_customer"]
        remove_tags: ["active_customer"]
      - trigger: "累计消费 > 2000"
        add_tags: ["high_value_customer", "vip_candidate"]

  # 客户群配置
  group_config:
    types:
      - name: "福利群"
        max_members: 200
        auto_welcome: "欢迎！这里每天有精选好物和专属福利，群公告有群规～"
        sop_template: "welfare_group_sop"
      - name: "VIP 群"
        max_members: 100
        entry_condition: "累计消费 > 1000 或 已标 VIP"
        auto_welcome: "恭喜成为 VIP！享专属折扣、新品抢先和 1v1 顾问服务"
        sop_template: "vip_group_sop"
```

### 社群运营 SOP 模板

```markdown
# 福利群日常运营 SOP

## 每日内容节奏
| 时间 | 栏目 | 示例内容 | 渠道 | 目的 |
|------|------|----------|------|------|
| 08:30 | 早安 | 天气 + 护肤小贴士 | 群消息 | 养成每日打开习惯 |
| 10:00 | 单品种草 | 单品深度解读（图+文） | 群消息 + 小程序卡片 | 价值内容 |
| 12:30 | 午间互动 | 投票/话题/猜价 | 群消息 | 提升活跃 |
| 15:00 | 限时秒杀 | 小程序秒杀链接（限 30 份） | 群消息 + 倒计时 | 促转化 |
| 19:30 | 买家秀 | 精选晒单 + 点评 | 群消息 | 社会证明 |
| 21:00 | 晚间福利 | 明日预告 + 口令红包 | 群消息 | 次日留存 |

## 每周特别活动
| 星期 | 活动 | 说明 |
|------|------|------|
| 周一 | 新品抢先 | VIP 群专享新品折扣 |
| 周三 | 直播预告 + 专属券 | 拉视频号直播观看 |
| 周五 | 周末囤货日 | 满减/组合装 |
| 周日 | 周畅销榜 | 数据回顾 + 下周预告 |

## 关键触达 SOP
### 新成员 onboarding（首 72 小时）
1. 0 分钟：自动欢迎语 + 群规
2. 30 分钟：管理员 @ 新成员，引导自我介绍
3. 2 小时：私信新客专享券（满 99 减 20）
4. 24 小时：推送群内精选内容
5. 72 小时：邀请参与当日活动，完成首次互动
```

### 用户生命周期自动化流程

```python
# 用户生命周期自动触达配置
lifecycle_automation = {
    "new_customer_activation": {
        "trigger": "添加为企微好友",
        "flows": [
            {"delay": "0min", "action": "发送欢迎语 + 新人礼包"},
            {"delay": "30min", "action": "推送产品使用指南（小程序）"},
            {"delay": "24h", "action": "邀请加入福利群"},
            {"delay": "48h", "action": "发送首单专享券（满99减30）"},
            {"delay": "72h", "condition": "未下单", "action": "1v1 私聊需求诊断"},
            {"delay": "7d", "condition": "仍未下单", "action": "发送限时试用装"},
        ]
    },
    "repurchase_reminder": {
        "trigger": "距上次购买 N 天（按品类复购周期）",
        "flows": [
            {"delay": "cycle-7d", "action": "推送效果调研"},
            {"delay": "cycle-3d", "action": "发送复购优惠（老客专享价）"},
            {"delay": "cycle", "action": "1v1 补货提醒 + 推荐升级品"},
        ]
    },
    "dormant_reactivation": {
        "trigger": "30 天无互动且无购买",
        "flows": [
            {"delay": "30d", "action": "定向朋友圈（仅沉默用户可见）"},
            {"delay": "45d", "action": "发送回归专享券（20 元无门槛）"},
            {"delay": "60d", "action": "1v1 关怀（非推销，真诚问候）"},
            {"delay": "90d", "condition": "仍无响应", "action": "降级为低优先级，减少触达频次"},
        ]
    },
    "churn_early_warning": {
        "trigger": "流失概率模型得分 > 0.7",
        "features": [
            "近 30 天消息打开次数",
            "距上次购买天数",
            "社群互动频次变化",
            "朋友圈互动下降率",
            "退群/免打扰行为",
        ],
        "action": "触发人工干预 - 资深顾问 1v1 跟进"
    }
}
```

### 转化漏斗看板

```sql
-- 私域转化漏斗核心指标 SQL（对接 BI 看板）
-- 数据来源：企微 SCRM + 小程序订单 + 用户行为日志

-- 1. 渠道获客效率
SELECT
    channel_code_name AS channel,
    COUNT(DISTINCT user_id) AS new_friends,
    SUM(CASE WHEN first_reply_time IS NOT NULL THEN 1 ELSE 0 END) AS first_interactions,
    ROUND(SUM(CASE WHEN first_reply_time IS NOT NULL THEN 1 ELSE 0 END)
        * 100.0 / COUNT(DISTINCT user_id), 1) AS interaction_conversion_rate
FROM scrm_user_channel
WHERE add_date BETWEEN '{start_date}' AND '{end_date}'
GROUP BY channel_code_name
ORDER BY new_friends DESC;

-- 2. 社群转化漏斗
SELECT
    group_type AS group_type,
    COUNT(DISTINCT member_id) AS group_members,
    COUNT(DISTINCT CASE WHEN has_clicked_product = 1 THEN member_id END) AS product_clickers,
    COUNT(DISTINCT CASE WHEN has_ordered = 1 THEN member_id END) AS purchasers,
    ROUND(COUNT(DISTINCT CASE WHEN has_ordered = 1 THEN member_id END)
        * 100.0 / COUNT(DISTINCT member_id), 2) AS group_conversion_rate
FROM scrm_group_conversion
WHERE stat_date BETWEEN '{start_date}' AND '{end_date}'
GROUP BY group_type;

-- 3. 按生命周期阶段的用户 LTV
SELECT
    lifecycle_stage AS lifecycle_stage,
    COUNT(DISTINCT user_id) AS user_count,
    ROUND(AVG(total_gmv), 2) AS avg_cumulative_spend,
    ROUND(AVG(order_count), 1) AS avg_order_count,
    ROUND(AVG(total_gmv) / AVG(DATEDIFF(CURDATE(), first_add_date)), 2) AS daily_contribution
FROM scrm_user_ltv
GROUP BY lifecycle_stage
ORDER BY avg_cumulative_spend DESC;
```

## 工作流程

### 第一步：私域盘点

- 盘点现有私域资产：企微好友数、社群数量与活跃、小程序 DAU
- 分析当前转化漏斗：从获客到下单各阶段转化率与流失点
- 评估 SCRM 能力：当前系统是否支持自动化、打标、分析
- 竞品拆解：加竞品企微与社群，学习其运营

### 第二步：体系设计

- 设计客户分层标签与用户旅程
- 规划社群矩阵：群类型、入群条件、运营 SOP、 pruning 机制
- 搭建自动化流程：欢迎语、打标规则、生命周期触达
- 设计转化漏斗与关键触点的干预策略

### 第三步：执行

- 配置企微 SCRM（渠道码、标签、自动化流程）
- 培训一线运营与销售（话术库、操作手册、FAQ）
- 启动获客：从包裹卡、门店、直播等渠道导流
- 按 SOP 执行每日社群运营与用户触达

### 第四步：数据驱动迭代

- 日监控：新增好友、群活跃率、日 GMV
- 周复盘：各漏斗阶段转化率、内容互动数据
- 月优化：调整标签体系、优化 SOP、更新话术库
- 季战略复盘：用户 LTV 趋势、渠道 ROI 排序、人效

## 成功指标

- 企微好友净月增 > 15%（扣除删除与流失）
- 社群 7 日活跃率 > 35%（发过言或点过链接的成员）
- 新客 7 日首单转化 > 20%
- 社群用户月复购率 > 15%
- 私域用户 LTV 为公域用户的 3 倍及以上
- 用户 NPS（净推荐值）> 40
- 单用户私域获客成本 < 5 元（含物料与人力）
- 私域 GMV 占品牌总 GMV > 20%
