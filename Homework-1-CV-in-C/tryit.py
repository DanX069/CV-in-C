from uwimg import *

# 1. Getting and setting pixels
im = load_image("data/self.jpg")
for row in range(im.h):
    for col in range(im.w):
        set_pixel(im, col, row, 0, 0)
save_image(im, "self_no_red")

# 1.1. Getting and setting pixels
im = load_image("data/self.jpg")
for row in range(im.h):
    for col in range(im.w):
        set_pixel(im, col, row, 1, 0)
save_image(im, "self_no_green")

# 1.2. Getting and setting pixels
im = load_image("data/self.jpg")
for row in range(im.h):
    for col in range(im.w):
        set_pixel(im, col, row, 2, 0)
save_image(im, "self_no_blue")


# 2.1. Grayscale image transform
im = load_image("data/self.jpg")
graydog = rgb_to_grayscale(im)
save_image(graydog, "self_gray")


# 3. Shift Image
im = load_image("data/self.jpg")
shift_image(im, 0, .4)
shift_image(im, 1, .4)
shift_image(im, 2, .4)
save_image(im, "self_overflow")


# 4. Clamp Image
clamp_image(im)
save_image(im, "self_light_fixed")

# 6-7. Colorspace and saturation
im = load_image("data/self.jpg")
rgb_to_hsv(im)
shift_image(im, 1, .2)
clamp_image(im)
hsv_to_rgb(im)
save_image(im, "self_saturated")