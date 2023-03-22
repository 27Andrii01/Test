from vehicle import *

def test_vehicle():
    """
    Print Done if all tests passed
    """
    print("Testing Vehicle class...", end="")
    v3 = Vehicle('Honda', 3)
    # check if main information about the vehicle and passengers is correct
    assert isinstance(v3, Vehicle) is True
    assert str(v3) == "Honda holds 3: [], free 3"
    assert v3.is_empty() is True
    p3 = Passenger('Olenka')
    assert str(p3) == "Olenka is passenger of ..."
    p4 = Passenger('Maksym')
    p5 = Passenger('Nastia')
    assert isinstance(p4, Passenger) is True
    # can't remove a passenger from an empty bus or vehicle
    assert v3.remove_passenger() is False
    # passengers can be added
    assert v3.add_passenger(p3) is True
    assert str(v3) == "Honda holds 3: ['Olenka'], free 2"
    assert v3.add_passenger(p4) is True
    assert str(v3) == "Honda holds 3: ['Olenka', 'Maksym'], free 1"
    assert v3.add_passenger(p5) is True
    assert str(v3) == "Honda holds 3: ['Olenka', 'Maksym', 'Nastia'], free 0"
    p6 = Passenger('Katia')
    # can't add passengers past the max capacity
    assert v3.add_passenger(p6) is False
    assert str(v3) == "Honda holds 3: ['Olenka', 'Maksym', 'Nastia'], free 0"
    assert v3.passengers == ['Olenka', 'Maksym', 'Nastia']
    assert v3.remove_passenger() == p5
    assert v3.add_passenger(p6) is True
    assert str(v3) == "Honda holds 3: ['Olenka', 'Maksym', 'Katia'], free 0"
    # some cars do not have passenger places at all
    v4 = Vehicle('Bugatti', 0)
    assert str(v4) == "Bugatti holds 0: [], free 0"
    assert p5.place is None
    assert str(p5) == "Nastia is passenger of ..."
    assert v4.add_passenger(p5) is False
    assert v4.remove_passenger() is False
    assert v4.is_empty() is True
    assert p5.place is None
    assert str(p5) == "Nastia is passenger of ..."
    # the last car
    v5 = Vehicle('BMW', 2)
    assert str(v5) == "BMW holds 2: [], free 2"
    assert v5.add_passenger(p5) is True
    assert str(v5) == "BMW holds 2: ['Nastia'], free 1"
    assert p5.place == v5
    assert str(p5) == "Nastia is passenger of BMW"
    # if a person is already in a vehicle and you want him/her to be in another one, he/she changes
    # her place to a new car and is removed from the previous one
    assert p6.place == v3
    assert v5.add_passenger(p6) is True
    assert str(v5) == "BMW holds 2: ['Nastia', 'Katia'], free 0"
    assert p6.place == v5
    assert str(v3) == "Honda holds 3: ['Olenka', 'Maksym'], free 1"
    print("Done!")
    
    path = "Lviv - Stari Kuty"
    assert(type(v2) == Bus and isinstance(v2, Bus))
    assert(v2 == Bus("Bus", 20, path))
    assert(v2 != Bus("Bus", 20, "Lviv - Tuziliv"))
    assert(v2 != v1)
        try: Bus("Bus", -10, "Lviv - Tuziliv")
    except: ok = False # should not reach here
    assert(ok == False)
    try:
        v2 = Bus("Bus", "invalid_capacity", "Lviv - Tuziliv")
        assert(False) # should not reach here
    except TypeError:
        pass
    
        v3 = Bus("Bus", 1, "Lviv - Kyiv")
    assert(v3 != Bus('Bus', 30, "Lviv - Kyiv"))
    assert(v3.remove_passenger() == (None, "Bus is empty!"))
    assert v2.remove_passenger() == (p2, "Bus is empty!")
    assert(v2.remove_passenger() == (None, "Bus is empty!"))

    # Test adding a passenger to a full bus
    v4 = Bus("Bus", 1, "Lviv - Ternopil")
    p3 = Passenger("Sophie")
    p4 = Passenger("Masha")
    assert(v4.add_passenger(p3) == True)
    assert(v4.add_passenger(p4) == False)
 
test_vehicle()
