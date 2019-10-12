# Vueling Game App BackEnd
HackUPC vueling game

### Prerequisites

- [Python](https://www.python.org/downloads/windows/)
- [Flask](https://www.python.org/downloads/windows/)
```Python
#pip install Flask
```
- [Numpy](https://scipy.org/install.html#pip-install)
```Bash
#python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
```
- Requests
```Python
#pip install requests
```

## Running the tests

[Unit test](https://docs.python.org/3/library/unittest.html)

In the test folder is a file by each test and an execute all tests script.

By now the input and output of every test must be a JSON format.

### Break down into end to end tests

Simon test game generator
> The input is a request with a json that indicate the difficulty <br>
> The output is a json with a random array of colors which size depends of difficulty param

Simon test game result
> The input indicates the number of players and for each one the sequence of colors choosen <br>
> The output is a ranking with all players score.

### And coding style tests

Syntax
```Python
everyVariable = "isCamelCase"

class BeginWithCapitals:

def functionsAndMethods(are,camelCase):

CONSTANTS = "ALL CAPITALS"
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

Based on DEBIAN standard.

Every version should be named by 3 numbers separed by dots like X.Y.Z
- X: Means a set of features that can be named as a complete app (example: 1.0.0 is a hello world programs that runs. 2.0.0 is a playable game. 3.0.0 a totallu new multiplayer mode...)  
- Y: Means separated functionality (example: 1.3.4 to 1.4.0 when we add a new feature)
- Z: Means fixes (example 1.4.0 has a bug and we fix it so the new version is 1.4.1)

## Authors

* **José Ignacio Bustamante** - *Initial work* - [Busvar](https://github.com/busvar)
* **Marc** - *Initial work* - [Marcazu](https://github.com/marcazu)
* **Jairo** - *Initial work* - [abyss0one](https://github.com/abyss0one)


See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* HackUPC
