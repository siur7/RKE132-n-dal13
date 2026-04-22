from animal import Animal, Cat, Dog

my_cat = Cat("Tuumapomm")
my_dog = Dog("Aatompomm")
neighbors_dog = Dog("Rex")
neighbors_cat = Cat("Miisu")

my_cat.sees(my_dog)
my_dog.dog_sees(my_cat)
neighbors_dog.dog_sees(my_dog)
my_cat.cat_sees(neighbors_dog)
my_cat.cat_sees(neighbors_cat)

