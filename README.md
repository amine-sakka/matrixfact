# matrixfact 
A program to predict the student performance based on its past data and other student history using matrix factorization technique.
Just a heads up, but there is a little bit of algebra involved

## Getting Started

to download this project you can download it directly using the download button or using the command :
```
git clone https://github.com/amine-sakka/matrixfact.git
```

You need two files to exist next to the program 

semester1.csv (data of the students previously) 

toPredict.csv  students data to predict where 0 represent the student exam notes to predict.

This how the toPredict.csv file looks like

![Screenshot_2019-08-18 finelMF](https://user-images.githubusercontent.com/43292310/63224040-7e60ea00-c1b6-11e9-8570-bd987de12290.png)


### Prerequisites

you will need to install python & pip  ,pip is the package installer for Python. 
```
python 3.5 or > 3.5
```

```
pip 

```

python libraries you need to install

```
pandas
csv
numpy
```

you need the semester1.csv file to existe next to the main program finelMF.py


### Installing

A step by step guide to install the prerequisite & libraries 
                                            

we are gonna Check if you have pip 

``` 
pip --version   
```
If you get responses similar to this  :
``` 
pip 19.1.1 from /usr/local/lib/python3.6/dist-packages/pip (python 3.6)
```
then you can skip this part else, please follow this tutorial that will show you how to install python and pip on ubunto

Installing python3 & pip

```
https://www.youtube.com/watch?v=ivBYd1IT408
```

Installing the libraries

You can install all the libraries together in one step using the command 
 ```
sudo pip install -r requirements.txt
 ```
 you should see something like this

![Screenshot from 2019-08-18 11-59-03](https://user-images.githubusercontent.com/43292310/63223577-a567ed80-c1af-11e9-973a-9729c16d38d8.png)

Or you can install them individually.

To install pandas :
```
sudo pip install pandas
```
To install csv :
```
sudo pip install python-csv
```
To install numpy  :
```
sudo pip install numpy
```

## Running the programm

The program consist of one part finelMF the program needs to takes the file sesmester1.csv (history data of all the students)
and it also take the file toPredict.csv .

toPredict.csv represent the students you want to predict their average the file  contains the exams results of the students the marks they got and the exam marks that the student didn t get (it will be represented by a zero 0.0 these are our targets we are gonna try to predict these so that we will be able to calculate the final average the average of the semester).

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

Prediction.csv contains the result of our program, it will contain the student and their exams notes all of the exams and the average of the student during the semester.

and this how Prediction.csv file looks like

![Screenshot_2019-08-18 finelMF(1)](https://user-images.githubusercontent.com/43292310/63224056-ab150180-c1b6-11e9-8faa-1e6b9cc9c684.png)

the same as toPredict.csv  only nthe zeros 0.0 has been replaced by the prediction


### Breaking down the program

Matrix factorization is a class of collaborative filtering algorithms used in recommender systems. Matrix factorization algorithms work by decomposing the user-item in our case student-subject interaction matrix into the product of two lower dimensionality rectangular matrices. 

Now let us talk about finelMF.py  

the program consists of a class MF matrix factorization which will be responsible for finding the tow matrix P, Q That factoziae our student-subject matrix

Our first step will be to read the Semester1.csv and toPredict.csv files, then we create a student-subject matrix that we will use to predict the student performance

Then we will create an instance of MF us In the student-subject matrix and start the training process

The function moy takes a list of exam results and calculate the average of the student 

Then we create a Prediction.csv & save all the data result of the MF in it

```
Give an example
```

## Deployment



## Built With



## Contributing



## Versioning

## Authors

* **sakka** 

## License


## Acknowledgments


