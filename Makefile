FILENAME  = EDOPro-HD-Downloader
LICENSE   = HdDownloader.LICENSE.txt
DISTPATH  = ./bin
WORKPATH  = ./workpath_pyinstaller

build:
	pyinstaller main.py -y --distpath "$(DISTPATH)" -F --specpath "$(DISTPATH)" -n "$(FILENAME)" -c --clean --workpath "$(WORKPATH)"
	cp "$(LICENSE)" "$(DISTPATH)/$(LICENSE)"

	rm -rf "$(WORKPATH)"
