from flaskblog import app,db
import os

if __name__== "__main__":
    with app.app_context():
        if not os.path.isfile("site.db"):
            db.create_all()
    app.run(debug=True)