# PDF Search Tool

A command-line tool written in Python that allows you to batch search for keywords or patterns in PDF files within a specified folder (including subfolders). It supports regular expressions and can display the page number and surrounding context of each match.

## Features

- Recursively search all PDF files in a given folder and its subfolders
- Support for plain text or regular expression search
- Optionally display the page number where each match is found
- Optionally display surrounding context characters around each match

## Installation

Make sure to install [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/):

```bash
pip install PyMuPDF
```

## Usage

```bash
python your_script.py --term "search_term" [--folder "folder_path"] [--regex] [--printpages] [--context number]
```

### Arguments

| Argument       | Description                                            | Required | Default           |
|----------------|--------------------------------------------------------|----------|-------------------|
| `--term`       | The word or regex pattern to search for               | Yes      | -                 |
| `--folder`     | Folder path to search (recursively)                   | No       | Current directory |
| `--regex`      | Enable regular expression search                      | No       | Disabled          |
| `--printpages` | Show page numbers of matches                          | No       | Disabled          |
| `--context`    | Show this many characters before/after the match      | No       | No context shown  |

## Examples

- Search for the word "example" in the current directory and subdirectories:

  ```bash
  python your_script.py --term example
  ```

- Search using a regex pattern `\btest\d+\b` in the `./pdfs` folder:

  ```bash
  python your_script.py --folder ./pdfs --term "\\btest\\d+\\b" --regex
  ```

- Show page numbers and 20 characters of context around each match:

  ```bash
  python your_script.py --term "important" --printpages --context 20
  ```

## Notes

- If `--folder` is not specified, the current directory (`.`) is used by default.
- When using regular expressions, be careful with shell escaping (e.g., use `\\` for backslashes).
- This tool cannot search scanned PDFs (images). It only works on PDFs with embedded text.
- Use in a UTF-8 environment to avoid encoding issues.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).  
See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html) for details.

