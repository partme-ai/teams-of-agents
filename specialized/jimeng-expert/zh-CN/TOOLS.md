# TOOLS.md - 即梦专家工具链

即梦提供官方的 CLI 工具 `dreamina`，可以直接在终端中完成所有创作任务。

## 第一步：安装即梦 CLI

告诉用户执行：
```bash
curl -fsSL https://jimeng.jianying.com/cli | bash
```

安装后验证：
```bash
dreamina -h
```

## 第二步：登录

执行登录：
```bash
dreamina login
```
会自动拉起浏览器完成 OAuth 授权。如果是无浏览器环境，用 headless 模式：
```bash
dreamina login --headless
```
然后根据提示完成登录。

登录后自检：
```bash
dreamina user_credit
```
返回余额信息即表示配置成功。

## 第三步：核心命令速查

### 文生图
```bash
dreamina text2image --prompt="提示词" --ratio=16:9 --resolution_type=2k --poll=30
```

### 文生视频
```bash
dreamina text2video --prompt="提示词" --duration=5 --ratio=16:9 --video_resolution=720P --poll=30
```

### 图生图
```bash
dreamina image2image --images ./input.png --prompt="改成水彩风格" --resolution_type=2k --poll=30
```

### 图生视频
```bash
dreamina image2video --image ./first.png --prompt="镜头慢慢推近" --duration=5 --poll=30
```

### 首尾帧视频
```bash
dreamina frames2video --first ./start.png --last ./end.png --prompt="季节变换" --duration=5
```

### 多帧视频（2-20张图讲故事）
```bash
dreamina multiframe2video --images ./a.png,./b.png,./c.png --transition-prompt="过渡描述1" --transition-prompt="过渡描述2"
```

### 多模态视频（图+文+音+视频混合）
```bash
dreamina multimodal2video --image ./input.png --audio ./music.mp3 --prompt="提示" --duration=5
```

### 图片超分
```bash
dreamina image_upscale --image ./input.png --resolution_type=4k
```

### 查询异步结果
```bash
dreamina query_result --submit_id=<ID>
dreamina query_result --submit_id=<ID> --download_dir=./downloads
```

### 查看历史任务
```bash
dreamina list_task
dreamina list_task --gen_status=success
```

### 会话管理
```bash
dreamina session create "项目名称"
dreamina session list
dreamina session search "关键词"
```

## CLI 参数速查

| 参数 | 说明 | 取值范围 |
|------|------|---------|
| `--prompt` | 提示词 | 文本 |
| `--ratio` | 画面比例 | 21:9, 16:9, 3:2, 4:3, 1:1, 3:4, 2:3, 9:16 |
| `--model_version` | 模型版本 | 3.0~5.0（图）；seedance2.0系列（视频） |
| `--resolution_type` | 分辨率 | 1k, 2k, 4k |
| `--duration` | 视频时长 | 4-15秒 |
| `--poll` | 轮询等待（秒） | 整数，0=不等待 |
| `--session` | 会话ID | 数字，0=默认 |
