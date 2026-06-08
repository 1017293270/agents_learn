# 部署说明

这个知识库是静态网站，不需要数据库和后端服务。

部署时需要一起发布这些路径：

- `index.html`
- `viewer/`
- `knowledge/`
- `90-references/`

## 本地预览

```powershell
cd D:\agents学习
python -m http.server 8765 --bind 127.0.0.1
```

访问：

```text
http://127.0.0.1:8765/
```

根路径会自动跳到：

```text
http://127.0.0.1:8765/viewer/
```

## GitHub Pages

1. 把本目录提交到 GitHub 仓库。
2. 进入仓库 `Settings -> Pages`。
3. Source 选择 `Deploy from a branch`。
4. Branch 选择你的主分支，目录选择 `/root`。
5. 保存后等待 GitHub Pages 生成站点。

`.nojekyll` 已经创建，用来避免 GitHub Pages 对静态文件做 Jekyll 处理。

## Vercel

1. 导入这个仓库。
2. Framework Preset 选择 `Other`。
3. Build Command 留空。
4. Output Directory 留空或填 `.`。
5. 部署后访问域名根路径即可。

`vercel.json` 已经配置根路径跳转到 `/viewer/`。

## Netlify

1. 导入这个仓库。
2. Build command 留空。
3. Publish directory 填 `.`。
4. 部署后访问域名根路径即可。

`netlify.toml` 已经配置根路径跳转到 `/viewer/`。

## 新增笔记后的部署检查

新增 Markdown 笔记后，确认：

1. 笔记在 `knowledge/模块目录/编号-标题.md`。
2. `viewer/manifest.json` 已新增对应条目。
3. 本地运行 `python -m http.server 8765 --bind 127.0.0.1` 能打开。
4. 浏览器里能搜索到新笔记。

