import requests
import json
from requests.structures import CaseInsensitiveDict



USERNAME = "ScreepCode"
TOPIC = "reference"
KEYS = ["name", "html_url", "description", "language"]

class ReposAPI(object):
    def __init__(self):
        self.headers = CaseInsensitiveDict()
        self.headers["Accept"] = "application/vnd.github.mercy-preview+json"

        self.generateAPI()

    def generateAPI(self):
        allPublicRepos = self.getPublicReposFromGitHub()
        filteredRepos = self.filterReposAfterTopic(allPublicRepos)
        repoInfos = self.getInfos(filteredRepos)

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

    def getInfos(self, filteredRepos):
        allInfos = []
        for repo in filteredRepos:
            repoInfos = {}
            for key in KEYS:
               repoInfos[key] = repo[key]
            
            allInfos.append(repoInfos)
        return json.loads(json.dumps(allInfos))


API = ReposAPI()




