# -*- coding: utf-8 -*-
import LineAlpha
from LineAlpha.lib.curve.ttypes import *
from datetime import datetime
#from imgurpython import ImgurClient
import time,random,sys,json,codecs,threading,glob,os,subprocess,multiprocessing

cl = LineAlpha.LINE()
cl.login(token=" ")
cl.loginResult()

kk = LineAlpha.LINE()
kk.login(token=" ")
kk.loginResult()

ki = LineAlpha.LINE()
ki.login(token=" ")
ki.loginResult()

kc = LineAlpha.LINE()
kc.login(token=" ")
kc.loginResult()

kg = LineAlpha.LINE()
kg.login(token=" ")
kg.loginResult()

adm = cl

adm = LineAlpha.LINE()
adm.login(token=" ")
adm.loginResult()

client_id = '511abc94ee71658'
client_secret = '948a2fcdbf566c04bcce5f990e349ce795ee7460'
access_token = '30181acf5583ad6a215b4f69e6e5c7bc5c66efdb'
refresh_token = '4a6b3f983b96714c2e9b581edf86f86e0d681938'

client = ImgurClient(client_id, client_secret, access_token, refresh_token)

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

album = None
image_path = 'tmp/tmp.jpg'

kk=ki=kc=cl

helpMessage ="""[Tree-] Bot(s)

Use Prefix 「tr」 to use the Bot(s)
Prefix is Case sensitive but the commands is not.

¤ Gid - Show Group ID
¤ Mid all - Show all the Bot(s) MID
¤ Bot 1/2/3/4/5 - Shows the specific Bot MID
¤ Bot all  - Show all the Bot(s) Contact
¤ Bot 1/2/3/4/5 - Shows the specific Bot Contact
¤ Yid  - Show your ID
¤ Contact 「mid」 - Give Contact by MID
¤ Join on/off - Auto join group
¤ Leave on/off - Allows the bot to leave the group

¤¤ Command in the groups ¤¤
¤ Ginfo - Group Info
¤ Banlist - Check Banlist
¤ Cancel - Cancel all pending(s) invitation
¤ Stalk 「ID」 - Upload lastest instagram picture from ID

¤¤ Admin and Staff Commands ¤¤
¤ Absen - Check if bot is Online
¤ Glink on/off - Turn invitation link for group on/off
¤ Cancel on/off - Turn auto cancel invite on/off 
¤ Gn 「group name」 - Change Group Name
¤ Sp/Speed - Check bot response speed
¤ Random:「A」  - Randomize group name A times
¤ Bc 「text」 - Let the bot send a text

¤¤ Admin only Commands ¤¤
¤ Cleanse - Clear all members in the group
¤ Bye all - Bot Leave
¤ Ban 「@」 - Ban By Tag
¤ Unban 「@」 - Unban By Tag
¤ Ban - By Sharing Contact
¤ Unban - By Sharing Contact
¤ Kill ban - Kick all banned contact(s)
¤ Staff add/remove [@] - Add or Remove Staff By Tag
"""

KAC=[cl,ki,kk,kc,kg]
mid = cl.getProfile().mid
Amid = kk.getProfile().mid
Bmid = ki.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kg.getProfile().mid
Bots = [mid,Amid,Bmid,Cmid,Dmid]
admin = ["u9489706a45fcf78bea076c6b77f7067d"]
staff = ["ucd886b532f581aa4de98af5898719392"]
adminMID = "u9489706a45fcf78bea076c6b77f7067d"
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName1":"[Tree-]BOT1",
    "cName2":"[Tree-]BOT2",
    "cName3":"[Tree-]BOT3",
    "cName4":"[Tree-]BOT4",
    "cName5":"[Tree-]BOT5",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

cancelinvite = {
    'autoCancel':True,
    'autoCancelUrl':True
}

bot1_name = {
    "1" : "[Tree-]BOT1",
    "2" : "ree-]BOT1[T",
    "3" : "ee-]BOT1[Tr",
    "4" : "e-]BOT1[Tre",
    "5" : "-]BOT1[Tree",
    "6" : "-]BOT1[Tree",
    "7" : "]BOT1[Tree-",
    "8" : "BOT1[Tree-]",
    "9" : "OT1[Tree-]B",
    "10" : "T1[Tree-]BO",
    "11" : "1[Tree-]BOT"
}
bot2_name = {
    "1" : "[Tree-]BOT2",
    "2" : "ree-]BOT2[T",
    "3" : "ee-]BOT2[Tr",
    "4" : "e-]BOT2[Tre",
    "5" : "-]BOT2[Tree",
    "6" : "-]BOT2[Tree",
    "7" : "]BOT2[Tree-",
    "8" : "BOT2T[Tree-]",
    "9" : "OT2[Tree-]B",
    "10" : "T2[Tree-]BO",
    "11" : "2[Tree-]BOT"
}
bot3_name = {
    "1" : "[Tree-]BOT3",
    "2" : "ree-]BOT3[T",
    "3" : "ee-]BOT3[Tr",
    "4" : "e-]BOT3[Tre",
    "5" : "-]BOT3[Tree",
    "6" : "-]BOT3[Tree",
    "7" : "]BOT3[Tree-",
    "8" : "BOT3[Tree-]",
    "9" : "OT3[Tree-]B",
    "10" : "T3[Tree-]BO",
    "11" : "3[Tree-]BOT"
}
bot4_name = {
    "1" : "[Tree-]BOT4",
    "2" : "ree-]BOT4[T",
    "3" : "ee-]BOT4[Tr",
    "4" : "e-]BOT4[Tre",
    "5" : "-]BOT4[Tree",
    "6" : "-]BOT4[Tree",
    "7" : "]BOT4[Tree-",
    "8" : "BOT4[Tree-]",
    "9" : "OT4[Tree-]B",
    "10" : "T4[Tree-]BO",
    "11" : "4[Tree-]BOT"
bot5_name = {
    "1" : "[Tree-]BOT5",
    "2" : "ree-]BOT5[T",
    "3" : "ee-]BOT5[Tr",
    "4" : "e-]BOT5[Tre",
    "5" : "-]BOT5[Tree",
    "6" : "-]BOT5[Tree",
    "7" : "]BOT5[Tree-",
    "8" : "BOT5[Tree-]",
    "9" : "OT5[Tree-]B",
    "10" : "T5[Tree-]BO",
    "11" : "5[Tree-]BOT"

setTime = {}
setTime = wait2['setTime']

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''

    # Here's the metadata for the upload. All of these are optional, including
    # this config dict itself.
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

    return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if cancelinvite["autoCancelUrl"] == True:
                if cl.getGroup(op.param1).preventJoinByTicket == False:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        cl.reissueGroupTicket(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        print "Url Opened, Autokick on"
                else:
                    print "random group update"
            else:
                pass

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    print "BOT 1 Joined"
                else:
                    print "autoJoin is Off"

            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    kk.acceptGroupInvitation(op.param1)
                    print "BOT 2 Joined"
                else:
                    print "autoJoin is Off"

            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    ki.acceptGroupInvitation(op.param1)
                    print "BOT 3 Joined"
                else:
                    print "autoJoin is Off"

            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    kc.acceptGroupInvitation(op.param1)
                    print "BOT 4 Joined"
                else:
                    print "autoJoin is Off"
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    kg.acceptGroupInvitation(op.param1)
            else:
                if cancelinvite["autoCancel"] == True:
                    try:
                        X = cl.getGroup(op.param1)
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
                        print gInviMids + "invite canceled"
                    except:
                        try:
                            print "Retry canceling invitation"
                            X = random.choice(KAC).getGroup(op.param1)
                            gInviMids = [contact.mid for contact in X.invitee]
                            random.choice(KAC).cancelGroupInvitation(op.param1, gInviMids)
                            print gInviMids + "invite canceled"
                        except:
                            print "Bot can't cancel the invitation"
                            pass

        if op.type == 15:
            random.choice(KAC).sendText(op.param1, "Good Bye :)")
            print op.param3 + "has left the group"

        if op.type == 17:
            if op.param3 in wait["blacklist"]:
                try:
                    cl.kickoutFromGroup(op.param1, op.param3)
                except:
                    random.choice(KAC).kickoutFromGroup(op.param1, op.param3)

        if op.type == 19:
            print "someone was kicked"
            if op.param3 in admin:
                print "Admin has been kicked"
                if op.param2 in Bots:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        cl.inviteIntoGroup(op.param1,op.param3)
                        adm.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        adm.acceptGroupInvitation(op.param1)
                print "Admin Joined"      

            if mid in op.param3:
                print "BOT1 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kk.inviteIntoGroup(op.param1,op.param3)
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        cl.acceptGroupInvitation(op.param1)
                    print "BOT1 Joined"

            if Amid in op.param3:
                print "BOT2 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        ki.inviteIntoGroup(op.param1,op.param3)
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        kk.acceptGroupInvitation(op.param1)
                    print "BOT2 Joined"

            if Bmid in op.param3:
                print "BOT3 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kc.inviteIntoGroup(op.param1,op.param3)
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        ki.acceptGroupInvitation(op.param1)
                    print "BOT3 Joined"

            if Cmid in op.param3:
                print "BOT4 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kg.inviteIntoGroup(op.param1,op.param3)
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        kc.acceptGroupInvitation(op.param1)
                    print "BOT4 Joined"

            if Dmid in op.param3:
                print "BOT5 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        cl.inviteIntoGroup(op.param1,op.param3)
                        kg.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        kg.acceptGroupInvitation(op.param1)
                    print "BOT5 Joined"

            else:
                cl.kickoutFromGroup(op.param1,[op.param2])
                kk.kickoutFromGroup(op.param1,[op.param2])
                ki.kickoutFromGroup(op.param1,[op.param2])
                kc.kickoutFromGroup(op.param1,[op.param2])
                kg.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
                print "autokick executed"

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                print "BOT(s) Leaving chat Room"
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                print "BOT(s) Leaving chat Room"

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already in the Blacklist")
                        wait["wblacklist"] = False
                        print "MID Already in the Blacklist"
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Added to the Blacklist")
                        print [msg.contentMetadata["mid"]] + " Added to the Blacklist"

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted from the Blacklist")
                        wait["dblacklist"] = False
                        print [msg.contentMetadata["mid"]] + " Removed from the Blacklist"

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Contact not in Blacklist")
                        print "MID not in blacklist"
               elif wait["contact"] == True:
                    if msg.from_ in admin:
                        msg.contentType = 0
                        if 'displayName' in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendText(msg.to,"[Display Name]:\n" + msg.contentMetadata["displayName"] + "\n\n[MID]:\n" + msg.contentMetadata["mid"] + "\n\n[Status Message]:\n" + contact.statusMessage + "\n\n[Profile Picture]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n[Cover Picture]:\n" + str(cu))
                            print "Contact sent"
                        else:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n\n[MID]:\n" + msg.contentMetadata["mid"] + "\n\n[Status Message]:\n" + contact.statusMessage + "\n\n[Profile Picture]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n[Cover Picture]:\n" + str(cu))
                            print "Contact sent"
#-----------------------[Help Section]------------------------                
            elif msg.text in ["Tr /help","Tr /Help"]:
                if wait["lang"] == "JP":
                    random.choice(KAC).sendText(msg.to,helpMessage)
                    print "[Command]/help executed"
                else:
                    cl.sendText(msg.to,helpt)
#-----------------------[Group Name Section]------------------------
            elif "Tr Gn " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Tr Gn ","")
                        random.choice(KAC).updateGroup(X)
                        print "[Command]Gn executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
                    print "Gn executed outside group chat"
            elif "Tr gn " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Tr gn ","")
                        random.choice(KAC).updateGroup(X)
                        print "[Command]Gn executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
                    print "Gn executed outside group chat"
#-----------------------[Kick Section]------------------------
            elif "Tr Kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Tr Kick ","")
                    cl.sendText(msg.to,"Good bye.")
                    random.choice(KAC).kickoutFromGroup(msg.to,[midd])
                    print "[Command]Kick executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif "Tr kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Tr kick ","")
                    cl.sendText(msg.to,"Good bye.")
                    random.choice(KAC).kickoutFromGroup(msg.to,[midd])
                    print "[Command]Kick executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Tr Kill ban","Tr kill ban"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        if matched_list != []:
                            cl.sendText(msg.to,"Blacklisted contact noticed...")
                            cl.sendText(msg.to,"Begin Kicking contact")
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendText(msg.to,"It looks empty here.")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        print "[Command]Kill ban executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Send Profile Section]------------------------                    
            elif msg.text in ["Tr Bot all","Tr bot all"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Amid}
                kk.sendMessage(msg)
                msg.contentMetadata = {'mid': Bmid}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                msg.contentMetadata = {'mid': Dmid}
                kg.sendMessage(msg)
                print "[Command]Bot all executed"

            elif msg.text in ["Tr Bot 1","Tr bot 1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                print "[Command]Bot 1 executed"

            elif msg.text in ["Tr Bot 2","Tr bot 2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                kk.sendMessage(msg)
                print "[Command]Bot 2 executed"

            elif msg.text in ["Tr Bot 3","Tr bot 3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki.sendMessage(msg)
                print "[Command]Bot 3 executed"

            elif msg.text in ["Tr Bot 4","Tr bot 4"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                print "[Command]Bot 4 executed"

            elif msg.text in ["Tr Bot 5","Tr bot 5"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                kg.sendMessage(msg)
                print "[Command]Bot 5 executed"
#-----------------------[Cancel invitation Section]------------------------
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:                    
                    X = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Canceling all pending(s) invitation")
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        print "[Command]Cancel executed"
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"This group doesn't have any pending invitation")
                            print "[Command]Group don't have pending invitation"
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "Cancel executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Group link Section]------------------------                        
            elif msg.text in ["Tr Glink off","Tr Link off","Tr glink off","Tr link off"]:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned off")
                            print "[Command]Glink off executed"
                        else:
                            cl.sendText(msg.to,"Already turned off")
                            print "[Command]Glink off executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Glink off executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tr Glink on","Tr Link on","Tr glink on","Tr link on"]:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned on")
                            print "[Command]Glink on executed"
                        else:
                            cl.sendText(msg.to,"Already turned on")
                            print "[Command]Glink on executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Glink on executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Group info Section]------------------------
            elif msg.text in ["Tr Ginfo","Tr ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                        print "[Command]Ginfo executed"
                    else:
                        random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                        print "[Command]Ginfo executed"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Ginfo executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Bot/User/Group ID Section]------------------------
            elif msg.text in ["Tr Gid","Tr gid"]:
                cl.sendText(msg.to,msg.to)
                print "[Command]Gid executed"
            elif msg.text in ["Ar Mid all","Ar mid all"]:
                cl.sendText(msg.to,"[Ardh-]Bot(s) ID\n[Tree-]BOT1\n" + mid + "\n\n[Tree-]BOT2\n" + Amid + "\n\n[Tree-]BOT3\n" + Bmid + "\n\n[Tree-]BOT4\n" + Cmid + "\n\n[Tree-]BOT5\n" + Dmid)
                print "[Command]Mid executed"
            elif msg.text in ["Tr Mid 1","Tr mid 1"]:
                cl.sendText(msg.to,mid)
                print "[Command]Mid 1 executed"
            elif msg.text in ["Tr Mid 2","Tr mid 2"]:
                kk.sendText(msg.to,Amid)
                print "[Command]Mid 2 executed"
            elif msg.text in ["Tr Mid 3","Tr mid 3"]:
                ki.sendText(msg.to,Bmid)
                print "[Command]Mid 3 executed"
            elif msg.text in ["Tr Mid 4","Tr mid 4"]:
                kc.sendText(msg.to,Cmid)
                print "[Command]Mid 4 executed"
            elif msg.text in ["Tr Mid 5","Tr mid 5"]:
                kc.sendText(msg.to,Dmid)
                print "[Command]Mid 5 executed"
            elif msg.text in ["Tr Yid","Tr yid"]:
                cl.sendText(msg.to,msg.from_)
                print "[Command]Yid executed"
#-----------------------[Send Contact Section]------------------------
            elif "Tr Contact" in msg.text:
                mmid = msg.text.replace("Tr Contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                print "[Command]Contact executed"
            elif "Tr contact" in msg.text:
                mmid = msg.text.replace("Tr contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                print "[Command]Contact executed"
#-----------------------[Auto Join Section]------------------------
            elif msg.text in ["Tr Join on","Tr join on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already on")
                        print "[Command]Join on executed"
                    else:
                        cl.sendText(msg.to,"Auto join already on")
                        print "[Command]Join on executed"
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned on")
                        print "[Command]Join on executed"
                    else:
                        cl.sendText(msg.to,"Auto join turned on")
                        print "Join on executed"
            elif msg.text in ["Tr Join off","Tr join off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already off")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Auto join already off")
                        print "[Command]Join off executed"
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned off")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Auto join turned off")
                        print "[Command]Join off executed"
#-----------------------[Group Url Section]------------------------
            elif msg.text in ["Tr Gurl","Tr gurl"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        x = cl.getGroup(msg.to)
                        if x.preventJoinByTicket == True:
                            x.preventJoinByTicket = False
                            cl.updateGroup(x)
                        gurl = cl.reissueGroupTicket(msg.to)
                        cl.sendText(msg.to,"line://ti/g/" + gurl)
                        print "[Command]Gurl executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                        print "[Command]Gurl executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[All bots join group Section]------------------------
            elif msg.text in ["Tr Join all","Tr join all"]:
                if msg.from_ in admin:
                    try:
                        ginfo = cl.getGroup(msg.to)
                        ginfo.preventJoinByTicket = False
                        cl.updateGroup(ginfo)

                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)

                        ginfo = random.choice(KAC).getGroup(msg.to)
                        ginfo.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(ginfo)
                    except:
                        print "Somethings wrong with the url"
                    print "[Command]Join all executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
#-----------------------[Bot(s) Leave Section]------------------------
            elif msg.text in ["Tr Bye all","Tr bye all"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                            kk.leaveGroup(msg.to)
                            ki.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            kg.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye all executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Tr Bye bot 1","Tr bye bot 1"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 1 executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Tr Bye bot 2","Tr bye bot 2"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kk.getGroup(msg.to)
                        try:
                            kk.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 2 executed"
                    else:
                        kk.sendText(msg.to,"Command denied.")
                        kk.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Tr Bye bot 3","Tr bye bot 3"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = ki.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 3 executed"
                    else:
                        ki.sendText(msg.to,"Command denied.")
                        ki.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Tr Bye bot 4","Tr bye bot 4"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kc.getGroup(msg.to)
                        try:
                            kc.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 4 executed"
                    else:
                        kc.sendText(msg.to,"Command denied.")
                        kc.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Tr Bye bot 5","Tr bye bot 5"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kc.getGroup(msg.to)
                        try:
                            kg.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 5 executed"
                    else:
                        kg.sendText(msg.to,"Command denied.")
                        kg.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Cleanse Section (USE AT YOUR OWN RISK!)]------------------------
            elif msg.text in ["Tr Cleanse","Tr cleanse"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Cleanse executing"
                        _name = msg.text.replace("Cleanse","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        kk.sendText(msg.to,"Group cleansing begin")
                        kc.sendText(msg.to,"Goodbye :)")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        # --------------[Bot and Admin MID]----------------
                        targets.remove(adminMID)
                        targets.remove(mid)
                        targets.remove(Amid)
                        targets.remove(Bmid)
                        targets.remove(Cmid)
                        targets.remove(Dmid)
                        # --------------[Bot and Admin MID]----------------
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    klist=[ki,kk,kc,cl,kg]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Group cleansed")
                        print "[Command]Cleanse executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Ban/Unban Section]------------------------
            elif "Tr Ban @" in msg.text:
                    if msg.toType == 2:
                        if msg.from_ in admin:
                            print "[Command]Ban executed"
                            _name = msg.text.replace("Tr Ban @","")
                            _nametarget = _name.rstrip('  ')
                            gs = ki.getGroup(msg.to)
                            gs = kk.getGroup(msg.to)
                            gs = kc.getGroup(msg.to)
                            gs = kg.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendText(msg.to,"Contact not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Added to Blacklist")
                                    except:
                                        ki.sendText(msg.to,"Error")
                        else:
                            cl.sendText(msg.to,"Command denied.")
                            cl.sendText(msg.to,"Admin permission required.")
            elif "Tr Unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Unban executed"
                        _name = msg.text.replace("Tr Unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Added to Whitelist")
                                except:
                                    ki.sendText(msg.to,"Added to Whitelist")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif "Tr ban @" in msg.text:
                    if msg.toType == 2:
                        if msg.from_ in admin:
                            print "[Command]Ban executed"
                            _name = msg.text.replace("Tr ban @","")
                            _nametarget = _name.rstrip('  ')
                            gs = ki.getGroup(msg.to)
                            gs = kk.getGroup(msg.to)
                            gs = kc.getGroup(msg.to)
                            gs = kg.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendText(msg.to,"Contact not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Added to Blacklist")
                                    except:
                                        ki.sendText(msg.to,"Error")
                        else:
                            cl.sendText(msg.to,"Command denied.")
                            cl.sendText(msg.to,"Admin permission required.")
            elif "Tr unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Unban executed"
                        _name = msg.text.replace("Tr unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Added to Whitelist")
                                except:
                                    ki.sendText(msg.to,"Added to Whitelist")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Tr Ban","Tr ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Ban")
                    print "[Command]Ban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Tr Unban","Tr unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Unban")
                    print "[Command]Unban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Tr Banlist","Tr banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No user is Blacklisted")
                else:
                    cl.sendText(msg.to,"Blacklisted user(s)")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Banlist executed"
#-----------------------[Bot Speak Section]------------------------
            elif "Tr Bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("Tr Bc ","")
                    random.choice(KAC).sendText(msg.to,(bctxt))
                    print "[Command]Bc executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif "Tr bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("Tr bc ","")
                    cl.sendText(msg.to,(bctxt))
                    print "[Command]Bc executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Bot speed test Section]------------------------
            elif msg.text in ["Tr Sp all","Tr Speed all","Tr sp all","Tr speed all"]:
                if msg.from_ in staff:

                    start = time.time()
                    cl.sendText(msg.to, "Bot 1 Processing Request")                    
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))

                    start2 = time.time()
                    kk.sendText(msg.to, "Bot 2 Processing Request")                    
                    elapsed_time2 = time.time() - start2
                    kk.sendText(msg.to, "%sseconds" % (elapsed_time2))
                    
                    start3 = time.time()
                    ki.sendText(msg.to, "Bot 3 Processing Request")                    
                    elapsed_time3 = time.time() - start3
                    ki.sendText(msg.to, "%sseconds" % (elapsed_time3))
                    
                    start4 = time.time()
                    kc.sendText(msg.to, "Bot 4 Processing Request")                    
                    elapsed_time4 = time.time() - start4
                    kc.sendText(msg.to, "%sseconds" % (elapsed_time4))
                    
                    start5 = time.time()
                    kg.sendText(msg.to, "Bot 5 Processing Request")                    
                    elapsed_time5 = time.time() - start5
                    kg.sendText(msg.to, "%sseconds" % (elapsed_time5))
                    print "[Command]Speed all executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Tr Sp 1","Tr Speed 1","Tr sp 1","Tr speed 1"]:
                if msg.from_ in staff: 
                    start = time.time()                   
                    cl.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 1 executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Tr Sp 2","Tr Speed 2","Tr sp 2","Tr speed 2"]:
                if msg.from_ in staff:
                    start = time.time()                    
                    kk.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    kk.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 2 executed"
                else:
                    kk.sendText(msg.to,"Command denied.")
                    kk.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Tr Sp 3","Tr Speed 3","Tr sp 3","Tr speed 3"]:
                if msg.from_ in staff:
                    start = time.time()                   
                    ki.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 3 executed"
                else:
                    ki.sendText(msg.to,"Command denied.")
                    ki.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Tr Sp 4","Tr Speed 4","Tr sp 4","Tr speed 4"]:
                if msg.from_ in staff: 
                    start = time.time()                   
                    kc.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    kc.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 4 executed"
                else:
                    kc.sendText(msg.to,"Command denied.")
                    kc.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Tr Sp 5","Tr Speed 5","Tr sp 5","Tr speed 5"]:
                if msg.from_ in staff:    
                    start = time.time()                
                    kg.sendText(msg.to, "Progress...")                                       
                    elapsed_time = time.time() - start
                    kg.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 5 executed"
                else:
                    kc.sendText(msg.to,"Command denied.")
                    kc.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Auto Cancel Section]------------------------
            elif "Tr staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Tr staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Tr Staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Tr Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Tr staff remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Tr staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Tr Staff remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Tr Staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Tr Stafflist","Tr stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------[Auto cancel Section]------------------------
            elif msg.text in ["Tr Cancel off","Tr cancel off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == True:
                        cancelinvite["autoCancel"] = False
                        cl.sendText(msg.to, "Auto Cancel turned off")
                        print "[Command]Cancel off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Cancel off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Tr Cancel on","Tr cancel on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == False:
                        cancelinvite["autoCancel"] = True
                        cl.sendText(msg.to, "Auto Cancel turned on")
                        print "[Command]Cancel on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned on")
                        print "[Command]Cancel on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Tr Url off","Tr url off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == True:
                        cancelinvite["autoCancelUrl"] = False
                        cl.sendText(msg.to, "Auto Cancel Url turned off")
                        print "[Command]Url off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Url off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Tr Url on","Tr url on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == True:
                        cancelinvite["autoCancelUrl"] = False
                        cl.sendText(msg.to, "Auto Cancel Url turned off")
                        print "[Command]Url on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Url on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Misc Section]-------------------------------------------
            elif "Tr random:" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        strnum = msg.text.replace("Tr random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.05)
                                group.name = name
                                random.choice(KAC).updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
                        print "[Command]Random executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

            elif "Tr Random:" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        strnum = msg.text.replace("Tr Random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.01)
                                group.name = name
                                cl.updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
                        print "[Command]Random executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Tr Tree","Tr tree"]:
                if msg.from_ in staff:
                    cl.sendText(msg.to, "Hadir")
                    kk.sendText(msg.to, "Hadir")
                    ki.sendText(msg.to, "Hadir")
                    kc.sendText(msg.to, "Hadir")
                    kg.sendText(msg.to, "Hadir")
                    print "[Command]Tree executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Tr Kernel","Tr kernel"]:
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel)
                    print "[Command]Kernel executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"

            # elif "Tr Stalk " in msg.text:
            #     print "[Command]Stalk executing"
            #     stalkID = msg.text.replace("Tr Stalk ","")
            #     subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
            #     files = glob.glob("tmp/*.jpg")
            #     for file in files:
            #         os.rename(file,"tmp/tmp.jpg")
            #     fileTmp = glob.glob("tmp/tmp.jpg")
            #     if not fileTmp:
            #         cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
            #         print "[Command]Stalk executed - no image found"
            #     else:
            #         image = upload_tempimage(client)
            #         cl.sendText(msg.to, format(image['link']))
            #         print "[Command]Stalk executed - success"

            # elif "Tr stalk " in msg.text:
            #     print "[Command]Stalk executing"
            #     stalkID = msg.text.replace("Tr stalk ","")
            #     subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
            #     files = glob.glob("tmp/*.jpg")
            #     for file in files:
            #         os.rename(file,"tmp/tmp.jpg")
            #     fileTmp = glob.glob("tmp/tmp.jpg")
            #     if not fileTmp:
            #         cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
            #         print "[Command]Stalk executed - no image found"
            #     else:
            #         image = upload_tempimage(client)
            #         cl.sendText(msg.to, format(image['link']))
            #         subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
            #         print "[Command]Stalk executed - success"

            elif "Tr Add @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Add executing"
                        _name = msg.text.replace("Tr Add @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    cl.findAndAddContactsByMid(target)
                                except:
                                    ki.sendText(msg.to,"Error")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")

            elif "Tr add @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Add executed"
                        _name = msg.text.replace("Tr Add @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                cl.findAndAddContactsByMid(target)
                                ki.findAndAddContactsByMid(target)
                                kk.findAndAddContactsByMid(target)
                                kc.findAndAddContactsByMid(target)
                                kg.findAndAddContactsByMid(target)
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        
            elif msg.text in ["Tr Like", "Tr like"]:
                if msg.from_ in staff:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Trying to Like post(s) from staff")
                    try:
                        likePost()
                    except:
                        pass


            elif msg.text in ["Tr Tagall", "Tr tagall"]:
                group = cl.getGroup(msg.to)
                msg_appended = ""
                mem = [contact.mid for contact in group.members]                
                for mm in mem:
                    xname = cl.getContact(mm).displayName
                    xlen = str(len(xname)+1)
                    msg.contentType = 0
                    msg.text = "@"+xname+" "
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
                    # msg_appended += "->" +msg+ "\n"
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error        

            else:
                if cl.getGroup(msg.to).preventJoinByTicket == False:
                    cl.reissueGroupTicket(msg.to)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                else:
                    if msg.from_ in Bots:
                        pass
                    else:
                        print "No Action"
        if op.type == 59:
            print op


    except Exception as error:
        print error

# def nameUpdate_Bot1():
#     while True:
#         try:
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["1"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["2"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["3"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["4"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["5"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["6"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["7"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["8"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["9"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["10"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["11"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#         except:
#             pass

# def nameUpdate_Bot2():
#     while True:
#         try:
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["1"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["2"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["3"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["4"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["5"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["6"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["7"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["8"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["9"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["10"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["11"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#         except:
#             pass

# def nameUpdate_Bot3():
#     while True:
#         try:
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["1"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["2"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["3"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["4"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["5"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["6"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["7"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["8"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["9"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["10"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["11"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#         except:
#             pass

# def nameUpdate_Bot4():
#     while True:
#         try:
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["1"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["2"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["3"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["4"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["5"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["6"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["7"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["8"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["9"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["10"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["11"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#         except:
#             pass

# def nameUpdate_Bot5():
#     while True:
#         try:
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["1"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["2"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["3"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["4"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["5"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["6"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["7"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["8"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["9"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["10"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["11"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#         except:
#             pass

# def nameUpdate():
#     while True:
#         try:
#         #while a2():
#             #pass
#             if wait["clock"] == True:
#                 now2 = datetime.now()
#                 nowT = datetime.strftime(now2,"(%H:%M)")
#                 profile = cl.getProfile()
#                 profile.displayName = wait["cName"]
#                 cl.updateProfile(profile)

#                 profile2 = kk.getProfile()
#                 profile2.displayName = wait["cName2"]
#                 kk.updateProfile(profile2)

#                 profile3 = ki.getProfile()
#                 profile3.displayName = wait["cName3"]
#                 ki.updateProfile(profile3)

#                 profile4 = kc.getProfile()
#                 profile4.displayName = wait["cName4"]
#                 kc.updateProfile(profile4)

#                 profile5 = kg.getProfile()
#                 profile5.displayName = wait["cName5"]
#                 kg.updateProfile(profile5)
#             time.sleep(600)
#         except:
#             pass
# thread2 = threading.Thread(target=nameUpdate)
# thread2.daemon = True
# thread2.start()

def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in staff:
                try:    
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kg.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by ARDH-")
                    print "Like"
                except:
                    pass
            else:
                print "Not Admin or staff"

# Auto Changing name
# thread1 = threading.Thread(target=nameUpdate_Bot1)
# thread1.daemon = True
# thread1.start()
# thread2 = threading.Thread(target=nameUpdate_Bot2)
# thread2.daemon = True
# thread2.start()
# thread3 = threading.Thread(target=nameUpdate_Bot3)
# thread3.daemon = True
# thread3.start()
# thread4 = threading.Thread(target=nameUpdate_Bot4)
# thread4.daemon = True
# thread4.start()
# thread5 = threading.Thread(target=nameUpdate_Bot5)
# thread5.daemon = True
# thread5.start()
# END


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
