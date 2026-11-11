# 发布到 GitHub 与 Pages

本文记录把本仓库发布到 GitHub 并让 Pages 渲染博客的确切步骤。仓库内已备好站点与工作流，网络与认证就绪后按此执行。

## 一、前置条件

| 条件 | 说明 |
|---|---|
| GitHub 可达 | `git ls-remote https://github.com/git/git.git HEAD` 能返回 HEAD；返回 502 说明出口代理拦截，需换网络 |
| 认证 | `gh auth login` 成功，或已配置可推送的 SSH key / PAT |
| 仓库名与可见性 | 建议 `sci-writing-workflow`，公开；Pages 免费版要求公开仓库 |

## 二、创建并推送

```bash
cd sci-writing-workflow

# 方式 A：gh（推荐，可一并启用 Pages）
gh repo create sci-writing-workflow --public --source=. --remote=origin --push

# 方式 B：已有远端
git remote add origin git@github.com:<账号>/sci-writing-workflow.git
git push -u origin main
```

仓库默认分支需为 `main`（工作流按 `main` 触发）：

```bash
git branch -M main
```

## 三、启用 Pages

```bash
# 用 Actions 作为 Pages 来源
gh api -X POST repos/<账号>/sci-writing-workflow/pages \
  -f source[branch]=main -f source[path]=/ \
  -f build_type=workflow
```

或在网页端：Settings → Pages → Build and deployment → Source 选 **GitHub Actions**。

首次推送后 `.github/workflows/pages.yml` 会自动构建 `site/` 并部署。之后访问：

```
https://<账号>.github.io/sci-writing-workflow/
```

## 四、仓库内的站点结构

```
site/
├─ _config.yml                       # minima 主题、中文语言、永久链接
├─ index.md                          # 首页：定位、入口指引
└─ _posts/2026-11-10-....md          # 长文，带 front matter
.github/workflows/pages.yml          # Jekyll 构建 + Pages 部署
.github/workflows/verify.yml         # 结构自检与私有痕迹拦截
scripts/check_repo.py                # 自检脚本
```

文章正文与 `blog/` 下的长文同源；改文章时两边同步，站点文章的 H1 由布局生成，正文不再重复标题。

## 五、验证

1. Actions 里 `Deploy GitHub Pages` 变绿；
2. 打开站点首页，长文可从首页进入，代码块与表格正常渲染；
3. `Verify` 工作流通过，说明技能 frontmatter、12 个模板、站点 front matter 与相对链接均正常。

## 六、常见失败

| 现象 | 原因 | 处理 |
|---|---|---|
| `CONNECT tunnel failed, response 502` | 出口代理拦截 GitHub | 换网络或调整代理白名单 |
| Pages 404 | 未启用 Pages，或首次部署未完成 | 检查 Settings → Pages 与 Actions 状态 |
| 文章不出现 | 文章日期在将来，Jekyll 默认不构建未来文章 | 改 `date` 或设置 `future: true` |
| 中文乱码 | 站点未声明语言或编码 | `_config.yml` 已设 `lang: zh-CN`，检查主题版本 |

## 七、本地预检

```bash
python -m pip install pyyaml
python scripts/check_repo.py
```

该脚本检查 18 个技能的 frontmatter、12 个登记册模板的 YAML 与门控一致性、站点文章 front matter、Markdown 相对链接与工作流 YAML，不依赖网络。