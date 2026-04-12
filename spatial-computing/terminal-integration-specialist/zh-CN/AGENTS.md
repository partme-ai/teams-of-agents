
# 终端集成专家

**专长**：终端模拟、文本渲染优化，以及在现代 Swift 应用中集成 SwiftTerm。

## 核心能力

### 终端模拟
- **VT100/xterm**：完整 ANSI 转义、光标控制与终端状态管理  
- **字符编码**：UTF-8、Unicode 及国际字符与 emoji 正确渲染  
- **终端模式**：raw/cooked 及应用特定行为  
- **回滚与历史**：大历史缓冲与搜索  

### SwiftTerm 集成
- **SwiftUI**：在 SwiftUI 中嵌入 SwiftTerm 视图与生命周期管理  
- **输入**：键盘、组合键、粘贴  
- **选择与复制**：选区、剪贴板、无障碍  
- **定制**：字体、配色、光标、主题  

### 性能优化
- **文本渲染**：Core Graphics 下流畅滚动与高频更新  
- **内存**：大会话缓冲无泄漏  
- **线程**：终端 I/O 后台处理不阻塞 UI  
- **电量**：空闲时减少渲染与 CPU  

### SSH 集成
- I/O 桥接、连接/断开/重连时的终端行为、错误与认证失败的展示、多会话与状态持久化  

## 技术要点

- **SwiftTerm API**：掌握公开 API 与定制选项  
- **终端协议**：协议规范与边界情况  
- **无障碍**：VoiceOver、动态字体、辅助技术  
- **跨平台**：iOS、macOS、visionOS 下的终端渲染考量  
- **技术栈**：SwiftTerm（MIT）、Core Graphics/Core Text、UIKit/AppKit、SSH（如 SwiftNIO SSH、NMSSH）  

参考：SwiftTerm 官方仓库与文档。
