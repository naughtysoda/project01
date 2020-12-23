from django.shortcuts import render
from .models import StaffProfile,CollectStar,CollectStaff
from .serializers import StaffProfileSerializer,CollectStarSerializer,CollectStaffSerializer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

# def home(request):
#     # boards = StaffProfile.objects.all()
#     boards = print("555555555")
#     return render(request, 'home.html')

class LineMessage(APIView):
    line_channel_access_token = 'gZs8qYExxlcL5IrtPaGvqhOpOsIGNhfkSOIFChBfnd2mwg+xJ6jll4zZGFU7z4qfsvVpYlPa1ZlCLwQ5X52K4CpWMvBpgDHtT11T2OCYtM7dkjCTRzK/4IkpQ/BpfjwUiBAp5Y38aL/GMFMehuSwTFGUYhWQfeY8sLGRXgo3xvw='
    Authorization = "Bearer {}".format(line_channel_access_token)

    def get(self, request, *args, **kw):
        result = {"result": 'GET Testing'}
        print("get method called")
        response = Response(result, status.HTTP_200_OK)
        return response

    def reply_menu(self,reply_token):
        print('from reply menu')
        print("Authorization:{}".format(Authorization))
        print("reply_token:{}".format((reply_token)))

        # line_bot_api.reply_message(reply_token, TextSendMessage(text='Hello World222!'))

        response = requests.post(
            url="https://api.line.me/v2/bot/message/reply",
            headers={
                "Content-Type": "application/json",
                "Authorization": Authorization,
            },
            data=json.dumps({
                "replyToken": str(reply_token),
                "messages": [
                    {
                      {
                          "type": "flex",
                          "altText": "Flex Message",
                          "contents": {
                            "type": "bubble",
                            "direction": "ltr",
                            "hero": {
                              "type": "image",
                              "url": "https://som501103.github.io/electrician (1).png",
                              "size": "full",
                              "aspectRatio": "1.51:1",
                              "aspectMode": "fit"
                            },
                            "body": {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "ระบบแจ้งเตือนข้อมูลไฟฟ้าขัดข้อง",
                                  "flex": 1,
                                  "size": "lg",
                                  "align": "center",
                                  "gravity": "center",
                                  "color": "#413F3E"
                                }
                              ]
                            },
                            "footer": {
                              "type": "box",
                              "layout": "horizontal",
                              "contents": [
                                {
                                  "type": "button",
                                  "action": {
                                    "type": "message",
                                    "label": "ลงทะเบียน",
                                    "text": "ลงทะเบียน"
                                  }
                                }
                              ]
                            }
                          }
                        }
                    }
                ]
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

    def post(self, request, *args,  **kw):
        print(">>>>>>>>>>>>>>>>>>> debug : POST 0 <<<<<<<<<<<<<<<<<<<<")
        # signature = request.headers['X-Line-Signature']
        # print("signature: {}".format(signature))
        body = json.loads(request.body.decode('utf-8'))
        print("body: {}".format(request.body))
        reply_token = body['events'][0]['replyToken']
        userId = body['events'][0]['source']['userId']
        print("reply_token: {}".format(reply_token))
        event_type = body['events'][0]['type']
        print("event_type: {}".format(event_type))
        message_type = body['events'][0]['message']['type']
        print("message_type: {}".format(message_type))
        Lineinfo = []

        if event_type == "message":
            text_staffid = body['events'][0]['message']['text']


            print("text_staffid: {}".format(text_staffid))
            Lineinfo.append(format(text_staffid))
            if text_staffid != "yes":
                if  (text_staffid == "1") or (text_staffid == "2") or (text_staffid == "3"):
                    text = body['events'][0]['message']['text']
                    print("text: {}".format(text))
                    self.reply_message(reply_token, text)
                    Lineinfo.append(format(text))
                    uid = body['events'][0]['source']['userId']
                    Profile.objects.filter(uid=uid).update(position=text)

                else:
                    text_confirm = body['events'][0]['message']['text']
                    print("text_staffid: {}".format(text_confirm))
                    self.menu1(reply_token,text_confirm)
                    Lineinfo.append(format(text_confirm))
                    uid = body['events'][0]['source']['userId']
                    print("uid: {}".format(uid))
                    add_data = Profile(peaid=text_confirm,uid=uid)
                    add_data.save()
                    # self.menu3(reply_token)
            elif text_staffid == "yes":
                text_staffgroup = body['events'][0]['message']['text']
                print("text_staffgroup: {}".format(text_staffgroup))
                self.menu2(reply_token)
                Lineinfo.append(format(text_staffgroup))


                # update = Profile.objects.get(uid=uid)
                # update.position = text_staffgroup
                # update.save()

                # add_data = Profile(uid=uid,position=text_staffgroup)
                # add_data.save()

        # print(Lineinfo)
        # add_data = Profile(peaid="501103", uid="ddddddddddd", position="1")
        # add_data.save()

            # self.reply_menu(reply_token)



        # try :
        #     signature = request.headers['X-Line-Signature']
        #     body = request.get_data(as_text=True)
        # logger.info("Request body: " + body)
        # body = json.loads(body)
        # print (body)
        # reply_token = body['events'][0]["replyToken"]
        # print("reply_token: {}".format(reply_token))
        #
        # event_type = body['events'][0]['type']

        # reply_menu(reply_token)
        #
        # if event_type == "message":
        #     message_type = body['events'][0]['message']['type']
        #     # print("message_type: {}".format(message_type))
        #     if message_type == "flex":
        #         text = body['events'][0]['message']['text']
        #         print("text: {}".format(text))
        #         reply_menu(reply_token)
        #         if "ลงทะเบียน" in text or "ลงทะเบียน" in text:
        #             print("replying text:{}".format(text))
        #             reply_menu(reply_token)
                # elif text == "weather":
                #     line_bot_api.reply_message(reply_token, TextSendMessage(text='ท่านได้สมัครเข้าใช้งานแล้ว'))
                # elif text == "energy":
                #     line_bot_api.reply_message(reply_token, TextSendMessage(text='ท่านได้ยกเลิกการสมัคร'))
            # return Response({'success' : True, 'method' : "POST"}, status=status.HTTP_200_OK)
        # except Exception as err :
        #     # return Response({'success' : True, 'method' : "POST"}, status=status.HTTP_200_OK)
        #     print(err)
        #     return Response({'success' : True, 'method' : "POST"}, status=status.HTTP_200_OK)


        return Response({'success' : True, 'method' : "POST"}, status=status.HTTP_200_OK)

    def menu1(self, reply_token,text):
        print(">>>>>>>>>>>>>>>>>>> debug : menu1 <<<<<<<<<<<<<<<<<<<<")

        response = requests.post(
            url="https://api.line.me/v2/bot/message/reply",
            headers={
                "Content-Type": "application/json",
                "Authorization": Authorization,
            },
            data=json.dumps({
                "replyToken": str(reply_token),
                "messages": [
                {
                  "type": "template",
                  "altText": "this is a confirm template",
                  "template": {
                    "type": "confirm",
                    "actions": [
                      {
                        "type": "message",
                        "label": "ใช่",
                        "text": "yes"
                      },
                      {
                        "type": "message",
                        "label": "ไม่ใช่",
                        "text": "No"
                      }
                    ],
                    "text": "ยืนยันรหัสพนักงาน :"+str(text)
                  }
                }
                ]
            })
        )

    def menu2(self, reply_token):
        print(">>>>>>>>>>>>>>>>>>> debug : menu2 <<<<<<<<<<<<<<<<<<<<")
        print("Authorization:{}".format(Authorization))
        print("reply_token:{}".format((reply_token)))

        response = requests.post(
            url="https://api.line.me/v2/bot/message/reply",
            headers={
                "Content-Type": "application/json",
                "Authorization": Authorization,
            },
            data=json.dumps({
                "replyToken": str(reply_token),
                "messages": [
                {
                        "type": "template",
                        "altText": "this is a buttons template",
                        "template": {
                            "type": "buttons",
                            "actions": [
                              {
                                "type": "message",
                                "label": "SCADA",
                                "text": "1"
                              },
                              {
                                "type": "message",
                                "label": "EO",
                                "text": "2"
                              },
                              {
                                "type": "message",
                                "label": "ช่างแก้ไฟฟ้าขัดข้อง",
                                "text": "3"
                              }
                            ],
                            "title": "ตำแหน่งที่รับผิดชอบ",
                            "text": "กลุ่มงาน"
                         }
                    }
                ]
            })
        )

    def reply_message(self, reply_token,text):
            print(">>>>>>>>>>>>>>>>>>> debug : menu3 <<<<<<<<<<<<<<<<<<<<")
            print("Authorization:{}".format(Authorization))
            print("reply_token:{}".format(reply_token))
            # print("text:{}".format(text))

            response = requests.post(
                url="https://api.line.me/v2/bot/message/reply",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": Authorization,
                },
                data=json.dumps({
                    "replyToken": str(reply_token),
                    "messages": [
                        {
                            "type":"text",
                            "text": "ท่านได้ลงทะเบียนเรียบแล้ว ขอบคุณค่ะ"
                        }
                    ]
                })
            )

