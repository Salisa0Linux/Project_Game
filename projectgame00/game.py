from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio.session import *
app = Flask(__name__)


def game():

    c = 0

    put_html("<h1>เขามีใจให้คุณหรือเปล่า</h1>", 'color:pink;')

    # input name in english to play
    name = input("เกมนี้ทำขึ้นเพื่อความสนุกเท่านั้น หากต้องการเริ่มเล่นโปรดพิมพ์ชื่อเพื่อเริ่มเกม",
                 type="text", validate=validate_name)
    # use radio to make question
    q1 = radio("Q1.เขามองและสบตาคุณ เมื่อคุณจับได้ว่าเขามองเขาพยายามหลบตา", [
               'เขามองฉันเสมอ หันไปทีไรก็สบตา', 'เขามองฉัน แต่ก็มองไปทางอื่นด้วย', 'เขามองฉัน แต่ก็มองคนอื่นด้วยเหมือนกัน', 'เขาคงซ่อนเความรู้สึก เขามองฉันแค่แปปเดียว'])
    if q1 == 'เขามองฉันเสมอ หันไปทีไรก็สบตา':
        c += 4
    elif q1 == 'เขามองฉัน แต่ก็มองไปทางอื่นด้วย':
        c += 3
    elif q1 == 'เขามองฉัน แต่ก็มองคนอื่นด้วยเหมือนกัน':
        c += 2
    elif q1 == 'เขาคงซ่อนเความรู้สึก เขามองฉันแค่แปปเดียว':
        c += 1

    q2 = radio("Q2.เมื่อได้ยินเรื่องตลก เขาจะหันมามองที่คุณ", [
               'ใช่ เหมือนเขาต้องการให้ฉันสนุกไปพร้อมกับเขา', 'เขามองไปที่ผู้หญิงคนอื่น', 'เขาหัวเราะกับตัวเอง ไม่ได้มองใคร', 'เขามองไปที่ผู้พูด'])
    if q2 == 'ใช่ เหมือนเขาต้องการให้ฉันสนุกไปพร้อมกับเขา':
        c += 4
    elif q2 == 'เขามองไปที่ผู้หญิงคนอื่น':
        c += 3
    elif q2 == 'เขาหัวเราะกับตัวเอง ไม่ได้มองใคร':
        c += 2
    elif q2 == 'เขามองไปที่ผู้พูด':
        c += 1

    q3 = radio("Q3.เมื่อมีงานกลุ่มเขาจะเลือกคุณเข้ากลุ่มใช่ไหม", [
               'เขาเลือกฉันเสมอ', 'เขาชอบทำงานคนเดียว แต่ถ้าใครขอเข้ากลุ่มเขาก็รับ', 'เขาเลือกเพื่อนในกลุ่มของเขา', 'เขาเลือกผู้หญิงอื่น'])
    if q3 == 'เขาเลือกฉันเสมอ':
        c += 4
    elif q3 == 'เขาชอบทำงานคนเดียว แต่ถ้าใครขอเข้ากลุ่มเขาก็รับ':
        c += 3
    elif q3 == 'เขาเลือกเพื่อนในกลุ่มของเขา':
        c += 2
    elif q3 == 'เขาเลือกผู้หญิงอื่น':
        c += 1

    q4 = radio("Q4.ดวงตาของเขาดูโตเป็นประกาย และเขาทำตัวแตกต่างไปจากปกติเมื่อคุณอยู่ใกล้ๆ", [
               'แววตาของเขาเป็นประกาย เสียงและการกระทำของเขาดูอ่อนโยนกว่าปกติ', 'ดวงตาของเขาเป็นประกาย แต่เขาก็เป็นแบบนี้กับคนอื่นๆเหมือนกัน', 'ฉันไม่เคยอยู่ใกล้พอที่จะสบตา และสังเกตเขา', 'ฉันไม่รู้ว่าเขาทำตัวต่างไปจากปกติหรือเปล่า'])
    if q4 == 'แววตาของเขาเป็นประกาย เสียงและการกระทำของเขาดูอ่อนโยนกว่าปกติ':
        c += 4
    elif q4 == 'ดวงตาของเขาเป็นประกาย แต่เขาก็เป็นแบบนี้กับคนอื่นๆเหมือนกัน':
        c += 3
    elif q4 == 'ฉันไม่เคยอยู่ใกล้พอที่จะสบตา และสังเกตเขา':
        c += 2
    elif q4 == 'ฉันไม่รู้ว่าเขาทำตัวต่างไปจากปกติหรือเปล่า':
        c += 1

    q5 = radio("Q5.เขาชอบชวนคุณคุยเวลาคุณออนไลน์ทางโซเชียล", [
               'เขาโทรหรือส่งข้อความหาฉันทุกวัน', 'เขาโทรหรือส่งข้อความมาบางครั้ง', 'เขาโทรหรือส่งข้อความเมื่อเขามีธุระเท่านั้น', 'เขาโทรหรือส่งข้อความเพื่อมาขอยืมเงิน'])
    if q5 == 'เขาโทรหรือส่งข้อความหาฉันทุกวัน':
        c += 4
    elif q5 == 'เขาโทรหรือส่งข้อความมาบางครั้ง':
        c += 3
    elif q5 == 'เขาโทรหรือส่งข้อความเมื่อเขามีธุระเท่านั้น':
        c += 2
    elif q5 == 'เขาโทรหรือส่งข้อความเพื่อมาขอยืมเงิน':
        c += 1

    q6 = radio("Q6.คุณคุยกันยาวไหม", ['เขาโทรคุยกับฉันตั้งแต่หัวค่ำจนถึงเข้ามืดอีกวัน', 'คุยยาวนะ แต่เขาก็คุยกับคนอื่นยาวเหมือนกัน',
               'เขาคุยกับฉัน เฉพาะตอนไม่มีเพื่อนคุยหรือมีธุระเท่านั้น', 'ยังไม่เคยคุยกันยาวเลย เขาไม่ว่าง ฉันก็ไม่ว่าง'])
    if q6 == 'เขาโทรคุยกับฉันตั้งแต่หัวค่ำจนถึงเข้ามืดอีกวัน':
        c += 4
    elif q6 == 'คุยยาวนะ แต่เขาก็คุยกับคนอื่นยาวเหมือนกัน':
        c += 3
    elif q6 == 'เขาคุยกับฉัน เฉพาะตอนไม่มีเพื่อนคุยหรือมีธุระเท่านั้น':
        c += 2
    elif q6 == 'ยังไม่เคยคุยกันยาวเลย เขาไม่ว่าง ฉันก็ไม่ว่าง':
        c += 1

    q7 = radio("Q7.เขาจำวันสำคัญของคุณได้", ['เขาอวยพรวันเกิดฉันทุกปี ตั้งแต่รู้จักกันมา',
               'เขาอวยพรวันเกิดฉัน เมื่อเห็นเพื่อนคนอื่นอวยพรผ่านไป 1-2 วัน', 'ไม่รู่สิ! เขาคงไม่ให้ความสำคัญกับเรื่องเล็กน้อย', 'ฉันคิดว่าเขาเป็นคนขี้ลืม'])
    if q7 == 'เขาอวยพรวันเกิดฉันทุกปี ตั้งแต่รู้จักกันมา':
        c += 4
    elif q7 == 'เขาอวยพรวันเกิดฉัน เมื่อเห็นเพื่อนคนอื่นอวยพรผ่านไป 1-2 วัน':
        c += 3
    elif q7 == 'ไม่รู่สิ เขาคงไม่ให้ความสำคัญกับเรื่องเล็กน้อย':
        c += 2
    elif q7 == 'ฉันคิดว่าเขาเป็นคนขี้ลืม':
        c += 1

    q8 = radio("Q8.เขาพูดกับคนอื่นถึงคุณบ่อย", ['ใช่ เขาพูดถึงและชมฉันบ่อยๆ มีหลายคนบอกอย่างนั้น',
               'เขามักจะพูดถึงทุกคนในกลุ่มเพื่อนของเขา', 'เขาพูดล้อเลียนฉัน ไม่เคยพูดชมเลย', 'ไม่รู้เลยอะ ฉันไม่เคยถาม'])
    if q8 == 'ใช่ เขาพูดถึงและชมฉันบ่อยๆ มีหลายคนบอกอย่างนั้น':
        c += 4
    elif q8 == 'เขามักจะพูดถึงทุกคนในกลุ่มเพื่อนของเขา':
        c += 3
    elif q8 == 'เขาพูดล้อเลียนฉัน ไม่เคยพูดชมเลย':
        c += 2
    elif q8 == 'ไม่รู้เลยอะ ฉันไม่เคยถาม':
        c += 1

    q9 = radio("Q9.เพื่อนคนอื่นๆล้อเขา ว่าแอบชอบคุณ", [
               'ได้ยินบ่อยมากๆ', 'เขาถูกล้อว่าชอบคนอื่นเหมือนกัน', 'เขาถูกล้อว่าชอบคนอื่น แต่ไม่เคยถูกล้อว่าชอบฉัน', 'ไม่เคยได้ยินเลยนะ'])
    if q9 == 'ได้ยินบ่อยมากๆ':
        c += 4
    elif q9 == 'เขาถูกล้อว่าชอบคนอื่นเหมือนกัน':
        c += 3
    elif q9 == 'เขาถูกล้อว่าชอบคนอื่น แต่ไม่เคยถูกล้อว่าชอบฉัน':
        c += 2
    elif q9 == 'ไม่เคยได้ยินเลยนะ':
        c += 1

    q10 = radio("Q10.คุณมีความรู้สึกว่าเขาชอบคุณหรือไม่", [
                'ฉันแน่ใจว่าเขาชอบฉัน', 'บางทีอาจจะ 50-50', 'ไม่แน่ใจ บอกไม่ได้เลย', 'ฉันคิดว่าไม่แน่นอน'])
    if q10 == 'ฉันแน่ใจว่าเขาชอบฉัน':
        c += 4
    elif q10 == 'บางทีอาจจะ 50-50':
        c += 3
    elif q10 == 'ไม่แน่ใจ บอกไม่ได้เลย':
        c += 2
    elif q10 == 'ฉันคิดว่าไม่แน่นอน':
        c += 1

    # count score and show the result
    if c > 27:
        message = [style(put_html("<h2 style='display:inline;border-radius:0px'>Congratulations !!  " + "</h2>" + ", your score is <b>" + str(c) + "</b><br><br>"), 'color:blue;'),
                   style(put_html(
                       "<p> Result : <b>เขากำลังหลงรักคุณ ลองรวบรวมความกล้าไปสารภาพรักดู คุณมีแววที่จะสละโสดเร็วๆนี้นะ><</b></p>"), 'color:black'),
                   put_html(
                       "<br><b>Thank You for your participation.</b><br><br>", 'color:red;'),
                   style(put_link('Retry ↺', ""), 'color:red;align-content: center;border-radius: 5px;color:#f9faf8;padding: 5px 100px;text-align:center;align-items : center;background-color: dark;\
            background-image: linear-gradient(270deg, #8cf5f5 1%, #0a43f3 100%);')]
    elif 14 < c < 28:
        message = [style(put_html("<h2 style='display:inline;border-bottom:0px'>50-50  " + "</h2>" + ", your score is <b>" + str(c) + "</b><br><br>"), 'color:blue;'),
                   style(put_html(
                       "<p>Result : <b>เขาก็สนใจคุณนะ แต่ก็สนใจคนอื่นอยู่ด้วยเช่นกัน ลองจีบเขาดูก่อนถ้าเขามีใจเขาจะมาสนใจแค่คุณคนเดียว</b></p>"), 'color:black;'),
                   put_html(
                       "<br><b>Thank You for your participation.</b><br><br>", 'color:red;'),
                   style(put_link('Retry ↺', ""), 'color:red;align-content: center;border-radius: 5px;color:#f9faf8;padding: 5px 100px;text-align:center;align-items : center;background-color: dark;\
            background-image: linear-gradient(270deg, #8cf5f5 1%, #0a43f3 100%);')]
    elif c < 14:
        message = [style(put_html("<h2 style='display:inline;border-bottom:0px'>เสียใจด้วยนะ  " + "</h2>" + ", your score is <b>" + str(c) + "</b><br><br>"), 'color:blue;'),
                   style(put_html("<p>Result : <b>เขาไม่ได้สนใจคุณเลย คุณอาจเป็นได้แค่เพื่อนหรือคนรู้จักที่ดีของเขาเท่านั้น</b></p>"),
                         'color:black;'),
                   put_html(
                       "<br><b>Thank You for your participation.</b><br><br>", 'color:red;'),
                   style(put_link('Retry ↺', ""), 'color:red;align-content: center;border-radius: 5px;color:#f9faf8;padding: 5px 100px;text-align:center;align-items : center;background-color: dark;\
            background-image: linear-gradient(270deg, #8cf5f5 1%, #0a43f3 100%);')]


"""A method to validate the name entered by user"""


def validate_name(name):
    # removing all spaces from the input name
    name = name.replace(" ", "")
    # It should contain only alphabets [a-z] or [A-Z]
    if(name == "" or not(name.isalpha())):
        return("Please enter a non empty name consisting of alphabets only")


app.add_url_rule('/', 'webio_view', webio_view(game),
                 methods=['GET', 'POST', 'OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port=8080)