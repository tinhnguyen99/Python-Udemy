from this import d
from art import logo
import os

def ClearConsole():
    command = "clear"
    os.system(command)


print(logo)

print("Welcome to the secret auction program")

def InputBid():
    UserName = input("what is your name? ")
    UserBid = int(input("what is your bid? "))
    return {UserName: UserBid}

def FindBigestBid(BidDic):
    OldBid = 0
    for user, bid in BidDic.items():
        if bid > OldBid:
            winner = {user: bid}
    return winner


while True:
    UserDictionary = {"Bigest bid": 0}
    while True:
        UserDictionary.update(InputBid())
        IsContinue = input("Are there any bidders? yes or no ")
        ClearConsole()
        if IsContinue == "no":
            break
    break

print(FindBigestBid(UserDictionary))
