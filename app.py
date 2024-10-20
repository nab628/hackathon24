# cmd shift p then make python venv
# pip install flask
# pip install sqlalchemy

from flask import *
from database import init_db, db_session
from models import *
from sqlalchemy import desc
from sqlalchemy import func

app = Flask(__name__)

with app.app_context():
        init_db()

app.secret_key = "y5T79tFS8HhEdQxcJg=="

#Done
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        session['count_users'] = db_session.query(User).count()
        return render_template("login.html")
    elif request.method == "POST":
        #check if credentials are valid then redirect to home
        password = request.form["password"]
        username = request.form["username"]
        print(username[len(username)-10:])
        if(username[len(username)-10:] =="lehigh.edu"):
            session["username"]=username
            session['count_users'] = db_session.query(User).count()
            session["page"]="home"
            return redirect(url_for('home'))
        else:
            flash("incorrect username or password", "error")
            return render_template("login.html")

#done
@app.route("/newpost", methods=["GET", "POST"])
def newpost():
    if "username" in session:
        if request.method=="GET":
            session['count_users'] = db_session.query(User).count()
            return render_template("addBook.html")
        elif request.method == "POST":
            #create and add post to database then redirect use to homepage
            topic = request.form["topic"]
            title = request.form["title"]
            isbn = request.form["isbn"]
            course = request.form["courseCode"]
            temp = Textbook(title,topic,isbn,session["username"], course)
            db_session.add(temp)
            db_session.commit()
            flash("Textbook successfully added")
            session['count_users'] = db_session.query(User).count()
            session["page"]="home"
            return redirect(url_for("home"))
    else:
        flash("You need to log in")
        session['count_users'] = db_session.query(User).count()
        return redirect(url_for("login"))

@app.route("/displayResults")
def displayResults():
    if "username" in session:
        session['count_users'] = db_session.query(User).count()
        if session["course1"]:
            textbooks = db_session.query(Textbook).where(session["course1"] ==Textbook.course).all()
            return render_template("textbookList.html", textbooks=textbooks)
    
    flash("You need to log in")
    session['count_users'] = db_session.query(User).count()
    return redirect(url_for("login"))

#done
@app.route("/home", methods=["GET", "POST"])
def home():
    if "username" in session:
        if request.method=="GET":
            session['count_users'] = db_session.query(User).count()
            session["page"]="home"
            return render_template("home.html")
        elif request.method=="POST":
            session["course1"]= request.form["course"]
            
            return redirect(url_for('displayResults'))
    else:
        flash("You need to log in")
        session['count_users'] = db_session.query(User).count()
        return redirect(url_for("login"))

#Done but needs button
@app.route("/logout")
def logout():
    session.pop("username")
    session['count_users'] = db_session.query(User).count()
    return redirect(url_for("login"))

@app.route("/profile")
def profile():
    textbooks = db_session.query(Textbook).where(session["username"] ==Textbook.owner_username).all()
    return render_template("profile.html", textbooks=textbooks)

@app.route("/delete", methods=['POST'])
def delete():
    isbn = request.form["isbn"]
    owner_username = request.form["owner_username"]
    textbook = db_session.query(Textbook).filter_by(
        isbn=isbn,
        owner_username=owner_username
    ).first()

    db_session.delete(textbook)
    db_session.commit()
    return redirect(url_for("profile"))


# #Post sorting functions
# @app.route('/home/recent')
# def recent():
#     posts = db_session.query(Post).order_by(Post.time.desc()).all()
#     session['count_users'] = db_session.query(User).count()
#     session["page"]="recent"
#     return render_template("home.html", posts=posts)

# @app.route('/home/popular')
# def popular():
#     posts = db_session.query(Post).join(Upvote).group_by(Post).order_by(func.count(Upvote.post_id).desc()).all()
#     session['count_users'] = db_session.query(User).count()
#     session["page"]="popular"
#     return render_template("home.html", posts=posts)

# @app.route('/home/academics')
# def academics():
#     posts = db_session.query(Post).where(Post.topic =='academics').order_by(Post.time.desc()).all()
#     session['count_users'] = db_session.query(User).count()
#     session["page"]="academics"
#     return render_template("home.html", posts=posts)

# @app.route('/home/social')
# def social():
#     posts = db_session.query(Post).where(Post.topic =='social').order_by(Post.time.desc()).all()
#     session['count_users'] = db_session.query(User).count()
#     session["page"]="social"
#     return render_template("home.html", posts=posts)

# @app.route('/home/teachers')
# def teachers():
#     posts = db_session.query(Post).where(Post.topic =='teachers').order_by(Post.time.desc()).all()
#     session['count_users'] = db_session.query(User).count()
#     session["page"]="teachers"
#     return render_template("home.html", posts=posts)

# @app.route('/home/athletics')
# def athletics():
#     posts = db_session.query(Post).where(Post.topic =='athletics').order_by(Post.time.desc()).all()
#     session['count_users'] = db_session.query(User).count()
#     session["page"]="athletics"
#     return render_template("home.html", posts=posts)

# @app.route('/home/other')
# def other():
#     posts = db_session.query(Post).where(Post.topic =='other').order_by(Post.time.desc()).all()
#     session['count_users'] = db_session.query(User).count()
#     session["page"]="other"
#     return render_template("home.html", posts=posts)

# @app.route('/upvote', methods=['POST'])
# def upvote():
#     #save where on the page the user was for later use
#     #check if user has already upvoted post
#     post_id = request.form['post-id']
#     anchor_input="post"+post_id
#     already_exist = db_session.query(Upvote).where((Upvote.post_id == post_id) & (Upvote.upvoter_username==session["username"])).all()
#     if len(already_exist)==0:
#         upvote = Upvote(post_id, session["username"])
#         db_session.add(upvote)
#         db_session.commit()
#         session['count_users'] = db_session.query(User).count()
#         return redirect(url_for(session["page"], _anchor=anchor_input))
#     else:
#         flash("You can only upvote a post once!", "error")
#         session['count_users'] = db_session.query(User).count()
        
#         return redirect(url_for(session["page"],_anchor=anchor_input))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

