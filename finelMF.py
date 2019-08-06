
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv


class MF():
    
    def __init__(self, R, K, alpha, beta, iterations):
        """
        Perform matrix factorization to predict empty
        entries in a matrix.
        
        Arguments
        - R (ndarray)   : user-item rating matrix
        - K (int)       : number of latent dimensions
        - alpha (float) : learning rate
        - beta (float)  : regularization parameter
        """
        
        self.R = R
        self.num_users, self.num_items = R.shape
        self.K = K
        self.alpha = alpha
        self.beta = beta
        self.iterations = iterations

    def train(self):
        # Initialize user and item latent feature matrice
        self.P = np.random.normal(scale=1./self.K, size=(self.num_users, self.K))
        self.Q = np.random.normal(scale=1./self.K, size=(self.num_items, self.K))
        
        # Initialize the biases
        self.b_u = np.zeros(self.num_users)
        self.b_i = np.zeros(self.num_items)
        self.b = np.mean(self.R[np.where(self.R != 0)])
        
        # Create a list of training samples
        self.samples = [
            (i, j, self.R[i, j])
            for i in range(self.num_users)
            for j in range(self.num_items)
            if self.R[i, j] > 0
        ]
        
        # Perform stochastic gradient descent for number of iterations
        training_process = []
        for i in range(self.iterations):
            np.random.shuffle(self.samples)
            self.sgd()
            mse = self.mse()
            training_process.append((i, mse))
            if (i+1) % 10 == 0:
                print("Iteration: %d ; error = %.4f" % (i+1, mse))
        
        return training_process

    def mse(self):
        """
        A function to compute the total mean square error
        """
        xs, ys = self.R.nonzero()
        predicted = self.full_matrix()
        error = 0
        for x, y in zip(xs, ys):
            error += pow(self.R[x, y] - predicted[x, y], 2)
        return np.sqrt(error)

    def sgd(self):
        """
        Perform stochastic graident descent
        """
        for i, j, r in self.samples:
            # Computer prediction and error
            prediction = self.get_rating(i, j)
            e = (r - prediction)
            
            # Update biases
            self.b_u[i] += self.alpha * (e - self.beta * self.b_u[i])
            self.b_i[j] += self.alpha * (e - self.beta * self.b_i[j])
            
            # Create copy of row of P since we need to update it but use older values for update on Q
            P_i = self.P[i, :][:]
            
            # Update user and item latent feature matrices
            self.P[i, :] += self.alpha * (e * self.Q[j, :] - self.beta * self.P[i,:])
            self.Q[j, :] += self.alpha * (e * P_i - self.beta * self.Q[j,:])

    def get_rating(self, i, j):
        """
        Get the predicted rating of user i and item j
        """
        prediction = self.b + self.b_u[i] + self.b_i[j] + self.P[i, :].dot(self.Q[j, :].T)
        return prediction
    
    
    def full_matrix(self):
        """
        Computer the full matrix using the resultant biases, P and Q
        """
        return mf.b + mf.b_u[:,np.newaxis] + mf.b_i[np.newaxis:,] + mf.P.dot(mf.Q.T)


data = pd.read_csv("Semester1.csv") 
startpoint=data.shape[0]
matrixOfResults=data.as_matrix()
#data.head()

data1 = pd.read_csv("toPredict.csv") 
toPredict=data1.as_matrix()
#data1


result = np.vstack ((matrixOfResults, toPredict) )/20
result.shape
endingPoint=result.shape[0]


mf = MF(result, K=18, alpha=0.1, beta=0.01, iterations=250)
training_process = mf.train()
print()
print("P x Q:")
print(mf.full_matrix())
print()
print("Global bias:")
print(mf.b)
print()
print("User bias:")
print(mf.b_u)
print()
print("Item bias:")
print(mf.b_i)

#mf.get_rating(4000,4)*20

def moy(listDesMoyenn):
    #l=Arabic 	French 	English 	Historique 	Geographiqye 	Civil 	Islemic 	Math 	Physique 	Siance 	technique 	Sport
    moy=0
    for i in range(3):
        moy+=l[i]*2
    for i in range(3,7):
        moy+=l[i]
    for i in range(7,9):
        moy+=l[i]*4
    for i in range(9,11):
        moy+=l[i]*2
    moy+=l[-1]
    return(moy/23)



csv_file = open('Prediction.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Arabic', 'French', 'English','Historique','Geographiqye','Civil','Islemic','Math','Physique','Siance','technique','Sport','moys'])


for k in range(startpoint,endingPoint):
    print("for user : "+str(k))
    l=[]
    for i in range(len(data.columns)-1):
        #notes[data.columns[i]]=mf.get_rating(k,i)*20
        l.append(mf.get_rating(k,i)*20)
        #ch=data.columns[i] +' : '+ str(mf.get_rating(k,i)*20)
    #print(len(l))
    moyenn=moy(l)
    l.append(moyenn)
    #print("moyenn : "+str(moyenn))
    csv_writer.writerow(l)


csv_file.close()

data = pd.read_csv("Prediction.csv") 
data

