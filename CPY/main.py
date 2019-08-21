import audioio
import board
import audiobusio
import time
import random
import adafruit_dotstar as dotstar
import adafruit_fancyled.adafruit_fancyled as fancy
import touchio




 
# # For Feather M0 Express, ItsyBitsy M0 Express, Metro M0 Express
audio = audiobusio.I2SOut(board.D1, board.D0, board.D9)
# # For Feather M4 Express
# # audio = audiobusio.I2SOut(board.D1, board.D10, board.D11)
# # For Metro M4 Express
# # audio = audiobusio.I2SOut(board.D3, board.D9, board.D8)
 
# while True:
#     audio.play(wave)
#     while audio.playing:
#         pass

touch1 = touchio.TouchIn(board.A0)
touch2 = touchio.TouchIn(board.A1)
touch3 = touchio.TouchIn(board.A2)
touch4 = touchio.TouchIn(board.A3)
touch5 = touchio.TouchIn(board.A4)

num_leds = 15

# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
pixels = dotstar.DotStar(board.APA102_MOSI, board.APA102_SCK, num_leds, brightness=1.0,
                           auto_write=False)

# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
# dots = dotstar.DotStar(board.SCK, board.MOSI, 30, brightness=0.2)

# Using a DotStar Digital LED Strip with 30 LEDs connected to digital pins
# dots = dotstar.DotStar(board.D6, board.D5, 30, brightness=0.2)
# Declare a 6-element RGB rainbow palette
palette = [fancy.CRGB(1.0, 0.0, 0.0), # Red
           fancy.CRGB(0.5, 0.5, 0.0), # Yellow
           fancy.CRGB(0.0, 1.0, 0.0), # Green
           # fancy.CRGB(0.0, 0.5, 0.5), # Cyan
           fancy.CRGB(0.0, 0.0, 1.0), # Blue
           fancy.CRGB(0.5, 0.0, 0.5)] # Magenta




def numberwang():
	thats_numberwang_file = open("thats_numberwang.wav", "rb")
	thats_numberwang = audioio.WaveFile(thats_numberwang_file)
	offset = 0  # Positional offset into color palette to get it to 'spin'
	audio.play(thats_numberwang)
	while audio.playing:
	    for i in range(num_leds):
	        # Load each pixel's color from the palette using an offset, run it
	        # through the gamma function, pack RGB value and assign to pixel.
	        color = fancy.palette_lookup(palette, offset + i / num_leds)
	        color = fancy.gamma_adjust(color, brightness=0.25)
	        pixels[i] = color.pack()
	    pixels.show()

	    offset += 0.2  # Bigger number = faster spin
	thats_numberwang_file.close()
	return

def numberwang_intro():
	numberwang_intro_file = open("numberwang_intro_w_welcome.wav", "rb")
	numberwang_intro = audioio.WaveFile(numberwang_intro_file)
	offset = 0  # Positional offset into color palette to get it to 'spin'
	audio.play(numberwang_intro)
	while audio.playing:
	    for i in range(num_leds):
	        # Load each pixel's color from the palette using an offset, run it
	        # through the gamma function, pack RGB value and assign to pixel.
	        color = fancy.palette_lookup(palette, offset + i / num_leds)
	        color = fancy.gamma_adjust(color, brightness=0.25)
	        pixels[i] = color.pack()
	    pixels.show()

	    offset += 0.2  # Bigger number = faster spin
	numberwang_intro_file.close()
	return

def nine():
	audio_file = open("9.wav", "rb")
	wave = audioio.WaveFile(audio_file)
	offset = 0  # Positional offset into color palette to get it to 'spin'
	audio.play(wave)
	while audio.playing:
	    for i in range(num_leds):
	        # Load each pixel's color from the palette using an offset, run it
	        # through the gamma function, pack RGB value and assign to pixel.
	        color = fancy.palette_lookup(palette, offset + i / num_leds)
	        color = fancy.gamma_adjust(color, brightness=0.25)
	        pixels[i] = color.pack()
	    pixels.show()

	    offset += 0.2  # Bigger number = faster spin
	audio_file.close()
	return

def eight():
	audio_file = open("8_2.wav", "rb")
	wave = audioio.WaveFile(audio_file)
	offset = 0  # Positional offset into color palette to get it to 'spin'
	audio.play(wave)
	while audio.playing:
	    for i in range(num_leds):
	        # Load each pixel's color from the palette using an offset, run it
	        # through the gamma function, pack RGB value and assign to pixel.
	        color = fancy.palette_lookup(palette, offset + i / num_leds)
	        color = fancy.gamma_adjust(color, brightness=0.25)
	        pixels[i] = color.pack()
	    pixels.show()

	    offset += 0.2  # Bigger number = faster spin
	audio_file.close()
	return

def rotate():
	audio_file = open("lets_rotate_the_board.wav", "rb")
	wave = audioio.WaveFile(audio_file)
	offset = 0  # Positional offset into color palette to get it to 'spin'
	audio.play(wave)
	while audio.playing:
	    for i in range(num_leds):
	        # Load each pixel's color from the palette using an offset, run it
	        # through the gamma function, pack RGB value and assign to pixel.
	        color = fancy.palette_lookup(palette, offset + i / num_leds)
	        color = fancy.gamma_adjust(color, brightness=0.25)
	        pixels[i] = color.pack()
	    pixels.show()

	    offset += 0.2  # Bigger number = faster spin
	audio_file.close()
	return

while True:
    if touch1.value:
        print("Touched!")
        numberwang()
    if touch2.value:
        print("Touched!")
        numberwang_intro()
    if touch3.value:
        print("Touched!")
        nine()
    if touch4.value:
        print("Touched!")
        eight()
    if touch5.value:
        print("Touched!")
        rotate()
    time.sleep(0.15)



# 	    offset += 0.08  # Bigger number = faster spin
    
    # while audio.playing:
    #     pass
# # HELPERS
# # a random color 0 -> 224
# def random_color():
#     return random.randrange(0, 7) * 32


# # MAIN LOOP
# n_dots = len(dots)
# while True:
#     # Fill each dot with a random color
#     for dot in range(n_dots):
#         dots[dot] = (20, 150, 200)

#     time.sleep(.25)
