# 8.4" display mura detection algorithm

# Useful links:
# https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
# https://en.wikipedia.org/wiki/Relative_luminance

# Key takeaways:
# Resolução do display é diferente da resolução da foto capturada.
# Biblioteca Image é a mais apropriada.
# Equação encontrada é da luminância relativa, necessário descobrir como calcular
# luminância absoluta.
# -----------------------------------------------------------------------

from PIL import Image

def relative_luminance(R_linha, G_linha, B_linha):
    return 0.2126*(R_linha**(2.2)) + 0.7152*(G_linha**(2.2)) + 0.0722*(B_linha**(2.2))


img = Image.open("Mura_8-4.png")  # loads the image from storage repository
pixels = img.load()  # loads all pixels

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