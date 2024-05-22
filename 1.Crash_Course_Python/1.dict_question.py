#!/usr/bin/python3

def email_list(domains):
    emails=[]
    for domain in domains.keys():
        for user in domains[domain]:
            email = user+'@'+domain
            emails.append(email)
    return emails

print(email_list({"gmail.com":["clark.kent","diana.prince","peter.parker"],"yahoo.com":["barbara.gordon","jean.grey"],"hotmail.com":["bruce.wayne"]}))
