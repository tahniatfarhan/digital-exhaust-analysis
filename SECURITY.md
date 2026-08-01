# Security Policy & Privacy Risks (Digital Exhaust)

## Educational Project Disclaimer

> 🎓 **Academic Security Project Notice:** This repository is an **educational laboratory toolkit** designed to demonstrate digital forensics, metadata privacy auditing, and EXIF sanitization concepts. It is designed for educational evaluation and privacy awareness, NOT as a commercial enterprise forensic suite.

---

## 🛡️ Digital Exhaust & Information Disclosure Risks (CWE-200)

1. **GPS Location Leaks:** EXIF metadata embedded in photos taken by smartphones or digital cameras often contains precise GPS latitude and longitude coordinates, exposing home addresses or physical locations.
2. **Device Identification:** Camera serial numbers, firmware versions, and smartphone model IDs allow cross-platform device tracking.
3. **Document Author Tracking:** PDF properties expose internal network usernames, corporate software versions, and local file directory structures.
4. **Information Minimization:** Always scrub metadata prior to publishing images or documents on public websites or social media.

---

## Reporting Vulnerabilities

If you discover a security flaw or parsing crash in this utility, please email **tahniatfarhan@gmail.com**.
