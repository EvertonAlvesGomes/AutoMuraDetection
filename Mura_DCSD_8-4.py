# 8.4" display mura detection algorithm

# Useful links:
# https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
# https://en.wikipedia.org/wiki/Relative_luminance
# https://pt.planetcalc.com/7779/ -> Relative Luminance Calculator
# https://www.w3schools.com/colors/colors_rgb.asp -> RGB Calculator
# GitHub repository: https://github.com/EvertonAlvesGomes/AutoMuraDetection



# Key takeaways:
# Resolução do display é diferente da resolução da foto capturada.
# Biblioteca Image é a mais apropriada.
# Equação encontrada é da luminância relativa, necessário descobrir como calcular
# luminância absoluta.

# Premissa: Resolution = 1200 x 920 (DCSD 8.4")

# -----------------------------------------------------------------------
# Imports

from PIL import Image


#------------
# Functions

# Calculates the relative luminance by given RGB' values
def relative_luminance(R_linha, G_linha, B_linha):
    return 0.2126*(R_linha**(2.2)) + 0.7152*(G_linha**(2.2)) + 0.0722*(B_linha**(2.2))


def getHexRGB(x, y):
    _pixels = img.load()
    rgb_tuple = _pixels[x, y]
    return hex('%02x%02x%02x' % rgb_tuple)

#------------
# Main scope

max_luminance_color = 0xFFFFFF #white color
min_luminance_color = 0x000000 #black color 
max_luminance_value = 5.5 #cd/m²
min_luminance_color = 0 #cd/m²


img = Image.open("Mura_8-4.png")  # loads the image from storage repository
pixels = img.load()  # loads all pixels

coordinate = x, y = 140, 40

Y_max = relative_luminance(1, 1, 1)  # max value / ref value

rgb = pixels[300,250]
vRGB = (rgb[0]/255, rgb[1]/255, rgb[2]/255)

print(f"RGB Values: {rgb}")
print(f"Linearized RGB: {vRGB}")

Y = relative_luminance(vRGB[0], vRGB[1], vRGB[2])

#Relative luminance:
print(f"Luminance Y: {Y}")

# Absolute luminance (cd/m²)
print(f"Luminance [cd/m²]= {Y*Y_max}")