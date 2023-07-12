# File: votingeligibility.py
# Name: Cameron Reynolds
# Assignment 10: Program to create a function to check Voting Eligibility
# Date: 7/04/2023

def voting_age():
    age = int(input("Please input age: "))
    if age >= 18:
        print("Eligible for voting")
    else:
        print("Not eligible for voting")


voting_age()
