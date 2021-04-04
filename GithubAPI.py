import requests
import json
from requests.structures import CaseInsensitiveDict



USERNAME = "ScreepCode"
TOPIC = "reference"

class ReposAPI(object):
    def __init__(self):
        self.headers = CaseInsensitiveDict()
        self.headers["Accept"] = "application/vnd.github.mercy-preview+json"

        self.generateAPI()

    def generateAPI(self):
        allPublicRepos = self.getPublicReposFromGitHub()
        filteredRepos = self.filterReposAfterTopic(allPublicRepos)
        print(len(filteredRepos))

    def getPublicReposFromGitHub(self):
        url = "https://api.github.com/users/"+ USERNAME +"/repos"
        resp = requests.get(url, headers=self.headers)
        return resp.json()

    def filterReposAfterTopic(self, allPublic):
        for repo in allPublic:
            containTopic = False
            if repo["topics"] != None:
                for topic in repo["topics"]:
                    if topic == TOPIC:
                        containTopic = True
            if containTopic == False:
                allPublic.remove(repo)

        return allPublic


API = ReposAPI()




