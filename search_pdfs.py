import os
import re
import fitz  # PyMuPDF
import argparse

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text()
        pages.append((i + 1, text))
    return pages

def search_term_in_text(text, term, use_regex=False):
    if use_regex:
        matches = list(re.finditer(term, text, flags=re.IGNORECASE))
    else:
        pattern = re.escape(term)
        matches = list(re.finditer(pattern, text, flags=re.IGNORECASE))
    return matches

def search_pdf(pdf_path, term, use_regex=False, context_window=None):
    pages = extract_text_from_pdf(pdf_path)
    results = []
    for page_num, text in pages:
        matches = search_term_in_text(text, term, use_regex)
        for m in matches:
            if context_window is not None:
                #snippet = '\033[92m' + text[max(0, m.start()-context_window):m.end()+context_window].strip() + '\033[0m'
                snippet = text[max(0, m.start()-context_window): m.start()] + '\033[31m' + text[m.start():m.end()].strip() + '\033[0m' + text[m.end():m.end()+context_window]
            else:
                snippet = None
            results.append((page_num, m.group(0), snippet))
    return results

def get_all_subfolders(base_folder):
    subfolders = []
    for root, dirs, _ in os.walk(base_folder):
        for d in dirs:
            subfolders.append(os.path.join(root, d))
    return subfolders or [base_folder]

def search_folder(folder_path, term, use_regex=False, context_window=None, print_pages=False):
    report = []
    cnt = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                full_path = os.path.join(root, file)
                # print(f"{full_path}")
                results = search_pdf(full_path, term, use_regex, context_window)
                if results:
                    cnt += len(results) 
                    print(f"\n📄 檔案: {full_path}")
                    print(f"🔍 共找到 {len(results)} 筆匹配")
                    if print_pages:
                        for page, match_text, context in results:
                            print(f"  ➤ 第 {page} 頁：『{match_text}』")
                            if context is not None:
                                print(f"     ...{context}...")
                    print(f"==================================================================")
    return cnt 

def main():
    parser = argparse.ArgumentParser(description="搜尋 PDF 是否包含指定詞語、句子或句型")
    parser.add_argument("--folder", help="PDF 資料夾路徑（可略）")
    parser.add_argument("--term", required=True, help="要搜尋的詞語或句型")
    parser.add_argument("--regex", action="store_true", help="是否使用正則表達式")
    parser.add_argument("--printpages", action="store_true", help="是否列出頁碼")
    parser.add_argument("--context", type=int, help="前後顯示幾個字元作為上下文", default=argparse.SUPPRESS)
    args = parser.parse_args()

    folders_to_search = [args.folder] if args.folder else get_all_subfolders(".")
    context_window = getattr(args, "context", None)
    print_pages = args.printpages or (context_window is not None)

    if not hasattr(args, "context"):
        print("ℹ️ 未指定 --context，將僅顯示匹配詞不含上下文。")

    result_cnt = 0
    for folder in folders_to_search:
        result_cnt += search_folder(folder, args.term, args.regex, context_window, print_pages)

    if result_cnt == 0:
        print("❌ 沒有找到任何匹配項目。")
    else:
        print(f"找到 {result_cnt} 個匹配項目。")
        

if __name__ == "__main__":
    main()

