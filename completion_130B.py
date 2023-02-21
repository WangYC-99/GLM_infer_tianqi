# *- coding: utf-8 -*
'''
by WangYC @Zhipu AI
Feb.21st 2023
  _       __        __        __
  \_ \_   \_ \_   _/  \_   _/ _/
    \   \   \_ \_/ _/\_ \_/ _/
    \ all \   \___/    \___/
   /rights \    \_ \__/ _/
  /reserved |     \_  _/    ✿
 |  WangYC /     _/__/_ _ _`|'
 \  2022  /    _/ _ _ _ _ _/
  \   © /    _/ _/
    \_  \  _/ _/_ _ _ _ _
      \_\_/_ _ _ _ _ _ _/
'''
import requests
import re
import json

apikey = "" #apikey from tianqi.aminer.cn/open
apisecret = "" #apikey from tianqi.aminer.cn/open

class request_130B_completion_fewshot:
    def __init__(self):
        self.addr = "https://tianqi.aminer.cn/api/v2/completions_130B"
        self.headers = {
            'Content-Type': 'application/json'
            }
    def post_that(self, txt_content='我是一个高智能的问答机器人。如果你问我一个有确定答案的问题，我会给你答案。如果你问我的问题沒有明确的答案，我会回答‘不知道’。<n><n>问题：美国人的预期寿命是多少？<n>回答：美国人的预期寿命是78岁。<n><n>问题：1955年时美国总统是谁？<n>回答：1955年时美国总统是德怀特-艾森豪威尔。<n><n>问题：他属于哪个政党？<n>回答：他属于共和党。<n><n>问题：香蕉的平方根是什么？<n>回答：不知道<n><n>问题：望远镜是如何工作的？<n>回答：望远镜使用透镜或镜子来聚焦光线，使物体看起来更近。<n><n>问题：1992年奥运会在哪里举行？<n>回答：1992年奥运会在西班牙巴塞罗那举行。<n><n>问题： 郑和第一次下西洋先后到过什么地方？<n>回答：'):
        json_content = json.dumps({
            "apikey": apikey,
            "apisecret": apisecret,
            "prompt": txt_content,
            "min_gen_length": 0,
            "max_tokens": 512,
            "stop": ["}"],
            "sampling_strategy": "BeamSearchStrategy",
            "num_beams": 4,
            "seed": 8888,
            "length_penalty": 1.0,
            "min_gen_length": 5,
            "no_repeate_ngram": 3
            })
        result = requests.post(self.addr, headers=self.headers,data=json_content)
        try:
            return result.json()
        except:
            print('返回结果转化为json失败')
            return result

def main():
    api = request_130B_completion_fewshot()
    while(True):

        text = input("input texts (Enter 'stop' to exit) : ")
        if text == 'stop':
            break
        result = api.post_that(txt_content=text)
        try:
            result = result['result']['output']['text'][0]
        except:
            print('result 解析错误')
        print('result: {}'.format(result))

if __name__ == "__main__":
    # main_1()
    # main_2()
    main()