# EnReach

Workspace-compliant Python project template.

This repository provides a ready-to-copy base structure for new Python projects.  
It is intended as a starting point for workspaces that may later evolve into full Python packages.  
The layout includes folders for source code, configuration, data, documentation, and scripts.

---

## Purpose

- Provide a standard and reusable folder layout for new projects  
- Simplify project setup and ensure consistency across repositories  
- Include standard metadata, license, and dependency management  
- Support future conversion into a Python package when the project stabilizes  

---

## Installation

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

After activating the environment, run the main module:

```bash
python -m EnReach
```

Or import it in Python code:

```python
from python_full_template_project import main
main()
```

---

## Structure

```text
EnReach/
├── build              # build artifacts or generated outputs
├── config             # configuration files
├── data               # input data or datasets
├── docs               # documentation and notes
├── LICENSE            # license file
├── metadata.yaml      # project metadata
├── pyproject.toml     # project definition and build metadata
├── README.md          # project overview
├── requirements.txt   # Python dependencies
├── results            # experiment or processing outputs
├── scripts            # standalone or helper scripts
├── src                # Python source code (uses src/ layout)
│   └── EnReach
│       ├── __init__.py
│       └── main.py
└── tests              # test and validation scripts
```

---

## Author

**Marek Sys**  
[marek.sys@gmail.com](mailto:marek.sys@gmail.com)

---

## License

MIT License — see [LICENSE](LICENSE) for details.
