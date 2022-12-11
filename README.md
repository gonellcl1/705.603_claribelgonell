# 705.603 - Creating AI Enabled Systems: Portfolio

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- ASSIGNMENT 3 -->
## Assignment 3


To download the repository image: 
* copy pull command for latest
  ```sh
  docker pull gonellcl/705.603_cgonell:latest
  ```
* select RUN
* Run a new container for the image. There are no ports exposed in the repository image. 
* The image is now in your host docker repository

* To access the image in your local repository: 
  ```sh
  $ docker run –v <host directory>:/output <REPOSTIORY>:<IMAGENAME>
  ```
   ```sh
  $ docker run –v <host directory>:/output gonellcl/705.603_cgonell:latest
  ```
To access the specific image that is tied to this repository, please download its associated image. 


<!-- ABOUT THE ASSIGNMENT -->
## Assignment 4

The assignment uses google ColaboratoryLinks to ingest Kaggle used car data for a deep neural network. The datset is first transformed via Categorical Preprocessing.

The Data Failure Spreadsheet contains several types of data failures, the remedial solutions, and disadvantages/considerations to the solutions. 

<!-- GETTING STARTED -->
## Links

Github: https://github.com/gonellcl1/705.603_claribelgonell/blob/master/assign_4/4_CategoricalData_ClaribelGonell.ipynb

Google Colab: https://colab.research.google.com/drive/1cfheLpJ6vjM7iU1IrfcK7Wxjk3ocWaRI?usp=sharing



<!-- ASSIGNMENT 6 -->
## Assignment 6

The Assignment uses MongoDB (a NoSQL document database) and Neo4J (a NoSQL graphical database) to store speed dating data. The data is then prepared to create a supervised machine learning model that predicts a match. The following models were used: Random Forest Classifier, Support Vector Machine, and Gaussian Naive Bayes.
SVM produced the highest vaildation metric accuracy. 

Contrasting MongoDB vs. Neo4J

Neo4J

Advantages: schema optional, navigation through tree traversal(very true to graph structure)

Disadvantages: no partioning methods

Best Suitable For: Graph database management systems; data that requires entity-relationship integrity

MongoDB

Advantages: document store structure makes it very easy to query and is schema-less, very flexible

Disadvantages: cannot create relationships

Best Suitable For: Everything else.



<!-- ASSIGNMENT 10 -->
## Assignment 10

The assignment explores AWS Sagemaker to build, train, and deploy reinforcement learning models. A local and AWS implementation of Blackjack RL (https://trevormcguire.medium.com/blackjack-stocks-and-reinforcement-learning-ea4014115aeb) are deployed. The local RL code is adapted to use AWS's virtual machine for training and developing an exposed web service.  



<!-- ASSIGNMENT 12-->
## Systems Project

To download the repository image: 
* copy pull command for latest
  ```sh
  docker pull gonellcl/systems_proj
  ```
* select RUN
* Run a new container for the image. There are no ports exposed in the repository image. 
* The image is now in your host docker repository

* To access the image in your local repository: 
  ```sh
  $ docker run –v <host directory>:/output <REPOSTIORY>:<IMAGENAME>
  ```
   ```sh
  $ docker run –v <host directory>:/output gonellcl/systems_proj:latest
  ```

<!-- CONTACT -->
## Contact

Claribel Gonell  - cgonell1@jh.edu.

Repository Link: [https://github.com/gonellcl1/705.603_claribelgonell](https://github.com/gonellcl1/705.603_claribelgonell)




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [othneildrew](https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
