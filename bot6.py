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
line_bot_api = LineBotApi("x2MD95t6bBSriSsgtAZyD5EyrTNV6SXJ7NHiFycxf5H8zXHqlzNOpqrsgcmaM0GQfn/3j1M1iXKEPheCEBWf0fy2zq8EaxaGqUGEFY5y1tdziMyeG4ar2RjFWyW95zZG2nR8aE4ZcF34QEhm+VsEMwdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("e36bb9a122463a52533753aa1f2bed40")

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
                        image_url='https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png',
                        action=PostbackTemplateAction(
                            label='Ham Burger',
                            text='Ham Burger',
                            data='Ham Burger'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://images-gmi-pmc.edge-generalmills.com/e59f255c-7498-4b84-9c9d-e578bf5d88fc.jpg',
                        action=PostbackTemplateAction(
                            label='Taco',
                            text='Taco',
                            data='Taco'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://media3.s-nbcnews.com/i/newscms/2020_27/1586837/hotdogs-te-main-200702_1e1ea98797356fd7f729a2b294d7bb26.jpg',
                        action=PostbackTemplateAction(
                            label='Hotdog',
                            text='Hotdog',
                            data='Hotdog'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, B_message)



@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    if data == "Ham Regular":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Ham Regular : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Ham_Regular_Row = [len(row),"Hamburger","Regular",250,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Ham_Regular_Row)

    if data == "Ham Large":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Ham Large : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Ham_Large_Row = [len(row),"Hamburger","Large",450,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Ham_Large_Row)


    if data == "Taco Regular":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Taco Regular : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Taco_Regular_Row = [len(row),"Taco","Regular",100,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Taco_Regular_Row)

    if data == "Taco Large":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Taco Large : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Taco_Large_Row = [len(row),"Taco","Large",200,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Taco_Large_Row)

    if data == "Hotdog Regular":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Hotdog Regular : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Hot_Regular_Row = [len(row),"Hotdog","Regular",150,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Hot_Regular_Row)

    if data == "Hotdog Large":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Hotdog Large : Submitted"))
        profile = line_bot_api.get_profile(event.source.user_id)
        sheet = client.open("Booktwo").sheet1
        row = sheet.col_values(1)
        Hot_Large_Row = [len(row),"Hotdog","Large",200,1,profile.display_name,"New",profile.user_id]
        sheet.append_row(Hot_Large_Row)


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

#Taco
    if data == "Taco":
        T_bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url="https://images-gmi-pmc.edge-generalmills.com/e59f255c-7498-4b84-9c9d-e578bf5d88fc.jpg",
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout="vertical",
                contents=[
                    TextComponent(text="Taco",weight="bold",size="xl"),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[

                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"),
                            TextComponent(text="100 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="450 kcl",size="sm",color="#976608",margin="md",align="end")

                        ]
                    ),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[
                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"),
                            TextComponent(text="200 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="750 kcl",size="sm",color="#976608",margin="md",align="end")

                        ]

                    ),
                    BoxComponent(
                        layout="vertical",margin="md",
                        contents=[TextComponent(text="Sauce, Onions, Pickles, lettuce & Cheese",size="xxs",color="#999999",margin="md"),]
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
                        action=PostbackAction(label="REGULAR", data="Taco Regular")
                        # URIAction(label="ORDER",uri="tel:00000000")
                    ),
                    ButtonComponent(
                        style="primary",
                        color= "#DFD805",
                        height="sm",
                        action=PostbackAction(label="LARGE", data="Taco Large")
                    )


                ]
            )
        )

        message = FlexSendMessage(alt_text="Hello T_bubble", contents=T_bubble)
        line_bot_api.reply_message(event.reply_token,message)
#Ham Burger
    if data == "Ham Burger":
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png",
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout="vertical",
                contents=[
                    TextComponent(text="Ham Burger",weight="bold",size="xl"),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[

                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"),
                            TextComponent(text="250 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="450 kcl",size="sm",color="#976608",margin="md",align="end")

                        ]
                    ),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[
                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"),
                            TextComponent(text="450 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="750 kcl",size="sm",color="#976608",margin="md",align="end")

                        ]

                    ),
                    BoxComponent(
                        layout="vertical",margin="md",
                        contents=[TextComponent(text="Sauce, Onions, Pickles, lettuce & Cheese",size="xxs",color="#999999",margin="md"),]
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
                        action=PostbackAction(label="REGULAR", data="Ham Regular")
                        # URIAction(label="ORDER",uri="tel:00000000")
                    ),
                    ButtonComponent(
                        style="primary",
                        color= "#905c44",
                        height="sm",
                        action=PostbackAction(label="LARGE", data="Ham Large")
                    )


                ]
            )
        )

        message = FlexSendMessage(alt_text="Hello Flex", contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
#Hotdog
    if data == "Hotdog":
        D_bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url="https://media3.s-nbcnews.com/i/newscms/2020_27/1586837/hotdogs-te-main-200702_1e1ea98797356fd7f729a2b294d7bb26.jpg",
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout="vertical",
                contents=[
                    TextComponent(text="Hotdog",weight="bold",size="xl"),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[

                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"),
                            TextComponent(text="150 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="450 kcl",size="sm",color="#976608",margin="md",align="end")

                        ]
                    ),
                    BoxComponent(
                        layout="baseline",margin="md",
                        contents=[
                            IconComponent(size="sm",url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"),
                            TextComponent(text="200 BHT",size="sm",color="#976608",margin="md"),
                            TextComponent(text="750 kcl",size="sm",color="#976608",margin="md",align="end")

                        ]

                    ),
                    BoxComponent(
                        layout="vertical",margin="md",
                        contents=[TextComponent(text="Sauce, Onions, Pickles, lettuce & Cheese",size="xxs",color="#999999",margin="md"),]
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
                        action=PostbackAction(label="REGULAR", data="Hotdog Regular")
                        # URIAction(label="ORDER",uri="tel:00000000")
                    ),
                    ButtonComponent(
                        style="primary",
                        color= "#F98A76",
                        height="sm",
                        action=PostbackAction(label="LARGE", data="Hotdog Large")
                    )


                ]
            )
        )

        message = FlexSendMessage(alt_text="Hello Flex", contents=D_bubble)
        line_bot_api.reply_message(event.reply_token,message)