from colorthief import ColorThief
import matplotlib.pyplot as plt


ct = ColorThief("hacker_2.jpg")
dom_color = ct.get_color(quality=1)

plt.imshow([[dom_color]])
plt.show()

palete = ct.get_palette(color_count=5)
plt.imshow([[palete[i] for i in range(5)]])
plt.show()
