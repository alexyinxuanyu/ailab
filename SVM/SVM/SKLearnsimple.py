from sklearn import svm
from sklearn import neighbors
from sklearn import datasets
iris = datasets.load_iris()
x = [[2, 0], [1, 1], [2, 3]]
y = [0, 0, 1]
clf = svm.SVC(kernel = 'linear')
# clf.fit(x, y)
clf.fit(iris.data, iris.target)
predictedLabel=[0,0,0,0,0,0,0,0,0,0]
predictedLabel[0]=clf.predict([[6.0, 3, 4.7, 1.9]])
predictedLabel[1]=clf.predict([[5.4, 3.4, 4, 1.1]])
predictedLabel[2]=clf.predict([[5.7, 2.8, 4.1, 1.3]])
predictedLabel[3]=clf.predict([[5.1, 2.5, 3, 1.1]])
predictedLabel[4]=clf.predict([[6.2, 2.9, 4.3, 1.3]])
predictedLabel[5]=clf.predict([[5.7, 2.9, 4.2, 1.3]])
predictedLabel[6]=clf.predict([[5.7, 3, 4.2, 1.2]])
predictedLabel[7]=clf.predict([[5.6, 2.7, 4.2, 1.3]])
predictedLabel[8]=clf.predict([[5.0, 2.3, 3.3, 1]])
predictedLabel[9]=clf.predict([[6.2, 2.6, 4.9, 1.8]])
for i in range(0,10):
    print "predictedLabel_i:"+str(i)
    print predictedLabel[i]
print clf
# 
# clf.predict([2,0])
# # get support vectors
# print clf.support_vectors_
# # get indices of support vectors
# print clf.support_
# # get number of support vectors for each class
# print clf.n_support_