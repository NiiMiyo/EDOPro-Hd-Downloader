FILENAME  = EDOPro-HD-Downloader
LICENSE   = HdDownloader.LICENSE.txt
DISTPATH  = bin
WORKPATH  = workpath_pyinstaller
ZIP_WIN   = windows.zip

build:
	pyinstaller main.py -y --distpath "$(DISTPATH)" -F --specpath "$(DISTPATH)" -n "$(FILENAME)" -c --clean --workpath "$(WORKPATH)"
	cp "$(LICENSE)" "$(DISTPATH)/$(LICENSE)"

	rm -rf "$(WORKPATH)"

7z-win: build
	cd "$(DISTPATH)" && 7z a "$(ZIP_WIN)" "$(FILENAME).exe" "$(LICENSE)"
