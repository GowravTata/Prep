from final_class import final

"""
Final decorator can be used to restrict to create a subclass
"""
@final
class Dish:
    pass

class Pizza(Dish):
    def recipe(self):
        return "PIzza Secret"

mcd = Pizza()

print(mcd.recipe())
