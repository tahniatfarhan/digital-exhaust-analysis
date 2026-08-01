
function auditMeta() {
    const out = document.getElementById('exhaustOut');
    out.innerHTML = `[DIGITAL EXHAUST AUDIT] Target: sample_photo.jpg (CWE-200 Risk Audit)\n----------------------------------------------------------------------------------------\n[CAMERA] Model: iPhone 15 Pro | Exposure: 1/120s | ISO: 100\n[GPS] Latitude: 31.5204° N | Longitude: 74.3587° E (UET Lahore Campus)\n[PRIVACY THREAT] Precise location & device serial number exposed to OSINT gathering!`;
}

function scrubMeta() {
    const out = document.getElementById('exhaustOut');
    out.innerHTML = `[METADATA SCRUBBER] Processing sample_photo.jpg...\n----------------------------------------------------------------------------------------\n[1] Stripping EXIF tag dictionary...\n[2] Rebuilding raw pixel raster data without headers...\n[3] Re-encoding clean JPEG output stream...\n[SUCCESS] Clean file generated: 'sample_photo_clean.jpg' (Zero EXIF tags remaining).`;
}
