<div align="center">

# 💗 LovCount · 写给ta的代码

**一个每秒加一的「想你计数器」，把心跳写进 Git 提交里。**

只要程序不停，思念就不会中断。

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Git](https://img.shields.io/badge/Git-required-F05032?logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-ready-222222?logo=githubpages&logoColor=white)](https://pages.github.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

</div>

---

## ✨ 这是什么

一个很小、很傻、但很认真的小程序。

它每秒把计数器 `+1`，打印一次「此刻累计想你的次数」，并把数字写回 `count.txt`，
每隔一段时间自动 `git commit` + `push` 到 GitHub。
配套的 `index.html` 是一个网页计数器，打开就能看到这个数字在跳动。

你离开后，它还在数。

> 写给她/他的情书，也能是一段能跑起来的代码。

---

## 📦 项目结构

```
lov/
├── app.py        # 最初的本地版：纯计数，不联网
├── commit.py     # 主力版本：计数 + 自动提交推送到 GitHub
├── count.txt     # 计数值（唯一被版本控制的数据文件）
├── index.html    # 网页计数器（可直接用 GitHub Pages 托管）
└── README.md
```

---

## 🚀 快速开始

### 1. 准备仓库

```bash
git clone https://github.com/findbaicha/lov.git
cd lov
```

确保已经配置好 Git 身份和推送权限：

```bash
git config user.name  "your-name"
git config user.email "you@example.com"
```

### 2. 运行

```bash
python commit.py
```

然后你会看到：

```
写给嘟嘟的代码
启动思念程序
距离下次见面的期待，一直在增加
只要程序不停，思念就不会中断
此刻累计想你的次数： 1
此刻累计想你的次数： 2
...
✅ synced to github
```

按 `Ctrl + C` 停止。下次启动会从 `count.txt` **接着数**，不会清零。

### 3. 打开网页

直接用浏览器打开 `index.html` 即可；或者推到 GitHub 后开启 **GitHub Pages**：

`Settings → Pages → Build and deployment → Source: Deploy from a branch → 分支选 main，目录选 / (root)`

访问 `https://<你的用户名>.github.io/lov/` 就能看到持续跳动的数字。

---

## ⚙️ 可调参数

打开 `commit.py` 顶部：

| 变量 | 默认值 | 说明 |
| --- | --- | --- |
| `FILE` | `count.txt` | 计数存放的文件 |
| `BRANCH` | `main` | 推送的分支（老仓库可能是 `master`） |
| `GIT_INTERVAL` | `10` | 每隔多少秒同步一次到 GitHub |

> 建议把 `GIT_INTERVAL` 调到 `60` 以上。10 秒一次推送对 GitHub 来说是合法但有点吵，
> 而网页端本来就在本地每秒自增，观感完全不受影响。

---

## 🔍 实现细节

- **计数持久化**：每次 `+1` 后立即写回 `count.txt`，进程被杀掉也不会丢太多。
- **历史不膨胀**：同步用的是 `git commit --amend --no-edit` + `push --force`，
  也就是**永远只保留一个提交**。不然每秒一次 commit，几个月后仓库会重到打不开。
- **网页端**：`index.html` 先用 `fetch('count.txt')` 取一次基准值，
  然后本地 `setInterval` 每秒 `+1`，无需后端、无需刷新。
- **`app.py` 的区别**：那是最早的本地版，路径写死成了 `/home/stu/lov/count.txt`，
  不推送 Git。日常使用请直接跑 `commit.py`。

---

## 🛠 常见问题

**Q：能不能让它 7×24 小时一直跑？**
可以，丢到一台常开的机器上（云服务器 / 树莓派 / 旧电脑），配合 `systemd`、`tmux` 或 `nohup`：

```bash
nohup python commit.py > lov.log 2>&1 &
```

**Q：GitHub Actions 可以代替本地常驻吗？**
不建议。Actions 有运行时长和调度精度限制，做不到真正的「每秒 +1」。
不过如果你只想每天 +1，那 Actions 完全够用。

**Q：`❌ sync failed` 怎么办？**
一般是网络或权限问题。检查 `git remote -v` 是否正确、SSH key 或 token 是否配置好、
分支名和本地是否一致。计数不会丢，恢复网络后会自动补上。

**Q：计数能不能改成分钟 / 小时？**
把 `commit.py` 里 `time.sleep(1)` 改成 `time.sleep(60)` 就行。

**Q：想把文案换成自己的？**
`commit.py` 里的四行 `print`，和 `index.html` 里的 `<h1>`、`<p>`。随便改，改成你想说的话。

---

## 🌱 从零搭建自己的版本

1. Fork 本仓库，或者 `git init` 一个空仓库；
2. 新建 `count.txt`，内容写一个 `0`；
3. 复制 `commit.py` 和 `index.html`；
4. 改文案、改参数、`git push`；
5. 在github pages里选择github action配置static html的workflow
6. 在actions等待部署完成拿url
7. 把链接发给那个ta

---

## 📄 License

[MIT](./LICENSE) — 随便 fork，随便改，随便写成你自己的版本。

如果它帮你说出了某句说不出口的话，那就够了。

---

## English

A tiny "missing you" counter. It increments once per second, writes the number to
`count.txt`, and pushes it to GitHub every few seconds. `index.html` renders the number
as a live web counter (works with GitHub Pages, no backend needed).

```bash
git clone https://github.com/<your-username>/lov.git
cd lov
python commit.py     # Ctrl+C to stop; the count resumes on next run
```

Config: `BRANCH`, `GIT_INTERVAL`, and `FILE` at the top of `commit.py`.
Sync uses `git commit --amend` + `push --force` so the repo keeps exactly one commit
no matter how long it runs.

MIT licensed. Fork it and write your own version.
