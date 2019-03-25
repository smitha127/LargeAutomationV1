import requests
from bs4 import BeautifulSoup
import json
import LargeAutomationV1.config


class Scrapy:
    def login(self, s, headers, credintials):
        url = "https://rolls-royce.leankit.com/Account/Membership/Authenticate?support=False"
        r = s.get(url, headers=headers)
        r = s.post(url, data=credintials, headers=headers)
        r = s.get("https://rolls-royce.leankit.com/io/user/me/board/recent?_=1551685125246")

    def boards(self, s):
        board_no = ["123457855", "111137067", "106606106", "107600350"]
        # board_no = ["111137067"]
        for i in board_no:
            # boardurl="https://rolls-royce.leankit.com/io/board/" + i + "/card?limit=200&id=" + i + ""
            r = s.get("https://rolls-royce.leankit.com/io/board/" + i + "/card?limit=200&id=" + i + "")
            # r=config().getUrl(boardurl)
            soup1 = BeautifulSoup(r.content, 'lxml')
            cards = soup1.find("p")
            # print(card_Nos)
            # cardnumbers = card_Nos['cards']
            return cards

    def scrapyparser(self, s):
        listofcards = []
        card_Nos = {}
        cardnumbers = card_Nos['cards']
        for i in range(len(cardnumbers)):
            # listofcards=['139017768','126333043','144770704']
            listofcards.append(card_Nos['cards'][i]['id'])
            print(listofcards)
        for i in listofcards:
            try:
                cardurl = "https://rolls-royce.leankit.com/io/card/" + i + "?id=" + i + ""
                # r = s.get("https://rolls-royce.leankit.com/io/card/" + i + "?id=" + i + "")
                r = s.get(cardurl)
                soup = BeautifulSoup(r.content, 'lxml')
                # print(soup.prettify())
                card = soup.findAll(text=True)
                # print(len(card))
                # print(card)
                # link=card[1]
                # card_data = card.text
                if len(card) > 1:
                    card = card[0] + card[len(card) - 1]
                    # print(card)
                    # card_data = card1.text
                elif len(card) == 1:
                    card = card[0]

                # print(card_data)
                card_Details_data = {}
                card_Details = {}
                # externalLinks = []

                card_Details = json.loads(card)
                # print(card_Details)
                card_body = soup.find('body')

                plannedFinish = card_Details['plannedFinish']
                externalLinks = card_Details['externalLinks']
                customId_ConsessionNo = card_Details['customId']['value']
                if (externalLinks != []):
                    externalLinks = card_Details['externalLinks'][0]['label']
                elif (externalLinks == None):
                    externalLinks = card_Details['externalLinks'][0]['url']
                elif (externalLinks == []):
                    externalLinks = soup.findAll(text=True)[1]
                card_ID = card_Details['id']
                lane_ID = card_Details['lane']['id']
                lane_ClassType = card_Details['lane']['laneClassType']
                lane_title = card_Details['lane']['title']
                # updatedOn = card_Details['updatedOn']
                # movedOn = card_Details['movedOn']
                priority = card_Details['priority']
                card_size = card_Details['size']
                card_title = card_Details['title']
                card_title1 = card_title.split(" ")
                engieneNo = card_title1[0]
                engpartNo = str(card_title1[1:])
                card_type = card_Details['type']['title']
                if (lane_ClassType == "backlog"):
                    card_Details_data = {"card_title": card_title, "engieneNo": engieneNo, "partNo": engpartNo,
                                         "customId_ConsessionNo": customId_ConsessionNo,
                                         "plannedFinish": plannedFinish, "externalLinks": externalLinks,
                                         "card_ID": card_ID,
                                         "lane_ID": lane_ID, "lane_ClassType": lane_ClassType,
                                         "priority": priority,
                                         "card_size": card_size, "card_type": card_type}
                    return (card_Details_data)

            except:
                pass
