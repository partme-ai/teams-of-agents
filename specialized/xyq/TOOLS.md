# TOOLS.md - 小云雀共享工具链

## 第一步：安装小云雀 Skill

执行：
```bash
npx skills add https://gitee.com/Pippit-dev/pippit-skills.git -y -g
```

## 第二步：配置 Access Key

```bash
export XYQ_ACCESS_KEY="你的 Access Key"
```

## 可用脚本

路径：`~/.agents/skills/xyq-nest-skill/scripts/`

| 脚本 | 功能 | 调用方式 |
|------|------|---------|
| `submit_run.py` | 创建会话/发送消息 | `python3 路径/submit_run.py --message "描述" [--thread-id ID] [--asset-ids ID1,ID2]` |
| `get_thread.py` | 查询进展（轮询） | `python3 路径/get_thread.py --thread-id ID --run-id ID --after-seq N` |
| `upload_file.py` | 上传参考文件 | `python3 路径/upload_file.py /path/to/file` |
| `download_results.py` | 下载生成产物 | `python3 路径/download_results.py --urls URL --output-dir ./out --prefix "name"` |

## API 细节
- 基础 URL：https://xyq.jianying.com
- 鉴权：`Authorization: Bearer {XYQ_ACCESS_KEY}`
- 上传限制：仅图片 (image/*) 和视频 (video/*)，单文件 <200MB
- 轮询：每 10 秒，48 小时超时，单次失败重试 1 次

## FAQ
- 失败 → 检查 Access Key / 订阅会员 / 积分
- 没出结果 → 还在生成中，过一会再查
- 返回链接没文件 → 正常，环境暂不支持直接发视频
