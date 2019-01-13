from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:////var/www/html/Catalog/Category.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Two Shinguards", description="Juicy grilled veggie patty with tomato mayo and lettuce"
                , category=category1)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Shinguards", description="with garlic and parmesan",
                        category=category1)

session.add(item2)
session.commit()

menuItem2 = Item(user_id=1, name="jersey", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                        category=category1)


session.add(menuItem2)
session.commit()
# Menu for UrbanBurger
category2 = Category(user_id=1, name="Football")

session.add(category2)
session.commit()

item1 = Item(user_id=1, name="Stick", description="Juicy grilled veggie patty with tomato mayo and lettuce"
                , category=category2)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Goggles", description="with garlic and parmesan",
                        category=category2)

session.add(item2)
session.commit()

menuItem2 = Item(user_id=1, name="Bat", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                        category=category2)

session.add(menuItem2)
session.commit()

# Create dummy user
User2 = User(name="Ahmed Abdullah", email="ahmed@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User2)
session.commit()

# Menu for UrbanBurger
category1 = Category(user_id=2, name="Basketball")

session.add(category1)
session.commit()

item1 = Item(user_id=2, name="Bat", description="Juicy grilled veggie patty with tomato mayo and lettuce"
                , category=category1)

session.add(item1)
session.commit()


item2 = Item(user_id=2, name="Random", description="with garlic and parmesan",
                        category=category1)

session.add(item2)
session.commit()

menuItem2 = Item(user_id=2, name="Frisbes", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                        category=category1)


session.add(menuItem2)
session.commit()
# Menu for UrbanBurger
category2 = Category(user_id=2, name="Hockey")

session.add(category2)
session.commit()

item1 = Item(user_id=2, name="Stick", description="Juicy grilled veggie patty with tomato mayo and lettuce"
                , category=category2)

session.add(item1)
session.commit()


item2 = Item(user_id=2, name="SnowBord", description="with garlic and parmesan",
                        category=category2)

session.add(item2)
session.commit()

menuItem2 = Item(user_id=2, name="Bat", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                        category=category2)

session.add(menuItem2)
session.commit()
print "added menu items!"
