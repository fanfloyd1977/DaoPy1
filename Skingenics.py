import time
import schedule

from pandas import pandas as pd

from random import randrange
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from linebot.models import ImageCarouselTemplate, ImageCarouselColumn

import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)

#Bot MsLee_DF
line_bot_api = LineBotApi("S7kS9QIa4TxHpyimmAXZfb2fvAfvP9twnuEKHOhitt28RFJT4U9sP4QLxbjM4Y7Z1gur1saRpYHRHNNqKj360akHQZmtmkuqmQEskx4GdSq1r5L2VA50ex5gA3VO1faeYDXTojf5IhhMlJg/q0gLTQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("353cd84bd7baec157b7499ef3e10fdcb")

#Goole sheet Key

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('fanfloyd1977-2bf294ca8a0e.json', scope)
client = gspread.authorize(creds)


#####################################################################################################


#Intent
greeting = ["Hello Hello","Hi Hi", "Hi", "Hi, there", "Good day", "สวัสดีครับ", "สวัสดีค่ะ ยินดีต้อนรับค่ะ"]
N = 1

@app.route("/")
def hello():
    return "Hello DAO Flask-Heroku"

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    #Intent greeting
    if event.message.text.lower() in [low.lower() for low in greeting]:
        value = randrange(0, len(greeting))
        reply_text = greeting[value]
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text))
    #Main Check Bill
    if event.message.text.lower() == "bill":
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet_instance = client.open("Booktwo")
        sheet = sheet_instance.get_worksheet(0)
        sheet1 = sheet_instance.get_worksheet(1)
        sum = 0
        num_row = sheet.col_values(1)
        row=len(num_row)
## Bill header
        Bill_bubble1 = BubbleContainer(
            direction='ltr',
            body=BoxComponent(
            layout="vertical",
            background_color= "#F9ED99",

                contents=[
                TextComponent(text="RECEIPT",weight="bold",size="md"),
                TextComponent(text="Cafe Camellia",weight="bold",size="lg"),
                TextComponent(text="Ladprao Street,3-9-2-8 Ladprao, Bangkok",weight="bold",size="xxs")
            ]))
        BB_message1 = FlexSendMessage(alt_text="Hello T_bubble", contents=Bill_bubble1)
        line_bot_api.push_message(profile.user_id,BB_message1)
## Bill Body
        for j in range(2,row+1):
            cus = sheet.row_values(j)
            if cus[7] == profile.user_id and cus[6] != "CHECKED":
                sheet.update_cell(j,7,"CHECKED")
                sum = sum + int(cus[3])
                bill_text = [TextSendMessage(text=cus[1] +"   "+ cus[2] +"         "+ cus[3]+ " BHT")]
                line_bot_api.push_message(profile.user_id, bill_text)
                sheet1.append_row(sheet.row_values(j))
                #sheet.delete_row(j)

## Bill Footer

        Bill_bubble2 = BubbleContainer(
            direction='ltr',
            body=BoxComponent(
                layout="baseline",
                background_color= "#F9ED99",
                contents=[
                    TextComponent(text="TOTAL : ",weight="bold",size="md",margin="sm"),
                    TextComponent(text=str(sum) + " BHT",weight="bold",size="md",margin="sm",align="end")

                ]))
        BB_message2 = FlexSendMessage(alt_text="Hello T_bubble", contents=Bill_bubble2)
        line_bot_api.push_message(profile.user_id,BB_message2)


#Main Table number
    if event.message.text.lower() == "table number":
        T_message = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://www.seekpng.com/png/detail/62-622544_clipart-numbers-polka-dot-cute-number-1-clipart.png',
                        size = "sm",
                        action=PostbackTemplateAction(
                        label='Table 1',
                        text='Table 1',
                        data='Table 1'
                    )
                ),
                    ImageCarouselColumn(
                        image_url='https://cdn2.vectorstock.com/i/1000x1000/98/76/hand-drawn-number-2-with-polka-dots-on-pastel-blue-vector-19159876.jpg',
                        size = "sm",
                        action=PostbackTemplateAction(
                        label='Table 2',
                        text='Table 2',
                        data='Table 2'
                    )
                ),
                    ImageCarouselColumn(
                        image_url='https://cdn2.vectorstock.com/i/1000x1000/98/91/hand-drawn-number-3-with-polka-dots-on-pastel-blue-vector-19159891.jpg',
                        size = "sm",
                        action=PostbackTemplateAction(
                        label='Table 3',
                        text='Table 3',
                        data='Table 3'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, T_message)



    #Main Menu

    if event.message.text.lower() == "menu":
        B_message = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://cdn.shopify.com/s/files/1/0463/7432/2326/products/gris_dior_1850x2000_e202a24d-57ef-413d-88bf-d816730e3c9e.jpg',
                        action=PostbackTemplateAction(
                            label='Gris',
                            text='Gris',
                            data='Gris'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://cdn.shopify.com/s/files/1/0463/7432/2326/products/Y0996414_E01_GHC.jpg',
                        action=PostbackTemplateAction(
                            label='Rosewood',
                            text='Rosewood',
                            data='Rosewood'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://cdn.shopify.com/s/files/1/0463/7432/2326/products/Y0996065_C099600577_E01_GHC_a2097cbc-72fb-4ad3-8e97-4ef73d13d18d.jpg',
                        action=PostbackTemplateAction(
                            label='Eden',
                            text='Eden',
                            data='Eden'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, B_message)



@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    if data == "Gris Regular":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Gris regular : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Gris_Regular_Row = [len(row),"Gris","Regular",2500,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Gris_Regular_Row)

    if data == "Gris Large":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Gris Large : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Gris_Large_Row = [len(row),"Gris","Large",4500,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Gris_Large_Row)


    if data == "Rosewood Regular":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Rosewood Regular : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Rosewood_Regular_Row = [len(row),"Rosewood","Regular",1000,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Rosewood_Regular_Row)

    if data == "Rosewood Large":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Rosewood Large : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Rosewood_Large_Row = [len(row),"Rosewood","Large",2000,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Rosewood_Large_Row)

    if data == "Eden Regular":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Eden Regular : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Eden_Regular_Row = [len(row),"Eden","Regular",1500,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Eden_Regular_Row)

    if data == "Eden Large":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Eden Large : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Eden_Large_Row = [len(row),"Eden","Large",2000,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Eden_Large_Row)


    if data == "Table 1":
        profileT = line_bot_api.get_profile(event.source.user_id)
        sheet_instance = client.open("Booktwo")
        sheet = sheet_instance.get_worksheet(1)
        row = sheet.col_values(1)
        Num_row = len(row)+1
        sheet.update_cell(Num_row,1,len(row))
        sheet.update_cell(Num_row,2,"Table 1")
        sheet.update_cell(Num_row,3,profileT.user_id)
        sheet.update_cell(Num_row,4,profileT.display_name)


    #Flex message

#Rosewood
    if data == "Rosewood":
        T_bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url="https://cdn.shopify.com/s/files/1/0463/7432/2326/products/Y0996414_E01_GHC.jpg",
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout="vertical",
                contents=[
                    TextComponent(text="Rosewood",weight="bold",size="xl"),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[

                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"),
                            TextComponent(text="1000 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="50 ml.",size="sm",color="#976608",margin="md",align="end")

                        ]
                    ),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[
                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"),
                            TextComponent(text="2000 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="100 ml.",size="sm",color="#976608",margin="md",align="end")

                        ]

                    ),
                    BoxComponent(
                        layout="vertical",margin="md",
                        contents=[TextComponent(text="Raspberry, Quince, Pickles, Sandalwood",size="xxs",color="#999999",margin="md"),]
                    )
                ]
            ),
            footer=BoxComponent(
                layout="vertical",spacing="sm",
                contents=[
                    ButtonComponent(
                        style="primary",
                        color= "#DFD805",
                        height="sm",
                        action=PostbackAction(label="REGULAR", data="Rosewood Regular")
                        # URIAction(label="ORDER",uri="tel:00000000")
                    ),
                    ButtonComponent(
                        style="primary",
                        color= "#DFD805",
                        height="sm",
                        action=PostbackAction(label="LARGE", data="Rosewood Large")
                    )


                ]
            )
        )

        message = FlexSendMessage(alt_text="Hello T_bubble", contents=T_bubble)
        line_bot_api.reply_message(event.reply_token,message)
#Gris
    if data == "Gris":
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url="https://cdn.shopify.com/s/files/1/0463/7432/2326/products/gris_dior_1850x2000_e202a24d-57ef-413d-88bf-d816730e3c9e.jpg",
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout="vertical",
                contents=[
                    TextComponent(text="Gris Dior",weight="bold",size="xl"),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[

                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"),
                            TextComponent(text="250 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="50 ml.",size="sm",color="#976608",margin="md",align="end")

                        ]
                    ),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[
                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"),
                            TextComponent(text="4500 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="100 ml.",size="sm",color="#976608",margin="md",align="end")

                        ]

                    ),
                    BoxComponent(
                        layout="vertical",margin="md",
                        contents=[TextComponent(text="Bergamot, Turkish rose, Patchouli, Amber",size="xxs",color="#999999",margin="md"),]
                    )
                ]
            ),
            footer=BoxComponent(
                layout="vertical",spacing="sm",
                contents=[
                    ButtonComponent(
                        style="primary",
                        color= "#905c44",
                        height="sm",
                        action=PostbackAction(label="REGULAR", data="Gris Regular")
                        # URIAction(label="ORDER",uri="tel:00000000")
                    ),
                    ButtonComponent(
                        style="primary",
                        color= "#905c44",
                        height="sm",
                        action=PostbackAction(label="LARGE", data="Gris Large")
                    )


                ]
            )
        )

        message = FlexSendMessage(alt_text="Hello Flex", contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
#Eden
    if data == "Eden":
        D_bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url="https://cdn.shopify.com/s/files/1/0463/7432/2326/products/Y0996065_C099600577_E01_GHC_a2097cbc-72fb-4ad3-8e97-4ef73d13d18d.jpg",
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout="vertical",
                contents=[
                    TextComponent(text="Eden",weight="bold",size="xl"),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[

                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"),
                            TextComponent(text="1500 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="50 ml.",size="sm",color="#976608",margin="md",align="end")

                        ]
                    ),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[
                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"),
                            TextComponent(text="2000 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="100 ml.",size="sm",color="#976608",margin="md",align="end")

                        ]

                    ),
                    BoxComponent(
                        layout="vertical",margin="md",
                        contents=[TextComponent(text="Sea Salt, Citruses, Jasmine, Mastic & Coconut",size="xxs",color="#999999",margin="md"),]
                    )
                ]
            ),
            footer=BoxComponent(
                layout="vertical",spacing="sm",
                contents=[
                    ButtonComponent(
                        style="primary",
                        color= "#F98A76",
                        height="sm",
                        action=PostbackAction(label="REGULAR", data="Eden Regular")
                        # URIAction(label="ORDER",uri="tel:00000000")
                    ),
                    ButtonComponent(
                        style="primary",
                        color= "#F98A76",
                        height="sm",
                        action=PostbackAction(label="LARGE", data="Eden Large")
                    )


                ]
            )
        )

        message = FlexSendMessage(alt_text="Hello Flex", contents=D_bubble)
        line_bot_api.reply_message(event.reply_token,message)
