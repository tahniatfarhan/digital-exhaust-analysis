"""
Automated Pytest Unit Test Suite for Metadata Privacy Analysis Tool
"""

import os
import pytest
from PIL import Image

from src.metadata_scrubber import (
    extract_image_metadata,
    scrub_image_metadata,
    audit_file,
    PIL_AVAILABLE,
)


@pytest.fixture
def sample_image(tmp_path):
    """Creates a temporary sample JPEG image for testing."""
    img_path = tmp_path / "test_sample.jpg"
    img = Image.new("RGB", (100, 100), color="blue")
    img.save(img_path)
    return str(img_path)


def test_image_metadata_extraction(sample_image):
    meta = extract_image_metadata(sample_image)
    assert meta is not None
    assert meta["Format"] == "JPEG"
    assert meta["Size"] == "100x100"


def test_image_metadata_scrubbing(sample_image, tmp_path):
    clean_path = str(tmp_path / "clean_sample.jpg")
    success = scrub_image_metadata(sample_image, clean_path)
    assert success is True
    assert os.path.exists(clean_path)

    clean_meta = extract_image_metadata(clean_path)
    assert "EXIF_Tags" not in clean_meta


def test_audit_file_valid_image(sample_image):
    success, meta = audit_file(sample_image)
    assert success is True
    assert "Format" in meta


def test_audit_file_invalid_path():
    success, meta = audit_file("nonexistent_file_path.jpg")
    assert success is False
    assert meta == {}


def test_audit_file_unsupported_extension(tmp_path):
    txt_file = tmp_path / "test.txt"
    txt_file.write_text("hello world")
    success, meta = audit_file(str(txt_file))
    assert success is False
    assert meta == {}


def test_audit_file_corrupted_image(tmp_path):
    corrupt_path = tmp_path / "corrupt.jpg"
    corrupt_path.write_bytes(b"NOT_A_REAL_IMAGE_DATA")
    with pytest.raises(ValueError, match="Failed to read image file"):
        extract_image_metadata(str(corrupt_path))
