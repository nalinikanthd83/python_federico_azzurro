from dataclasses import dataclass

@dataclass
class Coin:
    name: str
    value: float
    id: str

def main() -> None:
    bitcoin: Coin = Coin('Bitcoin', 10_000, 'BTC')
    bitcoin2: Coin = Coin('Bitcoin', 10_000, 'BTC')
    ripple: Coin = Coin('Ripple', 10_000, 'XRP')

    print(bitcoin) #OUTPUT: Coin(name='Bitcoin', value=10000, id='BTC')
    print(ripple)  #OUTPUT: Coin(name='Ripple', value=10000, id='XRP')

    print(bitcoin == ripple) #OUTPUT: False
    print(bitcoin == bitcoin2) #OUTPUT: True

    print(ripple.id) #OUTPUT: XRP

# So as you noticed, these classes do not contain functionality.
# They just hold information, which is just very convenient to keep track of.
# And another benefit is that if we were to print the Bitcoin and we were to print this
# ripple, what we would get back is something a lot more readable than what we would get
# back with a normal class.

if __name__ == '__main__':
    main()

# And thanks to this, it also makes comparing objects easier, which means we can print whether Bitcoin
# is equal to ripple or whether Bitcoin is equal to Bitcoin two.
# And this will check the values by default.
# And just like with a regular class, we can access all the attributes by using dot notation.




