# matrixfact 
a programm to predict the student prefomance based on it s past data and other student history using matrix factorzation technique 
just heads up but there is a little bit of algbere involved

## Getting Started

to download this project you can download it directly in the format of zip file or using the command :
git clone https://github.com/amine-sakka/matrixfact.git

you need to files to exist next to the programm 
semester1.csv (data of the students previsly )
toPredict.csv students data to predict where 0 present the nb to predict 

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

or you can install theme individually
to install pandas
```
pip install pandas
```
to install csv
```
pip install csv
```

to install numpy 
```
pip install numpy
```


## Running the programm

the program consist of one part  finelMF the programm needs takes the file sesmester1.csv history data of student and lean from it so that file is nessecair 

to run the programm you need to use the command
```
python3 fibelMF.py 
```
or if you have a python idle you can just run it from there after running the programm a file Prediction.csv will be created in your directery


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

