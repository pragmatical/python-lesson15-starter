from nrclex import NRCLex
import nltk
import product_review as pr
import twitter_posts as tp
import customer_survey as cs


nltk.download('punkt_tab')
#used to avoid the already installed package message
nltk.data.find('tokenizers/punkt')


def dataAnalysis(data):
  #Do something



def main():
   #Return highest emotions.

  #userData = pr.questionnaire()
  userData = tp.tweet2
  # userData= cs.survey()
  # userData = "Coding Python is a fun experience." # for testing only

  dataAnalysis(userData)


if __name__ == "__main__":
  main()
