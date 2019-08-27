Numberwang Badge
========

This is a stupid last minute project that came into existence for CCCamp19. If you are reading this you probably got an unpopulated PCB from me.

I did not expect that so many people got interested in it, so the documentation might be a little lacking. If you actually solder the badge and have any issue just create a Github issue here so others can profit from the discussion too.

THERE IS ONE BUG IN THE CIRCUIT. Please see the audio bodge fix png, in the hurry I misnamed a signal and it was NC when it was supposed to connect to the I2S amp. You need to solder one bodge wire, other than that all works fine.

The MCU on the board is the ATSAMD21G18, the pinout used is the same from the Adafruit Itsy Bitsy. I tried to stay as close to the Itsy Bitsy as possible so you can just refer to their documentation if you got any questions regarding pinout: https://learn.adafruit.com/introducing-itsy-bitsy-m0

Circuit wise its also really close (thanks to Adafruit for being open source), only difference is the added lipo charger which you usually find on Adafruit Feathers. It uses the same JST-PH 2.0 SMT right angle connector but the polarity is reversed to what the Adafruit batteries use! Why? Because I can't buy them in Germany and all other batteries with this connector use the opposite polarity so I went with what the batteries on Amazon offer.

Quick note on the BOM, the design isn't all that smart, there are some components that appear in both 0603 and 0805, you can get away with using just 0603 or just 0805, no need to get both sizes.

I think you can get all components from Mouser if you want, they will just be more expensive than getting them from LCSC. Especially the JST-PH, if you need that from 'not LCSC' go with Digikey or buy the over priced reselled one that is available from Mouser as an Adafruit product.

If anything is unclear in the BOM, please create an issue, I respond fairly quickly usually.

There is an SWD testpad pinout in 2.54mm raster, I used pogo pins for programming but you can also just use a right angle pin header that you press against the pad. Might be a bit flaky but works for flashing the bootloader. Here a tutorial from Adafruit that explains flashing with different programmers (can also use a Pi or other ARM MCU to flash if you dont got an SWD capable flasher)
https://learn.adafruit.com/how-to-program-samd-bootloaders

UF2 bootloader binary is provided in the repo as well as a slightly customized CircuitPython firmware (same as Itsy Bitsy M0 just different flash IC set). When using online docs you can always refer to Itsy Bitsy M0.
Same for Arduino, just get the Adafruit SAMD board package and choose Itsy Bitsy M0 as target.

