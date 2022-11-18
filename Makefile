FILENAME    = EDOPro-HD-Downloader
LICENSE     = LICENSE
LICENSE_BIN = HdDownloader.LICENSE.txt
DISTPATH    = bin
WORKPATH    = workpath_pyinstaller
ZIP_WIN     = windows.zip

build:
	pyinstaller main.py -y --distpath "$(DISTPATH)" -F --specpath "$(DISTPATH)" -n "$(FILENAME)" -c --clean --workpath "$(WORKPATH)"
	cp "$(LICENSE)" "$(DISTPATH)/$(LICENSE_BIN)"

	rm -rf "$(WORKPATH)"

7z-win: build
	cd "$(DISTPATH)" && 7z a "$(ZIP_WIN)" "$(FILENAME).exe" "$(LICENSE_BIN)"

clean:
	rm -rf "hd_cards_downloader_tracker"
	rm -rf "hd_fields_downloader_tracker"
