from app import db
from models import Pet

db.drop_all()
db.create_all()

dobby = Pet(name="Dobby", species="Dog", photo_url="https://cf.ltkcdn.net/dogs/dog-breeds/images/std-lg/325818-1200x800-meet-schipperke-clever-curious-devoted.webp",
          age='3', notes="Bonded pair with Jackson", available=True)
bubble = Pet(name="Bubble", species="Dog", photo_url="https://www.masslive.com/resizer/3WGzhbJc9mP9hW6FDM1NsXYlNFo=/800x0/smart/cloudfront-us-east-1.images.arcpublishing.com/advancelocal/3QBU6OMG4BELFPISDHYLZ7U264.png",
          age='14', notes="Only 3 teeth left", available=True)
jackson = Pet(name="Jackson", species="Dog", photo_url="https://preview.redd.it/3f84agmxtvy31.jpg?width=640&crop=smart&auto=webp&v=enabled&s=650905f66114ed3172aaa03e5a391b9f09c58fcc",
              age="6", notes="It's complicated with Dobby", available=False)
billie = Pet(name="Billie", species="Dog", photo_url="https://cdn.rescuegroups.org/7721/pictures/animals/9083/9083165/28610844.jpg?width=500",
             age='4', available=False)
db.session.add(dobby)
db.session.commit()
db.session.add(bubble)
db.session.commit()
db.session.add(jackson)
db.session.commit()
db.session.add(billie)
db.session.commit()
