class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")

        Pet.all.append(self)


    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        if self.owner:
            self.owner.pets_list.remove(self)
        self.owner = owner

        if owner and self not in owner.pet_list:
            owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        if pet not in self.pets_list:
            self.pets_list.append(pet)
        pet.set_owner(self)

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)

