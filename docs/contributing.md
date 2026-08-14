# 如何贡献

## 推荐流程

1. 从 `main` 创建新分支。
2. 修改对应的中文和英文 Markdown 文件。
3. 本地运行 `mkdocs serve` 检查效果。
4. 提交 Pull Request。
5. 由维护者审核后合并。

## 文件命名

- 中文默认页：`page.md`
- 英文页：`page.en.md`
- 使用小写和连字符

## 本地预览

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Windows PowerShell：

```powershell
.venv\Scripts\Activate.ps1
```

## 维护信息

- **维护者：** Wiki Team
- **最后核验：** 2026-08-14
