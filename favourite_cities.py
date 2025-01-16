#to make cities which i like and their information about them

#creating class
class City:
    def __init__(self, name, country, population, landmark,nickname):
        self.name = name
        self.country = country
        self.population = population
        self.landmark = landmark
        self.nickaname = nickname

#creating objects
hometown = City("Lucknow", "India", 3000000, ["Kashi Vishwanath","Kal Bhairov","Ganga Maa"],"City of Nawabs")

fav = City("New York", "USA", 8000000, ["Statue of Liberty","Times Square","Central Park"],"Big Apple")

#printing the objects
print(vars(hometown))
print(vars(fav))

