import requests
from requests.structures import CaseInsensitiveDict



USERNAME = "ScreepCode"
TOPIC = "reference"

class ReposAPI(object):
    def __init__(self):
        self.headers = CaseInsensitiveDict()
        self.headers["Accept"] = "application/vnd.github.mercy-preview+json"

        self.generateAPI()

    def generateAPI(self):
        allPublic = self.getPublicReposFromGitHub()
        print(len(self.filterReposAfterTopic(allPublic)))


    def getPublicReposFromGitHub(self):
        url = "https://api.github.com/users/"+ USERNAME +"/repos"
        resp = requests.get(url, headers=self.headers)
        return resp.json()

    def filterReposAfterTopic(self, allPublic):
        filteredRepos = []
        for repo in allPublic:
            if repo["topics"] != None:
                for topic in repo["topics"]:
                    if topic == TOPIC:
                        filteredRepos.append(repo)

        return filteredRepos


API = ReposAPI()




