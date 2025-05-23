# PDF 搜尋工具

一個使用 Python 製作的命令列工具，可在指定資料夾（含子資料夾）內批次搜尋 PDF 文件中的詞語或句型，支援正則表達式搜尋，並可顯示匹配結果所在頁碼及上下文。

## 功能特色

- 批次搜尋指定資料夾及子資料夾中的所有 PDF 檔案
- 支援普通字串及正則表達式搜尋
- 顯示匹配詞所在頁碼（可選）
- 顯示匹配詞前後指定字元數的上下文（可選）

## 安裝依賴

請先安裝 [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)：

```bash
pip install PyMuPDF
```

## 使用說明

```bash
python your_script.py --term "搜尋詞語" [--folder "資料夾路徑"] [--regex] [--printpages] [--context 數字]
```

### 參數說明

| 參數          | 說明                                   | 是否必填 | 預設值         |
| ------------- | ------------------------------------ | -------- | -------------- |
| `--term`      | 要搜尋的詞語或正則表達式               | 必填     | -              |
| `--folder`    | 要搜尋的資料夾路徑（含子資料夾）        | 選填     | 目前目錄（`.`） |
| `--regex`     | 是否使用正則表達式搜尋                   | 選填     | 否             |
| `--printpages`| 是否顯示匹配詞所在的 PDF 頁碼            | 選填     | 否             |
| `--context`   | 顯示匹配詞前後多少字元作為上下文，預設 10 | 選填     | 不指定則不顯示 |

## 範例

- 搜尋目前目錄及子目錄 PDF 中的詞語 "example"：

  ```bash
  python your_script.py --term example
  ```

- 指定資料夾 `./pdfs`，使用正則表達式搜尋符合 `\btest\d+\b` 的詞：

  ```bash
  python your_script.py --folder ./pdfs --term "\\btest\\d+\\b" --regex
  ```

- 顯示匹配詞頁碼，並顯示前後 20 字元上下文：

  ```bash
  python your_script.py --term "important" --printpages --context 20
  ```

## 注意事項

- 若未指定 `--folder`，預設搜尋目前目錄及所有子資料夾
- 使用正則表達式時，請注意命令行跳脫字元（例如反斜線需用 `\\`）
- 本工具無法解析圖片型掃描 PDF，只能搜尋內嵌文字
- 建議在 UTF-8 編碼環境下執行，以避免亂碼問題

## 授權 License

本專案採用 GNU General Public License v3.0 (GPL-3.0) 授權。  
詳情請參閱 [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html) 條款。

