import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return "￥eIMSYGrMQRe￥淘宝打开不限次数…点了@我回.  淘宝购物优惠券领取网站www.jweilan.com"

itchat.auto_login()
itchat.run()