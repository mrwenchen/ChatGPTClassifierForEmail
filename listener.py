# Find out who is writing you emails written by ChatGPT
# By Kat Sullivan
# Using code from https://github.com/promptslab/openai-detector

import win32com.client
import pythoncom
from detector import OpenaiDetector

class Handler_Class(object):
	def OnNewMailEx(self, receivedItemsIDs):
		# RecrivedItemIDs is a collection of mail IDs separated by a ",".
		# You know, sometimes more than 1 mail is received at the same moment.
		for ID in receivedItemsIDs.split(","):
			mail = outlook.Session.GetItemFromID(ID)
			subject = mail.Subject
			# print the sender's name
			print("Sender: ", mail.SenderName)
			# print the email subject line
			print("Subject: ", mail.Subject)
			# uses the OpenaiDetector algorithm to determine if email was composed by ChatGPT
			ai_response = od.detect(mail.Body)
			# ai_response will be a string if an error occured
			if isinstance(ai_response, str):
				print(ai_response)
			# if a result was produced, it will be returned as a dictionary
			else:
				print("Probability this email was generated by AI: ", ai_response['AI-Generated Probability'])
				print("Likelihood this email was written by AI: ", ai_response['Class'])
				print()

# collect OpenAI bearer token
with open('token.txt') as f:
	token = f.readline()
f.close()

# create the OpenaiDetector object 
od = OpenaiDetector(token)

outlook = win32com.client.DispatchWithEvents("Outlook.Application", Handler_Class)

# an infinite loop that waits for event
pythoncom.PumpMessages() 
