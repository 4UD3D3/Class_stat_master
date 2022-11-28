import requests
import datetime

LISTEURL = [
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=7f48522cb3de9575e95729758d450e444592592d3b282f749c9a606b710f264fdc5c094f7d1a811b903031bde802c7f597e5f20f622768ff000996ffaaa109f6112354f71ca98aa351320e533e1999aa166c54e36382c1aa3eb0ff5cb8980cdb,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=a04b190b2ed8e5caa650a8f87657b125c4984538c834c152743161cbf6139a4efa935b1946260073ec191f3b2a14d155ba7fed952318108933bbe21031e36f91d5a68b7a4b1a5ade545963132699eee235c3b8a223b47dfaccc4b6050f52e7b6,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=614fc9ddc278f089bff5eb3a1a1bbe41e3a8076f457f6472b5649913c2291cd1616b80bd836773d873637f2806cc3ea97440daaa829073328c0f7f4581dc9eaf30d5500f152ed0fe89dd465b28632b9a32c3e2f8d5c6adddb1d141712b429277,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=14ff6ab480b103c64555a8b58b202714fb25a16be18fcf93bc51cc680577d549616b80bd836773d873637f2806cc3ea97440daaa829073328c0f7f4581dc9eaf30d5500f152ed0fe89dd465b28632b9a89de6b078694b85ef28dbd27caa20aa1,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=923f2d96d3616e28cd87f8384f23b16c4592592d3b282f749c9a606b710f264fdc5c094f7d1a811b903031bde802c7f597e5f20f622768ff000996ffaaa109f6112354f71ca98aa351320e533e1999aa166c54e36382c1aa3eb0ff5cb8980cdb,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=757c399125f50c4ed58c9468b9d04117e1fff4518acc1b9ca0ef27a39a664d6f292fa4c04d77640dd7ddb2dc00c8e1c4692613b21192e5f0e0b7c5a5601c933d0927d3c2a8482204fb2d4878284bf07ae3765f7212952d79d8a1efcf5b5cdc7d29ecbbae75627a1e7d25d946b10dc628,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=90621515de8cc93f4a5865d1db97dba536205b94d7d29e90e2f5dfbb8890033330a5f72847b0c2c00c79892a4ff650a7315d113e09b20990871a82bc98f32f25a3cd23659737bfd689e3c09b6754f850,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=3a78d38f3b75f393931f03285b9ae3c0a3c1b8144ad3fbfb2ec1e6855df8e91d6764a6bc5965d719b79d9ddfea07bbb0b000ad8fe36fb185f9530ddbfd2b9dd27a99563a9aeb0376b7abd9810b651215133ad6be6bb6ef8cca0bc1791f45d792ec28a6fbe4619a3fc40ac0933c25fb80bc415534d05aa4d071038cc034efab18,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=5b3ce1fdee99067416d993869081aee0267a2b8267f81467f474d2bd24f6c58bdc822d254551495550c70b4cab2ade41a8df2af68f94010df23a07088c85bfd93d74ff1618c675af4ac260d3657eb7682e112dfe9936a79a5a8ecd8e0160d714e034a2cdbe2c210c5b0804b691125549bad5bc750672ab4c9cb2bb49c5ae1a6c001d5a01946ee41f0206d32b7fe7c4c5fa935b1946260073ec191f3b2a14d155ba7fed952318108933bbe21031e36f91d5a68b7a4b1a5ade545963132699eee235c3b8a223b47dfaccc4b6050f52e7b6,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=466b25e79366b832ccc8b6be17c5fed590b4e339b2978fcccf4a50716aa2b8724592592d3b282f749c9a606b710f264fdc5c094f7d1a811b903031bde802c7f597e5f20f622768ff000996ffaaa109f6112354f71ca98aa351320e533e1999aa166c54e36382c1aa3eb0ff5cb8980cdb,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=d9213863d6ad292435ea58b37eec56e54592592d3b282f749c9a606b710f264fdc5c094f7d1a811b903031bde802c7f597e5f20f622768ff000996ffaaa109f6112354f71ca98aa351320e533e1999aa166c54e36382c1aa3eb0ff5cb8980cdb,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=3e205bd37cc96f3ee4d34433b73d99d54592592d3b282f749c9a606b710f264fdc5c094f7d1a811b903031bde802c7f597e5f20f622768ff000996ffaaa109f6112354f71ca98aa351320e533e1999aa166c54e36382c1aa3eb0ff5cb8980cdb,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=54d6de9f43438801d18e45b1b3b756d71fe79030787ac942f33ce91822fec59d30f751596bf805029b3665e013527ca33b35f036e01b31d843308a474f2a28663aa1c501ef1b42449ebf95803f38797968efa3e27764dae6116bbd73fa89dab7759a197c311a1bf59a660527ea2f770b568fc3589bb9c75ba074ad4e7c1550a9,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=0d7ca81cce6f5170b6b139c980b7abe24592592d3b282f749c9a606b710f264fdc5c094f7d1a811b903031bde802c7f597e5f20f622768ff000996ffaaa109f6112354f71ca98aa351320e533e1999aa166c54e36382c1aa3eb0ff5cb8980cdb,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=a4ae7a27e556d504d51712438da6b42732e4de11fcc9c715921f49a10909f0b5fa7fa99d6e32fa89dd92890ccfd9e81f7a99563a9aeb0376b7abd9810b651215133ad6be6bb6ef8cca0bc1791f45d792ec28a6fbe4619a3fc40ac0933c25fb80bc415534d05aa4d071038cc034efab18,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=b7a078a199e4ee07b95a3d36a77b2a8e62d53dc194c2bc627db1b95d94bda3047f5e68a0f1f7ef4298fe4af03a1b5b86a0c5d70e5fa02090bfc466a9b79f18636f36d25e30cef5b821ac5921084a89d3304517f1a97a0a26f5c57bd0845df2f8dddfe43fc0605ce14ed156aff041f645,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=02c33becef463b1c14a50e3c3bbdccce9dd6d61c5f71896a87d42704e60e3629fa935b1946260073ec191f3b2a14d155ba7fed952318108933bbe21031e36f91d5a68b7a4b1a5ade545963132699eee235c3b8a223b47dfaccc4b6050f52e7b6,1',
    'https://planning.univ-ubs.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?data=432062fc0202a22ab7eb766beb8e7e284592592d3b282f749c9a606b710f264fdc5c094f7d1a811b903031bde802c7f597e5f20f622768ff000996ffaaa109f6112354f71ca98aa351320e533e1999aa166c54e36382c1aa3eb0ff5cb8980cdb,1']


def getICS(url):
    """

    :param url: url of the calendar to download
    :return:
    """
    r = requests.get(url, allow_redirects=True)
    open('data/icsfiletmp.ics', 'wb').write(r.content)


def fusion():
    """
    take the icsfiletmp file and write it at the end of the icsfileall filee
    :return:
    """
    with open('data/icsfiletmp.ics', 'r') as input:
        with open('data/icsfileall.ics', 'a') as output:
            for ligne in input:
                output.write(ligne)


def analyseEvent(myList, DateStart, DateEnd, Roomlist):
    """
    from the list given analyse it and writ it on the file if the event correspond to our specification
    :param myList: list of string with all a event from an ics file
    :param DateStart: start date of the range
    :param DateEnd: end date of the range
    :param Room: room to target
    """
    global datein, dateout, roomEvent
    for ligne in myList:
        if "DTSTART" in ligne:
            dateinEvent = ligne.split(":")[1]
            datein = datetime.date(int(dateinEvent[:4]), int(dateinEvent[4:6]), int(dateinEvent[6:8]))

        if "DTEND" in ligne:
            dateoutEvent = ligne.split(":")[1]
            dateout = datetime.date(int(dateoutEvent[:4]), int(dateoutEvent[4:6]), int(dateoutEvent[6:8]))

        if "LOCATION" in ligne:
            roomEvent = ligne.split(":")[1]

    for Room in Roomlist:
        if datein >= DateStart and dateout <= DateEnd and Room in roomEvent:
            with open('data/icsfileout.ics', 'a') as file:
                for ligne in myList:
                    file.write(ligne)


def getICSFile(DateStart, DateEnd, Roomlist, reload):
    """
    main function how save the ics file on data/icsfileout.ics from the next parameter
    :param DateStart: start date of the range type : datime.date
    :param DateEnd: end date of the range type : datetime.date
    :param Roomlist: room to target
    :param reaload: 1 if we want to reaload the the ics data else 0 the first time need to be at 1 to load a first tim the ics
    """
    if reload == 1 :
        loadICSFile()
        print("Output File ICS Fusion Done.")

    
    with open('data/icsfileout.ics', 'w') as file:
        file.write("BEGIN:VCALENDAR\nMETHOD:REQUEST\nPRODID:-//ADE/version 6.0\nVERSION:2.0\nCALSCALE:GREGORIAN\n")

    with open('data/icsfileall.ics', 'r') as file:
        myList = []
        write = False
        for ligne in file:
            if "BEGIN:VEVENT" in ligne:
                write = True
            if write:
                myList.append(ligne)
            if "END:VEVENT" in ligne:
                analyseEvent(myList, DateStart, DateEnd, Roomlist)
                myList = []
                write = False

    with open('data/icsfileout.ics', 'a') as file:
        file.write("END:VCALENDAR")
        
    return open('data/icsfileout.ics', 'r')

def loadICSFile():
    for url in LISTEURL:
            getICS(url)
            fusion()


"""if __name__ == '__main__':
    with open('data/out','r') as myFile:#build json for request
        tab = []
        for ligne in myFile:
            tab.append(ligne.split("\n")[0])
    getICSFile(datetime.date(2022, 9, 1), datetime.date(2022, 10, 1), tab, 0)"""
