# Digital Exhaust & Metadata Privacy Analysis Toolkit

[![Python Forensics CI](https://github.com/tahniatfarhan/digital-exhaust-analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/tahniatfarhan/digital-exhaust-analysis/actions/workflows/ci.yml)
[![CodeQL Analysis](https://github.com/tahniatfarhan/digital-exhaust-analysis/actions/workflows/codeql.yml/badge.svg)](https://github.com/tahniatfarhan/digital-exhaust-analysis/actions/workflows/codeql.yml)
[![CWE-200 Information Disclosure](https://img.shields.io/badge/CWE--200-Information_Disclosure-red.svg)](https://cwe.mitre.org/data/definitions/200.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

> 🎓 **Academic Project Disclaimer:** This repository is an **educational laboratory project** developed for the Digital Forensics / Cyber Security course in the BS Cyber Security degree program at UET Lahore. It demonstrates metadata extraction, information disclosure risk auditing (CWE-200 / OWASP WSTG-INFO-005), and EXIF/PDF metadata scrubbing concepts.

---

## 📐 Metadata Audit & Scrubbing Workflow

```mermaid
sequenceDiagram
    autonumber
    actor Analyst as Security Analyst
    participant CLI as metadata_scrubber.py
    participant Extractor as EXIF / PDF Metadata Parser
    participant Sanitizer as Metadata Sanitizer Engine
    participant Disk as File Storage

    Analyst->>CLI: Input File (JPEG, PNG, PDF)
    CLI->>Extractor: Parse EXIF Tags, GPS Coords, Author Properties
    Extractor-->>Analyst: Output Metadata Audit Findings Report
    opt User Requests --scrub
        CLI->>Sanitizer: Strip EXIF / Catalog Properties
        Sanitizer->>Disk: Save Clean Copy (file_clean.ext)
        Sanitizer-->>Analyst: Confirmation Report (0 Metadata Leaks Remaining)
    end
```

---

## 🛡️ Key Cybersecurity & Privacy Concepts

1. **Digital Exhaust:** Residual data passively generated when using digital devices, smartphones, and software applications (e.g., GPS coordinates, camera serial numbers, device timestamps).
2. **Information Disclosure (CWE-200):** Unintended exposure of internal network account names, software versions, or physical GPS locations embedded inside public media files.
3. **Data Minimization & Privacy-by-Design:** Stripping non-essential tracking metadata prior to publishing or sharing files.

---

## 📊 Sample Metadata Extraction & Audit Output

### Image EXIF Leak Audit Sample
```
=======================================================
 METADATA AUDIT REPORT: photo_sample.jpg
=======================================================
 Format: JPEG
 Size: 4032x3024
 [EXIF_Tags]:
    - Make: Apple
    - Model: iPhone 13 Pro
    - DateTimeOriginal: 2024:05:15 14:22:10
    - Software: iOS 17.4
 [GPS_Coordinates]:
    - GPSLatitudeRef: N
    - GPSLatitude: 31.5708
    - GPSLongitudeRef: E
    - GPSLongitude: 74.3142  (Resolves to Lahore, Pakistan)
=======================================================
```

---

## 📁 Repository Structure

```
digital-exhaust-analysis/
├── .github/
│   ├── dependabot.yml              # Automated monthly dependency scanner
│   └── workflows/
│       ├── ci.yml                  # Python test workflow across 3.10, 3.11, 3.12
│       └── codeql.yml              # CodeQL Application Security Analysis
├── assets/
│   └── screenshots/                # Project research artifacts
├── docs/                           # Research papers & presentation slides
│   ├── Digital Exhaust Presentation.pptx
│   └── Metadata_Privacy_and_MAT2_Report.docx
├── src/
│   └── metadata_scrubber.py        # Python Metadata Audit & Scrubbing CLI Utility
├── tests/
│   └── test_scrubber.py            # Automated Pytest Unit Test Suite
├── CODE_OF_CONDUCT.md              # Contributor Code of Conduct
├── CONTRIBUTING.md                 # Contribution guidelines
├── LICENSE                         # MIT License
├── pyproject.toml                  # Python PEP 517/518 build configuration
├── README.md                       # Comprehensive Documentation & Forensics Guide
├── requirements.txt                # Dependencies (Pillow, PyPDF2, pytest)
└── SECURITY.md                     # Security & Privacy Policy
```

---

## 🛠️ Execution & Testing

### 1. Installation
```bash
git clone https://github.com/tahniatfarhan/digital-exhaust-analysis.git
cd digital-exhaust-analysis
pip install -r requirements.txt
```

### 2. Audit File Metadata
```bash
python src/metadata_scrubber.py sample_image.jpg
```

### 3. Audit & Scrub Metadata
```bash
python src/metadata_scrubber.py sample_image.jpg --scrub
# Output saved to: sample_image_clean.jpg
```

### 4. Run Automated Pytest Suite
```bash
pytest -v tests/
```

---

## 📄 License & Author

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

**Author:** [Tahniat Farhan](https://github.com/tahniatfarhan) — BS Cyber Security, UET Lahore.
