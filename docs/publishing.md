# 仓库分工与发布

本仓库只承载**技能与模板**。博客站点与文章已迁到独立仓库 [`keyd164.github.io`](https://github.com/keyd164/keyd164.github.io)，两者各自部署、互不牵连。

| 仓库 | 内容 | 地址 |
|---|---|---|
| `sci-writing-workflow`（本仓库） | 19 个技能、12 个登记册模板、文档与自检脚本 | https://github.com/keyd164/sci-writing-workflow |
| `keyd164.github.io` | Jekyll 站点、文章、RSS、站点地图 | https://keyd164.github.io/ |

## 为什么分开

项目页地址带仓库名（`…github.io/sci-writing-workflow/`），读起来像代码项目的附属文档；用户站点仓库的根地址没有路径后缀，更接近独立博客。分开之后还有两个实际好处：改文章不再触发技能仓库的检查与部署，改技能也不影响站点；将来绑自定义域名只需在站点仓库改一处。

## 改文章

文章只维护在站点仓库：

1. 在 `keyd164.github.io` 仓库的 `_posts/` 新增 `YYYY-MM-DD-slug.md`，front matter 写 `layout: post`、`title`、`date`
2. 不要写 `categories`（中文分类会污染 URL），permalink 已统一为 `/posts/:title/`
3. 提交推送后，`Deploy GitHub Pages` 自动构建部署，约 40 秒生效

## 改技能

只在本仓库改，推送到 `main` 后 `Verify` 会跑结构自检：18 个技能 frontmatter、12 个模板 YAML、仓库边界（不得出现 `site/` 或 `pages.yml`）、相对链接与工作流 YAML。本地可先跑：

```bash
python -m pip install pyyaml
python scripts/check_repo.py
```

## 首次发布两个仓库

```bash
# 技能仓库
git clone https://github.com/keyd164/sci-writing-workflow.git
cd sci-writing-workflow && python scripts/check_repo.py

# 站点仓库
git clone https://github.com/keyd164/keyd164.github.io.git
cd keyd164.github.io
gh auth login            # 或已配置 GH_TOKEN
gh api -X PUT repos/keyd164/keyd164.github.io/pages -f build_type=workflow
gh workflow run pages.yml
```

站点仓库的 Pages 来源须为 **GitHub Actions**（`build_type=workflow`）。若设成"从分支部署"，GitHub 会用自带 Jekyll 再构建一次，与工作流互相覆盖。

## 常见失败

| 现象 | 原因 | 处理 |
|---|---|---|
| 站点 404 | Pages 未启用或首次部署未完成 | 查 Settings → Pages 与 Actions 状态 |
| 文章不出现 | `date` 在未来，Jekyll 默认跳过 | 改日期，或在 `_config.yml` 设 `future: true` |
| 站内链接 404 | `baseurl` 与部署路径不一致 | 用户站点仓库保持 `baseurl: ""` |
| 中文路径 | 写了 `categories` | 删除 categories，用 `/posts/:title/` |
| 部署与分支构建互覆盖 | `build_type` 仍为 legacy | 改为 `workflow` 后重跑 |

## 旧地址

迁移前的主仓库项目页 `https://keyd164.github.io/sci-writing-workflow/` 仍会继续返回最后一次部署的内容，但不再更新。分发时统一使用 `https://keyd164.github.io/`；确认旧链接无引用后可关闭该仓库的 Pages。