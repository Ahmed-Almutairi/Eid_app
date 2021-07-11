from flask import Flask, flash, jsonify, render_template, request, send_file
from PIL import Image, ImageFont, ImageDraw
from bidi.algorithm import get_display
import arabic_reshaper
import re



app = Flask(__name__)

@app.route('/')
def route_page():
    return render_template('index.html')

@app.route('/' , methods=['POST'])
def getCard():
    #    Happy-Eid-2020-2
    
    title_text = request.form["name"]
    

    reg = re.compile(r'[a-zA-Z]')
    
    my_image = Image.open("Happy-Eid-2021.png")
    title_font = ImageFont.truetype('Amiri-Regular.ttf', 60)
    image_editable = ImageDraw.Draw(my_image)
    
    if reg.match(title_text[0]):
        image_editable.text((530-(len(title_text)*13),1090), title_text, (255, 255, 255), font=title_font)
    else:
        reshaped_text = arabic_reshaper.reshape(title_text)
        bidi_text = reshaped_text[::-1]
        image_editable.text((530-(len(bidi_text)*10),1090), bidi_text, (255, 255, 255), font=title_font)
    full_filename= my_image.save("result.png")
    # my_image.show()
    return send_file("result.png",as_attachment=True)



