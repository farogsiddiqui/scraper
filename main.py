from flask import Flask, request, render_template,jsonify
from flask import CORS, cross_origin
imoort requests
from bs4 import BeautifulSoup as bs
from urlib.request import urlopen as uReq

app = flask(__main__)

@app.route("/", methods = ["GET"])
@cross_origin
def homePage():
    return render_template("index.html")

@app.route("/review", methods = ["POST","GET"])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipkart_url)
            flipkart_Page = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkart_Page , "html.parser")
            bigboxes = flipkart_html.findAll('div' , {'class' : '_1AtVbE col-12-12'})
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            proRes = requests.get(productLink)
            prodRes.encoding = 'utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            print(prod_html)
            commentboxes = prod_html.findAll('div' , {'class': '_1AtVbE col-12-12'})

            filename = searchString + ".csv"
            fw = open(filename,"w")
            headers = "Product, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            reviews = []
            for commentbox in commentboxes:
                try:
                    name = commentbox.div.div.find_all('p',{'class':#######'})

                except:
                    name = 'No Name'

                try:
                    rating = commentbox.div.div.div.div.text

                except:
                    rating = 'No Rating'

                try:
                    commentHead = commentboxe.div.div.div.div.p.text

                except:
                    commentHead = 'No Comment Head'

                try:
                    commentTag = commentbox.div.div.find_all('div',{'class':''})
                    custComment = commentTag[0].div.text
                except Exception as e:
                    print("Exception while creating dictionary: " , e)

                myDict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead, "Comment": custComment}

                reviews.append(myDict)
            return render_template('results,html', reviews[0:(len(reviews)-1)])

        except Exception as e:
            print('The Exception message is: ' , e)
            return 'Something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    #app.run(host = '127.0.0.1', port = 5000, debug = True)
    app.run(debug = True)
