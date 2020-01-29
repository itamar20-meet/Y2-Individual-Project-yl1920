from model import Base, User, Hero


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_user(username, password):
		user_object = User(
			username=username,
			password=password)
		session.add(user_object)
		session.commit()
		return user_object

def delete_user(session,their_id):
	 session.query(User).filter_by(
			 id=their_id).delete()
	 session.commit()

def get_all_votes():
    choice = session.query(choice).all()
    session.commit()
    return choice

def submit_option(option, username):
    vote = Vote(option=option, username=username)
    session.add(vote)
    session.commit()
    
Superman = Hero(name="Superman", votes = 10)
Batman = Hero(name="Batman", votes = 10)
All_might = Hero(name="Allmight", votes = 10)
Spiderman = Hero(name="Spiderman", votes = 10)
Ironman = Hero(name='Ironman', votes = 10)

def query_all():
    a = session.query(User).all()
    session.commit()
    return a

print(query_all())