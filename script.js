
        function runExhaustAudit() {
            document.getElementById('demoBody').innerHTML = `
                <div>$ python src/metadata_scrubber.py photo.jpg --scrub</div>
                <div style="color: #f59e0b; margin-top: 8px;">[AUDIT WARNING] EXIF Tags Detected:</div>
                <div>    - Camera: iPhone 15 Pro</div>
                <div>    - GPS: 31.5204° N, 74.3587° E (UET Lahore)</div>
                <div style="color: #4ade80; margin-top: 8px;">[SCRUBBING] Stripping EXIF metadata &amp; rebuilding pixel raster...</div>
                <div style="color: #e2e8f0;">[SUCCESS] Clean image saved to 'photo_clean.jpg' (Zero EXIF leakage).</div>
            `;
        }
        document.getElementById('demoBody').innerHTML = `
            <div>
                <button class="term-btn" onclick="runExhaustAudit()">Audit &amp; Scrub Sample Image EXIF</button>
            </div>
            <div>$ Click button to simulate metadata privacy audit...</div>
        `;
        