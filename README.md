# matrixfact 
A program to predict the student performance based on its past data and other student history using matrix factorization technique.
Just a heads up, but there is a little bit of algebra involved

## Getting Started

to download this project you can download it directly in the format of zip file or using the command :
git clone https://github.com/amine-sakka/matrixfact.git

You need two files to exist next to the program semester1.csv (data of the students previously) 
toPredict.csv students' data to predict where 0 represent the student exam notes to predict 

### Prerequisites

you will need to install python
```
python 3.5 or > 3.5
```

python libraries you need to install

```
pandas
csv
numpy
```

you need the semester1.csv file to existe next to the main program finelMF.py


### Installing

A step by step guid to install the prerequisites libraies
you can install all the libraries together in one step using the command 

```
pip install -r requirements.txt
```

or you can install theme individually.
To install pandas
```
pip install pandas
```
To install csv
```
pip install csv
```

To install numpy 
```
pip install numpy
```


## Running the programm

The program consist of one part finelMF the program needs takes the file sesmester1.csv history data of all the students
and it also take the file toPredict.csv .

toPredict.csv represent the students you want to predict their average the file toPredict.csv contains the notes of the students that they got and the exam mark that the student didn t get will be represented by a zero 0.0 these are our targets we are gonna try to predict these so will be able to calculate the final average the average of the semester.

to run the programm you need to use the command
```
python3 finelMF.py 
```
Or if you have a python idle you can just run it from there .
After running the program a file Prediction.csv will be created in your directory

Prediction.csv contains the result of our program, it will contain the student and their exams notes all of the exams and the average of the student during the semester


### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

