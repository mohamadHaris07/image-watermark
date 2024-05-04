from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image, output_image, text):
    org_img = Image.open(input_image)
    water_mrk_img = Image.new("RGBA", org_img.size)
    water_mrk_drow = ImageDraw.Draw(water_mrk_img)
    fond = ImageFont.truetype('arial.ttf', 100)
    width, height = org_img.size
    water_mrk_drow.text((0, height/2), text=text, fill=(255,255,255,140), font=fond )
    
    
    water_mrk_img = Image.alpha_composite(im1=org_img.convert("RGBA"), im2=water_mrk_img)
    water_mrk_img.save(output_image,'PNG')
    print("image generated...!")



input_image = 'haris.png.jpg'
output_image = 'output.png'
text = input("enter your text: ")

add_watermark(input_image, output_image, text)