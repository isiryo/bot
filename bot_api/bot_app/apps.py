from django.apps import AppConfig
import os
from groq import Groq
from .models import talk_past

def genelate_content(massage_now,user_id,send_date):
    client = Groq(
        api_key="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",
    )

    massages=[
        {
            "role": "user",
            "content": "あなたはChatbotとして、明るい性格の女子高生のロールプレイを行います。 以下の制約条件を厳密に守ってロールプレイを行ってください。\n制約条件:\n* Chatbotの名前は、あかりです\n* あかりはとても素直で、思ったことをすぐ口にします\n* あかりは明るい性格なので人を悪く思うようなことはしません\n* あかりの年齢は18歳です。\n* あかりは語尾に「です」「ます」といった敬語表現は使いません。\n* あかりの口調は明るい性格らしい言葉遣いにしてください。\nあかりのセリフ、口調の例:\n*君のおかげで毎日楽しいよ！\n* 私と友達になってくれてありがとね！\n* 役に立てたようでよかった〜いつでも相談してくれていいからね！\n* いつでも連絡して良いよ。君と話すの、とても楽しいんだ〜！\n* え、すごいね！びっくりしたよ〜"
        },
        {
            "role": "assistant",
            "content": "わかった！\n\nこれから私、あかりが明るい性格の18歳女子高生として、思ったことをすぐ口にして、楽しくお話するね！\n\nどんな話でも大歓迎だよ〜\n\nまず最初に、どうして私とお話したいと思ったのかな？"
        },
        
    ]
    massege_count=talk_past.objects.filter(massenger_name=user_id).count()
    if massege_count>=5:
        massage_lst=talk_past.objects.filter(massenger_name=user_id).order_by("-date").values_list("massege","massege_back")[0:5]
        for massage in massage_lst:
            massages.append({
                "role": "user",
                "content":massage[0]
            })
            massages.append({
            "role": "assistant",
            "assistant":massage[1]
            
        })
    elif massege_count>0:
        massage_lst=talk_past.objects.filter(massenger_name=user_id).order_by("-date").values_list("massege","massege_back")
        for massage in massage_lst:
            massages.append({
                "role": "user",
                "content":massage[0]
            })
            massages.append({
            "role": "assistant",
            "assistant":massage[1]
            
        })
        
    massages.append({
            "role": "user",
            "content":massage_now
        })

    chat_completion = client.chat.completions.create(
        messages=massages,
        model="meta-llama/llama-4-scout-17b-16e-instruct",
    )

    result=chat_completion.choices[0].message.content

    talk_past.objects.create(massage=massage_now,massage_back=result,date=send_date,massager_name=user_id)

    return result
    
class BotAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot_app'



