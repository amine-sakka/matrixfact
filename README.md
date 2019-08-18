# matrixfact 
A program to predict the student performance based on its past data and other student history using matrix factorization technique.
Just a heads up, but there is a little bit of algebra involved

## Getting Started

to download this project you can download it directly in the format of zip file or using the command :
git clone https://github.com/amine-sakka/matrixfact.git

You need two files to exist next to the program semester1.csv (data of the students previously) 
toPredict.csv students' data to predict where 0 represent the student exam notes to predict 
this how the toPredict.csv file looks like

![Screenshot_2019-08-18 finelMF](https://user-images.githubusercontent.com/43292310/63224040-7e60ea00-c1b6-11e9-8570-bd987de12290.png)


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

A step by step guide to install the prerequisite libraries You can install all the libraries together in one step using the command

```
sudo pip install -r requirements.txt

```
you should see something like this

![Screenshot from 2019-08-18 11-59-03](https://user-images.githubusercontent.com/43292310/63223577-a567ed80-c1af-11e9-973a-9729c16d38d8.png)

Or you can install them individually.
To install pandas
```
sudo pip install pandas
```
To install csv
```
sudo pip install python-csv
```

To install numpy 
```
sudo pip install numpy
```


## Running the programm

The program consist of one part finelMF the program needs takes the file sesmester1.csv history data of all the students
and it also take the file toPredict.csv .

toPredict.csv represent the students you want to predict their average the file toPredict.csv contains the notes of the students that they got and the exam mark that the student didn t get will be represented by a zero 0.0 these are our targets we are gonna try to predict these so will be able to calculate the final average the average of the semester.

to run the program you need to use the command
```
python3 finelMF.py 
```
you will get this 

![Screenshot from 2019-08-18 12-06-32](https://user-images.githubusercontent.com/43292310/63223699-e4973e00-c1b1-11e9-8cd9-611aaab28a4d.png)

the program will take time to finish but in the end you will get something like this

![Screenshot from 2019-08-18 12-13-22](https://user-images.githubusercontent.com/43292310/63223740-1a3c2700-c1b2-11e9-97f7-04607f639111.png)

If you see finish that means everything worked out smoothly

Or if you have a python idle you can just run it from there .
After running the program a file Prediction.csv will be created in your directory

![Screenshot from 2019-08-18 12-19-19](https://user-images.githubusercontent.com/43292310/63223775-84ed6280-c1b2-11e9-99b1-871eb1b3b404.png)

Prediction.csv contains the result of our program, it will contain the student and their exams notes all of the exams and the average of the student during the semester
and this how Prediction.csv file looks like

![Screenshot_2019-08-18 finelMF(1)](https://user-images.githubusercontent.com/43292310/63224056-ab150180-c1b6-11e9-8faa-1e6b9cc9c684.png)

the same as toPredict.csv  only nthe zeros 0.0 has been replaced by the prediction


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

