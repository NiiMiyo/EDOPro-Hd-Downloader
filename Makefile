FILENAME  = EDOPro-HD-Downloader
LICENSE   = HdDownloader.LICENSE.txt
DISTPATH  = ./bin

build:
	pyinstaller main.py -y --distpath "$(DISTPATH)" -F --specpath "$(DISTPATH)" -n "$(FILENAME)" -c --clean
	cp $(LICENSE) $(DISTPATH)/$(LICENSE)

	rm -rf build
