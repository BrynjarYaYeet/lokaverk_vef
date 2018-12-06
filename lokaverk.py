import pymysql
from bottle import *

@get('/')
def index():
    return template('index.tpl')


@route("/skraning")
def innskra():
    return template('innskra.tpl')

@route("/nyrnotandi", method='POST')
def skra():
    u = request.forms.get('user')
    p = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2110012590', passwd='mypassword', db='2110012590_verslun')
    cur = conn.cursor()

    cur.execute("SELECT count(*) FROM 2110012590_verslun.users where user=%s",(u))
    result=cur.fetchone()
    if result[0] == 0:
        cur.execute("INSERT INTO 2110012590_verslun.users Values(%s,%s)", (u, p))
        conn.commit()
        cur.close()
        conn.close()
        return template('nyrnot',u=u)
    else:
        return template('allsekki', u=u)

@route('/innskra', method='POST')
def doinn():
    u = request.forms.get('user')
    p = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2110012590', passwd='mypassword', db='2110012590_verslun')
    cur = conn.cursor()

    cur.execute("SELECT count(*) FROM 2110012590_verslun.users where user=%s and pass=%s",(u,p))
    result = cur.fetchone()
    print(result)
    if result[0] == 1:

        cur.close()
        conn.close()
        return template('komin',u=u) #, n=n, v=v)
    else:
        return template('nei')

@route("/members")
def member():
    conn=pymysql.connect(host="tsuts.tskoli.is", port=3306, user="2110012590", passwd="mypassword")
    c=conn.cursor()
    c.execute("SELECT user from 2110012590_verslun.users")
    result=c.fetchall()
    c.close()
    output=template("members", rows=result)
    return output

@route("/info")
def upplysingar():
    return template("info.tpl")

@route("/verslun")
def verslunn():
    conn=pymysql.connect(host="tsuts.tskoli.is", port=3306, user="2110012590", passwd="mypassword")
    c=conn.cursor()
    c.execute("SELECT * from 2110012590_verslun.vara")
    result=c.fetchall()
    c.close()
    budinn=template("verslun.tpl", rows=result)
    return budinn

@route("/kaupa")
def versla():
    return template("kaupa.tpl")

@route("/keypt")
def verslad():
    return template("keypt.tpl")

@route ("/admin")
def adallgaejinn():
    conn=pymysql.connect(host="tsuts.tskoli.is", port=3306, user="2110012590", passwd="mypassword")
    c=conn.cursor()
    c.execute("SELECT * from 2110012590_verslun.vara")
    result=c.fetchall()
    c.close()
    return template('admin.tpl', rows=result)

@route ("/breytasida")
def breyta():
    return template("breyta.tpl")

@route ("/breyta")#, method="POST")
def breyta():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2110012590', passwd='mypassword', db='2110012590_verslun')
    cur = conn.cursor()




@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root="./static/")

#try:
#    run(host="0.0.0.0", port=os.environ.get("PORT"))
#except:
#   run(debug=True)
run(host="localhost", port=8980)
