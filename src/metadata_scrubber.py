"""
Digital Exhaust & Metadata Privacy Analysis Utility
---------------------------------------------------
Educational Python CLI tool for auditing and scrubbing sensitive metadata
(EXIF tags, GPS coordinates, device serials, PDF properties) to prevent
information disclosure (CWE-200 / OWASP WSTG-INFO-005).

Author: Tahniat Farhan | BS Cyber Security, UET Lahore
"""

import sys
import os
import argparse
from typing import Dict, Any, Tuple

try:
    from PIL import Image, ImageOps
    from PIL.ExifTags import TAGS, GPSTAGS
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

try:
    import PyPDF2
    PYPDF2_AVAILABLE = True
except ImportError:
    PYPDF2_AVAILABLE = False


def extract_image_metadata(filepath: str) -> Dict[str, Any]:
    """Extracts EXIF metadata tags, camera details, and GPS coordinates from JPEG/PNG images."""
    if not PIL_AVAILABLE:
        raise RuntimeError("Pillow library is required. Install via 'pip install Pillow'.")

    metadata = {}
    try:
        with Image.open(filepath) as img:
            metadata["Format"] = img.format
            metadata["Mode"] = img.mode
            metadata["Size"] = f"{img.width}x{img.height}"

            exif_data = img._getexif() if hasattr(img, "_getexif") and img._getexif() else None
            if exif_data:
                exif_tags = {}
                gps_tags = {}
                for tag_id, value in exif_data.items():
                    tag_name = TAGS.get(tag_id, tag_id)
                    if tag_name == "GPSInfo":
                        for g_id in value:
                            g_name = GPSTAGS.get(g_id, g_id)
                            gps_tags[str(g_name)] = str(value[g_id])
                    else:
                        exif_tags[str(tag_name)] = str(value)
                metadata["EXIF_Tags"] = exif_tags
                if gps_tags:
                    metadata["GPS_Coordinates"] = gps_tags
    except Exception as e:
        raise ValueError(f"Failed to read image file or corrupted format: {e}")

    return metadata


def extract_pdf_metadata(filepath: str) -> Dict[str, Any]:
    """Extracts document properties (Author, Creator, Producer, Dates) from PDF files."""
    if not PYPDF2_AVAILABLE:
        raise RuntimeError("PyPDF2 library is required. Install via 'pip install PyPDF2'.")

    metadata = {}
    try:
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            metadata["Total_Pages"] = len(reader.pages)
            doc_info = reader.metadata
            if doc_info:
                info_dict = {}
                for key, val in doc_info.items():
                    clean_key = str(key).lstrip("/")
                    info_dict[clean_key] = str(val)
                metadata["PDF_Properties"] = info_dict
    except Exception as e:
        raise ValueError(f"Failed to read PDF document or corrupted format: {e}")

    return metadata


def scrub_image_metadata(input_path: str, output_path: str) -> bool:
    """Removes all EXIF metadata from image while preserving visual pixel data."""
    if not PIL_AVAILABLE:
        raise RuntimeError("Pillow library is required.")

    try:
        with Image.open(input_path) as img:
            data = list(img.getdata())
            clean_img = Image.new(img.mode, img.size)
            clean_img.putdata(data)
            clean_img = ImageOps.exif_transpose(img) if hasattr(ImageOps, "exif_transpose") else clean_img
            
            # Save image stripped of EXIF info
            clean_img.save(output_path)
            return True
    except Exception as e:
        raise RuntimeError(f"Error scrubbing image metadata: {e}")


def scrub_pdf_metadata(input_path: str, output_path: str) -> bool:
    """Strips metadata document properties from PDF file."""
    if not PYPDF2_AVAILABLE:
        raise RuntimeError("PyPDF2 library is required.")

    try:
        reader = PyPDF2.PdfReader(input_path)
        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        # Clear document metadata catalog
        writer.add_metadata({})

        with open(output_path, "wb") as f_out:
            writer.write(f_out)
        return True
    except Exception as e:
        raise RuntimeError(f"Error scrubbing PDF metadata: {e}")


def audit_file(filepath: str) -> Tuple[bool, Dict[str, Any]]:
    """Audits file for sensitive metadata leakage."""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return False, {}

    ext = os.path.splitext(filepath)[1].lower()
    if ext in [".jpg", ".jpeg", ".png"]:
        meta = extract_image_metadata(filepath)
    elif ext == ".pdf":
        meta = extract_pdf_metadata(filepath)
    else:
        print(f"Error: Unsupported file format '{ext}'. Supported formats: .jpg, .jpeg, .png, .pdf")
        return False, {}

    return True, meta


def main():
    parser = argparse.ArgumentParser(description="Digital Exhaust & Metadata Privacy Analysis Tool")
    parser.add_argument("file", help="Path to target file (.jpg, .jpeg, .png, .pdf)")
    parser.add_argument("--scrub", action="store_true", help="Scrub metadata and save clean output file")
    parser.add_argument("--output", help="Output path for scrubbed file (default: file_clean.ext)")
    args = parser.parse_args()

    success, metadata = audit_file(args.file)
    if not success:
        sys.exit(1)

    print("\n=======================================================")
    print(f" METADATA AUDIT REPORT: {os.path.basename(args.file)}")
    print("=======================================================")
    for key, val in metadata.items():
        if isinstance(val, dict):
            print(f" [{key}]:")
            for sub_k, sub_v in val.items():
                print(f"    - {sub_k}: {sub_v}")
        else:
            print(f" {key}: {val}")
    print("=======================================================")

    if args.scrub:
        ext = os.path.splitext(args.file)[1].lower()
        out_path = args.output if args.output else f"{os.path.splitext(args.file)[0]}_clean{ext}"
        
        print(f"\nScrubbing metadata from '{args.file}' -> '{out_path}'...")
        if ext in [".jpg", ".jpeg", ".png"]:
            scrub_image_metadata(args.file, out_path)
        elif ext == ".pdf":
            scrub_pdf_metadata(args.file, out_path)
            
        print(f"✅ Metadata successfully scrubbed! Clean file saved to: {out_path}")


if __name__ == "__main__":
    main()
