# Git 常用命令小抄

> 仓库：`github.com/yxmyc/git` ｜ 认证：SSH over 443 ｜ 身份：`hoshino`

## 一、每天都会用到的 4 条

```bash
git status              # 看现在改了哪些文件（最常用，随时跑）
git add .               # 把所有改动放进暂存区
git commit -m "说明"     # 提交，说明写清楚改了什么
git push                # 推到 GitHub
```

拉取别人的改动：

```bash
git pull                # = fetch + merge
```

## 二、第一次用（新仓库）

```bash
# 方式 A：从 GitHub 克隆已有仓库
git clone git@github.com:yxmyc/仓库名.git

# 方式 B：把本地目录变成仓库
cd D:\你的目录
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:yxmyc/仓库名.git
git push -u origin main
```

## 三、查看历史

```bash
git log --oneline --graph --all      # 图形化历史
git log --oneline -5                 # 最近 5 条
git show 6c54cc4                     # 看某次提交改了什么
git diff                             # 看还没 add 的改动
git diff --staged                    # 看已经 add 的改动
git blame 文件名                      # 每行是谁改的
```

## 四、撤销（按危险程度递增）

```bash
# 1. 改坏了但没 add：丢弃工作区改动
git restore 文件名.py

# 2. 已经 add 了，想拿出来
git restore --staged 文件名.py

# 3. 已经 commit 了，但想改说明（还没 push）
git commit --amend -m "新的说明"

# 4. 已经 commit 了，想整个撤销但保留改动
git reset --soft HEAD~1

# 5. 已经 push 了，想撤销（生成一条反向提交，安全）
git revert 提交哈希
```

⚠️ 不要随便用 `git reset --hard`，它会**真的删掉**未提交的改动。

## 五、分支

```bash
git branch                    # 列出本地分支
git branch 新分支名            # 新建分支
git switch 分支名              # 切换分支（旧写法：git checkout）
git switch -c 新分支名          # 新建并切换
git merge 分支名               # 把某分支合并到当前分支
git push -u origin 分支名      # 把新分支推到远端
git branch -d 分支名           # 删除已合并的分支
```

## 六、临时存一下（不改完不想提交）

```bash
git stash          # 把当前改动暂存起来，工作区变干净
git stash list     # 看暂存了哪些
git stash pop      # 取回最近的暂存
```

## 七、忽略文件

在 `.gitignore` 里写规则，例如：

```gitignore
__pycache__/
*.pyc
.venv/
.vscode/
*.zip
```

已经提交过的文件想改成忽略：

```bash
git rm --cached 文件名
git commit -m "stop tracking 文件名"
```

## 八、认证与网络（本机特殊配置）

```bash
ssh -T git@github.com     # 验证绑定：应返回 "Hi yxmyc!"
```

- 本机 `C:\Users\hoshino\.ssh\config` 里把 `github.com` 指向了 `ssh.github.com:443`，**必须保留**，否则网页被限速时 push 会卡住
- 克隆时用 **SSH 地址**（`git@github.com:...`），不要用 `https://` 地址

## 九、常见报错对照

| 报错 | 原因 / 处理 |
|---|---|
| `Permission denied (publickey)` | 公钥没登记，或不是用 `ssh -T` 那套密钥 |
| `Updates were rejected` | 远端有你本地没有的提交，先 `git pull --rebase` |
| `fatal: not a git repository` | 当前目录不是仓库，`cd` 到正确目录 |
| `Please tell me who you are` | 缺 `user.name` / `user.email`，见下 |
| `LF will be replaced by CRLF` | 只是提示，已配 `core.autocrlf=input`，忽略即可 |

## 十、身份配置（换电脑时要重做）

```bash
git config --global user.name "hoshino"
git config --global user.email "317537320+yxmyc@users.noreply.github.com"
git config --global init.defaultBranch main
git config --global core.autocrlf input
git config --global core.quotepath false
```
