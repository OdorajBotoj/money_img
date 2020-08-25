# -*- coding:utf-8 -*-
#by:Odoraj_Botoj
__author__ = 'Odoraj_Botoj'
#仅供娱乐.

from PIL import Image as img
from time import sleep
from random import choice

colours = [(45, 28, 77), (53, 83, 134), (61, 103, 86), (62, 86, 59), (62, 104, 160), (65, 68, 69), (69, 48, 47), (70, 119, 109), (74, 97, 92), (77, 52, 52), (77, 88, 76), (79, 119, 100), (80, 145, 192), (80, 154, 128), (81, 113, 119), (84, 60, 79), (89, 70, 117), (89, 71, 61), (99, 68, 89), (104, 78, 148), (106, 133, 91), (110, 86, 85), (118, 221, 234), (120, 80, 89), (126, 141, 122), (141, 75, 69), (146, 82, 60), (148, 210, 239), (154, 123, 129), (160, 93, 70), (162, 172, 158), (167, 212, 195), (175, 154, 139), (176, 206, 149), (177, 134, 163), (186, 221, 233), (187, 214, 157), (190, 15, 45), (203, 54, 74), (203, 206, 193), (206, 172, 179), (207, 39, 60), (207, 227, 239), (213, 95, 111), (213, 192, 207), (219, 168, 128), (220, 207, 192), (223, 231, 215), (227, 199, 197), (231, 221, 184), (235, 64, 53), (240, 201, 134), (241, 224, 220), (245, 171, 183)]
hex_colours = ['#2D1C4D', '#355386', '#3D6756', '#3E563B', '#3E68A0', '#414445', '#45302F', '#46776D', '#4A615C', '#4D3434', '#4D584C', '#4F7764', '#5091C0', '#509A80', '#517177', '#543C4F', '#594675', '#59473D', '#634459', '#684E94', '#6A855B', '#6E5655', '#76DDEA', '#785059', '#7E8D7A', '#8D4B45', '#92523C', '#94D2EF', '#9A7B81', '#A05D46', '#A2AC9E', '#A7D4C3', '#AF9A8B', '#B0CE95', '#B186A3', '#BADDE9', '#BBD69D', '#BE0F2D', '#CB364A', '#CBCEC1', '#CEACB3', '#CF273C', '#CFE3EF', '#D55F6F', '#D5C0CF', '#DBA880', '#DCCFC0', '#DFE7D7', '#E3C7C5', '#E7DDB8', '#EB4035', '#F0C986', '#F1E0DC', '#F5ABB7']

def RGB_TO_HEX(rgb):
    rgb = str(rgb).lstrip('(').rstrip(')')
    RGB = rgb.split(',')
    color = '#'
    for i in RGB:
        num = int(i)
        color += str(hex(num))[-2:].replace('x', '0').upper()
    return color

def HEX_TO_RGB(hrgb):
    hrgb = hrgb.lstrip('#')
    tmp1 = int(hrgb[0:2],16)
    tmp2 = int(hrgb[2:4],16)
    tmp3 = int(hrgb[4:],16)
    return (tmp1,tmp2,tmp3)

def comparison(r,g,b,hc):
    rgb = RGB_TO_HEX((r,g,b))
    for i in hc:
        if rgb == i:
            return rgb
        else:
            pass
    hc.append(rgb)
    hc.sort()
    if hc.index(rgb) == 0:
        return hc[1]
    elif hc.index(rgb) == len(hc)-1:
        return hc[len(hc)-2]
    else:
        pass
    tmp1 = hc.index(rgb) - 1
    tmp2 = hc.index(rgb) + 1
    n_tmp1 = int('0x'+hc[tmp1].lstrip('#'),16)
    n_rgb = int('0x'+hc[hc.index(rgb)].lstrip('#'),16)
    n_tmp2 = int('0x'+hc[tmp2].lstrip('#'),16)
    if n_rgb - n_tmp1 > n_tmp2 - n_rgb:
        return '#'+str(hex(n_tmp2)).lstrip('0x')
    elif n_rgb - n_tmp1 < n_tmp2 - n_rgb:
        return '#'+str(hex(n_tmp1)).lstrip('0x')
    else:
        ch = choice([n_tmp1,n_tmp2])
        return '#'+str(hex(ch)).lstrip('0x')

if __name__ == '__main__':
    p = img.open(input('请输入bmp图片位置>>>'))
    np = img.new('RGB',p.size,0x0)
    for i in range(p.size[0]-1):
        for j in range(p.size[1]-1):
            r,g,b = p.getpixel((i,j))
            nrgb = comparison(r,g,b,hex_colours.copy())
            np.putpixel((i,j), HEX_TO_RGB(nrgb))
    np.save('out.bmp')
    print('转换完成!10秒后退出...')
    sleep(10)
    exit()