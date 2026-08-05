document.addEventListener('DOMContentLoaded', () => {
    const filePreset = document.getElementById('file-preset');
    const btnScrub = document.getElementById('btn-scrub-file');
    const rawContent = document.getElementById('raw-content');
    const cleanContent = document.getElementById('clean-content');

    btnScrub.addEventListener('click', () => {
        const val = filePreset.value;
        if (val === 'photo') {
            rawContent.textContent = "Format: JPEG (1920x1080)\nCamera: Apple iPhone 14 Pro\nGPS Latitude: 31.5204 N\nGPS Longitude: 74.3587 E\nDate/Time: 2026-07-28 14:22:01";
            cleanContent.textContent = "Format: JPEG (1920x1080)\nEXIF Tags: STRIPPED (0 tags)\nGPS Coordinates: REMOVED\nCamera Hardware ID: REMOVED\nStatus: CLEAN_NO_PRIVACY_LEAK";
        } else {
            rawContent.textContent = "Total Pages: 12\nPDF Author: Tahniat Farhan\nProducer: macOS Quartz PDFContext\nCreationDate: D:20260601120000Z";
            cleanContent.textContent = "Total Pages: 12\nPDF Catalog Properties: CLEARED\nAuthor / Producer Headers: REMOVED\nStatus: CLEAN_DOCUMENT";
        }
    });
});