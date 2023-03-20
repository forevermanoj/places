## Installation

Installation of this application is not available right now.

## Documentation

Documentation of this application is not available right now.


## Development

### Running a development version

To run the program in development, clone the project (or download its zip) and go to the `places` directory. You can run the source by executing:

	./main.py

### Tests

    A. Put this in a file named places.csv:
    Name,Latitude,Longitude
    Alta,69.96887,23.27165
    Anchorage,61.21806,-149.90028
    Jakarta,-6.21462,106.84513
    London,51.50853,-0.12574
    Longyearbyen,78.22334,15.64689
    North pole,90,0
    Oslo,59.91273,10.74609
    South pole,-90,0
    Troll research station,-72.00194,2.53389
    Vardø,70.37048,31.11066

    B. Write a command line program that takes one optional integer argument n, in python.
    C. If no argument is given, use places.csv as input.
    D. If n is given, use n randomly generated places as input.
    E. Find the air distance (great circle distance) between all pairs of places. Discard pairs having the same pair of places as another pair.
    F. Write out all place pairs and distances by ascending distance, lines column aligned and formatted like this: Someplace Otherplace 152.6 km
    G. On the last line, write out the average distance and the place pair and corresponding distance having the distance closest to the average value, like this: Average distance: 321.8 km. Closest pair: Thisplace – Thatplace 312.5 km.

To run the tests with command line without parameter, Open the `Terminal` and execute the below command:

	python main.py

To run the tests with command line with parameter, Open the `Terminal` and execute the below command:

	python main.py 4

### Contributing

Submit issues for bug reports or enhancement ideas.


### License

MIT. See [LICENSE.txt](https://github.com/forevermanoj/places/blob/main/LICENSE)