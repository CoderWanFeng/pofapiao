# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@读者群     ：https://www.python4office.cn/wechat-group/
@个人网站 ：www.python-office.com
@Date    ：2023/4/10 22:13 
@Description     ：
'''
import poocr

res = poocr.ocr.VatRollInvoiceOCR(img_path=r'docs/8.png', configPath=r'D:\workplace\code\github\poocr\tests\poocr-config.toml')
print(res)
