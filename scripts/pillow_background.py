from PIL import Image


# 创建一个图片对象, not me its github copliet joy
for _ in range(604):
    img = Image.open(f'../images/{_+1}.png')
    background = Image.new(mode="RGB", size=(img.width, img.height))
    background.paste(img.copy(), (0, 0, img.width, img.height))
    background.save(f'../imgs/{_+1}.png')
