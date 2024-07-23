

#class CoopFoo:
#    def __init__(self, **kwargs):
#        super().__init__(**kwargs)  # forwards all unused arguments
#        self.foo = 'foo'
#
#class CoopBar:
#    def __init__(self, bar, myvar, **kwargs):
#        super().__init__(**kwargs)  # forwards all unused arguments
#        self.bar = bar
#        self.myvar = myvar
#
#class CoopFooBar(CoopFoo, CoopBar):
#    def __init__(self, bar="bar", hello="roooo"):
#        super().__init__(bar=bar, myvar=hello)  # pass all arguments on as keyword
#                                   # arguments to avoid problems with
#                                   # positional arguments and the order
#                                   # of the parent classes






#class Base:
#    def __init__(self, **kwargs) -> None:
#        kwargs.clear

class Sex:
    def __init__(self, **kwargs) -> None:
        self.sex = kwargs.setdefault("sex",None)
        kwargs.pop("sex")
        super().__init__(**kwargs)

class Name:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.setdefault("name",None)
        kwargs.pop("name")
        super().__init__(**kwargs)


class Color:
    def __init__(self, **kwargs) -> None:
        self.color = kwargs.setdefault("color",None)    # like kwargs.get(), but if key not found, add it and set to None.
        kwargs.pop("color")                             # Remove key that you used or just added, to make sure no args are leftover by the end of the chain.
        super().__init__(**kwargs)                      # Pass along the remaining args, if any.
        
class Length:
    def __init__(self, **kwargs):
        self.length = kwargs.setdefault("length",None)
        kwargs.pop("length")
        super().__init__(**kwargs)

    def islongerthan5(self):
        return self.length > 5

class Waviness:
    def __init__(self, **kwargs) -> None:
        self.waviness = kwargs.setdefault("waviness",None)
        kwargs.pop("waviness")
        super().__init__(**kwargs)

class Hair(Length, Color, Waviness):
    def __init__(self, **kwargs) -> None:
        self.somehairvar = kwargs.setdefault("somehairvar",None)
        kwargs.pop("somehairvar")
        super().__init__(**kwargs)

class Eyes(Color):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class Character(Name, Sex):
    def __init__(self, **kwargs) -> None:
        self.hair = Hair(
            color=kwargs.setdefault("haircolor", None),
            length=kwargs.setdefault("hairlength", None),
            waviness=kwargs.setdefault("hairwaviness", None)
        )
        self.eyes = Eyes(
            color=kwargs.setdefault("eyecolor", None)
        )
        kwargs.pop("haircolor")
        kwargs.pop("hairlength")
        kwargs.pop("hairwaviness")
        kwargs.pop("eyecolor")
        super().__init__(**kwargs)



chara1 = Character(
    name="John",
    sex="male",
    haircolor="Black",
    hairlength=6,
    hairwaviness="straight",
    eyecolor="blue"
)


print("Character name:",chara1.name)
print(chara1.sex)
print("Hair color:",chara1.hair.color)
print("Hair waviness:",chara1.hair.waviness)
print("Hair length:",chara1.hair.length)
print("Hair is longer than 5?",chara1.hair.islongerthan5())
print("Eye color:",chara1.eyes.color)



