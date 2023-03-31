from detector import OpenaiDetector

sentence = "Dear [Line Manager's Name], I am writing to request annual leave from [start date] to [end date] to embark on an interrailing trip in Europe. As you are aware, I have been planning this trip for quite some time now, and I am excited to finally have the opportunity to explore different parts of Europe. During my absence, I will make sure that all my tasks and responsibilities are delegated to my colleagues, and I will provide them with any necessary guidance or support before I leave. I am confident that my colleagues will be able to handle my workload efficiently and effectively. I understand that my absence may cause some inconvenience, and I apologize for any inconvenience that it may cause. However, I will be reachable via email in case of any urgent matters that may require my attention. I believe that this trip will not only provide me with an opportunity to rejuvenate and relax but also enable me to learn about different cultures and gain new perspectives, which will be beneficial to my personal and professional growth. I appreciate your consideration of my request, and I look forward to hearing from you soon. Thank you. Best regards, [Your Name]"

with open('token.txt') as file:
	bearer_token = file.readline()
file.close()

# creating an OpenaiDetecter object
# my bearer token will be the parameter
od = OpenaiDetector(bearer_token)

# detect is the function
# sentence is the parameter we're passing
response = od.detect(sentence)
print(response)