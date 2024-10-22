pyinstaller --onefile --name SII --noconsole --add-data "C:/Users/jporlles/Desktop/dev/python-arquitecture/modulos/SII/chromedriver-win32/chromedriver.exe;chromedriver-win32" --add-data "C:/Users/jporlles/Desktop/dev/python-arquitecture/modulos/SII/.env;." interface.py --distpath ./app/dist --workpath ./app/build --specpath ./app/spec


pyinstaller --onefile --name SII --add-data "C:/Users/jporlles/Desktop/dev/python-arquitecture/modulos/SII/chromedriver-win32/chromedriver.exe;chromedriver-win32" --add-data "C:/Users/jporlles/Desktop/dev/python-arquitecture/modulos/SII/.env;." interface.py --distpath ./app/dist --workpath ./app/build --specpath ./app/spec


pyinstaller SII.spec




