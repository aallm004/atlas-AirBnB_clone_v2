#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage



class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value(city_id="id")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value(user_id="user")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value(name="name")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value(description="description")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value(number_rooms=2)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value(number_bathrooms=2)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value(max_guest=10)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value(price_by_night=100)
        self.assertEqual(type(new.price_by_night), int)

    def test_amenity_ids(self):
        """ """
        new = self.value(amenity_ids=[1, 2, 3])
        self.assertEqual(type(new.amenity_ids), list)

    def test_latitude(self):
        """ """
        new = self.value(latitude=1.2)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value(longitude=1.2)
        self.assertEqual(type(new.longitude), float)
    
    def test_reviews_property(self):
        """Tests the reviews property method."""
        place = self.value()
        review1 = Review(place_id=place.id, text="Great place!")
        review2 = Review(place_id=place.id, text="Needs improvement.")
        models.storage.new(review1)
        models.storage.new(review2)
        models.storage.save()

        reviews = place.reviews

        self.assertIn(review1, reviews)
        self.assertIn(review2, reviews)
    
    def test_amenities_property(self):
        """Tests the amenities property method."""
    
    def test_amenities_setter(self):
        """
        Tests for amenities setter method to ensure it correctly
        appends Amenity IDs to the amenity_ids list
        """
    
    def test_invalid_city_id(self):
        """Tests handling of invalid city_id input."""
    
    def test_zero_rooms(self):
        """Tests creating a Place with zero rooms."""