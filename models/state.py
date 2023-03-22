#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
=======
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
>>>>>>> e323df1bb25f5b63fff9976b6c4cd228ac430f1f


class State(BaseModel, Base):
    """ State class """
<<<<<<< HEAD
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
=======
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref = 'states', cascade = 'all, delete')
    else:
        @property
        def cities(self):
            from models import storage
            cities = []
            for city in storage.all(City):
                if city.state_id == self.id:
                    cities.append(city)
            return cities

>>>>>>> e323df1bb25f5b63fff9976b6c4cd228ac430f1f
