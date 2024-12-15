class person:
  def __init__(self, name,age):
    self.name = name
    self._age = age
    self.__salary =50000
  def get_salary(self):
    return self.__salary
  def set_salary(self,new_salary):
        if new_salary > 0:
          self.__salary = new_salary
        else:
          print("salary must be positive.")
  def display_info(self):
      print(f"name:{self.name},age:{self._age},salary:{self.__salary}")
perso=person("alice",30)
print(perso.name)
print(perso._age)
print(perso.get_salary())
perso.set_salary(60000)
perso.display_info()
