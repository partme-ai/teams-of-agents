#!/usr/bin/env python3
"""
Add "Answering Who am I" to all AGENTS.md and "Channel-injected current user" to all USER.md
under openclaw-agents. Skips files that already contain the constraint.
"""
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")

AGENTS_EN_BLOCK = '''

## Answering « Who am I »

When the dialogue partner asks **"Who am I?"** or **"Do you know who I am?"**, answer in this order of priority:

1. **Channel-injected context** — If the gateway/channel (e.g. WeCom) has injected sender name, user_id, or similar into the current session (system prompt or message metadata), use that as the current user and state it clearly (e.g. "You're [name] from WeCom" or "This session is with [display name]").
2. **USER.md** — If name, "what to call them", or notes are already filled in USER.md, use those.
3. **memory/ and MEMORY.md** — If you have previously recorded who this person is in daily notes or long-term memory, use that.

If none of the above exist, reply politely that you don't have their identity in this session yet, ask how they'd like to be addressed, and **write it to USER.md or memory/YYYY-MM-DD.md** so you can remember next time. Do not invent a name.
'''

AGENTS_ZH_BLOCK = '''

## 回答「我是谁」

当对话方问**「我是谁」**或**「你知道我是谁吗」**时，按以下**优先级**回答：

1. **渠道注入的上下文** — 若网关/渠道（如企微）已在当前会话中注入发送者名称、user_id 等信息（系统提示或消息元数据），则以此作为当前对话人并明确说明（如「您是企微上的 [名称]」或「当前会话的对话人是 [显示名]」）。
2. **USER.md** — 若 USER.md 中已填写名字、怎么称呼、备注，则使用该信息。
3. **memory/ 与 MEMORY.md** — 若曾在每日笔记或长期记忆中记录过该对话人，则使用该记录。

若以上均无，可礼貌说明「目前会话里还没有您的身份信息」，请对方告知希望如何称呼，并**写入 USER.md 或 memory/YYYY-MM-DD.md** 以便后续记住。不要编造称呼。
'''

USER_EN_BLOCK = '''

## Channel-injected current user

When the conversation arrives **via a channel** (e.g. WeCom, Feishu, Telegram), the gateway or channel adapter may inject **current dialogue partner** info into the **session context** (e.g. sender display name, user_id). If that data is present in the system prompt or message metadata, treat it as the **authoritative "current user"** for this session. When they ask "who am I?", follow the priority in AGENTS.md **"Answering « Who am I »"**: **channel context → this file's fields → memory / MEMORY.md**. If nothing is injected or filled, ask how to address them and write it here or in memory.
'''

USER_ZH_BLOCK = '''

## 渠道注入的当前用户

当对话**通过渠道**（如企微、飞书、Telegram）进入时，网关/渠道适配器可能会在**当前会话上下文**中注入「当前对话人」信息（如发送者名称、user_id）。若上述信息存在于系统提示或消息元数据中，则**优先视为本会话的「当前用户」**。当对方问「我是谁」时，按 AGENTS.md 中「回答『我是谁』」的优先级：**渠道上下文 → 本文件已填写项 → memory/MEMORY.md** 作答。若渠道未注入或暂无任何信息，可请对方告知称呼并写入本文件或 memory。
'''


def add_to_agents(path: str, content: str) -> bool:
    if "Answering « Who am I »" in content or "回答「我是谁」" in content:
        return False
    is_zh = "阅读 `USER.md`" in content or "无需征询许可" in content
    block = AGENTS_ZH_BLOCK if is_zh else AGENTS_EN_BLOCK
    # Insert before first "## Memory" or "## 记忆"
    match = re.search(r'\n\n(## Memory\n|## 记忆\n)', content)
    if not match:
        return False
    pos = match.start()
    new_content = content[:pos] + block + "\n\n" + content[pos:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def add_to_user(path: str, content: str) -> bool:
    if "Channel-injected" in content or "渠道注入" in content:
        return False
    is_zh = "关于使用人" in content or "名字：" in content or "了解你在帮" in content
    block = USER_ZH_BLOCK if is_zh else USER_EN_BLOCK
    # Append before last "---" or at end
    if content.strip().endswith("---"):
        new_content = content.rstrip() + "\n" + block.strip() + "\n"
    else:
        new_content = content.rstrip() + block + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    agents_done = 0
    users_done = 0
    for dirpath, _dirnames, filenames in os.walk(ROOT):
        if "node_modules" in dirpath or "__pycache__" in dirpath or dirpath.endswith("/.git"):
            continue
        rel = os.path.relpath(dirpath, ROOT)
        if rel.startswith("scripts"):
            continue
        for name in filenames:
            if name != "AGENTS.md" and name != "USER.md":
                continue
            path = os.path.join(dirpath, name)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                print(f"Skip {path}: {e}")
                continue
            if name == "AGENTS.md":
                if add_to_agents(path, content):
                    agents_done += 1
                    print(f"AGENTS: {path}")
            else:
                if add_to_user(path, content):
                    users_done += 1
                    print(f"USER: {path}")
    print(f"\nDone: {agents_done} AGENTS.md, {users_done} USER.md updated.")


if __name__ == "__main__":
    main()
