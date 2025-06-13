# 🧑‍💻 TwoDish 開發協作指引（Git 操作守則）

## ✅ 分支命名規則

- `main`：只放穩定版本（已完成、可部署）
- `kenny/feature-xxx`：Kenny 寫新功能（例如 `kenny/feature-user-login`）
- `jacky/bugfix-xxx`：Jacky 修 bug（例如 `jacky/bugfix-image-upload`）

---

## 🔧 開發流程

1️⃣ **從 GitHub clone repo**
```bash
git clone https://github.com/KdKenny/TwoDish.git
cd TwoDish
2️⃣ 開一條屬於你自己嘅分支

git checkout -b kenny/feature-xxx
3️⃣ 進行開發 + 提交 commit

git add .
git commit -m "新增用戶登入頁面"
4️⃣ 推上 GitHub

git push -u origin kenny/feature-xxx
5️⃣ 到 GitHub 開 Pull Request（PR）

請確保 PR 目標分支係 main，簡單寫明你做咗啲咩。

6️⃣ 等隊長 / reviewer Approve 合併

2️⃣ 開一條屬於你自己嘅分支

🔒 main 分支保護規則（已啟用）
規則	                ｜   描述
✅ 不可直接 push	    ｜   必須經 PR 合併
✅ 至少一人審批	      ｜   所有更改需獲批
✅ 管理員都唔可以繞過  ｜	 保證主線乾淨穩定
🚫 禁止強制 push	    ｜   防止 overwrite 他人更改
🚫 禁止刪除 main 分支 ｜   永遠保留穩定主線

💬 溝通協作建議
建議每次開發前先 git pull origin main

有衝突唔好亂改，先問！

PR 標題清楚描述做咗咩，方便 review

唔好改人哋分支，自己開分支
