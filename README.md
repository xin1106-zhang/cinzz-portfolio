# Cinzz Studio｜Cinzia 剪輯作品集

線上網址(Artifact):https://claude.ai/code/artifact/824072ad-5249-4967-920e-620bed275b6e
(私人連結,分享請從頁面右上的 share 選單開啟存取權)

## 檔案結構

- `portfolio.html` — 原始模板(改內容、文案、CSS 都改這支;含 `/*FONTS*/` `/*THUMBS*/` `__PHOTO__` `__CLAUDE__` 佔位符)
- `portfolio_final.html` — 組裝後的發布版(自動產生,勿手改)
- `build/build_page.py` — 組裝腳本:把縮圖、照片、logo 圖形注入模板
- `build/build_fonts.py` — 字體子集化工具(目前未使用,系統字型;要嵌字體時用)
- `build/thumbs/` + `build/thumbs.css` — 所有影片縮圖與內嵌 CSS
- `build/photo.jpg` — 關於我照片(壓縮版;原檔在 shared-assets/cinzia-portrait.png)
- `build/logo.jpg` — Cinzz Studio logo 裁切版(原檔在 shared-assets/cinzzstudio_LOGO.png)
- `build/claude.path` — Claude logo SVG 路徑(工具區圖示用)

## 更新流程

1. 修改 `portfolio.html`
2. 執行:`python build/build_page.py`
3. 把產出的 `portfolio_final.html` 重新發布到同一個 Artifact 網址
   (請 Claude 代發,或未來自行架站直接上傳這個檔案)

## 新增影片卡片時

1. 下載縮圖:`curl -o build/thumbs/<ID>.jpg https://i.ytimg.com/vi/<ID>/mqdefault.jpg`
2. 在 `build/thumbs.css` 加一行 `.t-<ID>{background-image:url(data:image/jpeg;base64,<base64>)}`
3. 在 `portfolio.html` 複製一張現有卡片改連結、標題、觀看數
4. 重新組裝發布

## 內容原則(2026-08 定稿)

- 觀看數據:封面左下深色毛玻璃藥丸 + 眼睛圖示,數字為抓取當下快照,需手動更新
- 見證:口語化短句 + hashtag 署名,不放具名
- 聯絡:Email(cinzzstudio@gmail.com)為唯一 CTA
- 交件條件:5 個工作天、含 2 次修改(詳見 FAQ)
