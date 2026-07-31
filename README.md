# Digital Exhaust & Metadata Privacy Analysis

## Professional Overview
The **Digital Exhaust & Metadata Privacy Analysis** project investigates the privacy risks, threat vectors, and mitigation techniques associated with file metadata and digital footprint leakage. Developed for the *Cyber Security* degree program at UET Lahore, this project combines analytical research with empirical demonstrations using the **Metadata Anonymisation Toolkit (MAT2)** to demonstrate how sensitive data (GPS coordinates, author names, software specs, device serials) is embedded in files and how it can be systematically sanitized.

## Objectives
- Identify passive digital footprint vectors and privacy risks in everyday document/media files.
- Evaluate file metadata extraction tools (EXIF tooling) and privacy-enhancing technologies.
- Demonstrate empirical metadata stripping using MAT2 (Metadata Anonymisation Toolkit v2).

## Features
- **Metadata Threat Analysis**: Exhaustive report examining hidden EXIF, office XML metadata, and revision histories (`Metadata_Privacy_and_MAT2_Report.docx`).
- **Visual Attack & Defense Presentation**: Professional slide presentation detailing real-world digital footprint tracking scenarios (`Digital Exhaust Presentation.pptx`).
- **Empirical Scrubbing Screenshots**: Documented evidence of image and document metadata before and after MAT2 anonymization (`cyber_ss.pdf`).

## Technologies Used
- **Anonymization Toolkit**: MAT2 (Metadata Anonymisation Toolkit v2)
- **Analysis Tools**: ExifTool, PDF/Office Metadata Analyzers
- **Domain**: Cyber Security, Privacy Engineering, Digital Forensics

## Architecture Overview
The evaluation methodology follows a 3-step privacy verification pipeline:
1. **Extraction**: Inspect raw document/image metadata to record exposed sensitive attributes.
2. **Anonymization**: Pass files through MAT2 sanitization engine to scrub non-essential metadata fields.
3. **Verification**: Re-examine processed files to verify complete metadata elimination without corrupting visual/text contents.

## Folder Structure
```text
digital-exhaust-analysis/
├── docs/
│   ├── Metadata_Privacy_and_MAT2_Report.docx
│   └── Digital Exhaust Presentation.pptx
├── assets/
│   └── screenshots/
│       └── cyber_ss.pdf
├── .gitignore
├── LICENSE
└── README.md
```

## Installation Guide & Usage
To perform metadata analysis and anonymization using MAT2:
1. Install MAT2 on Linux/macOS:
```bash
sudo apt install mat2
```
2. Inspect metadata of a target file:
```bash
mat2 -s target_file.jpg
```
3. Scrub metadata cleanly:
```bash
mat2 target_file.jpg
```

## Screenshots & Verification Proof
- [Empirical Metadata Scrubbing Proof (PDF)](assets/screenshots/cyber_ss.pdf)
- [Metadata Privacy Full Technical Report (Word)](docs/Metadata_Privacy_and_MAT2_Report.docx)
- [Digital Exhaust Attack Presentation (PowerPoint)](docs/Digital%20Exhaust%20Presentation.pptx)

## Learning Outcomes
- Developed deep understanding of file format specifications (JPEG EXIF, PDF dictionary structures, Office OpenXML).
- Analyzed privacy threats resulting from unintentional location, identity, and system metadata disclosure.
- Evaluated open-source privacy tooling for automated enterprise metadata sanitization workflows.

## Future Improvements
- Build an automated Python pipeline for batch metadata stripping across cloud storage buckets.
- Implement web-based drag-and-drop file sanitization microservice.
- Research steganographic payload detection within sanitized media files.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Author
**Tahniat Farhan**  
BS Cyber Security  
University of Engineering and Technology (UET) Lahore
